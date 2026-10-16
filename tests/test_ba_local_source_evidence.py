"""BA source evidence claims are linked to actual files when local proof requested."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from validate_artifacts import audit

class LocalSourceEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.graph=json.loads((BA/"examples/rental-fleet-traceability.json").read_text(encoding="utf8"))

    def test_synthetic_source_is_real_and_no_approval_forged(self):
        self.assertEqual(len(self.graph["artifacts"]),5)
        self.assertTrue(all(item.get("status")!="approved" for item in self.graph["artifacts"]))
        result=audit(self.graph,source_root=BA)
        self.assertTrue(result["ok"],result)
        text=(BA/"examples/synthetic-requirement.md").read_text(encoding="utf8")
        self.assertIn("Demonstration Data Only",text)
        self.assertIn("FR-IVTS-02",text)
        self.assertEqual(result["coverage"]["uncovered"],["FR-IVTS-02"])

    def test_rejects_missing_and_escaping_source_files(self):
        bad=json.loads(json.dumps(self.graph))
        bad["sources"][0]["uri"]="examples/no-such-source.md"
        self.assertTrue(any("missing" in x for x in audit(bad,source_root=BA)["errors"]))
        bad["sources"][0]["uri"]="../AGENTS.md"
        self.assertTrue(any("escapes" in x for x in audit(bad,source_root=BA)["errors"]))
        with tempfile.TemporaryDirectory() as root:
            self.assertFalse(audit(self.graph,source_root=Path(root))["ok"])

    def test_external_links_are_not_treated_as_verified_local_files(self):
        alternate=json.loads(json.dumps(self.graph))
        alternate["sources"][0]["uri"]="https://iiba.org/example-requirement"
        result=audit(alternate,source_root=BA)
        self.assertTrue(result["ok"])
        self.assertTrue(any("external" in msg for msg in result["warnings"]))

if __name__=="__main__":
    unittest.main()
