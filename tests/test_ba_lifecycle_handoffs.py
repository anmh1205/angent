"""Evidence-backed BA handoffs: checked gaps are not confused with missing input."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from audit_lifecycle_handoffs import inspect
from extract_markdown_graph import collect

class BAHandoffAssurance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=BA/"examples"
        feat=root/"docs/atlas-re"
        cls.atlas=collect({
            "urd":feat/"atlas-re-urd.md",
            "brd":feat/"atlas-re-brd.md",
            "prd":feat/"atlas-re-prd.md",
            "srs":feat/"srs/atlas-re-spec.md",
            "checklist":feat/"test/checklist/atlas-re-checklist-index.md",
            "cases":feat/"test/testcases/atlas-re-testcase-index.md",
            "stories":feat/"userstories/atlas-re-story-index.md",
            "usecases":feat/"usecases/atlas-re-usecase-index.md",
        },root)["graph"]
        cls.fleet=json.loads((BA/"examples/rental-fleet-traceability.json").read_text(encoding="utf-8"))

    def test_full_lifecycle_reports_genuine_missing_test_links(self):
        report=inspect(self.atlas)
        self.assertTrue(report["ok"])
        stages={row["stage"]:row for row in report["stages"]}
        early=("need_to_objective","objective_to_capability","capability_to_requirement")
        self.assertTrue(all(stages[k]["state"]=="inspected" for k in early))
        self.assertEqual(stages["capability_to_requirement"]["target_count"],8)
        self.assertEqual(stages["functional_requirement_to_test"]["source_count"],8)
        self.assertEqual(stages["functional_requirement_to_test"]["verified_links"],4)
        self.assertEqual(len(stages["functional_requirement_to_test"]["missing"]),4)
        self.assertEqual(len(report["test_artifacts_without_execution_evidence"]),
                         len([x for x in self.atlas["artifacts"] if x["kind"]=="TEST"]))
        self.assertGreater(len(report["test_artifacts_without_execution_evidence"]),
                           stages["functional_requirement_to_test"]["verified_links"])
        self.assertFalse(report["writes_performed"])
        for source,path in stages["functional_requirement_to_test"]["witness_paths"].items():
            self.assertEqual(source,path[0])
            self.assertTrue(path[-1].startswith("TC-"))
        self.assertFalse(inspect(self.atlas,require_known_handoffs=True)["ok"])

    def test_no_false_failure_for_uninspected_document_types(self):
        subset=deepcopy(self.fleet)
        subset["artifacts"]=[entry for entry in subset["artifacts"] if entry["kind"] not in ("NFR","NEED")]
        report=inspect(subset,require_known_handoffs=True)
        stages={row["stage"]:row for row in report["stages"]}
        self.assertEqual(stages["need_to_objective"]["state"],"not-inspected")
        self.assertEqual(stages["quality_requirement_to_test"]["state"],"not-inspected")
        self.assertIn("need_to_objective",report["not_inspected_stages"])
        self.assertFalse(report["writes_performed"])

    def test_false_lineage_cannot_be_washed_through_story_membership(self):
        # A broad story may encompass the requirement, but only a test/AC/
        # checklist chain explicitly referencing the requirement can count.
        graph=deepcopy(self.atlas)
        test=next(item for item in graph["artifacts"] if item["kind"]=="TEST")
        fr=next(item for item in graph["artifacts"] if item["kind"]=="FR")
        story=next(item for item in graph["artifacts"] if item["kind"]=="STORY")
        test["depends_on"]=[story["id"]]
        result=inspect(graph)
        self.assertFalse(result["ok"])  # Invalid reverse typed link, fail closed.

    def test_self_reported_pass_is_not_runtime_execution_evidence(self):
        graph=deepcopy(self.atlas)
        test=next(item for item in graph["artifacts"] if item["kind"]=="TEST")
        test["verification_status"]="passed"
        report=inspect(graph)
        self.assertTrue(report["ok"], report)
        self.assertIn(test["id"],report["test_artifacts_claimed_executed_but_unverified"])
        self.assertIn(test["id"],report["test_artifacts_without_execution_evidence"])
        self.assertFalse(report["writes_performed"])

    def test_missing_source_graph_fails_closed(self):
        bad=deepcopy(self.fleet)
        bad["artifacts"][0]["depends_on"]=["FR-NO-SOURCE"]
        report=inspect(bad)
        self.assertFalse(report["ok"])
        self.assertTrue(any("missing dependency" in x for x in report["errors"]))

if __name__=="__main__":
    unittest.main()
