"""Inventory records must match the real 67 installed BA and Figma specialists.

This checks audit completeness; it cannot validate business or runtime parity.
"""
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/"hub/research/ba-figma-audit-67.json"

class EvidenceInventory(unittest.TestCase):
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
