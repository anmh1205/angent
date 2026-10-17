"""Cross-kit BA evidence checks reject backwards or circular justifications."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from validate_artifacts import audit
from extract_markdown_graph import collect

class TypedRequirementLineageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fleet=json.loads((BA/"examples/rental-fleet-traceability.json").read_text(encoding="utf8"))
        base=BA/"examples"
        feat=base/"docs/atlas-re"
        cls.atlas=collect({
            "urd":feat/"atlas-re-urd.md",
            "brd":feat/"atlas-re-brd.md",
            "prd":feat/"atlas-re-prd.md",
            "srs":feat/"srs/atlas-re-spec.md",
            "checklist":feat/"test/checklist/atlas-re-checklist-index.md",
            "cases":feat/"test/testcases/atlas-re-testcase-index.md",
            "stories":feat/"userstories/atlas-re-story-index.md",
            "usecases":feat/"usecases/atlas-re-usecase-index.md",
        },base)["graph"]

    def test_real_lifecycles_continue_to_validate(self):
        for graph in (self.fleet,self.atlas):
            outcome=audit(graph)
            self.assertTrue(outcome["ok"],outcome)

    def test_reverse_link_fails_even_when_every_id_exists(self):
        atlas_tc=next(x["id"] for x in self.atlas["artifacts"] if x["kind"]=="TEST")
        mutations=(
            (self.fleet,"FR-IVTS-02","TC-IVTS-01"),
            (self.fleet,"BR-IVTS-01","TC-IVTS-01"),
            (self.atlas,"BO-atlas-re-03",atlas_tc),
        )
        for graph,child,target in mutations:
            with self.subTest(child=child,target=target):
                changed=copy.deepcopy(graph)
                ids={x["id"]:x for x in changed["artifacts"]}
                self.assertIn(child,ids)
                self.assertIn(target,ids)
                ids[child]["depends_on"]=[target]
                result=audit(changed)
                self.assertFalse(result["ok"])
                self.assertTrue(any("invalid BA evidence dependency type" in err for err in result["errors"]),
                                result["errors"])

    def test_known_legal_partial_evidence_is_not_auto_approved(self):
        outcome=audit(self.fleet)
        self.assertTrue(outcome["ok"])
        self.assertEqual(outcome["coverage"]["functional_requirements"],2)
        self.assertEqual(outcome["coverage"]["traced_to_test"],1)
        self.assertIn("FR-IVTS-02",outcome["coverage"]["uncovered"])

    def test_requirement_identity_type_mismatch_must_not_hide_coverage(self):
        original=copy.deepcopy(self.fleet)
        for ident,wrong in (("FR-IVTS-01","BR"),("TC-IVTS-01","FR"),
                            ("AC-IVTS-01","TEST")):
            with self.subTest(artifact=ident):
                model=copy.deepcopy(original)
                next(x for x in model["artifacts"] if x["id"]==ident)["kind"]=wrong
                result=audit(model)
                self.assertFalse(result["ok"])
                self.assertTrue(any("ID prefix" in x for x in result["errors"]),result)
        bad=copy.deepcopy(original)
        bad["sources"][0]["id"]="SRC INVALID"
        bad["artifacts"][0]["source_refs"]=["SRC INVALID"]
        self.assertFalse(audit(bad)["ok"])
        self.assertTrue(any("invalid source identity" in x for x in audit(bad)["errors"]))

    def test_custom_domain_kinds_do_not_break_existing_project_models(self):
        graph=copy.deepcopy(self.fleet)
        graph["artifacts"].append({"id":"NOTE-IVTS-01","kind":"DESIGN_NOTE",
                                   "title":"Research evidence","depends_on":["FR-IVTS-01"],
                                   "source_refs":[graph["sources"][0]["id"]]})
        self.assertTrue(audit(graph)["ok"])

if __name__=="__main__":
    unittest.main()
