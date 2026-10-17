"""Exercise candidate lookup and real extracted resource identities, not model routing."""
import importlib.util
import json
from pathlib import Path
import posixpath
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_packages
import hub_registry
import package_unified


class HubDiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = package_unified.collect_entries(ROOT)
        spec = importlib.util.spec_from_file_location("hub_discover", ROOT / "hub/discover.py")
        cls.helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.helper)
        cls.temp = tempfile.TemporaryDirectory()
        cls.hub = Path(cls.temp.name)
        for path, payload in cls.source.items():
            if path.startswith("hub/"):
                target = cls.hub / path[len("hub/"):]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(payload)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_manual_workflow_is_not_automatic_advice(self):
        auto = self.helper.discover(self.hub, "architecture advice")
        self.assertIn("ak-ask", {c["entry"] for c in auto["candidates"]})
        self.assertNotIn("ak-advise", {c["entry"] for c in auto["candidates"]})
        explicit = self.helper.discover(self.hub, "Advise phỏng vấn", explicit=True)
        card = next(c for c in explicit["candidates"] if c["entry"] == "ak-advise")
        self.assertEqual(card["invocation"], "explicit")
        self.assertTrue(card["requires"])
        self.assertEqual(explicit["activation"], "not-performed")
        self.assertEqual(explicit["availability"], "not-checked")

    def test_domain_is_soft_and_missing_contract_remains_unknown(self):
        result = self.helper.discover(self.hub, "Excalidraw", domain="operations")
        self.assertEqual(result["candidates"][0]["entry"], "ak-excalidraw")
        result = self.helper.discover(self.hub, "watzup")
        card = next(c for c in result["candidates"] if c["entry"] == "ak-watzup")
        self.assertEqual(card["contract_status"], "inspect-required")
        self.assertEqual(card["invocation"], "inspect-required")
        self.assertEqual(card["outputs"], [])
        result = self.helper.discover(self.hub, "unmatchedxyz")
        self.assertEqual(result["candidates"], [])
        self.assertIn("does not prove absence", result["next_on_miss"])

    def test_denied_entries_excluded_and_response_bounded(self):
        result = self.helper.discover(self.hub, "architecture", limit=1, exclude=["ak-ask"])
        self.assertLessEqual(len(result["candidates"]), 1)
        self.assertNotIn("ak-ask", {c["entry"] for c in result["candidates"]})
        for limit in (0, 21):
            with self.assertRaises(ValueError):
                self.helper.discover(self.hub, "architecture", limit=limit)

    def test_every_profile_resolves_exact_method_and_role_bytes(self):
        for profile in build_packages.PACKAGES:
            with self.subTest(profile=profile):
                files = build_packages.assemble(ROOT, profile, self.source)
                hubs = [p.rsplit("/", 1)[0] for p in files if p.endswith("/bindings.json")]
                for hub in hubs:
                    binding = json.loads(files[hub + "/bindings.json"])
                    self.assertEqual(len(binding["methods"]), 103)
                    self.assertEqual(len(binding["roles"]), 16)
                    for entry, relative in binding["methods"].items():
                        path = posixpath.normpath(hub + "/" + relative)
                        self.assertIn(path, files)
                        self.assertEqual(files[path], self.source[f"skills/{entry}/SKILL.md"])
                        card = json.loads(files[f"{hub}/methods/{entry}.json"])
                        self.assertEqual(card["entry"], entry)
                    for identity, relative in binding["roles"].items():
                        ext, role = identity.split(":")
                        path = posixpath.normpath(hub + "/" + relative)
                        self.assertEqual(files[path], self.source[f"extensions/{ext}/agents/{role}.md"])

    def test_extracted_gateway_helper_inspects_without_invocation(self):
        files = build_packages.assemble(ROOT, "openai-plugin", self.source)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name, payload in files.items():
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(payload)
            hub = root / "skills/angent/references/hub"
            result = subprocess.run([sys.executable, str(hub / "discover.py"), "--method", "ak-team"],
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            card = json.loads(result.stdout)
            self.assertEqual(card["activation"], "not-performed")
            self.assertTrue((hub / card["resource"]).is_file())
            self.assertIn("shutdown", " ".join(card["requires"]))

    def test_v2_invalid_method_contracts_fail_closed(self):
        path = "extensions/angent-engineer/extension.json"
        valid = json.loads(self.source[path])
        for field, value in (("entry", "ak-explain"), ("invocation", "always"),
                             ("outputs", []), ("capabilities", ["invalid"]),
                             ("requires", "all tools")):
            source = dict(self.source)
            m = json.loads(json.dumps(valid))
            m["methods"][0][field] = value
            source[path] = json.dumps(m).encode()
            with self.subTest(field=field), self.assertRaises(hub_registry.HubError):
                hub_registry.build_registry(source)

    def test_compiled_kit_and_global_capability_routes_agree(self):
        registry = json.loads(self.source["hub/registry.json"])
        for ext in registry["extensions"]:
            local = {(c["id"], c["entry"]) for c in ext["capabilities"]}
            global_routes = {(c["id"], p["entry"]) for c in registry["capabilities"]
                             for p in c["providers"] if p["extension"] == ext["id"]}
            self.assertEqual(local, global_routes)
        architecture = next(c for c in registry["capabilities"] if c["id"] == "software.architecture")
        self.assertTrue({"ak-ask", "ak-advise", "ak-brainstorm"} <= {p["entry"] for p in architecture["providers"]})


if __name__ == "__main__":
    unittest.main()
