"""Complete Reqwise OSS six-kind evidence and skill-to-runner parity audit.

Checks all kinds, source IDs and dry-run request format; does NOT claim
Figma canvas writes without an actual native MCP session.
"""
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
FIGMA=ROOT/"extensions/angent-figma"
sys.path.insert(0,str(BA/"scripts"))
sys.path.insert(0,str(FIGMA/"scripts"))
from validate_artifacts import audit
from to_reqwise_payload import compile_model

SIX=("activity","erd","sequence","state","sitemap","userflow")

class SixOSSFigmaMethodsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph=json.loads((BA/"examples/rental-fleet-traceability.json").read_text(encoding="utf8"))
        cls.ids={node["id"] for node in cls.graph["artifacts"]}

    def test_every_public_oss_kind_has_a_source_linked_dry_run(self):
        self.assertTrue(audit(self.graph,source_root=BA)["ok"])
        for name in SIX:
            with self.subTest(name=name):
                path=FIGMA/"examples"/("rental-fleet-"+name+".json")
                self.assertTrue(path.is_file())
                model=json.loads(path.read_text(encoding="utf8"))
                self.assertEqual(model["type"],name)
                self.assertTrue(model.get("source_refs"))
                payload=compile_model(model,evidence_ids=self.ids)
                self.assertEqual(payload["tool"],"figma_diagram")
                self.assertEqual(payload["arguments"]["type"],name)
                self.assertTrue(payload["dry_run"])
                self.assertFalse(payload["writes_performed"])
                self.assertEqual(payload["source_link_check"],"ids-resolved-only")
                expected=FIGMA/"skills"/("figma-"+name)/"SKILL.md"
                skill=expected.read_text(encoding="utf8")
                self.assertIn("to_reqwise_payload.py",skill)
                self.assertIn(path.name,skill)
                self.assertIn("get_diagram_spec",skill)
                self.assertIn("layout_audit",skill)
                self.assertIn("not written to Figma",skill)

    def test_every_pro_only_method_denies_false_oss_support(self):
        for name in ("bpmn","usecase","journey","persona","design-system","demo"):
            with self.subTest(name=name):
                text=(FIGMA/"skills"/("figma-"+name)/"SKILL.md").read_text(encoding="utf8").lower()
                self.assertGreater(len(text),1350)
                self.assertTrue("oss" in text or "native" in text or "pro" in text)
                self.assertTrue("not" in text or "only" in text)
                self.assertFalse("to_reqwise_payload.py" in text and "supports "+name in text)

if __name__=="__main__":
    unittest.main()
