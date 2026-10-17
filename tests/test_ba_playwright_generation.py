"""Real source-based Python Playwright generation, coverage and security checks."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_playwright import generate, generate_files

class PlaywrightGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=json.loads((BA/"examples/authentication-screen-model.json").read_text(encoding="utf8"))

    def test_every_control_and_mock_outcome_is_exercised(self):
        plan=generate(self.model)
        self.assertEqual(len(plan["cases"]),7)
        self.assertEqual(len({case["id"] for case in plan["cases"]}),7)
        self.assertEqual(plan["execution_status"],"not-run")
        names={(case["screen"],case["kind"],case.get("scenario")) for case in plan["cases"]}
        self.assertIn(("login","submit","success"),names)
        self.assertIn(("login","submit","locked"),names)
        self.assertIn(("home","navigate",None),names)
        case=next(x for x in plan["cases"] if x["screen"]=="home")
        self.assertEqual(case["path"][0]["kind"],"submit")
        self.assertEqual(case["path"][0]["scenario"],"success")
        self.assertEqual(case["path"][0]["target"],"home")
        self.assertEqual(plan["source_link_check"],"not-performed")

    def test_generated_source_is_real_python_and_model_data_safe(self):
        files=generate_files(self.model)
        self.assertEqual(set(files),{"test_prototype.py","traceability.json"})
        compile(files["test_prototype.py"],"test_prototype.py","exec")
        self.assertIn("page.get_by_role",files["test_prototype.py"])
        self.assertIn('proto.as_uri()',files["test_prototype.py"])
        self.assertIn("local-file-only",files["traceability.json"])
        injection=copy.deepcopy(self.model)
        injection["screens"][0]["title"]='"; __import__("os").system("echo bad")'
        injection["screens"][0]["controls"][2]["outcomes"]["invalid"]["message"]="\\nmalicious: ;"
        generated=generate_files(injection)["test_prototype.py"]
        compile(generated,"test_prototype.py","exec")
        self.assertNotIn('exec(',generated)
        self.assertNotIn('eval(',generated)

    def test_evidence_identity_is_optional_but_exact_when_provided(self):
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"][2]["requirements"]=["FR-AUTH-001"]
        ids={"FR-AUTH-001","FR-AUTH-002","BR-AUTH-001"}
        self.assertEqual(generate(data,ids)["source_link_check"],"ids-resolved-only")
        with self.assertRaisesRegex(ValueError,"Unresolved evidence"):
            generate(data,{"BR-AUTH-001"})
        data["screens"][0]["controls"][2]["requirements"]=["FR NOT VALID"]
        with self.assertRaisesRegex(ValueError,"Invalid source"):
            generate(data)

    def test_rejects_real_password_fixtures(self):
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"][1]["test_value"]="a-secret"
        with self.assertRaisesRegex(ValueError,"password"):
            generate(data)

    def test_rejects_uncovered_actions_or_invalid_model(self):
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"].append({"id":"island","type":"button","label":"Island",
                                                "action":{"type":"navigate","target":"missing"}})
        with self.assertRaisesRegex(ValueError,"Invalid screen model"):
            generate(data)
        data=copy.deepcopy(self.model)
        data["screens"].append({"id":"island","title":"Isolation","controls":[
            {"id":"back","type":"button","label":"Back","action":{"type":"navigate","target":"login"}}]})
        with self.assertRaisesRegex(ValueError,"Invalid screen model"):
            generate(data)

if __name__=="__main__":
    unittest.main()
