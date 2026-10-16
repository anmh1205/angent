"""Deep real-world BA graphs must be audited without Python recursion failures."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "extensions/angent-ba/scripts"))
from validate_artifacts import audit


class DeepGraphAuditTests(unittest.TestCase):
    @staticmethod
    def large_chain(count=1600):
        artifacts = []
        for i in range(count):
            artifacts.append({
                "id": f"CAP-LONG-{i:04d}", "kind": "CAPABILITY",
                "title": f"Capability {i}",
                "depends_on": [f"CAP-LONG-{i-1:04d}"] if i else [],
                "source_refs": ["SRC-LONG"],
            })
        return {"sources": [{"id": "SRC-LONG", "uri": "example.md"}],
                "artifacts": artifacts}

    def test_long_acyclic_lineage_is_valid(self):
        result = audit(self.large_chain())
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["artifact_count"], 1600)

    def test_long_back_edge_reports_cycle_instead_of_crashing(self):
        graph = self.large_chain()
        graph["artifacts"][0]["depends_on"] = ["CAP-LONG-1599"]
        result = audit(graph)
        self.assertFalse(result["ok"])
        self.assertTrue(any("dependency cycle" in error for error in result["errors"]), result)


if __name__ == "__main__":
    unittest.main()
