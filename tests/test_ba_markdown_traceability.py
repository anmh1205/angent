"""Real Atlas Markdown -> requirement graph -> honest coverage and preview."""
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from extract_markdown_graph import collect, markdown_tables
from validate_artifacts import audit
from render_preview import render

PROJECT=BA/"examples"
FEATURE=PROJECT/"docs/atlas-re"
SRS=FEATURE/"srs/atlas-re-spec.md"
CHECKLIST=FEATURE/"test/checklist/atlas-re-checklist-index.md"
CASES=FEATURE/"test/testcases/atlas-re-testcase-index.md"

class MarkdownTraceabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=collect({"srs":SRS,"checklist":CHECKLIST,"cases":CASES},PROJECT)

    def test_real_worked_example_has_explicit_typed_nodes(self):
        result=self.result
        self.assertEqual(result["counts"],{"BR":3,"CHECKLIST":9,"ERROR":4,
                                           "FR":8,"NFR":3,"TEST":11})
        self.assertEqual(len(result["graph"]["artifacts"]),38)
        self.assertTrue(audit(result["graph"])["ok"])

    def test_declared_test_links_not_equal_manual_summary(self):
        c=self.result["coverage"]
        self.assertEqual(c["functional_requirements"],8)
        self.assertEqual(c["traced_to_test"],4)
        self.assertIn("FR-atlas-re-005",c["uncovered"])
        # The upstream checklist narrative says 6/8. Only 4/8 FRs are
        # explicitly linked end-to-end within the three inspected files.
        self.assertFalse(any(x["id"]=="AC-001" for x in self.result["graph"]["artifacts"]))
        refs=self.result["unresolved_external_refs"]
        self.assertTrue(any(x["artifact"]=="CHK-001" and "AC-001" in x["referenced_ids"] for x in refs))
        self.assertTrue(any(x["artifact"]=="FR-atlas-re-001" and
                            "CAP-atlas-re-01" in x["referenced_ids"] for x in refs))

    def test_test_approval_not_execution(self):
        cases=[x for x in self.result["graph"]["artifacts"] if x["kind"]=="TEST"]
        self.assertEqual(len(cases),11)
        self.assertTrue(all(x["verification_status"]=="not-executed" for x in cases))
        self.assertTrue(all(x["source_refs"]==["SOURCE-CASES"] for x in cases))

    def test_generated_preview_uses_real_documents_not_fixture_counts(self):
        html=render(self.result["graph"],"Atlas evidence")
        self.assertEqual(html.count("<article "),38)
        self.assertIn("FR to test traceability: 4/8",html)
        self.assertIn("FR-atlas-re-006",html)

    def test_missing_checklist_does_not_fabricate_test_edges(self):
        report=collect({"srs":SRS,"cases":CASES},PROJECT)
        self.assertEqual(report["coverage"]["traced_to_test"],0)
        self.assertTrue(any(x["artifact"]=="TC-001" and
                            "CHK-001" in x["referenced_ids"] for x in report["unresolved_external_refs"]))

    def test_invalid_headers_or_duplicate_ids_are_rejected(self):
        malformed="| ID | Requirement |\n| --- | --- |\n| FR-demo-001 | One |\n| FR-demo-001 | Two |\n"
        with tempfile.TemporaryDirectory() as temp:
            directory=Path(temp)
            srs=directory/"srs.md"
            srs.write_text("---\ntype: srs\nstatus: approved\n---\n"+malformed,encoding="utf8")
            with self.assertRaisesRegex(ValueError,"Duplicate"):
                collect({"srs":srs},directory)

    def test_unrelated_source_directory_is_not_read(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError,"outside project root"):
                collect({"srs":SRS},Path(temp))

if __name__=="__main__":
    unittest.main()
