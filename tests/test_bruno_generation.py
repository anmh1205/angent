"""Canonical Bruno request contract, actual .bru output and safety checks."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_bruno import compile_collection, validate

class BrunoGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=json.loads((BA/"examples/synthetic-fleet-api-tests.json").read_text(encoding="utf8"))

    def test_actual_four_request_collection_with_traceability(self):
        generated=compile_collection(self.model)
        self.assertEqual(len(generated),len(self.model["requests"])+3)
        self.assertEqual(len(self.model["requests"]),4)
        tracking=json.loads(generated["traceability.json"])
        self.assertEqual(len(tracking["tests"]),4)
        self.assertEqual(tracking["execution_status"],"not-run")
        self.assertEqual(json.loads(generated["bruno.json"])["type"],"collection")
        self.assertIn("baseUrl: http://127.0.0.1:18497",generated["environments/Mock.bru"])
        self.assertIn("url: {{baseUrl}}/vehicles/{{vehicleId}}/status?mode=ok",generated["requests/TC-FLEET-001.bru"])
        self.assertIn("expect(res.getStatus()).to.eql(200)",generated["requests/TC-FLEET-001.bru"])
        self.assertIn('expect(res.getBody()["state"]).to.deep.equal("online")',generated["requests/TC-FLEET-001.bru"])
        self.assertIn("expect(res.getStatus()).to.eql(403)",generated["requests/TC-FLEET-002.bru"])
        self.assertEqual(generated,compile_collection(self.model))
        self.assertTrue(validate(self.model)["ok"])

    def test_auth_is_runtime_secret_only(self):
        model=deepcopy(self.model)
        model["requests"][0]["auth"]="bearer"
        generated=compile_collection(model)
        bru=generated["requests/TC-FLEET-001.bru"]
        self.assertIn("auth:bearer {",bru)
        self.assertIn("token: {{authToken}}",bru)
        self.assertNotIn("authToken:",generated["environments/Mock.bru"])
        model["environment"]["authToken"]="real-secret"
        self.assertFalse(validate(model)["ok"])
        model=deepcopy(self.model)
        model["requests"][0]["headers"]={"Authorization":"Bearer real-secret"}
        self.assertFalse(validate(model)["ok"])

    def test_injection_and_invalid_paths_are_blocked(self):
        for path in ("/../admin","https://example.com/steal","/api/\nheader: malicious","/foo/{bad}"):
            model=deepcopy(self.model)
            model["requests"][0]["path"]=path
            with self.subTest(path=path):
                self.assertFalse(validate(model)["ok"])
        for field in ("constructor.prototype","__proto__","foo);code()"):
            model=deepcopy(self.model)
            model["requests"][0]["expected_json"]={field:"bad"}
            with self.subTest(field=field):
                self.assertFalse(validate(model)["ok"])

    def test_duplicate_ids_and_unsupported_methods(self):
        model=deepcopy(self.model)
        model["requests"][1]["id"]=model["requests"][0]["id"]
        self.assertFalse(validate(model)["ok"])
        model=deepcopy(self.model)
        model["requests"][0]["method"]="TRACE"
        self.assertFalse(validate(model)["ok"])
        model=deepcopy(self.model)
        model["requests"][0]["expected_status"]=True
        self.assertFalse(validate(model)["ok"])

    def test_nested_property_assertions_are_escaped(self):
        model=deepcopy(self.model)
        model["requests"][0]["expected_json"]={"vehicle.state":"online"}
        self.assertIn('res.getBody()["vehicle"]["state"]',compile_collection(model)["requests/TC-FLEET-001.bru"])

if __name__=="__main__":
    unittest.main()
