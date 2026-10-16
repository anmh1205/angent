"""Negative controls for BA documents and HTML artifact viewer."""
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from validate_documents import inspect
from render_preview import render

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=[]
    def handle_starttag(self,tag,attrs):
        if tag=="article":
            self.ids.extend(value for key,value in attrs if key=="id")

class TestDocuments(unittest.TestCase):
    def test_valid_completed_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"source.md").write_text("# Evidence",encoding="utf8")
            target=root/"spec.md"
            target.write_text("---\ntype: srs\nstatus: draft\nupdated: 2026-10-16\n---\n# SRS\n\n| ID | Requirement |\n| --- | --- |\n| FR-AUTH-001 | The system shall reject unauthorized access. |\n\n[Source](source.md)\n",encoding="utf8")
            result=inspect(target,root)
            self.assertTrue(result["ok"],result)
            self.assertIn("FR-AUTH-001",result["table_ids"])

    def test_invalid_content_and_bad_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            path=root/"spec.md"
            path.write_text("---\ntype: srs\nstatus: magic\n---\n# Spec\n\n{{missing}}\n\n[Secret](../sensitive.txt)\n\n[Missing](nope.md)\n",encoding="utf8")
            result=inspect(path,root)
            self.assertFalse(result["ok"])
            self.assertTrue(any("template" in e for e in result["errors"]))
            self.assertTrue(any("path traversal" in e for e in result["errors"]))
            self.assertTrue(any("broken" in e for e in result["errors"]))

    def test_real_mit_sample_srs_uses_resolvable_docs_layout(self):
        root=ROOT / "extensions/angent-ba/examples"
        sample=root / "docs/atlas-re/srs/atlas-re-spec.md"
        outcome=inspect(sample,root)
        self.assertTrue(outcome["ok"],outcome)
        self.assertGreaterEqual(len(outcome["table_ids"]),10)

    def test_source_template_is_not_a_completed_document(self):
        path=ROOT/"extensions/angent-ba/skills/ba-kg/references/templates/doc-srs.md"
        result=inspect(path,ROOT)
        self.assertFalse(result["ok"])
        self.assertTrue(any("template" in e for e in result["errors"]))

    def test_escaped_html_and_no_javascript_url(self):
        model=json.loads((ROOT/"extensions/angent-ba/examples/rental-fleet-traceability.json").read_text(encoding="utf8"))
        model["artifacts"][1]["title"]="<script>alert('x')</script>"
        model["sources"][0]["uri"]="javascript:alert('x')"
        document=render(model,"<test>")
        self.assertNotIn("<script>",document)
        self.assertIn("&lt;script&gt;",document)
        self.assertNotIn("href='javascript:",document)
        self.assertIn("FR to test traceability: 1/1",document)
        parser=Parser();parser.feed(document)
        self.assertEqual(len(parser.ids),4)

    def test_invalid_graph_is_rejected(self):
        with self.assertRaises(ValueError):
            render({"sources":[],"artifacts":[{"id":"FR-1","kind":"FR","title":"X","depends_on":["MISSING"],"source_refs":[]}]})

if __name__=="__main__":
    unittest.main()
