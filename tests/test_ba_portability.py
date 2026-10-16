"""Guard kit portability after substantive adaptations from the MIT source kits."""
import re
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba/skills"
FIGMA=ROOT/"extensions/angent-figma/skills"

class KitPortabilityTests(unittest.TestCase):
    def load(self,name):
        return (BA/name/"SKILL.md").read_text(encoding="utf8")

    def test_no_automatic_remote_diagram_disclosure(self):
        for name in ("ba-activity-swimlane","ba-usecase-diagram","ba-dbdiagram"):
            with self.subTest(skill=name):
                text=self.load(name)
                self.assertGreater(len(text),1700)
                self.assertFalse(re.search(r"(?im)^\s*(?:-|\d+\.)?\s*render via plantuml\.com",text))
                self.assertNotIn("render.sh --png",text)
                self.assertRegex(text.lower(),r"privacy|external|remote")
        self.assertIn("build_d2.py",self.load("ba-activity-swimlane"))

    def test_provider_methods_do_not_persist_shadow_state(self):
        for name in ("ba-jira","ba-confluence"):
            with self.subTest(skill=name):
                content=self.load(name)
                self.assertFalse(re.search(r"(?i)update\s+\.claude/state/",content))
                self.assertIn("read",content.lower())
                self.assertIn("provider",content.lower())
                self.assertIn("source",content.lower())
                self.assertIn("ANGENT",content)

    def test_discovery_never_requires_uninstalled_claude_loader(self):
        doc=self.load("ba-discover")
        self.assertNotIn("staleness is enforced at the loader",doc.lower())
        self.assertNotIn("write each answer back",doc.lower())
        self.assertIn("actual available tools",doc.lower())
        self.assertIn("source",doc.lower())

    def test_production_tools_are_not_faked(self):
        self.assertIn("not",self.load("ba-playwright-gen").lower())
        self.assertIn("openapi",self.load("ba-api-test").lower())
        for name in ("figma-usecase","figma-bpmn","figma-demo"):
            method=(FIGMA/name/"SKILL.md").read_text(encoding="utf8")
            self.assertIn("ANGENT",method)
            self.assertGreater(len(method),1600)

if __name__=="__main__":
    unittest.main()
