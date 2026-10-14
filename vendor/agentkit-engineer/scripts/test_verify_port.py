"""Regression tests for Engineer fallback structural gate."""
import tempfile
import unittest
from pathlib import Path

from verify_port import audit_port


class PortAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.skill = self.root / "skills" / "ak-example"
        self.skill.mkdir(parents=True)
        (self.skill / "references").mkdir()
        (self.skill / "references" / "real.md").write_text("# Real", encoding="utf-8")
        (self.skill / "SKILL.md").write_text(
            "---\nname: ak-example\ndescription: Example\n"
            "metadata: {port: angent-fallback, mode: adapted}\n---\n"
            "See `references/real.md`.\n", encoding="utf-8"
        )
        (self.root / "agents").mkdir()
        (self.root / "agents" / "example.md").write_text(
            "---\nname: example\ndescription: Example\n---\n# Example\n", encoding="utf-8"
        )
        (self.root / "PORTING_MANIFEST.md").write_text(
            "## Skills — 102 identities\n"
            "| `ak-example` | VERIFIED_ADAPTED | example |\n"
            "## Agents — 16 identities\n"
            "| `example` | VERIFIED_ADAPTED | example |\n"
            "## Upstream evidence boundary\n", encoding="utf-8"
        )

    def tearDown(self):
        self.tmp.cleanup()

    def check(self):
        return audit_port(self.root, expected_skills=1, expected_agents=1)

    def test_valid_fixture(self):
        self.assertEqual(self.check(), [])

    def test_mode_mismatch_blocks(self):
        p = self.skill / "SKILL.md"
        p.write_text(p.read_text().replace("mode: adapted", "mode: degraded"))
        self.assertTrue(any("mode mismatch" in e for e in self.check()))

    def test_missing_reference_blocks(self):
        (self.skill / "references" / "real.md").unlink()
        self.assertTrue(any("missing local reference" in e for e in self.check()))

    def test_broken_support_link_blocks(self):
        p = self.skill / "references" / "real.md"
        p.write_text("[Unresolved](missing.md)", encoding="utf-8")
        self.assertTrue(any("broken markdown link" in e for e in self.check()))

    def test_reference_escape_blocks(self):
        p = self.skill / "SKILL.md"
        p.write_text(p.read_text().replace("references/real.md", "references/../../agents/example.md"))
        self.assertTrue(any("unsafe local reference traversal" in e for e in self.check()))

    def test_missing_entrypoint_blocks(self):
        (self.skill / "SKILL.md").unlink()
        self.assertTrue(any("unreadable" in e for e in self.check()))

    def test_mismatched_identity_blocks(self):
        p = self.skill / "SKILL.md"
        p.write_text(p.read_text().replace("name: ak-example", "name: ak-other"))
        self.assertTrue(any("name mismatch" in e for e in self.check()))


if __name__ == "__main__":
    unittest.main()
