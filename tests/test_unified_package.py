"""Deterministic single-plugin artifact regression tests."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "package_unified.py"
spec = importlib.util.spec_from_file_location("package_unified", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class UnifiedPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = tempfile.TemporaryDirectory()
        cls.first = Path(cls.dir.name) / "unified-1.zip"
        cls.second = Path(cls.dir.name) / "unified-2.zip"
        cls.report = module.build(ROOT, cls.first)

    @classmethod
    def tearDownClass(cls):
        cls.dir.cleanup()

    def test_one_plugin_and_exact_catalog(self):
        self.assertEqual(self.report["plugin_name"], "angent")
        self.assertEqual(self.report["discoverable_skills"], 1)
        self.assertEqual(self.report["engineer_skills"], 103)
        self.assertEqual(self.report["discoverable_engineer_skills"], 0)
        self.assertEqual(self.report["internal_engineer_methods"], 102)
        self.assertEqual(self.report["internal_frontend_methods"], 1)
        self.assertEqual(self.report["engineer_roles"], 16)
        with zipfile.ZipFile(self.first) as z:
            self.assertTrue(all(i.create_system == 3 and i.external_attr >> 16 == 0o100644 for i in z.infolist()))
            self.assertNotIn("extensions/angent-engineer/plugin.json", z.namelist())
            self.assertNotIn("extensions/angent-engineer/.codex-plugin/plugin.json", z.namelist())
            self.assertIn("extensions/angent-engineer/source-manifest.json", z.namelist())
            self.assertIn("extensions/angent-engineer/skills/ak-explain/SKILL.md", z.namelist())
            self.assertNotIn("skills/ak-explain/SKILL.md", z.namelist())
            self.assertEqual(json.loads(z.read("plugin.json"))["version"],
                             json.loads(z.read(".codex-plugin/plugin.json"))["version"])
            discovery = [p for p in z.namelist() if p.startswith("skills/") and p.count("/") == 2 and p.endswith("/SKILL.md")]
            self.assertEqual(discovery, ["skills/angent/SKILL.md"])
            self.assertNotIn("skills/ak-agentkit/SKILL.md", z.namelist())
            self.assertNotIn("skills/angent-frontend-design/SKILL.md", z.namelist())
            self.assertIn("skills/angent/references/INDEX.md", z.namelist())
            self.assertEqual(z.read("skills/angent/references/catalog/ak-agentkit/SKILL.md"),
                             z.read("extensions/angent-engineer/skills/ak-agentkit/SKILL.md"))
            self.assertEqual(z.read("skills/angent/references/catalog/angent-frontend-design/SKILL.md"),
                             z.read("extensions/angent-frontend/skills/angent-frontend-design/SKILL.md"))
            inner = [p for p in z.namelist() if p.startswith("skills/angent/references/catalog/") and p.endswith("/SKILL.md")]
            self.assertEqual(len(inner), self.report["core_skills"] - 1 + self.report["internal_specialist_methods"])
            self.assertNotIn(b"ak-explain", z.read("skills/angent/references/INDEX.md"))

    def test_reproducible_bytes(self):
        module.build(ROOT, self.second)
        digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
        self.assertEqual(digest(self.first), digest(self.second))

    def test_selector_modes_in_unified_archive(self):
        with tempfile.TemporaryDirectory() as dest:
            with zipfile.ZipFile(self.first) as z:
                z.extractall(dest)
            script = Path(dest) / "extensions/angent-engineer/scripts/select_engineer.py"
            for native, expected in (("yes", "native"), ("no", "fallback"), ("unknown", "fallback")):
                result = subprocess.run(
                    [sys.executable, str(script), "--doctor", "none", "--native-usable", native],
                    text=True, capture_output=True, timeout=20,
                )
                self.assertEqual(result.returncode, 0, result.stderr + result.stdout[-1000:])
                state = json.loads(result.stdout)
                self.assertEqual(state["mode"], expected)
                self.assertTrue(state["fallback"]["ready"])
                self.assertFalse(state["policy"]["load_both"])

    def test_collision_fails_closed(self):
        paths = module._tracked(ROOT)
        with self.assertRaises(module.PackagingError):
            module.collect_entries(ROOT, paths + ["extensions/angent-engineer/skills/ak-agentkit/SKILL.md"])

    def test_missing_hidden_source_skill_fails_closed(self):
        paths = [p for p in module._tracked(ROOT) if p != "extensions/angent-engineer/skills/ak-explain/SKILL.md"]
        with self.assertRaises(module.PackagingError):
            module.collect_entries(ROOT, paths)

    def test_missing_skill_fails_closed(self):
        paths = [p for p in module._tracked(ROOT) if p != "extensions/angent-engineer/skills/ak-agentkit/SKILL.md"]
        with self.assertRaises(module.PackagingError):
            module.collect_entries(ROOT, paths)


if __name__ == "__main__":
    unittest.main()
