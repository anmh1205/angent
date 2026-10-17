"""Source-preserving BA stakeholder export tests."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from build_export import gather,export

class ExportSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=BA/"examples"
        cls.files=["docs/atlas-re/atlas-re-urd.md",
                   "docs/atlas-re/atlas-re-brd.md",
                   "docs/atlas-re/atlas-re-prd.md"]

    def test_explicit_order_provenance_and_markdown(self):
        output,manifest=export(self.root,self.files,"Atlas review","md")
        contents=output.decode("utf8")
        self.assertEqual(len(manifest),3)
        self.assertIn("SHA-256",contents)
        self.assertIn("## Document 3: docs/atlas-re/atlas-re-prd.md",contents)
        self.assertLess(contents.index("Document 1:"),contents.index("Document 2:"))
        for item in manifest:
            self.assertEqual(len(item["sha256"]),64)
        self.assertEqual(output,export(self.root,self.files,"Atlas review","md")[0])

    def test_invalid_source_paths_and_duplicate_or_empty_scope(self):
        with tempfile.TemporaryDirectory() as temp:
            sandbox=Path(temp)
            (sandbox/"safe.md").write_text("# Safe",encoding="utf8")
            cases=[[],["safe.md","safe.md"],["../secret.md"],["safe.txt"],["missing.md"]]
            for case in cases:
                with self.subTest(case=case):
                    with self.assertRaises(ValueError):
                        export(sandbox,case,"Review","md")

    def test_requires_real_converter_instead_of_false_pdf(self):
        with self.assertRaisesRegex(ValueError,"Pandoc not installed"):
            export(self.root,self.files,"Atlas review","pdf",pandoc="__missing_pandoc_binary__")

if __name__=="__main__":
    unittest.main()
