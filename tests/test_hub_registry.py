"""Hub contract, runtime boundaries, overlap and growing Kit inventory."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import hub_registry
import package_unified
import build_packages


class HubRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = package_unified.collect_entries(ROOT)
        cls.registry = json.loads(cls.source["hub/registry.json"])

    def test_registered_kits_and_native_exclusivity(self):
        self.assertEqual([e["id"] for e in self.registry["extensions"]],
                         ["angent-engineer", "angent-frontend"])
        engineer = self.registry["extensions"][0]
        self.assertEqual(engineer["source_skill_count"], 103)
        self.assertEqual(len(engineer["skills"]), 102)
        self.assertNotIn("ak-explain", engineer["skills"])
        self.assertEqual(len(engineer["roles"]), 16)
        self.assertTrue(engineer["runtime"]["exclusive"])
        self.assertEqual(self.registry["published_skills"].count("ak-debug"), 1)
        self.assertEqual(self.source["skills/ak-debug/SKILL.md"],
                         self.source["extensions/angent-engineer/skills/ak-debug/SKILL.md"])

    def test_semantic_overlap_and_third_kit_without_core_edit(self):
        source = {k: v for k, v in self.source.items() if k != "hub/registry.json"}
        item = {
            "schema_version": 1, "id": "angent-example", "name": "Sample Tester",
            "kind": "direct", "authority": "specialist",
            "description": "A synthetic extra kit for extensibility tests",
            "source": {"origin": "unit-test", "type": "fixture", "license": "test only"},
            "skills": {"directory": "skills", "expose": "all", "exclude": [],
                       "expected_source_count": 1},
            "roles": {"directory": "agents", "expected_count": 0},
            "runtime": {"native": None, "fallback": "portable",
                        "selection": "available", "exclusive": False},
            "capabilities": [{"id": "software.test", "entry": "example-test",
                              "when": "Specific sample-test specialty"}]
        }
        source["extensions/angent-example/extension.json"] = (json.dumps(item) + "\n").encode()
        payload = b"---\nname: example-test\ndescription: Synthetic test method\n---\nMethod\n"
        source["extensions/angent-example/skills/example-test/SKILL.md"] = payload
        registry = hub_registry.build_registry(source)
        providers = next(c["providers"] for c in registry["capabilities"]
                         if c["id"] == "software.test")
        self.assertEqual({p["extension"] for p in providers},
                         {"angent-engineer", "angent-example"})
        self.assertIn("example-test", registry["published_skills"])

        # The projection is declared data; no extra hardcoded gateway route.
        source["hub/registry.json"] = (json.dumps(registry) + "\n").encode()
        source["skills/example-test/SKILL.md"] = payload
        gateway = package_unified.gateway_entries(source)
        self.assertNotIn("skills/example-test/SKILL.md", gateway)
        self.assertIn("skills/angent/references/catalog/example-test/SKILL.md", gateway)
        self.assertIn(b"Sample Tester", gateway["skills/angent/references/INDEX.md"])
        cli = build_packages.assemble(ROOT, "local-agent", source)
        self.assertIn(".agents/skills/example-test/SKILL.md", cli)
        gemini = build_packages.assemble(ROOT, "gemini-web", source)
        self.assertIn("references/catalog/example-test/SKILL.md", gemini)

    def test_invalid_manifest_and_collision_fail_closed(self):
        base = {k: v for k, v in self.source.items() if k != "hub/registry.json"}
        manifest = "extensions/angent-frontend/extension.json"
        valid = json.loads(base[manifest])
        cases = []
        bad = json.loads(json.dumps(valid))
        bad["authority"] = "supervisor"
        cases.append(bad)
        bad = json.loads(json.dumps(valid))
        bad["capabilities"][0]["entry"] = "does-not-exist"
        cases.append(bad)
        bad = json.loads(json.dumps(valid))
        bad["skills"]["expected_source_count"] = 999
        cases.append(bad)
        for mutation in cases:
            with self.subTest(mutation=mutation):
                source = dict(base)
                source[manifest] = json.dumps(mutation).encode()
                with self.assertRaises(hub_registry.HubError):
                    hub_registry.build_registry(source)
        source = dict(base)
        source["extensions/angent-engineer/skills/angent-frontend-design/SKILL.md"] = (
            b"---\nname: angent-frontend-design\ndescription: Duplicate\n---\n"
        )
        manifest_engineer = "extensions/angent-engineer/extension.json"
        m = json.loads(source[manifest_engineer])
        m["skills"]["expected_source_count"] = 104
        source[manifest_engineer] = json.dumps(m).encode()
        with self.assertRaises(hub_registry.HubError):
            hub_registry.build_registry(source)


if __name__ == "__main__":
    unittest.main()
