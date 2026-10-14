"""Project-local Plan scaffold and read-only phase inspection test cases."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("plan_files.py")


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def invoke(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), "--project-root",
                               str(self.root), *args], capture_output=True, text=True)

    def make_plan(self) -> dict:
        r = self.invoke("create", "--title", "Fleet device runtime")
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout)

    def test_create_status_validate_and_add_phase(self):
        result = self.make_plan()
        self.assertFalse(result["accepted"])
        plan_id = result["plan_id"]
        self.assertEqual(self.invoke("validate", "--plan-id", plan_id).returncode, 0)
        add = self.invoke("add-phase", "--plan-id", plan_id, "--title", "Cloud sync")
        self.assertEqual(add.returncode, 0, add.stderr)
        report = json.loads(self.invoke("status", "--plan-id", plan_id).stdout)
        self.assertEqual(report["phase_count"], 2)
        self.assertEqual(report["unchecked_total"], 2)
        self.assertEqual(report["acceptance"], "requires_independent_evidence")
        self.assertIn(plan_id, json.loads(self.invoke("list").stdout)["plans"])

    def test_duplicate_create_preserves_all_plans(self):
        a = self.make_plan()
        b = self.make_plan()
        self.assertNotEqual(a["plan_id"], b["plan_id"])
        self.assertTrue(Path(a["plan_file"]).is_file())
        self.assertTrue(Path(b["plan_file"]).is_file())

    def test_status_is_read_only_and_not_acceptance(self):
        a = self.make_plan()
        phase = Path(a["plan_file"]).parent / "phase-01-start.md"
        phase.write_text(phase.read_text(encoding="utf-8").replace(
            "- [ ]", "- [x]"), encoding="utf-8")
        prior = phase.read_bytes()
        result = json.loads(self.invoke("status", "--plan-id", a["plan_id"]).stdout)
        self.assertEqual(result["checked_total"], 1)
        self.assertEqual(result["acceptance"], "requires_independent_evidence")
        self.assertEqual(prior, phase.read_bytes())

    def test_invalid_plan_does_not_pass_validation(self):
        a = self.make_plan()
        Path(a["plan_file"]).unlink()
        result = self.invoke("validate", "--plan-id", a["plan_id"])
        self.assertEqual(result.returncode, 3)
        self.assertIn("missing_plan_md", result.stdout)

    def test_path_traversal_denied(self):
        result = self.invoke("status", "--plan-id", "../../etc")
        self.assertEqual(result.returncode, 2)

    def test_listing_does_not_create_folder(self):
        result = self.invoke("list")
        self.assertEqual(result.returncode, 0)
        self.assertFalse((self.root / "plans").exists())

    def test_symlinked_plans_folder_denied(self):
        try:
            (self.root / "plans").symlink_to(Path(self.tmp.name).parent,
                                            target_is_directory=True)
        except OSError:
            self.skipTest("symlinks unavailable")
        self.assertEqual(self.invoke("create", "--title", "Unsafe").returncode, 2)

    def test_phase_number_uniqueness_checked(self):
        a = self.make_plan()
        plan = Path(a["plan_file"]).parent
        (plan / "phase-01-duplicate.md").write_text("# duplicate", encoding="utf-8")
        result = self.invoke("validate", "--plan-id", a["plan_id"])
        self.assertEqual(result.returncode, 3)
        self.assertIn("duplicate_phase_number", result.stdout)


if __name__ == "__main__":
    unittest.main()
