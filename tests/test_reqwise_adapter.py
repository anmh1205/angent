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

    def test_structural_payload_retains_warnings_and_does_not_claim_approval(self):
        payload=compile_model(self.activity)
        self.assertEqual(payload["semantic_approval"],"not-established")
        self.assertTrue(isinstance(payload["model_warnings"],list))
        erd=json.loads((FIGMA/"examples/rental-fleet-erd.json").read_text(encoding="utf8"))
        erd["edges"][0].pop("cardinality",None)
        erd["edges"][0].pop("fromCard")
        erd["edges"][0].pop("toCard")
        result=compile_model(erd)
        self.assertTrue(any("cardinality" in warning for warning in result["model_warnings"]))

    def test_invalid_metadata_title_must_not_be_silently_replaced(self):
        for key in ("title","artifact_id"):
            for bad in ([],{},0,False,""):
                with self.subTest(key=key,bad=bad):
                    model=deepcopy(self.activity)
                    model["metadata"][key]=bad
                    with self.assertRaisesRegex(ValueError,"metadata."+key):
                        compile_model(model)
        sample=deepcopy(self.activity)
        sample["metadata"]["artifact_id"]="FR-IVTS-01"
        self.assertEqual(compile_model(sample)["arguments"]["spec"]["title"],"FR-IVTS-01")

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

    def test_six_oss_diagram_types_preserve_source_backed_annotations(self):
        flow=json.loads((FIGMA/"examples/rental-fleet-userflow.json").read_text(encoding="utf8"))
        flow["metadata"]["linkScreens"]=True
        flow["nodes"][1].update({"detail":"Search and select a vehicle",
                                 "slug":"vehicle-list","cls":"happy"})
        out=compile_model(flow)["arguments"]["spec"]
        self.assertTrue(out["options"]["linkScreens"])
        self.assertEqual(out["nodes"][1]["slug"],"vehicle-list")
        self.assertEqual(out["nodes"][1]["detail"],"Search and select a vehicle")
        self.assertEqual(out["nodes"][1]["cls"],"happy")
        activity=deepcopy(self.activity)
        activity["nodes"][1].update({"detail":"Check access policy","cls":"decision"})
        node=compile_model(activity)["arguments"]["spec"]["nodes"][1]
        self.assertEqual(node["detail"],"Check access policy")
        self.assertEqual(node["cls"],"decision")
        state=json.loads((FIGMA/"examples/rental-fleet-state.json").read_text(encoding="utf8"))
        state["nodes"][1].update({"entry":"initialize receiver",
                                  "do":"read heartbeat","exit":"close connection"})
        state["edges"][1].update({"action":"notify operator","kind":"return"})
        compiled=compile_model(state)["arguments"]["spec"]
        self.assertEqual(compiled["states"][1]["entry"],"initialize receiver")
        self.assertEqual(compiled["transitions"][1]["action"],"notify operator")
        self.assertEqual(compiled["transitions"][1]["kind"],"return")
        seq=json.loads((FIGMA/"examples/rental-fleet-sequence.json").read_text(encoding="utf8"))
        seq["nodes"][1]["detail"]="Authorization boundary"
        seq["edges"][1]["note"]="Timeout must be handled separately"
        compiled=compile_model(seq)["arguments"]["spec"]
        self.assertEqual(compiled["participants"][1]["detail"],"Authorization boundary")
        self.assertEqual(compiled["messages"][1]["note"],"Timeout must be handled separately")
        site=json.loads((FIGMA/"examples/rental-fleet-sitemap.json").read_text(encoding="utf8"))
        site["nodes"][1]["screenId"]=["fleet-overview","fleet-overview-empty"]
        self.assertEqual(compile_model(site)["arguments"]["spec"]["pages"][1]["screenId"],
                         ["fleet-overview","fleet-overview-empty"])
        erd=json.loads((FIGMA/"examples/rental-fleet-erd.json").read_text(encoding="utf8"))
        erd["nodes"][0].update({"detail":"Authoritative owner", "cls":"happy"})
        entity=compile_model(erd)["arguments"]["spec"]["entities"][0]
        self.assertEqual(entity["detail"],"Authoritative owner")
        self.assertEqual(entity["cls"],"happy")

    def test_diagram_annotations_reject_fake_provider_semantics(self):
        model=json.loads((FIGMA/"examples/rental-fleet-userflow.json").read_text(encoding="utf8"))
        for invalid in ("yes", 1, None):
            with self.subTest(linkScreens=invalid):
                bad=deepcopy(model)
                bad["metadata"]["linkScreens"]=invalid
                with self.assertRaisesRegex(ValueError,"linkScreens"):
                    compile_model(bad)
        for field,value in (("cls","unknown-theme"),("detail",[]),("slug",False)):
            with self.subTest(field=field):
                bad=deepcopy(model)
                bad["nodes"][1][field]=value
                with self.assertRaisesRegex(ValueError,"Model failed structural check"):
                    compile_model(bad)
        bad=deepcopy(model)
        bad["edges"][2]["label"]="No"
        with self.assertRaisesRegex(ValueError,"conflicting guard and label"):
            compile_model(bad)
        site=json.loads((FIGMA/"examples/rental-fleet-sitemap.json").read_text(encoding="utf8"))
        site["nodes"][1]["screenId"]=["duplicate","duplicate"]
        with self.assertRaisesRegex(ValueError,"invalid screenId"):
            compile_model(site)

    def test_sequence_fragments_preserve_business_alternatives_and_stable_ids(self):
        original=json.loads((FIGMA/"examples/rental-fleet-sequence.json").read_text(encoding="utf8"))
        result=compile_model(original)["arguments"]["spec"]
        self.assertEqual(result["fragments"][0]["kind"],"alt")
        self.assertEqual(result["fragments"][0]["else"]["messages"],["message-5"])
        self.assertEqual(len(result["messages"]),5)
        changed=deepcopy(original)
        changed["edges"][3]["id"]="authorized-answer"
        changed["edges"][4]["id"]="denied-answer"
        changed["fragments"][0]["messages"]=["authorized-answer"]
        changed["fragments"][0]["else"]["messages"]=["denied-answer"]
        generated=compile_model(changed)["arguments"]["spec"]
        self.assertEqual(generated["messages"][3]["id"],"authorized-answer")
        self.assertEqual(generated["fragments"][0]["else"]["messages"],["denied-answer"])

    def test_sequence_fragments_must_be_contiguous_and_alternatives_have_else(self):
        original=json.loads((FIGMA/"examples/rental-fleet-sequence.json").read_text(encoding="utf8"))
        missing_else=deepcopy(original)
        missing_else["fragments"][0].pop("else")
        with self.assertRaisesRegex(ValueError,"alt needs an else branch"):
            compile_model(missing_else)
        gap=deepcopy(original)
        gap["fragments"][0]["messages"]=["message-2","message-4"]
        gap["fragments"][0]["else"]["messages"]=["message-5"]
        with self.assertRaisesRegex(ValueError,"contiguous"):
            compile_model(gap)
        misplaced=deepcopy(original)
        misplaced["fragments"][0]["messages"]=["message-5"]
        misplaced["fragments"][0]["else"]["messages"]=["message-4"]
        with self.assertRaisesRegex(ValueError,"contiguous time range"):
            compile_model(misplaced)
        valid=deepcopy(original)
        valid["fragments"]=[{"kind":"loop","label":"Poll latest status",
                             "messages":["message-2","message-3"]}]
        self.assertEqual(compile_model(valid)["arguments"]["spec"]["fragments"][0]["kind"],"loop")

    def test_sequence_rejects_missing_and_duplicated_fragment_messages(self):
        original=json.loads((FIGMA/"examples/rental-fleet-sequence.json").read_text(encoding="utf8"))
        mutants=[]
        unknown=deepcopy(original)
        unknown["fragments"][0]["messages"]=["unknown-message"]
        mutants.append((unknown,"unknown messages"))
        repeated=deepcopy(original)
        repeated["fragments"][0]["messages"]=["message-4","message-4"]
        mutants.append((repeated,"repeats a message"))
        collision=deepcopy(original)
        collision["edges"][3]["id"]="message-5"
        mutants.append((collision,"duplicate message ID"))
        invalid=deepcopy(original)
        invalid["fragments"][0]["kind"]="tryexcept"
        mutants.append((invalid,"unsupported fragment kind"))
        ambiguous=deepcopy(original)
        ambiguous["fragments"][0]["else"]["messages"]=["message-4"]
        mutants.append((ambiguous,"both branches"))
        no_array=deepcopy(original)
        no_array["fragments"]={}
        mutants.append((no_array,"fragments must be an array"))
        for bad, message in mutants:
            with self.subTest(message=message):
                with self.assertRaisesRegex(ValueError,message):
                    compile_model(bad)

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
