"""Watzup local read-only scanner: realistic Git and plan fixtures."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("scan_local.py")


class WatzupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        subprocess.run(["git", "init", "-q", "-b", "main", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.email", "test@example.com"], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "Test"], check=True)
        (self.root / "plans").mkdir()
        (self.root / "plans" / "active.md").write_text(
            "# Plan\n- [x] Complete\n- [ ] Pending\n", encoding="utf-8")
        (self.root / "ROADMAP.md").write_text("# Roadmap\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-qm", "baseline"], check=True)
        subprocess.run(["git", "-C", str(self.root), "branch", "feature"], check=True)

    def tearDown(self):
        self.tmp.cleanup()

    def call(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root),
                               "--json", *args], capture_output=True, text=True)

    def test_clean_repo_plan_and_refs(self):
        out = self.call()
        self.assertEqual(out.returncode, 0, out.stderr)
        result = json.loads(out.stdout)
        self.assertEqual(result["current"]["branch"], "main")
        self.assertFalse(result["current"]["dirty"])
        self.assertIn("feature", result["refs"]["local"])
        active = next(p for p in result["plans"] if p["path"] == "plans/active.md")
        self.assertEqual((active["checked"], active["unchecked"]), (1, 1))
        self.assertTrue(result["next_steps"])
        self.assertFalse(result["complete_runtime_parity"])

    def test_dirty_tree_does_not_mutate_files(self):
        p = self.root / "ROADMAP.md"
        p.write_text("# Modified but not staged\n", encoding="utf-8")
        before = p.read_text(encoding="utf-8")
        out = self.call()
        self.assertEqual(out.returncode, 0, out.stderr)
        result = json.loads(out.stdout)
        self.assertTrue(result["current"]["dirty"])
        self.assertIn("preserve existing changes", result["next_steps"][0]["recommendation"])
        self.assertEqual(before, p.read_text(encoding="utf-8"))
        self.assertEqual(subprocess.run(["git", "-C", str(self.root), "status", "--porcelain"],
                                        capture_output=True, text=True).stdout.rstrip("\n"),
                         " M ROADMAP.md")

    def test_detached_head_report_not_repaired(self):
        subprocess.run(["git", "-C", str(self.root), "checkout", "--detach", "-q"], check=True)
        out = self.call()
        self.assertEqual(out.returncode, 0, out.stderr)
        result = json.loads(out.stdout)
        self.assertTrue(result["current"]["detached"])
        self.assertIsNone(result["current"]["branch"])

    def test_secondary_worktree_listing(self):
        location = Path(self.tmp.name) / "second"
        subprocess.run(["git", "-C", str(self.root), "worktree", "add", "-q",
                        str(location), "feature"], check=True)
        out = self.call()
        self.assertEqual(out.returncode, 0, out.stderr)
        branches = {item.get("branch") for item in json.loads(out.stdout)["worktrees"]}
        self.assertIn("main", branches)
        self.assertIn("feature", branches)

    def test_no_network_fetch_from_remote(self):
        subprocess.run(["git", "-C", str(self.root), "remote", "add",
                        "origin", "https://example.invalid/repository"], check=True)
        out = self.call()
        self.assertEqual(out.returncode, 0, out.stderr)
        result = json.loads(out.stdout)
        self.assertEqual(result["refs"]["remote_cached"], [])
        self.assertIn("no network fetch", result["limitations"][0])

    def test_symlink_plan_is_skipped(self):
        path = self.root / "plans" / "external.md"
        try:
            path.symlink_to(Path(__file__))
        except OSError:
            self.skipTest("symlinks unsupported")
        subprocess.run(["git", "-C", str(self.root), "add", "plans/external.md"], check=True)
        out = self.call()
        self.assertEqual(out.returncode, 0, out.stderr)
        result = json.loads(out.stdout)
        self.assertTrue(any("skipped nonlocal plan" in issue for issue in result["limitations"]))
        self.assertFalse(any(p["path"] == "plans/external.md" for p in result["plans"]))


if __name__ == "__main__":
    unittest.main()
