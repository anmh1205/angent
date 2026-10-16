"""Core benchmark catalog integrity; not proof of a running model's quality."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("eval_generic", ROOT / "scripts" / "evaluate_authoring.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CoreCatalogTests(unittest.TestCase):
    def test_core_behaviors_and_controls(self):
        cases = module.load_cases(ROOT / "evals" / "core" / "cases.json")
        self.assertGreaterEqual(len(cases), 12)
        self.assertGreaterEqual(sum(c["negative_control"] for c in cases.values()), 2)
        genres = {c["genre"] for c in cases.values()}
        self.assertTrue({"reasoning", "research", "context", "memory", "execution", "learning", "routing", "quality"} <= genres)
        result = module.compare(cases, {"schema_version": 1, "trials": []})
        self.assertEqual(result["verdict"], "NOT_YET_VERIFIED")


if __name__ == "__main__":
    unittest.main()
