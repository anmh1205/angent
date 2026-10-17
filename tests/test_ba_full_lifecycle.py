"""Verify the full BA need → objective → capability → FR → test links from real Atlas docs."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from extract_markdown_graph import collect
from validate_artifacts import audit

class FullLifecycleSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base=BA/"examples"
        feat=base/"docs/atlas-re"
        cls.files={
            "urd":feat/"atlas-re-urd.md",
            "brd":feat/"atlas-re-brd.md",
            "prd":feat/"atlas-re-prd.md",
            "srs":feat/"srs/atlas-re-spec.md",
            "checklist":feat/"test/checklist/atlas-re-checklist-index.md",
            "cases":feat/"test/testcases/atlas-re-testcase-index.md",
            "stories":feat/"userstories/atlas-re-story-index.md",
            "usecases":feat/"usecases/atlas-re-usecase-index.md",
        }
        cls.report=collect(cls.files,base)

    def test_end_to_end_linked_from_actual_markdown(self):
        report=self.report
        self.assertTrue(audit(report["graph"])["ok"])
        counts=report["counts"]
        self.assertEqual(counts["NEED"],6)
        self.assertEqual(counts["BUSINESS_OBJECTIVE"],4)
        self.assertEqual(counts["CAPABILITY"],6)
        self.assertEqual(counts["FR"],8)
        self.assertEqual(sum(counts.values()),58)
        self.assertEqual(report["lifecycle"]["functional_requirements"],8)
        self.assertEqual(report["lifecycle"]["fr_traced_via_capability_objective_need"],8)
        self.assertEqual(report["lifecycle"]["fr_linked_to_test_artifact"],4)
        self.assertEqual(report["lifecycle"]["fr_with_complete_structural_chain"],4)
        self.assertEqual(report["lifecycle"]["missing_upstream_chain"],[])
        self.assertEqual(len(report["lifecycle"]["missing_test_artifact"]),4)

    def test_concrete_source_rows_and_preexisting_stable_ids(self):
        byid={item["id"]:item for item in self.report["graph"]["artifacts"]}
        self.assertEqual(byid["BO-atlas-re-03"]["depends_on"],["UN-atlas-re-005"])
        self.assertIn("BO-atlas-re-03",byid["CAP-atlas-re-04"]["depends_on"])
        self.assertIn("CAP-atlas-re-04",byid["FR-atlas-re-006"]["depends_on"])
        self.assertEqual(byid["UN-atlas-re-005"]["source_refs"],["SOURCE-URD"])
        self.assertEqual(byid["FR-atlas-re-006"]["source_refs"],["SOURCE-SRS"])

    def test_requirement_proofs_are_true_graph_edges(self):
        proofs={item["id"]:item for item in self.report["lifecycle"]["per_requirement"]}
        self.assertEqual(len(proofs),8)
        actual=proofs["FR-atlas-re-006"]
        self.assertEqual(actual["upstream_path"],[
            "UN-atlas-re-005","BO-atlas-re-03","CAP-atlas-re-04","FR-atlas-re-006"
        ])
        self.assertTrue(actual["complete_structural_chain"])
        self.assertEqual(actual["test_execution_status"],"not-executed")
        self.assertTrue(actual["test_path"][-1].startswith("TC-"))
        self.assertEqual(actual["source"]["uri"],"docs/atlas-re/srs/atlas-re-spec.md")
        without_test=[row for row in proofs.values() if row["test_path"] is None]
        self.assertEqual(len(without_test),4)
        self.assertTrue(all(row["test_execution_status"]=="no-test-artifact" for row in without_test))
        byid={item["id"]:item for item in self.report["graph"]["artifacts"]}
        for item in proofs.values():
            for path in (item["upstream_path"],item["test_path"]):
                if not path:
                    continue
                for idx in range(1,len(path)):
                    self.assertIn(path[idx-1],byid[path[idx]]["depends_on"])

    def test_no_fake_full_coverage_when_parent_removed(self):
        # Presence of correct IDs alone is not proof the ancestry is linked.
        files={key:val for key,val in self.files.items() if key not in ("urd","brd","prd")}
        subset=collect(files,BA/"examples")
        self.assertEqual(subset["lifecycle"]["fr_traced_via_capability_objective_need"],0)
        self.assertEqual(subset["lifecycle"]["fr_with_complete_structural_chain"],0)
        self.assertEqual(subset["lifecycle"]["fr_linked_to_test_artifact"],4)
        self.assertTrue(subset["unresolved_external_refs"])

if __name__=="__main__":
    unittest.main()
