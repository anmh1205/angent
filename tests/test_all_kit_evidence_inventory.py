"""Inventory records must match the real 67 installed BA and Figma specialists.

This checks audit completeness; it cannot validate business or runtime parity.
"""
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/"hub/research/ba-figma-audit-67.json"

class EvidenceInventory(unittest.TestCase):
    def test_evidence_references_are_real_but_not_live_claims(self):
        rows=json.loads(AUDIT.read_text(encoding="utf8"))
        verified_tiers={"source-validated","runtime-mock","payload-verified"}
        for item in rows:
            with self.subTest(skill=item["skill"]):
                refs=item["proof_refs"]
                if item["evidence"] in verified_tiers:
                    self.assertTrue(refs, "A promoted evidence tier requires inspectable test sources")
                else:
                    self.assertFalse(refs, "Method-only/unverified/provider claims must not cite invented runs")
                for path in refs:
                    self.assertTrue((ROOT/path).is_file(), "Missing proof source "+path)
                if item["evidence"]=="runtime-mock":
                    self.assertTrue(any("integration/" in ref for ref in refs))
                if item["evidence"]=="provider-blocked":
                    self.assertEqual(item["proof_scope"],"live-provider-readback-required")

    def test_every_skill_covered_without_fabricating_runtime_success(self):
        entries=json.loads(AUDIT.read_text(encoding="utf8"))
        names=[item["skill"] for item in entries]
        actual={f.parent.name for kit in ("angent-ba","angent-figma")
                for f in (ROOT/"extensions"/kit/"skills").glob("*/SKILL.md")}
        self.assertEqual(len(entries),67)
        self.assertEqual(len(set(names)),67)
        self.assertEqual(set(names),actual)
        types={"method","source-validated","runtime-mock","unverified","provider-blocked","payload-verified"}
        for item in entries:
            with self.subTest(skill=item["skill"]):
                self.assertIn(item["evidence"],types)
                self.assertGreater(len(item["deliverable"]),15)
                self.assertGreater(len(item["remaining"]),16)
                if item["skill"].startswith("figma-") and item["stage"]=="Figma OSS":
                    self.assertEqual(item["evidence"],"payload-verified")
        self.assertEqual(sum(x["stage"]=="Figma OSS" for x in entries),6)
        self.assertEqual(sum(x["stage"]=="Figma Pro" for x in entries),6)
        self.assertEqual(sum(x["stage"] not in ("Figma OSS","Figma Pro") for x in entries),55)
        self.assertGreater(sum(x["evidence"] in ("unverified","provider-blocked") for x in entries),0)

if __name__=="__main__":
    unittest.main()
