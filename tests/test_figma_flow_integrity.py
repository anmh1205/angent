"""Portable Figma diagram models must not create convincing but invalid flows.

Only local structure and request-shape are checked; no Figma canvas is written.
"""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIGMA = ROOT / "extensions/angent-figma"
sys.path.insert(0, str(FIGMA / "scripts"))

from validate_diagram_model import audit
from to_reqwise_payload import compile_model


class DiagramFlowIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.activity = json.loads((FIGMA / "examples/rental-fleet-activity.json").read_text(encoding="utf-8"))
        cls.userflow = json.loads((FIGMA / "examples/rental-fleet-userflow.json").read_text(encoding="utf-8"))
        cls.state = json.loads((FIGMA / "examples/rental-fleet-state.json").read_text(encoding="utf-8"))
        cls.sitemap = json.loads((FIGMA / "examples/rental-fleet-sitemap.json").read_text(encoding="utf-8"))

    def test_existing_valid_fixtures_and_retry_cycles_remain_supported(self):
        for model in (self.activity, self.userflow, self.state, self.sitemap):
            with self.subTest(kind=model["type"]):
                report = audit(model)
                self.assertTrue(report["ok"], report)
                self.assertTrue(compile_model(model)["dry_run"])

    def test_closed_loop_reachable_from_start_without_terminal_exit_is_rejected(self):
        m = deepcopy(self.activity)
        m["nodes"] += [
            {"id": "retry1", "kind": "task", "label": "First retry"},
            {"id": "retry2", "kind": "task", "label": "Second retry"},
        ]
        m["edges"] += [
            {"from": "start", "to": "retry1"},
            {"from": "retry1", "to": "retry2"},
            {"from": "retry2", "to": "retry1"},
        ]
        report = audit(m)
        self.assertFalse(report["ok"])
        self.assertIn("activity: no path from retry1 to a terminal", report["errors"])
        with self.assertRaisesRegex(ValueError, "no path"):
            compile_model(m)

    def test_terminal_exit_and_reentered_initial_rejected(self):
        for edge, fragment in [
            ({"from": "allowed", "to": "authorize"}, "terminal node allowed has outgoing"),
            ({"from": "authorize", "to": "start"}, "initial node start has incoming"),
        ]:
            with self.subTest(edge=edge):
                m = deepcopy(self.activity)
                m["edges"].append(edge)
                report = audit(m)
                self.assertFalse(report["ok"])
                self.assertTrue(any(fragment in message for message in report["errors"]), report)

    def test_userflow_allows_external_terminal_and_labeled_decisions(self):
        m = deepcopy(self.userflow)
        denied = next(node for node in m["nodes"] if node["id"] == "denied")
        denied["kind"] = "external"
        for edge in m["edges"]:
            if edge["from"] == "authorized":
                edge["label"] = edge.pop("guard")
        report = audit(m)
        self.assertTrue(report["ok"], report)
        self.assertEqual(compile_model(m)["arguments"]["type"], "userflow")

    def test_reqwise_activity_decisions_support_labeled_edges(self):
        m = deepcopy(self.activity)
        for edge in m["edges"]:
            if edge["from"] == "authorize":
                edge["label"] = edge.pop("guard")
        self.assertTrue(audit(m)["ok"], audit(m))
        compiled = compile_model(m)
        self.assertEqual(compiled["arguments"]["spec"]["edges"][1]["label"], "yes")

    def test_decision_guard_collision_is_rejected(self):
        m = deepcopy(self.activity)
        m["edges"][-1]["guard"] = "yes"
        self.assertIn("activity: decision authorize has duplicate branch conditions", audit(m)["errors"])

    def test_official_reqwise_activity_fork_join_event_and_external_handoff(self):
        m = {"type": "activity", "nodes": [
            {"id": "start", "kind": "start", "label": "Begin"},
            {"id": "fork", "kind": "fork", "label": "Parallel split"},
            {"id": "work1", "kind": "action", "label": "Work 1"},
            {"id": "work2", "kind": "event", "label": "Event received"},
            {"id": "join", "kind": "join", "label": "Merge"},
            {"id": "external", "kind": "external", "label": "External handoff"}],
            "edges": [{"from": "start", "to": "fork"},
                      {"from": "fork", "to": "work1"},
                      {"from": "fork", "to": "work2"},
                      {"from": "work1", "to": "join"},
                      {"from": "work2", "to": "join"},
                      {"from": "join", "to": "external"}]}
        self.assertTrue(audit(m)["ok"], audit(m))
        payload = compile_model(m)["arguments"]["spec"]
        self.assertEqual([n["kind"] for n in payload["nodes"]][-4:],
                         ["action", "event", "join", "external"])

    def test_official_reqwise_state_fork_join_accepted(self):
        m = {"type": "state",
             "nodes": [{"id": "initial", "kind": "initial", "label": "Start"},
                       {"id": "fork", "kind": "fork", "label": "Split"},
                       {"id": "join", "kind": "join", "label": "Join"},
                       {"id": "final", "kind": "final", "label": "Done"}],
             "edges": [{"from": "initial", "to": "fork"},
                       {"from": "fork", "to": "join"},
                       {"from": "join", "to": "final"}]}
        self.assertTrue(audit(m)["ok"], audit(m))
        self.assertEqual(compile_model(m)["arguments"]["spec"]["states"][1]["kind"], "fork")

    def test_unknown_kind_is_not_forwarded_as_valid_reqwise_payload(self):
        m = deepcopy(self.activity)
        m["nodes"][1]["kind"] = "invented-step-kind"
        self.assertFalse(audit(m)["ok"])
        with self.assertRaisesRegex(ValueError, "unsupported activity node kind"):
            compile_model(m)

    def test_deep_sitemap_validates_without_recursive_stack_overflow(self):
        count = 1400
        m = {"type": "sitemap",
             "nodes": [{"id": f"page{i}", "kind": "page", "label": f"Page {i}"}
                       for i in range(count)],
             "edges": [{"from": f"page{i}", "to": f"page{i+1}"}
                       for i in range(count - 1)]}
        result = audit(m)
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(len(compile_model(m)["arguments"]["spec"]["pages"]), count)

    def test_sitemap_rejects_multiple_containment_parents(self):
        m = deepcopy(self.sitemap)
        m["edges"].append({"from": "vehicles", "to": "alerts"})
        self.assertIn("sitemap: page alerts has multiple parents", audit(m)["errors"])
        with self.assertRaisesRegex(ValueError, "multiple parents"):
            compile_model(m)


if __name__ == "__main__":
    unittest.main()
