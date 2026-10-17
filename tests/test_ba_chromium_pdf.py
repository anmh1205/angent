"""PDF export changes must remain explicit and never silently fake a renderer."""
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_export import export

class PDFExportBoundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=ROOT/"extensions/angent-ba/examples"
        cls.files=["docs/atlas-re/atlas-re-urd.md"]

    def test_non_pdf_cannot_request_pdf_renderer(self):
        with self.assertRaisesRegex(ValueError,"only valid for PDF"):
            export(self.root,self.files,"Report","md",pdf_engine="chromium")

    def test_chromium_requires_real_pandoc_html_stage(self):
        with self.assertRaisesRegex(ValueError,"Pandoc not installed"):
            export(self.root,self.files,"Report","pdf",pandoc="__missing_pandoc_test_cli__",
                   pdf_engine="chromium")

if __name__=="__main__":
    unittest.main()
