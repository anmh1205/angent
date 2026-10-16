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

    def test_each_extracted_claim_has_a_real_source_line(self):
        graph=self.result["graph"]
        for node in graph["artifacts"]:
            with self.subTest(node=node["id"]):
                loc=node["source_location"]
                source=next(x for x in graph["sources"] if x["uri"]==loc["uri"])
                line=(PROJECT/loc["uri"]).read_text(encoding="utf-8").splitlines()[loc["line"]-1]
                self.assertIn(node["id"],line)
        page=render(graph)
        self.assertIn("srs/atlas-re-spec.md:L",page)

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
        malformed="| ID | Requirement | Covers |\n| --- | --- | --- |\n| FR-demo-001 | One | CAP-demo-01 |\n| FR-demo-001 | Two | CAP-demo-01 |\n"
        with tempfile.TemporaryDirectory() as temp:
            directory=Path(temp)
            srs=directory/"srs.md"
            srs.write_text("---\ntype: srs\nstatus: approved\n---\n"+malformed,encoding="utf8")
            with self.assertRaisesRegex(ValueError,"Duplicate"):
                collect({"srs":srs},directory)

    def test_malformed_recognized_id_cannot_silently_reduce_coverage(self):
        document=(
            "---\ntype: srs\nstatus: draft\n---\n"
            "| ID | Requirement | Covers |\n| --- | --- | --- |\n"
            "| FR-good-001 | First accepted requirement | CAP-demo-01 |\n"
            "| FR-bad-002? | This obligation cannot simply vanish | CAP-demo-01 |\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)
            source=base/"srs.md"
            source.write_text(document,encoding="utf8")
            with self.assertRaisesRegex(ValueError,"malformed artifact ID"):
                collect({"srs":source},base)
            source.write_text(
                document.replace("| FR-bad-002? |","| FR-bad-002 |"),
                encoding="utf8"
            )
            result=collect({"srs":source},base)
            self.assertEqual(result["counts"]["FR"],2)

    def test_unrelated_markdown_ids_are_not_misclassified_as_requirements(self):
        document=(
            "---\ntype: srs\nstatus: draft\n---\n"
            "| ID | Requirement | Covers |\n| --- | --- | --- |\n"
            "| FR-good-001 | Real requirement | CAP-demo-01 |\n"
            "| NOTE-002 | An explanatory item, not a requirement | |\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)
            source=base/"srs.md"
            source.write_text(document,encoding="utf8")
            self.assertEqual(collect({"srs":source},base)["counts"]["FR"],1)

    def test_examples_inside_markdown_fences_do_not_become_requirements(self):
        tick=chr(96)*3
        doc="\n".join([
            "---","type: srs","status: draft","---","# Source evidence",
            tick+"markdown",
            "| ID | Requirement | Covers |","| --- | --- | --- |",
            "| FR-FAKE-01 | This is an example, not a requirement | CAP-DEMO-01 |",
            tick,
            "~~~md",
            "| ID | Requirement | Covers |","| --- | --- | --- |",
            "| FR-FAKE-02 | Another syntax-only example | CAP-DEMO-02 |",
            "~~~",
            "| ID | Requirement | Covers |","| --- | --- | --- |",
            "| FR-REAL-03 | Authorized users can read the status | CAP-REAL-01 |",
            ""
        ])
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)
            source=base/"srs.md"
            source.write_text(doc,encoding="utf8")
            result=collect({"srs":source},base)
            self.assertEqual(result["counts"]["FR"],1)
            item=result["graph"]["artifacts"][0]
            self.assertEqual(item["id"],"FR-REAL-03")
            self.assertIn("FR-REAL-03",doc.splitlines()[item["source_location"]["line"]-1])

    def test_unrelated_source_directory_is_not_read(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError,"outside project root"):
                collect({"srs":SRS},Path(temp))


    def test_user_stories_and_usecases_extend_graph_without_making_up_ac(self):
        stories=FEATURE/"userstories/atlas-re-story-index.md"
        usecases=FEATURE/"usecases/atlas-re-usecase-index.md"
        result=collect({"srs":SRS,"checklist":CHECKLIST,"cases":CASES,
                        "stories":stories,"usecases":usecases},PROJECT)
        self.assertEqual(result["counts"]["STORY"],3)
        self.assertEqual(result["counts"]["USECASE"],1)
        self.assertEqual(len(result["graph"]["artifacts"]),42)
        by_id={a["id"]:a for a in result["graph"]["artifacts"]}
        self.assertEqual(by_id["US-001"]["depends_on"],["FR-atlas-re-006","FR-atlas-re-007"])
        self.assertEqual(by_id["UC-approve-claim"]["depends_on"],
                         ["FR-atlas-re-006","FR-atlas-re-007"])
        self.assertTrue(result["coverage"]["traced_to_test"]==4)
        self.assertNotIn("AC-001",by_id)
        self.assertEqual(by_id["US-001"]["source_location"]["uri"],
                         "docs/atlas-re/userstories/atlas-re-story-index.md")
        self.assertTrue(audit(result["graph"])["ok"])

    def test_new_sources_increase_change_impact_without_false_passes(self):
        from change_impact import impact
        result=collect({"srs":SRS,"checklist":CHECKLIST,"cases":CASES,
                        "stories":FEATURE/"userstories/atlas-re-story-index.md",
                        "usecases":FEATURE/"usecases/atlas-re-usecase-index.md"},PROJECT)
        changed=impact(result["graph"],["FR-atlas-re-006"])
        self.assertTrue(changed["ok"],changed)
        self.assertIn("US-001",changed["affected"])
        self.assertIn("UC-approve-claim",changed["affected"])
        self.assertFalse(changed["writes_performed"])

if __name__=="__main__":
    unittest.main()
