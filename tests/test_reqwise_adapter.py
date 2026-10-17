"""Compile portable diagrams to inspectable OSS figma_diagram payloads."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIGMA = ROOT / "extensions/angent-figma"
sys.path.insert(0, str(FIGMA / "scripts"))
from to_reqwise_payload import compile_model

class ReqwisePayloadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.activity = json.loads((FIGMA / "examples/rental-fleet-activity.json").read_text())

    def test_source_references_checked_only_when_graph_supplied(self):
        graph_path=ROOT / "extensions/angent-ba/examples/rental-fleet-traceability.json"
        data=json.loads(graph_path.read_text(encoding="utf8"))
        ids={item["id"] for item in data["artifacts"]}
        outcome=compile_model(self.activity,evidence_ids=ids)
        self.assertEqual(outcome["source_link_check"],"ids-resolved-only")
        self.assertEqual(outcome["source_refs"],["FR-IVTS-01"])
        self.assertEqual(outcome["tool"],"figma_diagram")
        self.assertFalse(outcome["writes_performed"])
        bad=deepcopy(self.activity)
        bad["source_refs"]=["FR-NONEXISTENT"]
        with self.assertRaisesRegex(ValueError,"Unresolved evidence"):
            compile_model(bad,evidence_ids=ids)
        bad["source_refs"]=[]
        with self.assertRaisesRegex(ValueError,"No source_refs"):
            compile_model(bad,evidence_ids=ids)
        bad["source_refs"]=["FR-IVTS-01","FR-IVTS-01"]
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            compile_model(bad,evidence_ids=ids)

    def test_activity_dry_run_by_default(self):
        p = compile_model(self.activity)
        self.assertEqual(p["tool"], "figma_diagram")
        self.assertTrue(p["arguments"]["spec"]["options"]["dryRun"])
        self.assertEqual(p["arguments"]["spec"]["edges"][1]["label"], "yes")
        self.assertFalse(p["writes_performed"])

    def test_write_payload_is_still_not_a_tool_call(self):
        p = compile_model(self.activity, ready_to_write=True)
        self.assertFalse(p["dry_run"])
        self.assertFalse(p["writes_performed"])

    def test_invalid_lane_and_orientation_do_not_crash_adapter(self):
        for invalid in ([], {}, 12, True):
            with self.subTest(lane=invalid):
                m=deepcopy(self.activity)
                m["nodes"][0]["lane"]=invalid
                with self.assertRaisesRegex(ValueError,"lane must be a nonempty string"):
                    compile_model(m)
            with self.subTest(rankdir=invalid):
                m=deepcopy(self.activity)
                m["metadata"]["rankdir"]=invalid
                with self.assertRaisesRegex(ValueError,"rankdir"):
                    compile_model(m)

    def test_swimlane_requires_owner_and_orientation(self):
        m = deepcopy(self.activity)
        for n in m["nodes"]:
            n["lane"] = "fleet"
        with self.assertRaisesRegex(ValueError, "rankdir"):
            compile_model(m)
        m["metadata"]["rankdir"] = "LR"
        self.assertEqual(compile_model(m)["arguments"]["spec"]["lanes"], [{"id":"fleet","label":"fleet"}])
        del m["nodes"][2]["lane"]
        with self.assertRaisesRegex(ValueError, "owner"):
            compile_model(m)

    def test_userflow_return_is_not_silently_downgraded_to_normal_navigation(self):
        model=json.loads((FIGMA/"examples/rental-fleet-userflow.json").read_text(encoding="utf8"))
        # Re-entry to the same screen is an explicit retry, not a regular step.
        model["edges"].append({"from":"vehicle_list","to":"vehicle_list",
                               "label":"Refresh list","kind":"return"})
        self.assertTrue(compile_model(model)["dry_run"])
        edges=compile_model(model)["arguments"]["spec"]["edges"]
        self.assertEqual(edges[-1]["kind"],"return")

    def test_erd_rejects_invalid_cardinality_and_preserves_identifying(self):
        model=json.loads((FIGMA/"examples/rental-fleet-erd.json").read_text(encoding="utf8"))
        model["edges"][0]["identifying"]=True
        out=compile_model(model)["arguments"]["spec"]["relations"][0]
        self.assertTrue(out["identifying"])
        for field,bad in (("fromCard","exactly-five"),("toCard",False),("identifying","true")):
            with self.subTest(field=field):
                wrong=deepcopy(model)
                wrong["edges"][0][field]=bad
                with self.assertRaisesRegex(ValueError,"invalid|boolean"):
                    compile_model(wrong)
        wrong=deepcopy(model)
        del wrong["edges"][0]["toCard"]
        with self.assertRaisesRegex(ValueError,"cardinality shorthand"):
            compile_model(wrong)

    def test_state_and_sequence_mapping(self):
        state = deepcopy(self.activity)
        state["type"] = "state"
        p = compile_model(state)["arguments"]["spec"]
        self.assertEqual(p["states"][0]["kind"], "initial")
        self.assertEqual(p["transitions"][1]["guard"], "yes")
        seq = {"type":"sequence","nodes":[{"id":"api","kind":"system","label":"API"},{"id":"db","kind":"db","label":"DB"}],
               "edges":[{"from":"api","to":"db","label":"SELECT status"}], "metadata":{"title":"Status exchange"}}
        p = compile_model(seq)["arguments"]["spec"]
        self.assertEqual(p["participants"][1]["kind"], "db")
        self.assertEqual(p["messages"][0]["label"], "SELECT status")
        seq["edges"][0].pop("label")
        with self.assertRaisesRegex(ValueError, "message"):
            compile_model(seq)

    def test_sitemap_single_parent(self):
        m = {"type":"sitemap","nodes":[{"id":"root","label":"Root"},{"id":"a","label":"Page A"},{"id":"b","label":"Page B"}],
             "edges":[{"from":"root","to":"a"},{"from":"root","to":"b"}]}
        p = compile_model(m)["arguments"]["spec"]
        self.assertEqual(p["pages"][1]["parent"], "root")

    def test_erd_requires_column_integrity(self):
        base = {"type":"erd","nodes":[{"id":"users","kind":"entity","label":"users",
                    "attributes":[{"name":"id","type":"uuid","key":"pk"}]},
                    {"id":"vehicles","kind":"entity","label":"vehicles",
                    "attributes":[{"name":"user_id","type":"uuid","key":"fk"},{"name":"id","key":"pk"}]}],
                "edges":[{"from":"users","to":"vehicles","fromField":"id","toField":"user_id","fromCard":"one","toCard":"zero-many"}]}
        p = compile_model(base)["arguments"]["spec"]
        self.assertEqual(p["relations"][0]["toField"], "user_id")
        del base["edges"][0]["fromField"]
        with self.assertRaisesRegex(ValueError, "both columns"):
            compile_model(base)

    def test_erd_rejects_fake_external_ownership_and_invalid_columns(self):
        base = {"type": "erd", "nodes": [
            {"id": "external", "kind": "entity", "label": "External",
             "attributes": [{"name": "id", "type": "uuid"}]}], "edges": []}
        for value in ("false", 1, None):
            with self.subTest(external=value):
                altered = deepcopy(base)
                altered["nodes"][0]["external"] = value
                with self.assertRaisesRegex(ValueError, "external must be a boolean"):
                    compile_model(altered)
        good = deepcopy(base)
        good["nodes"][0]["external"] = True
        self.assertTrue(compile_model(good)["dry_run"])
        for attribute, message in [
            ({"name": "id", "key": "primary"}, "unsupported column key"),
            ({"name": "id", "required": "false"}, "required flag must be boolean"),
            ({"name": "id", "type": 0}, "invalid column type"),
        ]:
            changed = deepcopy(good)
            changed["nodes"][0]["attributes"] = [attribute]
            with self.subTest(attribute=attribute):
                with self.assertRaisesRegex(ValueError, message):
                    compile_model(changed)
        duplicates = deepcopy(good)
        duplicates["nodes"][0]["attributes"].append({"name": "id"})
        with self.assertRaisesRegex(ValueError, "duplicate column"):
            compile_model(duplicates)

    def test_unsupported_pro_diagram_not_claimed(self):
        bad = {"type":"bpmn","nodes":[{"id":"start","kind":"start","label":"Start"}],"edges":[]}
        with self.assertRaisesRegex(ValueError,"does not support"):
            compile_model(bad)

if __name__ == "__main__":
    unittest.main()
