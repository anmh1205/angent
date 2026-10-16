"""Behavioral structural checks for standalone BA evidence and Figma models."""
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
BA = ROOT / "extensions/angent-ba"
FIGMA = ROOT / "extensions/angent-figma"
sys.path.insert(0, str(BA / "scripts"))
sys.path.insert(0, str(FIGMA / "scripts"))
from validate_artifacts import audit as audit_ba
from change_impact import impact
from validate_diagram_model import audit as audit_figma

class BAAndFigmaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ba = json.loads((BA / "examples/rental-fleet-traceability.json").read_text())
        cls.fig = json.loads((FIGMA / "examples/rental-fleet-activity.json").read_text())

    def test_full_skill_and_template_inventory(self):
        self.assertEqual(len(list((BA / "skills").glob("*/SKILL.md"))), 55)
        self.assertEqual(len(list((FIGMA / "skills").glob("*/SKILL.md"))), 12)
        self.assertEqual(len(list((BA / "skills/ba-kg/references/templates").glob("*.md"))), 48)
        self.assertEqual(len(list((BA / "skills/ba-kg/references/rules").glob("*.md"))), 19)

    def test_graph_valid_and_coverage(self):
        result = audit_ba(self.ba, require_tests=True)
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["coverage"]["traced_to_test"], 1)

    def test_dangling_refs_and_cycle_are_errors(self):
        data = json.loads(json.dumps(self.ba))
        data["artifacts"][0]["depends_on"] = ["FR-IVTS-01", "UNKNOWN-XYZ"]
        outcome = audit_ba(data)
        self.assertFalse(outcome["ok"])
        self.assertTrue(any("missing dependency" in e for e in outcome["errors"]))
        self.assertTrue(any("cycle" in e for e in outcome["errors"]))

    def test_real_change_impact_traces_reverse_dependencies(self):
        outcome = impact(self.ba, ["BR-IVTS-01"])
        self.assertTrue(outcome["ok"])
        self.assertEqual(outcome["affected"], ["AC-IVTS-01","FR-IVTS-01","TC-IVTS-01"])
        self.assertEqual(outcome["impact_paths"]["TC-IVTS-01"], ["BR-IVTS-01","FR-IVTS-01","AC-IVTS-01","TC-IVTS-01"])
        self.assertFalse(outcome["writes_performed"])

    def test_bad_change_does_not_modify(self):
        self.assertFalse(impact(self.ba, ["UNKNOWN"])["ok"])

    def test_figma_graph_validation_success(self):
        out = audit_figma(self.fig)
        self.assertTrue(out["ok"], out)
        self.assertFalse(out["rendered_or_written_to_figma"])

    def test_figma_missing_node_and_unlabeled_guard_fail(self):
        model = json.loads(json.dumps(self.fig))
        model["edges"][1]["to"] = "MISSING"
        model["edges"][2].pop("guard")
        out = audit_figma(model)
        self.assertFalse(out["ok"])
        self.assertTrue(any("unknown endpoint" in e for e in out["errors"]))
        self.assertTrue(any("unlabeled guard" in e for e in out["errors"]))

    def test_sitemap_cycle_fails(self):
        diagram = {"type":"sitemap", "nodes":[{"id":"a","label":"A"},{"id":"b","label":"B"}],
                   "edges":[{"from":"a","to":"b"},{"from":"b","to":"a"}]}
        self.assertFalse(audit_figma(diagram)["ok"])

if __name__ == "__main__":
    unittest.main()
