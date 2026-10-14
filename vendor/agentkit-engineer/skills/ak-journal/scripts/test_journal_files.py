"""Journal file contract, collision and refusal regression tests."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("journal_files.py")


class JournalTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def invoke(self, *args: str, input: str = "") -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), "--project-root", str(self.root),
                               *args], text=True, input=input, capture_output=True)

    def test_create_collision_safe_read_back_and_validation(self):
        args = ("create", "--title", "Fix install race", "--date", "2026-10-15",
                "--summary", "Evidence-linked race fix", "--stdin")
        first = self.invoke(*args, input="Cause: reordering\nResult: fixed\n")
        second = self.invoke(*args, input="Different evidence\n")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        a = json.loads(first.stdout)["name"]
        b = json.loads(second.stdout)["name"]
        self.assertNotEqual(a, b)
        self.assertEqual(self.invoke("validate", "--name", a).returncode, 0)
        result = self.invoke("show", "--name", a)
        self.assertIn("Cause: reordering", json.loads(result.stdout)["content"])
        self.assertNotIn("Different evidence", result.stdout)
        self.assertIn(a, json.loads(self.invoke("list").stdout)["entries"])
        self.assertIn(b, json.loads(self.invoke("list").stdout)["entries"])

    def test_list_only_does_not_create_folder(self):
        p = self.root / "plans" / "journals"
        result = self.invoke("list")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["entries"], [])
        self.assertFalse(p.exists())

    def test_invalid_title_and_date_rejected(self):
        self.assertEqual(self.invoke("create", "--title", "../bad", "--date",
                                     "2026-99-01").returncode, 2)
        self.assertEqual(self.invoke("create", "--title", "test\nnext").returncode, 2)

    def test_untrusted_entry_name_cannot_traverse(self):
        self.invoke("create", "--title", "safe", "--date", "2026-10-15")
        self.assertEqual(self.invoke("show", "--name", "../../secret.md").returncode, 2)

    def test_modified_frontmatter_fails_without_mutating(self):
        created = json.loads(self.invoke("create", "--title", "Bug",
                                         "--date", "2026-10-15").stdout)
        path = Path(created["path"])
        path.write_text(path.read_text(encoding="utf-8").replace(
            "date: 2026-10-15", "date: 2026-10-14"), encoding="utf-8")
        before = path.read_text(encoding="utf-8")
        checked = self.invoke("validate", "--name", path.name)
        self.assertEqual(checked.returncode, 3)
        self.assertIn("filename_date_mismatch", checked.stdout)
        self.assertEqual(before, path.read_text(encoding="utf-8"))

    def test_journal_directory_symlink_escape_rejected(self):
        outside = Path(self.temp.name).parent
        plan = self.root / "plans"
        plan.mkdir()
        try:
            (plan / "journals").symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("no symlink support")
        self.assertEqual(self.invoke("create", "--title", "Oops").returncode, 2)


if __name__ == "__main__":
    unittest.main()
