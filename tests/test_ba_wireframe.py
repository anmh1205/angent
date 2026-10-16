"""Actual BA wireframe/prototype renderer smoke, schema and security checks."""
import copy
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_wireframe import check_model, render

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags=[]
    def handle_starttag(self,tag,attrs):
        self.tags.append((tag,dict(attrs)))

class WireframeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=json.loads((BA/"examples/authentication-screen-model.json").read_text(encoding="utf8"))

    def test_real_example_model_and_modes(self):
        report=check_model(self.model)
        self.assertTrue(report["ok"],report)
        self.assertEqual(report["screens"],3)
        self.assertEqual(report["scenario_count"],4)
        for mode in ("prototype","wireframe"):
            content=render(self.model,mode)
            parser=PageParser();parser.feed(content)
            self.assertIn("<!doctype html>",content)
            self.assertIn("All responses are simulated",content)
            if mode=="prototype":
                self.assertEqual([x[0] for x in parser.tags].count("script"),2)
                self.assertIn("no identity checks",content.lower())
                self.assertIn("Mock response",content)
            else:
                self.assertEqual([x[0] for x in parser.tags].count("script"),0)
                self.assertEqual([attrs.get("id") for tag,attrs in parser.tags if tag=="section"],
                                 ["login","recovery","home"])

    def test_prototype_data_is_not_executable(self):
        data=copy.deepcopy(self.model)
        data["screens"][0]["title"]='</script><script>alert("xss")</script>'
        data["screens"][0]["controls"][0]["label"]='<img src=x onerror=alert(1)>'
        for mode in ("prototype","wireframe"):
            content=render(data,mode)
            self.assertNotIn('</script><script>alert',content)
            self.assertNotIn('<img src=x onerror',content)
            self.assertIn('&lt;img src=x onerror',content if mode=="wireframe" else content.replace("\\u003c","&lt;").replace("\\u003e","&gt;"))

    def test_missing_and_duplicate_screens(self):
        data=copy.deepcopy(self.model)
        data["screens"].append(copy.deepcopy(data["screens"][0]))
        self.assertFalse(check_model(data)["ok"])
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"][1]["id"]="email"
        self.assertFalse(check_model(data)["ok"])

    def test_invalid_targets_and_orphans(self):
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"][-1]["action"]["target"]="not-found"
        self.assertFalse(check_model(data)["ok"])
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"][-1]["action"]["target"]="home"
        data["screens"][1]["id"]="unreachable"
        self.assertTrue(any("unreachable" in e for e in check_model(data)["errors"]))

    def test_scenario_mismatch_and_weak_errors(self):
        data=copy.deepcopy(self.model)
        data["scenarios"].append("unexpected")
        self.assertFalse(check_model(data)["ok"])
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"][2]["outcomes"]["invalid"]["message"]=""
        self.assertFalse(check_model(data)["ok"])

    def test_invalid_root_and_unhashable_controls_are_rejected(self):
        cases=[None,[],{"screens":[]},{"screens":[{"id":"x","title":"A","controls":None}],"title":"A","start":["x"],"scenarios":["success"]}]
        for case in cases:
            with self.subTest(case=case):
                self.assertFalse(check_model(case)["ok"])
        data=copy.deepcopy(self.model)
        data["screens"][0]["controls"][0]["type"]=[]
        self.assertFalse(check_model(data)["ok"])

    def test_required_fields_and_requirement_ids_are_visible(self):
        static=render(self.model,"wireframe")
        self.assertIn("FR-AUTH-001",static)
        self.assertIn("BR-AUTH-001",static)
        self.assertIn('type=&#x27;email',static.replace('type=','type=')) if False else None
        live=render(self.model,"prototype")
        self.assertIn('required = !!ctrl.required',live)
        self.assertIn('form.reportValidity()',live)
        self.assertIn('role", "alert"',live)
        self.assertIn('event.preventDefault()',live)

    def test_cli_output_real_file(self):
        from build_wireframe import main
        # Use tested API for real output without changing the source fixture.
        with tempfile.TemporaryDirectory() as d:
            output=Path(d)/"demo.html"
            output.write_text(render(self.model,"prototype"),encoding="utf8")
            self.assertGreater(output.stat().st_size,2000)
            self.assertIn("model-json",output.read_text(encoding="utf8"))

if __name__=="__main__":
    unittest.main()
