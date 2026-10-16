"""Real source-to-package structural, fidelity and reproducibility gates."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_packages as packs
import package_unified as legacy


class MultiPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = legacy.collect_entries(ROOT)

    def test_five_complete_independent_packages(self):
        for package in packs.PACKAGES:
            with self.subTest(package=package):
                files = packs.assemble(ROOT, package, self.source)
                prefix = packs.SKILL_PREFIX[package]
                paths = [p for p in files if p.startswith(prefix) and p.endswith("/SKILL.md")]
                self.assertEqual(len(paths), 115)
                self.assertIn(prefix + "angent/SKILL.md", files)
                self.assertIn(prefix + "ak-agentkit/SKILL.md", files)
                self.assertEqual(files[prefix + "angent/SKILL.md"], self.source["skills/angent/SKILL.md"])
                self.assertEqual(files[prefix + "ak-agentkit/SKILL.md"], self.source["skills/ak-agentkit/SKILL.md"])
                self.assertNotIn("extensions/angent-engineer/plugin.json", files)
                self.assertIn("extensions/angent-engineer/source-manifest.json", files)
                self.assertIn("extensions/angent-engineer/scripts/select_engineer.py", files)
                self.assertIn("INSTALL.md", files)
                if package in ("gemini-extension", "claude-code"):
                    self.assertEqual(len([p for p in files if p.startswith("agents/") and p.endswith(".md")]), 16)
                    self.assertIn(b"description: ", files["agents/code-reviewer.md"])
                    self.assertNotIn(b"memory_scope:", files["agents/code-reviewer.md"].split(b"---", 2)[1])
                else:
                    self.assertFalse(any(p.startswith("agents/") for p in files))

    def test_platform_bootstrap_and_manifests(self):
        local = packs.assemble(ROOT, "local-agent", self.source)
        self.assertIn("AGENTS.md", local)
        self.assertNotEqual(local["AGENTS.md"], ROOT.joinpath("AGENTS.md").read_bytes())
        self.assertNotIn("plugin.json", local)
        self.assertIn(".gemini/skills/angent/SKILL.md", packs.assemble(ROOT, "gemini-skills", self.source))
        gemini = packs.assemble(ROOT, "gemini-extension", self.source)
        meta = json.loads(gemini["gemini-extension.json"])
        self.assertEqual(meta["contextFileName"], "GEMINI.md")
        claude = packs.assemble(ROOT, "claude-code", self.source)
        self.assertIn(".claude-plugin/plugin.json", claude)
        self.assertIn("bootstrap/CLAUDE.md", claude)
        self.assertNotIn("CLAUDE.md", claude)
        openai = packs.assemble(ROOT, "openai-plugin", self.source)
        self.assertEqual(json.loads(openai["plugin.json"])["version"], "1.5.0")
        self.assertEqual(json.loads(openai[".codex-plugin/plugin.json"])["version"], "1.5.0")
        self.assertEqual(openai["skills/angent/SKILL.md"], self.source["skills/angent/SKILL.md"])

    def test_negative_agent_frontmatter(self):
        with self.assertRaises(legacy.PackagingError):
            packs._agent_projection("agents/foo.md", b"no metadata")
        with self.assertRaises(legacy.PackagingError):
            packs._agent_projection("agents/foo.md", b"---\nname: another\ndescription: fine\n---\nBody")

    def test_reproducible_and_copy_ready_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            first = packs.build(ROOT, p / "packages", p / "dist")
            self.assertEqual(set(first), set(packs.PACKAGES))
            checksums = {name: hashlib.sha256((p / "dist" / f"angent-{name}.zip").read_bytes()).hexdigest() for name in packs.PACKAGES}
            second = packs.build(ROOT, p / "packages", p / "dist")
            for name in packs.PACKAGES:
                with self.subTest(package=name):
                    self.assertEqual(first[name]["sha256"], second[name]["sha256"])
                    self.assertEqual(checksums[name], hashlib.sha256((p / "dist" / f"angent-{name}.zip").read_bytes()).hexdigest())
                    with zipfile.ZipFile(p / "dist" / f"angent-{name}.zip") as z:
                        self.assertIsNone(z.testzip())
                        self.assertEqual(len(z.namelist()), len(set(z.namelist())))
                        self.assertEqual(z.read("INSTALL.md"), (p / "packages" / name / "INSTALL.md").read_bytes())

    def test_legacy_openai_builder_still_works(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = legacy.build(ROOT, Path(tmp) / "angent-chatgpt.zip")
            self.assertEqual(report["discoverable_skills"], 115)
            self.assertEqual(report["engineer_roles"], 16)


if __name__ == "__main__":
    unittest.main()
