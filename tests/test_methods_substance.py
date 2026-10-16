"""Prevent regression from real specialist content to mass-generated skill stubs."""
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
FIGMA=ROOT/"extensions/angent-figma"
ORIGINAL_BA={"code-to-srs","prototype-next","playwright-gen","doc-drift","ask",
             "kg","preview","reverse-preview","update-overview","delegate"}
ORIGINAL_FIGMA={"usecase","bpmn","journey","persona","design-system","demo"}

class MethodsSubstanceTests(unittest.TestCase):
    def test_55_distinct_methods_with_attributed_source(self):
        skills=list((BA/"skills").glob("ba-*/SKILL.md"))
        self.assertEqual(len(skills),55)
        content={p.parent.name[3:]:p.read_text(encoding="utf8") for p in skills}
        self.assertEqual(set(content),ORIGINAL_BA | (set(content)-ORIGINAL_BA))
        self.assertEqual(len(ORIGINAL_BA),10)
        for name,body in content.items():
            with self.subTest(skill=name):
                self.assertGreater(len(body),1500)
                self.assertGreater(len(set(body.splitlines())),20)
                if name not in ORIGINAL_BA:
                    self.assertIn("nv-minh/dev-ba-kit",body)
                    self.assertIn("##",body)
        self.assertIn("Copyright (c) 2026 Edward Ngo",(BA/"THIRD_PARTY_NOTICES.md").read_text())

    def test_12_figma_methods_provenance(self):
        skills=list((FIGMA/"skills").glob("figma-*/SKILL.md"))
        self.assertEqual(len(skills),12)
        for p in skills:
            body=p.read_text(encoding="utf8")
            with self.subTest(name=p.parent.name):
                self.assertGreater(len(body),1600)
                if p.parent.name[6:] not in ORIGINAL_FIGMA:
                    self.assertIn("reqwise-figma-mcp",body)
        self.assertTrue((FIGMA/"THIRD_PARTY_NOTICES.md").is_file())

    def test_templates_not_48_repeated_fillers(self):
        root=BA/"skills/ba-kg/references"
        templates=list((root/"templates").glob("*.md"))
        self.assertEqual(len(templates),48)
        self.assertEqual(sum(p.name.startswith(("doc-","diagram-")) for p in templates),40)
        self.assertEqual(sum(p.name.startswith("original-") for p in templates),8)
        self.assertEqual(len(list((root/"source-methods").glob("*.md"))),21)
        self.assertEqual(len(list((root/"rules").glob("*.md"))),19)

if __name__=="__main__":
    unittest.main()
