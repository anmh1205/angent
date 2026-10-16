"""Portable BA references: all templates, source methods and rules are real and coherent.

Unlike counting skill files, this gate checks that a user of any ANGENT host
is never sent to the source kit's Claude hooks/state or unsupported renderers.
"""
from pathlib import Path
import re
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/"extensions/angent-ba/skills/ba-kg/references"
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from extract_markdown_graph import markdown_tables,HEADERS

class BAReferencePortabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.templates=list((REF/"templates").glob("*.md"))
        cls.rules=list((REF/"rules").glob("*.md"))
        cls.methods=list((REF/"source-methods").glob("*.md"))

    def test_complete_reference_inventory_and_method_quality(self):
        self.assertEqual(len(self.templates),48)
        self.assertEqual(len(self.rules),19)
        self.assertEqual(len(self.methods),21)
        for file in self.methods:
            with self.subTest(method=file.stem):
                body=file.read_text(encoding="utf8")
                self.assertIn("**Provenance:**",body)
                self.assertIn("https://github.com/nv-minh/dev-ba-kit",body)
                self.assertGreater(len(body.split()),145)
                self.assertGreaterEqual(len(re.findall(r"^## ",body,re.MULTILINE)),2)
        for file in self.rules:
            with self.subTest(rule=file.stem):
                self.assertGreater(len(file.read_text(encoding="utf8")),350)

    def test_no_inherited_claude_runtime_or_shadow_state_in_active_references(self):
        legacy=(
            "CLAUDE_PLUGIN_ROOT", "tsrun.sh", "render.sh", "icon-path.sh",
            "docs/_shared", "activity.log", "profile_hash",
            "source_watermark", "staleness_budget", ".claude/",
            "L1 approval", "L3 iterate",
        )
        for file in self.templates+self.methods+self.rules:
            text=file.read_text(encoding="utf8")
            for pattern in legacy:
                with self.subTest(file=file.name,legacy=pattern):
                    self.assertNotIn(pattern.lower(),text.lower())

    def test_template_index_links_resolve_to_all_real_template_files(self):
        import re
        index=REF/"template-index.md"
        targets=re.findall(r"\\]\\((templates/[A-Za-z0-9_-]+\\.md)\\)",
                           index.read_text(encoding="utf8"))
        self.assertEqual(len(targets),48)
        self.assertEqual(len(set(targets)),48)
        self.assertEqual(
            {REF/path for path in targets},
            set(self.templates),
            "Every referenced template must exist, with no missing or orphan file"
        )

    def test_supported_ba_template_tables_can_enter_actual_extractor(self):
        requirements={
            "doc-urd.md":["UN"],
            "doc-brd.md":["BO"],
            "doc-prd.md":["CAP"],
            "doc-srs.md":["FR","NFR","BR","E"],
            "doc-test-checklist-index.md":["CHK"],
            "doc-testcase-index.md":["TC"],
            "doc-story-index.md":["US"],
            "doc-usecase-index.md":["UC"],
        }
        for filename,kinds in requirements.items():
            source=(REF/"templates"/filename).read_text(encoding="utf8")
            tables=markdown_tables(source)
            headers=[set(table[0]) for table in tables if table]
            for kind in kinds:
                with self.subTest(template=filename,artifact=kind):
                    required=set(HEADERS[kind])
                    identifier="Slug" if kind=="UC" else "ID"
                    self.assertTrue(
                        any(required|{identifier}<=header for header in headers),
                        f"{filename} lacks an extractor-compatible {kind} table",
                    )

    def test_rendering_examples_do_not_claim_unavailable_runtimes(self):
        bpmn=(REF/"templates/diagram-bpmn.md").read_text(encoding="utf8")
        self.assertIn("build_bpmn.py",bpmn)
        self.assertIn("acyclic",bpmn)
        self.assertIn("not a general-purpose workflow engine",bpmn.lower())
        diagram=(REF/"source-methods/diagram-principles.md").read_text(encoding="utf8")
        self.assertIn("to_reqwise_payload.py",diagram)
        self.assertIn("zero live Figma writes",diagram)
        language=(REF/"source-methods/language.md").read_text(encoding="utf8")
        self.assertIn("Vietnamese",language)
        self.assertIn("code identifiers",language)

if __name__=="__main__":
    unittest.main()
