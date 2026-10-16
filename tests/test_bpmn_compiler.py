"""Semantic and XML-DI integrity tests for the bounded BPMN exporter."""
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"extensions/angent-ba/scripts"))
from build_bpmn import audit_ir, compile_bpmn, audit_geometry, BPMN, BPMNDI, DC, DI

CASE = ROOT/"extensions/angent-ba/examples/atlas-re/bpmn/claim-approval.ir.json"
Q = lambda ns, name: "{"+ns+"}"+name

class BPMNCompilerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ir = json.loads(CASE.read_text(encoding="utf-8"))

    def test_real_mit_case_semantics_and_export(self):
        checked = audit_ir(self.ir)
        self.assertTrue(checked["ok"], checked)
        xml = compile_bpmn(self.ir)
        root = ET.fromstring(xml)
        self.assertEqual(root.tag, Q(BPMN,"definitions"))
        p = root.find(Q(BPMN,"process"))
        self.assertEqual(p.attrib["isExecutable"],"false")
        flow_elems = p.findall(Q(BPMN,"sequenceFlow"))
        self.assertEqual(len(flow_elems), len(self.ir["flows"]))
        node_elems = sum((p.findall(Q(BPMN,x)) for x in
                         ("startEvent","endEvent","task","exclusiveGateway")), [])
        self.assertEqual(len(node_elems), len(self.ir["nodes"]))
        for elem in node_elems:
            expected = {f["id"] for f in self.ir["flows"] if f["src"] == elem.attrib["id"]}
            self.assertEqual({x.text for x in elem.findall(Q(BPMN,"outgoing"))},expected)
        lanes = p.find(Q(BPMN,"laneSet")).findall(Q(BPMN,"lane"))
        self.assertEqual(len(lanes),len(self.ir["lanes"]))
        all_refs = [n.text for lane in lanes for n in lane.findall(Q(BPMN,"flowNodeRef"))]
        self.assertEqual(Counter(all_refs),Counter(n["id"] for n in self.ir["nodes"]))
        plane = root.find(Q(BPMNDI,"BPMNDiagram")).find(Q(BPMNDI,"BPMNPlane"))
        shapes = plane.findall(Q(BPMNDI,"BPMNShape"))
        edges = plane.findall(Q(BPMNDI,"BPMNEdge"))
        self.assertEqual(len(shapes),len(self.ir["nodes"])+len(self.ir["lanes"]))
        self.assertEqual(len(edges),len(self.ir["flows"]))
        for edge in edges:
            self.assertGreaterEqual(len(edge.findall(Q(DI,"waypoint"))),2)
        for shape in shapes:
            bounds = shape.find(Q(DC,"Bounds"))
            self.assertGreater(float(bounds.attrib["width"]),0)
            self.assertGreater(float(bounds.attrib["height"]),0)
        self.assertEqual(xml,compile_bpmn(self.ir))

    def test_no_shape_or_connector_collisions_in_real_fixture(self):
        xml = compile_bpmn(self.ir)
        result = audit_geometry(xml)
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["checked_nodes"], 13)
        self.assertEqual(result["checked_flows"], 12)

    def test_layout_collisions_are_detected_by_negative_mutation(self):
        root=ET.fromstring(compile_bpmn(self.ir))
        plane=root.find(Q(BPMNDI,"BPMNDiagram")).find(Q(BPMNDI,"BPMNPlane"))
        shapes={shape.get("bpmnElement"):shape for shape in plane.findall(Q(BPMNDI,"BPMNShape"))}
        first=shapes["End_decline"].find(Q(DC,"Bounds"))
        second=shapes["Task_progress"].find(Q(DC,"Bounds"))
        first.set("x",second.get("x"))
        first.set("y",second.get("y"))
        outcome=audit_geometry(ET.tostring(root))
        self.assertFalse(outcome["ok"])
        self.assertTrue(any("overlaps" in e for e in outcome["errors"]))

    def test_single_lane_free_process(self):
        ir = deepcopy(self.ir)
        ir["lanes"]=[]
        for node in ir["nodes"]:
            node.pop("lane",None)
        self.assertTrue(audit_ir(ir)["ok"])
        root=ET.fromstring(compile_bpmn(ir))
        self.assertIsNone(root.find(".//"+Q(BPMN,"laneSet")))

    def test_missing_branch_label_and_dangling_reference(self):
        ir=deepcopy(self.ir)
        ir["flows"][3].pop("name")
        self.assertFalse(audit_ir(ir)["ok"])
        ir=deepcopy(self.ir)
        ir["flows"][3]["tgt"]="NOT_HERE"
        self.assertTrue(any("unknown" in e for e in audit_ir(ir)["errors"]))

    def test_cycle_rejected_instead_of_mislaid(self):
        ir=deepcopy(self.ir)
        ir["flows"].append({"id":"Flow_back","src":"Task_close","tgt":"Task_validate"})
        self.assertFalse(audit_ir(ir)["ok"])
        with self.assertRaises(ValueError):
            compile_bpmn(ir)

    def test_task_fork_without_gateway_rejected(self):
        ir=deepcopy(self.ir)
        ir["flows"].append({"id":"Flow_undocumented","src":"Task_validate","tgt":"End_rejected"})
        self.assertTrue(any("only gateway" in e for e in audit_ir(ir)["errors"]))

    def test_invalid_lane_or_identifiers_rejected(self):
        ir=deepcopy(self.ir)
        ir["nodes"][0]["lane"]="UNKNOWN"
        self.assertFalse(audit_ir(ir)["ok"])
        ir=deepcopy(self.ir)
        ir["nodes"][0]["id"]="not valid id"
        self.assertFalse(audit_ir(ir)["ok"])

    def test_invalid_container_types_fail_with_diagnostics_not_exceptions(self):
        mutations=[]
        a=deepcopy(self.ir);a["nodes"][0]["kind"]=["start"];mutations.append(a)
        a=deepcopy(self.ir);a["nodes"][0]["lane"]=["first"];mutations.append(a)
        a=deepcopy(self.ir);a["flows"][0]["src"]=["Node_unknown"];mutations.append(a)
        a=deepcopy(self.ir);a["flows"][0]["tgt"]={"invalid":"end"};mutations.append(a)
        for model in mutations:
            with self.subTest(model=model):
                outcome=audit_ir(model)
                self.assertFalse(outcome["ok"],outcome)
                self.assertTrue(outcome["errors"])
                with self.assertRaises(ValueError):
                    compile_bpmn(model)

    def test_xml_escape_for_untrusted_names(self):
        ir=deepcopy(self.ir)
        ir["nodes"][1]["name"]='Register <claim> & check "status"'
        content=compile_bpmn(ir)
        self.assertIn(b"&lt;claim&gt; &amp;",content)
        parsed=ET.fromstring(content)
        self.assertIn("&",parsed.find(".//"+Q(BPMN,"task")).get("name"))

if __name__=="__main__":
    unittest.main()
