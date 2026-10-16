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
        cls.registry = json.loads(cls.source['hub/registry.json'])
        cls.expected_skills = 12 + len(cls.registry['published_skills'])
        cls.expected_roles = sum(len(x['roles']) for x in cls.registry['extensions'])

    def test_five_complete_independent_packages(self):
        for package in (p for p in packs.PACKAGES if p != 'gemini-web'):
            with self.subTest(package=package):
                files = packs.assemble(ROOT, package, self.source)
                prefix = packs.SKILL_PREFIX[package]
                paths = [p for p in files if p.startswith(prefix) and p.endswith("/SKILL.md") and p.count("/") == prefix.count("/") + 1]
                expected = 1 if package == "openai-plugin" else self.expected_skills
                self.assertEqual(len(paths), expected)
                self.assertNotIn(prefix + "ak-explain/SKILL.md", files)
                self.assertIn("extensions/angent-engineer/skills/ak-explain/SKILL.md", files)
                self.assertIn(prefix + "angent/SKILL.md", files)
                if package == "openai-plugin":
                    self.assertNotIn(prefix + "ak-agentkit/SKILL.md", files)
                    self.assertNotIn(prefix + "angent-frontend-design/SKILL.md", files)
                    self.assertIn(prefix + "angent/references/INDEX.md", files)
                    self.assertEqual(files[prefix + "angent/references/catalog/ak-agentkit/SKILL.md"],
                                     self.source["skills/ak-agentkit/SKILL.md"])
                    self.assertEqual(files[prefix + "angent/references/catalog/angent-frontend-design/SKILL.md"],
                                     self.source["skills/angent-frontend-design/SKILL.md"])
                    self.assertTrue(files[prefix + "angent/SKILL.md"].startswith(self.source["skills/angent/SKILL.md"]))
                else:
                    self.assertIn(prefix + "ak-agentkit/SKILL.md", files)
                    self.assertIn(prefix + "angent-frontend-design/SKILL.md", files)
                    self.assertEqual(files[prefix + "angent/SKILL.md"], self.source["skills/angent/SKILL.md"])
                    self.assertEqual(files[prefix + "ak-agentkit/SKILL.md"], self.source["skills/ak-agentkit/SKILL.md"])
                self.assertNotIn("extensions/angent-engineer/plugin.json", files)
                self.assertIn("extensions/angent-engineer/source-manifest.json", files)
                self.assertIn("extensions/angent-engineer/scripts/select_engineer.py", files)
                self.assertIn("INSTALL.md", files)
                if package in ("gemini-extension", "claude-code"):
                    self.assertEqual(len([p for p in files if p.startswith("agents/") and p.endswith(".md")]), self.expected_roles)
                    self.assertIn(b"description: ", files["agents/code-reviewer.md"])
                    self.assertNotIn(b"memory_scope:", files["agents/code-reviewer.md"].split(b"---", 2)[1])
                else:
                    self.assertFalse(any(p.startswith("agents/") for p in files))

    def test_specialist_execution_scripts_are_physically_bundled(self):
        scripts = (
            "extensions/angent-ba/scripts/build_d2.py",
            "extensions/angent-ba/scripts/build_bpmn.py",
            "extensions/angent-ba/scripts/build_bruno.py",
            "extensions/angent-ba/scripts/build_wireframe.py",
            "extensions/angent-ba/scripts/build_playwright.py",
            "extensions/angent-ba/scripts/compare_artifact_revisions.py",
            "extensions/angent-ba/scripts/audit_api_contract.py",
            "extensions/angent-ba/scripts/validate_artifacts.py",
            "extensions/angent-figma/scripts/to_reqwise_payload.py",
        )
        for name in ("local-agent", "claude-code", "gemini-extension", "gemini-skills", "openai-plugin"):
            with self.subTest(package=name):
                content=packs.assemble(ROOT,name,self.source)
                for path in scripts:
                    self.assertIn(path,content)
                    self.assertEqual(content[path],self.source[path])
        # Browser-only Gemini package has the reference library, not a
        # filesystem/CLI runner: do not report native script execution there.
        browser=packs.assemble(ROOT,"gemini-web",self.source)
        for path in scripts:
            self.assertNotIn(path,browser)

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
        self.assertEqual(json.loads(openai["plugin.json"])["version"], json.loads(self.source["plugin.json"])["version"])
        self.assertEqual(json.loads(openai[".codex-plugin/plugin.json"])["version"], json.loads(self.source["plugin.json"])["version"])
        self.assertTrue(openai["skills/angent/SKILL.md"].startswith(self.source["skills/angent/SKILL.md"]))
        self.assertEqual({p for p in openai if p.startswith("skills/") and p.endswith("/SKILL.md") and p.count("/") == 2},
                         {"skills/angent/SKILL.md"})

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

    def test_complete_skill_and_support_byte_fidelity(self):
        source_skills = {p: data for p, data in self.source.items() if p.startswith("skills/")}
        source_support = {p: data for p, data in self.source.items() if p.startswith("extensions/")}
        for package in (p for p in packs.PACKAGES if p != 'gemini-web'):
            with self.subTest(package=package):
                files = packs.assemble(ROOT, package, self.source)
                for path, data in source_skills.items():
                    if package == "openai-plugin":
                        if path == "skills/angent/SKILL.md":
                            self.assertTrue(files[path].startswith(data))
                        elif path == "skills/angent/references/INDEX.md":
                            self.assertIn(b"## ANGENT Engineer", files[path])
                        elif path.startswith("skills/angent/"):
                            self.assertEqual(files[path], data, path)
                        else:
                            relative = path[len("skills/"):]
                            self.assertEqual(files["skills/angent/references/catalog/" + relative], data, path)
                    else:
                        self.assertEqual(files[packs.SKILL_PREFIX[package] + path[len("skills/"):]], data, path)
                for path, data in source_support.items():
                    self.assertEqual(files[path], data, path)

    def test_gemini_web_one_root_skill_with_full_reference_library(self):
        files = packs.assemble(ROOT, "gemini-web", self.source)
        self.assertTrue(files["SKILL.md"].startswith(b"---\nname: angent\n"))
        self.assertIn("references/INDEX.md", files)
        for ext in ("angent-ba", "angent-figma"):
            notice = f"references/licenses/{ext}.md"
            self.assertIn(notice, files)
            self.assertIn(b"MIT License", files[notice])
        self.assertEqual(files["references/catalog/angent/SKILL.md"], self.source["skills/angent/SKILL.md"])
        self.assertEqual(files["references/catalog/ak-agentkit/SKILL.md"], self.source["skills/ak-agentkit/SKILL.md"])
        self.assertEqual(len([p for p in files if p.startswith("references/catalog/") and p.endswith("/SKILL.md")]), self.expected_skills)
        self.assertIn("references/catalog/angent-frontend-design/SKILL.md", files)
        self.assertNotIn("references/catalog/ak-explain/SKILL.md", files)
        self.assertNotIn(b"ak-explain", files["references/INDEX.md"])
        self.assertEqual(len([p for p in files if p.startswith("references/roles/") and p.endswith(".md")]), self.expected_roles)
        self.assertNotIn(".gemini/skills/angent/SKILL.md", files)
        self.assertNotIn("plugin.json", files)
        self.assertNotIn("gemini-extension.json", files)
        self.assertLess(sum(map(len, files.values())), 100_000_000)

    def test_legacy_openai_builder_still_works(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = legacy.build(ROOT, Path(tmp) / "angent-chatgpt.zip")
            self.assertEqual(report["discoverable_skills"], 1)
            self.assertEqual(report["internal_engineer_methods"], 102)
            self.assertEqual(report["engineer_skills"], 103)
            self.assertEqual(report["engineer_roles"], 16)


if __name__ == "__main__":
    unittest.main()
