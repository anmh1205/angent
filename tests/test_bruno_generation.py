"""Bruno generation must be deterministic, secret-free and reject unsafe plans."""
from pathlib import Path
import json
import sys
import tempfile
import unittest
from copy import deepcopy

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_bruno import compile_plan, validate

class BrunoGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan=json.loads((BA/"examples/vehicle-status-api-plan.json").read_text(encoding="utf8"))

    def test_two_real_requests_with_status_and_body_assertions(self):
        artifacts=compile_plan(self.plan)
        self.assertEqual(set(artifacts),{"bruno.json","README.md","environments/Local.bru",
                                         "requests/AUTHZ001.bru","requests/AUTHZ002.bru"})
        self.assertEqual(json.loads(artifacts["bruno.json"])["name"],self.plan["name"])
        allowed=artifacts["requests/AUTHZ001.bru"]
        denied=artifacts["requests/AUTHZ002.bru"]
        self.assertIn("url: {{baseUrl}}/api/vehicles/{{vehicleId}}/status",allowed)
        self.assertIn("auth:bearer {",allowed)
        self.assertIn("expect(res.getStatus()).to.equal(200)",allowed)
        self.assertIn('expect(res.getBody()["status"]).to.deep.equal("online")',allowed)
        self.assertIn("auth: none",denied)
        self.assertIn("expect(res.getStatus()).to.equal(403)",denied)
        self.assertNotIn("authToken: ",artifacts["environments/Local.bru"])
        self.assertEqual(compile_plan(self.plan),artifacts)

    def test_injection_and_path_traversal_rejected(self):
        for path in ("/../admin","/api/{danger}","/path\nother","https://real.example.com"):
            p=deepcopy(self.plan)
            p["scenarios"][0]["path"]=path
            with self.subTest(path=path),self.assertRaises(ValueError):
                compile_plan(p)
        for field in ("data[0]","foo); code(); //","constructor.prototype"):
            p=deepcopy(self.plan)
            p["scenarios"][0]["body_checks"]={field:1}
            with self.subTest(field=field),self.assertRaises(ValueError):
                compile_plan(p)

    def test_duplicate_and_unsupported_scenarios(self):
        p=deepcopy(self.plan)
        p["scenarios"][1]["id"]=p["scenarios"][0]["id"]
        with self.assertRaisesRegex(ValueError,"duplicate"):
            compile_plan(p)
        p=deepcopy(self.plan)
        p["scenarios"][1]["method"]="TRACE"
        with self.assertRaisesRegex(ValueError,"unsupported"):
            compile_plan(p)
        p=deepcopy(self.plan)
        p["scenarios"][1]["expected_status"]=True
        with self.assertRaisesRegex(ValueError,"HTTP status"):
            compile_plan(p)
        p=deepcopy(self.plan)
        p["scenarios"][1]["body"]={"raw":"x"}
        with self.assertRaisesRegex(ValueError,"GET cannot"):
            compile_plan(p)

    def test_json_body_and_scalar_checks_are_not_executable_strings(self):
        p=deepcopy(self.plan)
        p["scenarios"][0]["method"]="POST"
        p["scenarios"][0]["body"]={"name":"Alice });\nattack()","nested":{"allowed":True}}
        p["scenarios"][0]["body_checks"]={"count":0,"enabled":True}
        result=compile_plan(p)["requests/AUTHZ001.bru"]
        self.assertIn("body:json {",result)
        self.assertIn('"nested"',result)
        self.assertIn('expect(res.getBody()["enabled"]).to.deep.equal(true)',result)
        self.assertIn('expect(res.getBody()["count"]).to.deep.equal(0)',result)
        self.assertNotIn("attack()\n",result.split("tests {")[1])

if __name__=="__main__":
    unittest.main()
