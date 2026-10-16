"""D2 model checks: semantics, deterministic DSL, refusal to assert absent renderer."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_d2 import validate,compile_source,render_svg

class D2BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.examples={kind:json.loads((BA/f"examples/d2-{kind}.json").read_text(encoding="utf8"))
                      for kind in ("activity","erd","architecture")}

    def test_compile_three_distinct_diagram_kinds(self):
        for kind,model in self.examples.items():
            with self.subTest(kind=kind):
                outcome=validate(model)
                self.assertTrue(outcome["ok"],outcome)
                compiled=compile_source(model)
                self.assertEqual(compiled,compile_source(model))
                self.assertIn("direction: right",compiled)
                self.assertEqual(compiled.count(" -> "),len(model["edges"]))
                self.assertNotIn("style.fill: transparent",compiled)
        erd=compile_source(self.examples["erd"])
        self.assertEqual(erd.count("shape: sql_table"),3)
        self.assertIn("constraint: primary_key",erd)
        self.assertIn("constraint: foreign_key",erd)
        activity=compile_source(self.examples["activity"])
        self.assertIn('\"authorized\"',activity)
        self.assertIn("shape: diamond",activity)
        architecture=compile_source(self.examples["architecture"])
        self.assertIn('\"MQTT/TLS\"',architecture)

    def test_rejects_incomplete_activity(self):
        a=deepcopy(self.examples["activity"])
        a["edges"][2].pop("guard")
        self.assertFalse(validate(a)["ok"])
        a=deepcopy(self.examples["activity"])
        a["nodes"].append({"id":"orphan","kind":"task","label":"Unreachable","lane":"API"})
        self.assertTrue(any("unreachable" in err for err in validate(a)["errors"]))
        a=deepcopy(self.examples["activity"])
        a["nodes"][0]["lane"]=None
        self.assertTrue(any("lanes" in err for err in validate(a)["errors"]))

    def test_erd_field_semantics(self):
        a=deepcopy(self.examples["erd"])
        a["edges"][0]["toField"]="non_existent"
        self.assertTrue(any("not declared" in err for err in validate(a)["errors"]))
        a=deepcopy(self.examples["erd"])
        a["nodes"][0]["attributes"][0]["key"]="wrong"
        self.assertFalse(validate(a)["ok"])
        a=deepcopy(self.examples["erd"])
        a["nodes"][0]["attributes"][0]["type"]="uuid\\nstyle.fill: red"
        self.assertFalse(validate(a)["ok"])

    def test_graph_input_injection_is_quoted_and_not_executed(self):
        a=deepcopy(self.examples["activity"])
        a["nodes"][0]["label"]='</script>\\nfoo -> unauthorized: injected'
        script=compile_source(a)
        self.assertNotIn("\nfoo -> unauthorized",script)
        self.assertIn(r"\nfoo -> unauthorized",script)

    def test_missing_renderer_fails_explicitly(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            source=root/"input.d2"
            source.write_text(compile_source(self.examples["activity"]),encoding="utf8")
            outcome=render_svg(source,root/"result.svg",executable="__not_installed_d2_test__")
            self.assertFalse(outcome["ok"])
            self.assertFalse(outcome["rendered"])
            self.assertFalse((root/"result.svg").exists())


    def test_malformed_nested_inputs_fail_closed(self):
        base=deepcopy(self.examples["activity"])
        variants=[]
        a=deepcopy(base);a["direction"] = [];variants.append(a)
        a=deepcopy(base);a["nodes"][0]["kind"] = [];variants.append(a)
        a=deepcopy(base);a["edges"][0]["from"] = [];variants.append(a)
        a=deepcopy(self.examples["erd"]);a["nodes"][0]["attributes"][0]["key"] = [];variants.append(a)
        a=deepcopy(self.examples["architecture"]);a["nodes"][0]["kind"] = {"not":"a shape"};variants.append(a)
        for model in variants:
            with self.subTest(model=model):
                self.assertFalse(validate(model)["ok"])

    def test_type_and_limit_checks(self):
        for bad in (None,[],{},{"type":[],"nodes":[],"edges":[]}):
            self.assertFalse(validate(bad)["ok"])
        a=deepcopy(self.examples["architecture"])
        a["edges"][0]["protocol"]=""
        self.assertFalse(validate(a)["ok"])
        a=deepcopy(self.examples["activity"])
        a["nodes"][1]["id"]=a["nodes"][0]["id"]
        self.assertFalse(validate(a)["ok"])

if __name__=="__main__":
    unittest.main()
