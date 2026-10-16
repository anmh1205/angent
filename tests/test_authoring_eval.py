"""Executable checks for the authoring evaluation protocol, not model proficiency."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "evaluate_authoring.py"
spec = importlib.util.spec_from_file_location("authoring_eval", TARGET)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AuthoringEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.cases = module.load_cases(ROOT / "evals" / "authoring" / "cases.json")
        self.case = self.cases["chat-short"]

    def trial(self, before=None, after=None):
        before = before or ["PASS", "FAIL"]
        after = after or ["PASS", "PASS"]
        keys = list(self.case["criteria"])
        def record(identity, verdicts):
            return {
                "identity": identity,
                "model": "same-model",
                "host": "same-host",
                "input_ref": "frozen-context-1",
                "output_ref": f"reviewed-output-{identity}",
                "ratings": {k: {"verdict": v, "evidence": f"reviewed excerpt {k}"} for k, v in zip(keys, verdicts)}
            }
        return {"case_id": self.case["id"], "baseline": record("old", before), "candidate": record("new", after)}

    def test_case_coverage(self):
        self.assertGreaterEqual(len(self.cases), 12)
        self.assertGreaterEqual(sum(x["negative_control"] for x in self.cases.values()), 2)
        genres = {x["genre"] for x in self.cases.values()}
        self.assertTrue({"chat", "audit", "research", "status", "education", "publication"} <= genres)

    def test_missing_runs_are_not_pass(self):
        result = module.compare(self.cases, {"schema_version": 1, "trials": []})
        self.assertEqual(result["verdict"], "NOT_YET_VERIFIED")

    def test_improvement_per_case_not_global_proof(self):
        result = module.compare(self.cases, {"schema_version": 1, "trials": [self.trial()]})
        self.assertEqual(result["cases"][0]["outcome"], "IMPROVEMENT")
        self.assertEqual(result["verdict"], "NOT_YET_VERIFIED")

    def test_regression_detection(self):
        row = self.trial(before=["PASS", "PASS"], after=["FAIL", "PASS"])
        result = module.compare(self.cases, {"schema_version": 1, "trials": [row]})
        self.assertEqual(result["cases"][0]["outcome"], "REGRESSION")

    def test_non_comparable_model_blocked(self):
        row = self.trial()
        row["candidate"]["model"] = "different-model"
        result = module.compare(self.cases, {"schema_version": 1, "trials": [row]})
        self.assertEqual(result["cases"][0]["outcome"], "INCOMPARABLE")

    def test_missing_review_evidence_rejected(self):
        row = self.trial()
        k = next(iter(self.case["criteria"]))
        row["candidate"]["ratings"][k]["evidence"] = ""
        with self.assertRaises(module.EvaluationError):
            module.compare(self.cases, {"schema_version": 1, "trials": [row]})

    def test_duplicate_cases_rejected(self):
        row = self.trial()
        with self.assertRaises(module.EvaluationError):
            module.compare(self.cases, {"schema_version": 1, "trials": [row, row]})


if __name__ == "__main__":
    unittest.main()
