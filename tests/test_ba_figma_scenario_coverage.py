"""Every BA and Figma specialist has a concrete acceptance scenario, not a fake pass."""
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SCENARIOS=ROOT/"evals/ba-figma/scenarios.json"
INVENTORY=ROOT/"hub/research/ba-figma-audit-67.json"

class SpecialistScenarioCoverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenarios=json.loads(SCENARIOS.read_text(encoding="utf8"))
        cls.inventory=json.loads(INVENTORY.read_text(encoding="utf8"))

    def test_all_67_specialists_have_specific_falsifiable_acceptance(self):
        assigned=[]
        for case in self.scenarios:
            with self.subTest(case=case["id"]):
                self.assertGreater(len(case["input"]),90)
                self.assertGreaterEqual(len(case["must"]),3)
                self.assertGreaterEqual(len(case["reject"]),2)
                self.assertEqual(case["execution_status"],"not-run")
                self.assertFalse(case["approved_business_facts"])
                self.assertEqual(case["live_provider_writes"],0)
                self.assertNotIn("TODO",str(case).upper())
                assigned.extend(case["skills"])
        all_names={x["skill"] for x in self.inventory}
        self.assertEqual(len(assigned),67)
        self.assertEqual(set(assigned),all_names)
        self.assertEqual(len(set(assigned)),67)

    def test_provider_cases_cannot_self_claim_live_results(self):
        for case in self.scenarios:
            if any(x.startswith("figma-") for x in case["skills"]) or "ba-jira" in case["skills"]:
                self.assertEqual(case["execution_status"],"not-run")
                self.assertEqual(case["live_provider_writes"],0)
                self.assertIn("provider",case["scope"].lower()) if "ba-jira" in case["skills"] else self.assertTrue(
                    "provider" in case["scope"].lower() or "figma" in case["scope"].lower())
                self.assertTrue(any("claim" in rule.lower() or "pretend" in rule.lower()
                                    or "report" in rule.lower() for rule in case["reject"]),
                                "A falsifiable false-success condition is required")

if __name__=="__main__":
    unittest.main()
