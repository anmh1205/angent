"""Source/provider identity comparator tests. Observations here are synthetic."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("activation", ROOT / "scripts" / "verify_activation.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class ActivationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = module.source_identity(ROOT)

    def provider(self):
        return {"name": "angent", "version": self.source["version"],
                "complete_listing": True, "paths": list(self.source["expected_paths"]),
                "other_active_plugins": [],
                "sha256_by_path": dict(self.source["probed_sha256"])}

    def test_source_counts(self):
        self.assertEqual(len(self.source["expected_paths"]), 114)
        self.assertNotIn("skills/ak-explain/SKILL.md", self.source["expected_paths"])

    def test_no_provider_is_not_verified(self):
        self.assertEqual(module.verify_provider(self.source, None)["status"], "PROVIDER_NOT_CHECKED")

    def test_matched_probes_are_bounded_proof(self):
        result = module.verify_provider(self.source, self.provider())
        self.assertEqual(result["status"], "MATCHED_PROBED_CONTENT")
        self.assertIn("Not proof", result["note"])

    def test_old_version_rejected(self):
        observed = self.provider()
        observed["version"] = "1.2.2"
        self.assertEqual(module.verify_provider(self.source, observed)["status"], "IDENTITY_MISMATCH")

    def test_missing_skill_detected(self):
        observed = self.provider()
        observed["paths"].pop()
        self.assertEqual(module.verify_provider(self.source, observed)["status"], "CATALOG_MISMATCH")

    def test_suppressed_skill_cannot_be_reintroduced_by_provider(self):
        observed = self.provider()
        observed["paths"].append("skills/ak-explain/SKILL.md")
        self.assertEqual(module.verify_provider(self.source, observed)["status"], "CATALOG_MISMATCH")

    def test_partial_inventory_detected(self):
        observed = self.provider()
        observed["complete_listing"] = False
        self.assertEqual(module.verify_provider(self.source, observed)["status"], "INCOMPLETE_PROVIDER_INVENTORY")

    def test_wrong_content_detected(self):
        observed = self.provider()
        observed["sha256_by_path"]["skills/angent/SKILL.md"] = "wrong"
        self.assertEqual(module.verify_provider(self.source, observed)["status"], "SOURCE_CONTENT_MISMATCH")

    def test_active_engineer_duplication_detected(self):
        observed = self.provider()
        observed["other_active_plugins"].append("angent-engineer-fallback")
        self.assertEqual(module.verify_provider(self.source, observed)["status"], "DUPLICATE_ENGINEER_ACTIVE")

    def test_catalog_version_only_not_full_proof(self):
        observed = self.provider()
        del observed["sha256_by_path"]
        self.assertEqual(module.verify_provider(self.source, observed)["status"], "CATALOG_AND_VERSION_ONLY")


if __name__ == "__main__":
    unittest.main()
