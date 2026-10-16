"""Prevent installed-kit instructions from advertising source-only regression scripts."""
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from package_unified import collect_entries
from build_packages import assemble

class DistributedInstructionTests(unittest.TestCase):
    def test_all_kit_test_references_disclose_checkout_requirement(self):
        paths=[f for kit in ("angent-ba","angent-figma")
               for f in (ROOT/"extensions"/kit).rglob("*.md")]
        reviewed=[]
        for file in paths:
            body=file.read_text(encoding="utf8")
            if "tests/integration/" not in body and "tests/test_" not in body:
                continue
            with self.subTest(file=str(file.relative_to(ROOT))):
                self.assertIn("**Repository-only verification:**",body)
                self.assertIn("not the development test suite",body)
                reviewed.append(file)
        self.assertGreaterEqual(len(reviewed),18)

    def test_shipped_package_contains_executables_but_no_source_test_tree(self):
        source=collect_entries(ROOT)
        for name in ("local-agent","openai-plugin","claude-code","gemini-skills","gemini-extension"):
            with self.subTest(package=name):
                package=assemble(ROOT,name,source)
                self.assertFalse(any(path.startswith("tests/") for path in package))
                self.assertIn("extensions/angent-ba/scripts/build_bruno.py",package)
                self.assertIn("extensions/angent-figma/scripts/to_reqwise_payload.py",package)

if __name__=="__main__":
    unittest.main()
