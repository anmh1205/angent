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

    def test_index_managed_body_files_keep_metadata_in_sibling_index(self):
        cases=(
            ("usecases", "uc-approve.md", "atlas-usecase-index.md", "usecase-index"),
            ("userstories", "us-001.md", "atlas-story-index.md", "userstory-index"),
            ("ascii-wireframe", "approval.md", "atlas-wireframe-index.md", "screen-index"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for folder,filename,index_name,index_type in cases:
                with self.subTest(folder=folder):
                    parent=root/folder
                    parent.mkdir()
                    body=parent/filename
                    body.write_text("# Reviewed source body\n\nDetails.\n",encoding="utf8")
                    self.assertFalse(inspect(body,root)["ok"])
                    index=parent/index_name
                    index.write_text("---\ntype: "+index_type+"\nstatus: draft\n---\n"
                                     "# Feature index\n",encoding="utf8")
                    if folder != "ascii-wireframe":
                        self.assertFalse(inspect(body,root)["ok"],
                                         "Missing index row must not authorize body")
                        with index.open("a",encoding="utf8") as stream:
                            stream.write("| ID | Document |\n| --- | --- |\n"
                                         "| [entry]("+filename+") | Reviewed |\n")
                    result=inspect(body,root)
                    self.assertTrue(result["ok"],result)
                    self.assertTrue(any("Index-managed" in x for x in result["warnings"]))
                    index.write_text("---\ntype: incorrect\n---\n# Invalid index\n",encoding="utf8")
                    self.assertFalse(inspect(body,root)["ok"])
            unrelated=root/"untracked.md"
            unrelated.write_text("# Untracked\n",encoding="utf8")
            self.assertFalse(inspect(unrelated,root)["ok"])

    def test_index_membership_rejects_unreferenced_neighbor(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            folder=root/"usecases"
            folder.mkdir()
            (folder/"feature-usecase-index.md").write_text(
                "---\ntype: usecase-index\n---\n# Use cases\n"
                "| Slug | Status |\n| --- | --- |\n"
                "| [uc-known](uc-known.md) | draft |\n",encoding="utf8"
            )
            known=folder/"uc-known.md"
            unknown=folder/"uc-unknown.md"
            for item in (known,unknown):
                item.write_text("# Actor goal\n",encoding="utf8")
            self.assertTrue(inspect(known,root)["ok"])
            self.assertFalse(inspect(unknown,root)["ok"])

    def test_updated_date_is_real_calendar_day_not_just_regex(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            path=root/"spec.md"
            for bad_date in ("2026-02-30","2026-13-01","2026-00-00"):
                path.write_text("---\nstatus: draft\nupdated: "+bad_date+
                                "\n---\n# Title\n",encoding="utf8")
                report=inspect(path,root)
                self.assertIn("invalid date format",report["errors"])
            path.write_text("---\nstatus: draft\nupdated: 2026-02-28\n---\n# Title\n",
                            encoding="utf8")
            self.assertTrue(inspect(path,root)["ok"])

    def test_code_samples_are_not_treated_as_real_links_or_requirements(self):
        source=(
            "---\nstatus: draft\n---\n# Handbook\n"
            "```md\n"
            "{{example_variable}}\n"
            "[Bad example](../nonexistent.md)\n"
            "| FR-AUTH-001 | Example only |\n"
            "```\n"
            "~~~markdown\n"
            "[Other example](missing.md)\n"
            "~~~\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            target=root/"guide.md"
            target.write_text(source,encoding="utf8")
            report=inspect(target,root)
            self.assertTrue(report["ok"],report)
            self.assertEqual(report["table_ids"],[])
            target.write_text(source+"~~~python\nprint('unfinished')\n",encoding="utf8")
            result=inspect(target,root)
            self.assertIn("unclosed code fence",result["errors"])
            target.write_text(source+"[Actual missing](missing.md)\n",encoding="utf8")
            result=inspect(target,root)
            self.assertTrue(any("broken local reference" in x for x in result["errors"]))

    def test_unresolved_frontmatter_values_are_not_ignored_by_code_masking(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            target=root/"doc.md"
            target.write_text(
                "---\ntype: srs\nfeature: {{unknown_feature}}\nstatus: draft\n---\n"
                "# Complete body\n",encoding="utf8"
            )
            report=inspect(target,root)
            self.assertFalse(report["ok"])
            self.assertIn("unresolved template variables",report["errors"])

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

    def test_markdown_fragment_links_resolve_to_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"source.md").write_text("# Evidence\n\n## Section\n",encoding="utf8")
            target=root/"spec.md"
            target.write_text("---\nstatus: draft\n---\n# Spec\n"
                              "[Evidence](source.md#section)\n"
                              "[Local](#spec)\n",encoding="utf8")
            report=inspect(target,root)
            self.assertTrue(report["ok"],report)
            target.write_text("---\nstatus: draft\n---\n# Spec\n"
                              "[Missing](absent.md#section)\n"
                              "[Escape](../hidden.md#section)\n",encoding="utf8")
            bad=inspect(target,root)
            self.assertFalse(bad["ok"])
            self.assertTrue(any("broken" in e for e in bad["errors"]))
            self.assertTrue(any("path traversal" in e for e in bad["errors"]))

    def test_bad_optional_source_location_never_breaks_evidence_preview(self):
        graph=json.loads((ROOT/"extensions/angent-ba/examples/rental-fleet-traceability.json").read_text(encoding="utf8"))
        graph["artifacts"][0]["source_location"]="not-an-object"
        graph["artifacts"][1]["source_location"]={"uri":graph["sources"][0]["uri"],"line":True}
        page=render(graph)
        self.assertIn("BR-IVTS-01",page)
        self.assertNotIn(":LTrue",page)

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
        self.assertIn("FR to test traceability: 1/2",document)
        parser=Parser();parser.feed(document)
        self.assertEqual(len(parser.ids),5)

    def test_invalid_graph_is_rejected(self):
        with self.assertRaises(ValueError):
            render({"sources":[],"artifacts":[{"id":"FR-1","kind":"FR","title":"X","depends_on":["MISSING"],"source_refs":[]}]})

if __name__=="__main__":
    unittest.main()
