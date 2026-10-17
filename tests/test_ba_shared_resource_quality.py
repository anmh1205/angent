"""Prove 19 BA review rules and 8 original templates are substantive and distinct.

This test is a content-quality gate, not a substitute for stakeholder review.
The short triage and MIT source templates intentionally remain concise.
"""
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"extensions/angent-ba/skills/ba-kg/references"

RULE_TOPICS={
"r01":"Evidence precedence","r02":"Facts, inferences","r03":"Stable artifact",
"r04":"Business outcome","r05":"Requirements verifiability",
"r06":"Failure and recovery","r07":"Data and decision ownership",
"r08":"NFR workload","r09":"Decision-grade open questions",
"r10":"Privacy, security","r11":"Error semantics","r12":"Entity, identifier",
"r13":"Scoped change","r14":"Source freshness",
"r15":"External integration","r16":"Test independence",
"r17":"Real runtime","r18":"Audience-focused",
"r19":"ANGENT root authority"
}
ORIGINAL={
"original-code-to-srs.md":("Inspection map","Candidate requirements","Contradictions"),
"original-doc-drift.md":("Line-level comparison","Exception and trust-boundary","Decision record"),
"original-feature-preview.md":("Source-linked inventory","Verification summary","Approval questions"),
"original-knowledge-graph.md":("Declared relationships","Full lifecycle metrics","Graph integrity"),
"original-playwright.md":("Source to test mapping","Locators and environment","Run evidence"),
"original-prototype-next.md":("Screen-to-route model","Mock and real data boundaries","Build and browser evidence"),
"original-reverse-preview.md":("Source claim register","Navigable review","Read-back"),
"original-update-overview.md":("Actual change candidates","Safe before/after","Provider mutation"),
}

class BASharedResourceQuality(unittest.TestCase):
    def test_rules_have_distinct_operational_review_and_counterexamples(self):
        root=BASE/"rules"
        docs=sorted(root.glob("*.md"))
        self.assertEqual(len(docs),19)
        for i,path in enumerate(docs,1):
            with self.subTest(path=path.name):
                s=path.read_text(encoding="utf8")
                self.assertTrue(path.name.startswith("r"+str(i).zfill(2)+"-"))
                self.assertGreater(len(s),750)
                self.assertIn("## Operational contract",s)
                self.assertIn("## Checks before accepting an artifact",s)
                self.assertIn("## Failure response",s)
                self.assertIn("## Grounded example",s)
                self.assertIn(RULE_TOPICS["r"+str(i).zfill(2)],s)

    def test_all_48_templates_counted_but_short_inbox_is_valid(self):
        templates=BASE/"templates"
        paths=sorted(templates.glob("*.md"))
        self.assertEqual(len(paths),48)
        self.assertEqual(len(set(x.name for x in paths)),48)
        inbox=(templates/"doc-inbox.md").read_text(encoding="utf8")
        self.assertIn("{{note}}",inbox)
        for name,sections in ORIGINAL.items():
            with self.subTest(template=name):
                content=(templates/name).read_text(encoding="utf8")
                self.assertGreater(len(content),950)
                for heading in sections:
                    self.assertIn(heading,content)
                self.assertNotRegex(content,r"\| Stable ID \| Actual observation or accepted decision \|")

if __name__=="__main__":
    unittest.main()
