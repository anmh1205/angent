"""Malformed model data must fail closed rather than crashing the validator."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "extensions/angent-figma/scripts"))
from validate_diagram_model import audit

class DiagramInputSafetyTests(unittest.TestCase):
    def test_unhashable_diagram_kind(self):
        result = audit({"type": ["activity"], "nodes": [], "edges": []})
        self.assertFalse(result["ok"])
        self.assertIn("Unsupported type", result["errors"])

    def test_invalid_node_id_with_spaces(self):
        result = audit({"type":"sequence", "nodes":[{"id":"Node One", "label":"A"}], "edges":[]})
        self.assertFalse(result["ok"])
        self.assertTrue(any("whitespace" in e for e in result["errors"]))

    def test_missing_arrays(self):
        self.assertFalse(audit({"type":"activity"})["ok"])

if __name__ == "__main__":
    unittest.main()
