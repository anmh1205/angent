"""Real BA revision comparison, dependency propagation and source churn."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from compare_artifact_revisions import compare
from validate_artifacts import audit

BASE=json.loads((ROOT/"extensions/angent-ba/examples/rental-fleet-traceability.json").read_text(encoding="utf8"))

class RevisionDiffTests(unittest.TestCase):
    def test_meaningful_change_marks_transitive_dependents(self):
        revised=copy.deepcopy(BASE)
        revised["artifacts"][0]["title"]="Only authorized fleet managers may read vehicle status"
        result=compare(BASE,revised)
        self.assertEqual(len(result["modified"]),1)
        self.assertEqual(result["modified"][0]["id"],"BR-IVTS-01")
        self.assertEqual(list(result["modified"][0]["fields"]),["title"])
        self.assertIn("TC-IVTS-01",result["dependent_review"])
        self.assertEqual(result["dependent_review"]["TC-IVTS-01"][0],
                         ["BR-IVTS-01","FR-IVTS-01","AC-IVTS-01","TC-IVTS-01"])
        self.assertFalse(result["writes_performed"])
        self.assertEqual(result["approval_status"],"not-established")

    def test_adding_and_removing_requirements(self):
        revised=copy.deepcopy(BASE)
        revised["artifacts"].append({"id":"FR-IVTS-03","kind":"FR","title":"Show telemetry age",
                                     "status":"draft","depends_on":["BR-IVTS-01"],"source_refs":["SRC-01"]})
        added=compare(BASE,revised)
        self.assertEqual(added["added"],["FR-IVTS-03"])
        removed=compare(revised,BASE)
        self.assertEqual(removed["removed"],["FR-IVTS-03"])
        self.assertEqual(removed["review_required"],["FR-IVTS-03"])

    def test_source_revision_is_review_not_proof_of_changed_rule(self):
        revised=copy.deepcopy(BASE)
        revised["sources"][0]["revision"]="new-edition"
        result=compare(BASE,revised)
        self.assertEqual(result["modified"],[])
        self.assertEqual(len(result["source_changes"]),1)
        self.assertIn("TC-IVTS-01",result["review_required"])
        self.assertIn("BR-IVTS-01",result["direct_review"])
        self.assertEqual(result["scope"].startswith("document/evidence graph"),True)

    def test_invalid_graph_versions_rejected(self):
        revised=copy.deepcopy(BASE)
        revised["artifacts"][1]["depends_on"].append("UNKNOWN")
        self.assertFalse(audit(revised)["ok"])
        with self.assertRaisesRegex(ValueError,"after graph invalid"):
            compare(BASE,revised)
        with self.assertRaisesRegex(ValueError,"before graph invalid"):
            compare(revised,BASE)

    def test_no_change_is_no_drama(self):
        result=compare(BASE,copy.deepcopy(BASE))
        self.assertEqual(result["added"],[])
        self.assertEqual(result["removed"],[])
        self.assertEqual(result["modified"],[])
        self.assertEqual(result["review_required"],[])
        self.assertEqual(result["dependent_review"],{})
        self.assertTrue(result["ok"])

if __name__=="__main__":
    unittest.main()
