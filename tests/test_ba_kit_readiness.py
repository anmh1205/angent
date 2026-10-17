"""Kit readiness report is evidence-limited rather than a synthetic release pass."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("kit_readiness",ROOT/"scripts/report_kit_readiness.py")
module=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

class KitReleaseEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory=json.loads((ROOT/"hub/research/ba-figma-audit-67.json").read_text(encoding="utf8"))
        cls.cases=json.loads((ROOT/"evals/ba-figma/scenarios.json").read_text(encoding="utf8"))

    def test_every_skill_and_eval_is_explicitly_pending_live_proof(self):
        result=module.summarize(self.inventory,self.cases)
        self.assertEqual(result["capability_records"],67)
        self.assertEqual(result["case_count"],13)
        self.assertEqual(result["cases_pending"],13)
        self.assertEqual(result["verified_capability_claims"],0)
        self.assertEqual(result["release_readiness"],"NOT_YET_VERIFIED")
        self.assertFalse(result["merged"])
        self.assertEqual(result["evidence_tiers"]["payload-verified"],6)
        self.assertEqual(result["evidence_tiers"]["provider-blocked"],10)

    def test_unreviewed_method_cannot_be_silently_promoted(self):
        rows=json.loads(json.dumps(self.inventory))
        target=next(r for r in rows if r["evidence"]=="method")
        target["evidence"]="runtime-mock"
        with self.assertRaisesRegex(ValueError,"lacks proof"):
            module.summarize(rows,self.cases)

    def test_duplicate_scenario_coverage_rejected(self):
        cases=json.loads(json.dumps(self.cases))
        cases[0]["skills"].append(cases[1]["skills"][0])
        with self.assertRaisesRegex(ValueError,"coverage"):
            module.summarize(self.inventory,cases)

if __name__=="__main__":
    unittest.main()
