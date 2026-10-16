"""Contract tests: Bruno files are real generated requests, not fake test results."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_bruno import compile_collection, validate

class BrunoGeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture=json.loads((BA/"examples/synthetic-fleet-api-tests.json").read_text(encoding="utf8"))

    def test_real_collection_and_assertions(self):
        files=compile_collection(self.fixture)
        self.assertEqual(len(files),7)
        self.assertIn("bruno.json",files)
        manifest=json.loads(files["traceability.json"])
        self.assertEqual(len(manifest["tests"]),4)
        self.assertEqual(manifest["tests"][3]["source_link_state"],"missing")
        self.assertEqual(manifest["source_evidence_id_check"],"not-performed")
        self.assertIn("environments/Mock.bru",files)
        self.assertEqual(json.loads(files["bruno.json"])["name"],"Synthetic Fleet Access Tests")
        self.assertIn("baseUrl: http://127.0.0.1:18497",files["environments/Mock.bru"])
        for req in self.fixture["requests"]:
            body=files["requests/"+req["id"]+".bru"]
            self.assertIn("tests {",body)
            self.assertIn("expect(res.getStatus()).to.eql("+str(req["expected_status"])+")",body)
            for field in req["expected_json"]:
                self.assertIn('res.getBody()["'+field+'"]',body)
            self.assertNotIn("production",body.lower())
        self.assertIn("network_requests_sent",validate(self.fixture))
        self.assertEqual(validate(self.fixture)["network_requests_sent"],0)

    def test_injection_and_undefined_variables_fail_closed(self):
        cases=[]
        a=copy.deepcopy(self.fixture);a["requests"][0]["path"]="/vehicles/{{missing}}";cases.append(a)
        a=copy.deepcopy(self.fixture);a["requests"][0]["path"]="https://example.com/admin";cases.append(a)
        a=copy.deepcopy(self.fixture);a["requests"][0]["name"]="x\n}\ntests { ok";cases.append(a)
        a=copy.deepcopy(self.fixture);a["requests"][0]["id"]="TC-AUTH-001\n";cases.append(a)
        a=copy.deepcopy(self.fixture);a["environment"]["baseUrl"]="http://localhost/\n}";cases.append(a)
        a=copy.deepcopy(self.fixture);a["requests"][0]["expected_json"]={"foo();":1};cases.append(a)
        a=copy.deepcopy(self.fixture);a["requests"][0]["expected_status"]=True;cases.append(a)
        a=copy.deepcopy(self.fixture);a["environment"]["baseUrl"]=42;cases.append(a)
        a=copy.deepcopy(self.fixture);a["requests"][0]["headers"]={"X-Demo":"}"};cases.append(a)
        for case in cases:
            with self.subTest(case=case["requests"][0]["path"]):
                self.assertFalse(validate(case)["ok"])
                with self.assertRaises(ValueError):
                    compile_collection(case)

    def test_header_variables_must_resolve_before_collection_generation(self):
        good=copy.deepcopy(self.fixture)
        good["requests"][0]["headers"]={"X-Vehicle":"{{vehicleId}}"}
        self.assertTrue(validate(good)["ok"],validate(good))
        compiled=compile_collection(good)
        self.assertIn("X-Vehicle: {{vehicleId}}",compiled["requests/TC-FLEET-001.bru"])
        bad=copy.deepcopy(good)
        bad["requests"][0]["headers"]={"X-Undefined":"{{unknownKey}}"}
        result=validate(bad)
        self.assertFalse(result["ok"])
        self.assertTrue(any("undefined header variables" in x for x in result["errors"]))
        with self.assertRaisesRegex(ValueError,"undefined header variables"):
            compile_collection(bad)

    def test_base_url_rejects_malformed_hosts_and_credentials(self):
        for invalid in ("http://","https://","https://:1234",
                        "https://user:password@example.com", "https://example.com?q=a",
                        "https://example.com#fragment", "https://example.com:bad"):
            with self.subTest(baseUrl=invalid):
                model=copy.deepcopy(self.fixture)
                model["environment"]["baseUrl"]=invalid
                self.assertFalse(validate(model)["ok"])
        model=copy.deepcopy(self.fixture)
        model["environment"]["baseUrl"]="https://example.test/api"
        self.assertTrue(validate(model)["ok"],validate(model))

    def test_nonfinite_json_body_cannot_generate_invalid_json(self):
        model=copy.deepcopy(self.fixture)
        model["requests"][3]["body_json"]["measurement"]=float("nan")
        result=validate(model)
        self.assertFalse(result["ok"])
        self.assertTrue(any("finite JSON values" in e for e in result["errors"]))
        with self.assertRaisesRegex(ValueError,"finite JSON values"):
            compile_collection(model)

    def test_deduplicate_and_reject_unsafe_body(self):
        a=copy.deepcopy(self.fixture)
        a["requests"][1]["id"]=a["requests"][0]["id"]
        self.assertFalse(validate(a)["ok"])
        a=copy.deepcopy(self.fixture)
        a["requests"][0]["body_json"]={"role":"admin"}
        self.assertFalse(validate(a)["ok"])
        a=copy.deepcopy(self.fixture)
        a["requests"][0]["expected_json"]={"device":{"id":1}}
        self.assertFalse(validate(a)["ok"])

    def test_post_json_body_generation(self):
        a=copy.deepcopy(self.fixture)
        req=a["requests"][0]
        req["method"]="POST"
        req["path"]="/sandbox/test-resource"
        req["expected_status"]=201
        req["body_json"]={"vehicleId":"demo-001","count":1,"verified":False}
        generated=compile_collection(a)["requests/"+req["id"]+".bru"]
        self.assertIn("post {",generated)
        self.assertIn("body: json",generated)
        self.assertIn("body:json {",generated)
        self.assertIn("Content-Type: application/json",generated)
        self.assertIn('"vehicleId": "demo-001"',generated)
        self.assertIn("to.eql(201)",generated)

    def test_requirement_graph_identity_not_semantic_approval(self):
        from validate_artifacts import audit
        graph=json.loads((BA/"examples/rental-fleet-traceability.json").read_text(encoding="utf8"))
        self.assertTrue(audit(graph)["ok"])
        ids={item["id"] for item in graph["artifacts"]}
        files=compile_collection(self.fixture,evidence_ids=ids)
        manifest=json.loads(files["traceability.json"])
        self.assertEqual(manifest["source_evidence_id_check"],"performed")
        self.assertEqual(manifest["tests"][0]["source_link_state"],"ids-resolved-only")
        modified=copy.deepcopy(self.fixture)
        modified["requests"][0]["requirements"]=["FR-MISSING-999"]
        self.assertFalse(validate(modified,evidence_ids=ids)["ok"])
        with self.assertRaisesRegex(ValueError,"unresolved evidence requirement"):
            compile_collection(modified,evidence_ids=ids)

    def test_default_secrets_are_not_assumed(self):
        a=copy.deepcopy(self.fixture)
        a["requests"][0]["headers"]={"Authorization":"Bearer {{apiToken}}"}
        # A token variable is explicit, not inserted by the generator.
        self.assertNotIn("apiToken",a["environment"])
        self.assertFalse(validate(a)["ok"])
        with self.assertRaisesRegex(ValueError, "secrets must be supplied"):
            compile_collection(a)
        del a["requests"][0]["headers"]
        a["requests"][0]["auth"]="bearer"
        generated=compile_collection(a)["requests/TC-FLEET-001.bru"]
        self.assertIn("auth:bearer {",generated)
        self.assertIn("token: {{authToken}}",generated)
        self.assertNotIn("apiToken",generated)

if __name__=="__main__":
    unittest.main()
