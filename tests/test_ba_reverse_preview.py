"""Executable, provenance-aware reverse preview: escaping, links and truth status."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from render_reverse_preview import validate,render

class ReversePreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=json.loads((BA/"examples/reverse-evidence-synthetic.json").read_text(encoding="utf8"))

    def test_real_render_and_distinct_evidence_classes(self):
        report=validate(self.model)
        self.assertTrue(report["ok"],report)
        self.assertEqual(report["claim_count"],3)
        self.assertEqual(report["confidence_breakdown"]["CONTRADICTORY"],1)
        page=render(self.model,"Legacy evidence")
        self.assertIn('Content-Security-Policy',page)
        self.assertIn('aria-label="Evidence claims"',page)
        self.assertEqual(page.count("<article "),3)
        self.assertIn("SOURCE-OBSERVED",page)
        self.assertIn("CONTRADICTORY",page)
        self.assertIn("none automatically promoted to accepted requirements",page.lower())
        self.assertNotIn("<script",page)

    def test_rejects_fabricated_approval_and_weak_contradiction(self):
        a=deepcopy(self.model)
        a["claims"][0]["confidence"]="APPROVED-DECISION"
        self.assertFalse(validate(a)["ok"])
        with self.assertRaises(ValueError):
            render(a)
        a=deepcopy(self.model)
        a["claims"][2]["source_refs"]=["SRC-DOC"]
        self.assertTrue(any("two distinct" in e for e in validate(a)["errors"]))
        a=deepcopy(self.model)
        a["claims"][1]["source_refs"]=["NOT-FOUND"]
        self.assertFalse(validate(a)["ok"])

    def test_observed_claim_without_real_source_is_not_represented_as_observed(self):
        for refs in ([],["SRC-CODE","SRC-CODE"],["UNKNOWN"]):
            with self.subTest(refs=refs):
                a=deepcopy(self.model)
                a["claims"][0]["source_refs"]=refs
                result=validate(a)
                self.assertFalse(result["ok"])
                self.assertTrue(any("source" in e for e in result["errors"]))
                with self.assertRaisesRegex(ValueError,"source"):
                    render(a)

    def test_unverified_claimed_approval_needs_bounded_decision_id(self):
        a=deepcopy(self.model)
        a["claims"][0]["confidence"]="APPROVED-DECISION"
        a["claims"][0]["approval_source"]="SRC-CODE"
        for did in ([],{"text":"accepted"},"", "not a stable identifier"):
            with self.subTest(decision_id=did):
                a["claims"][0]["decision_id"]=did
                result=validate(a)
                self.assertFalse(result["ok"])
                self.assertTrue(any("stable decision ID" in e for e in result["errors"]))
        a["claims"][0]["decision_id"]="DEC-001"
        result=validate(a)
        self.assertTrue(result["ok"],result)
        self.assertIn("not independently verified",result["approval_source_checked"])

    def test_html_injection_and_unsafe_urls_remain_literal(self):
        a=deepcopy(self.model)
        a["claims"][0]["statement"]='<script>alert("private")</script>'
        a["sources"][1]["uri"]='javascript:alert("bad")'
        result=render(a,"<danger>")
        self.assertNotIn("<script>",result)
        self.assertIn("&lt;script&gt;",result)
        self.assertIn("&lt;danger&gt;",result)
        self.assertNotIn('href="javascript:',result)
        self.assertIn("javascript:alert",result)

if __name__=="__main__":
    unittest.main()
