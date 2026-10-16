#!/usr/bin/env python3
"""Compile a bounded BA BPMN IR to importable BPMN 2.0 XML with basic diagram interchange.

Supported: one non-executable process, start/end events, tasks, exclusive
split/join gateways, optional lanes, directed acyclic sequence flows.
Unsupported semantics (loops, subprocesses, messages between pools, parallel
forks, boundary events, timer/cancel/compensation) are REJECTED rather than
misrepresented. Diagram geometry is deterministic, not a visual quality proof.
"""
from __future__ import annotations

import argparse
from collections import defaultdict, deque
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from typing import Any

BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"
BPMNDI = "http://www.omg.org/spec/BPMN/20100524/DI"
DC = "http://www.omg.org/spec/DD/20100524/DC"
DI = "http://www.omg.org/spec/DD/20100524/DI"
for prefix, uri in (("bpmn", BPMN), ("bpmndi", BPMNDI), ("dc", DC), ("di", DI)):
    ET.register_namespace(prefix, uri)
NCNAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_.-]*$")
NODE_TAGS = {"start": "startEvent", "end": "endEvent", "task": "task",
             "gateway": "exclusiveGateway"}
SHAPES = {"start": (36, 36), "end": (36, 36), "task": (178, 68),
          "gateway": (60, 60)}


def _id(value: Any, location: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not NCNAME.fullmatch(value):
        errors.append(location + ": invalid XML NCName")
        return ""
    return value


def audit_ir(ir: Any) -> dict[str, Any]:
    """Validate semantic contracts and reject flows that the layout cannot handle."""
    errors: list[str] = []
    if not isinstance(ir, dict):
        return {"ok": False, "errors": ["IR root must be an object"]}
    process = ir.get("process")
    if not isinstance(process, dict):
        return {"ok": False, "errors": ["process object required"]}
    pid = _id(process.get("id"), "process.id", errors)
    if not isinstance(process.get("title"), str) or not process["title"].strip():
        errors.append("process.title required")
    raw_nodes, raw_flows = ir.get("nodes"), ir.get("flows")
    raw_lanes = ir.get("lanes", [])
    if not isinstance(raw_nodes, list) or not isinstance(raw_flows, list) or not isinstance(raw_lanes, list):
        return {"ok": False, "errors": errors + ["nodes, flows and lanes must be arrays"]}
    lanes: dict[str, dict] = {}
    for i, lane in enumerate(raw_lanes):
        if not isinstance(lane, dict):
            errors.append(f"lanes[{i}] must be an object")
            continue
        key = _id(lane.get("id"), f"lanes[{i}].id", errors)
        if not isinstance(lane.get("name"), str) or not lane["name"].strip():
            errors.append(f"lanes[{i}].name required")
        if key in lanes:
            errors.append(f"duplicate lane ID {key}")
        if key:
            lanes[key] = lane
    nodes: dict[str, dict] = {}
    for i, node in enumerate(raw_nodes):
        if not isinstance(node, dict):
            errors.append(f"nodes[{i}] must be an object")
            continue
        key = _id(node.get("id"), f"nodes[{i}].id", errors)
        kind = node.get("kind")
        if kind not in NODE_TAGS:
            errors.append(f"nodes[{i}]: unsupported kind {kind!r}")
        if not isinstance(node.get("name"), str) or not node["name"].strip():
            errors.append(f"nodes[{i}]: name required")
        if lanes and node.get("lane") not in lanes:
            errors.append(f"nodes[{i}]: lane unknown or missing")
        if not lanes and node.get("lane"):
            errors.append(f"nodes[{i}]: lane specified without lanes list")
        if key in nodes:
            errors.append(f"duplicate node ID {key}")
        if key:
            nodes[key] = node
    starts = [k for k, v in nodes.items() if v.get("kind") == "start"]
    ends = [k for k, v in nodes.items() if v.get("kind") == "end"]
    if len(starts) != 1:
        errors.append("exactly one start event required")
    if not ends:
        errors.append("at least one end event required")
    flows: dict[str, dict] = {}
    outgoing: dict[str, list[str]] = defaultdict(list)
    incoming: dict[str, list[str]] = defaultdict(list)
    for i, flow in enumerate(raw_flows):
        if not isinstance(flow, dict):
            errors.append(f"flows[{i}] must be an object")
            continue
        key = _id(flow.get("id"), f"flows[{i}].id", errors)
        src, dest = flow.get("src"), flow.get("tgt")
        if src not in nodes or dest not in nodes:
            errors.append(f"flows[{i}]: unknown source or target")
            continue
        if src == dest:
            errors.append(f"flows[{i}]: self-loop not supported")
        if key in flows:
            errors.append(f"duplicate flow ID {key}")
        if key:
            flows[key] = flow
            outgoing[src].append(key)
            incoming[dest].append(key)
    all_ids = [pid] + list(nodes) + list(flows) + list(lanes)
    if len(set(all_ids)) != len(all_ids):
        errors.append("process, lane, node and flow IDs must be globally unique")
    for key, node in nodes.items():
        kind = node.get("kind")
        ins, outs = incoming[key], outgoing[key]
        if kind == "start" and (ins or len(outs) != 1):
            errors.append(f"{key}: start requires zero incoming and one outgoing")
        if kind == "end" and (not ins or outs):
            errors.append(f"{key}: end requires incoming and no outgoing")
        if kind not in ("start", "end") and (not ins or not outs):
            errors.append(f"{key}: nonterminal task/gateway requires incoming and outgoing")
        if kind == "gateway":
            if len(outs) >= 2:
                guards = [str(flows[f].get("name", "")).strip() for f in outs]
                if not all(guards) or len(set(guards)) != len(guards):
                    errors.append(f"{key}: diverging gateway needs distinct named branches")
            elif len(ins) < 2 or len(outs) != 1:
                errors.append(f"{key}: gateway must split >=2 or join >=2 flows")
        elif len(outs) > 1:
            errors.append(f"{key}: only gateway may split into multiple branches")
    if errors:
        return {"ok": False, "errors": sorted(set(errors))}
    indegree = {key: len(incoming[key]) for key in nodes}
    queue = deque(sorted(key for key, value in indegree.items() if value == 0))
    order: list[str] = []
    rank = {key: 0 for key in nodes}
    while queue:
        key = queue.popleft()
        order.append(key)
        for fid in sorted(outgoing[key]):
            dest = flows[fid]["tgt"]
            rank[dest] = max(rank[dest], rank[key] + 1)
            indegree[dest] -= 1
            if indegree[dest] == 0:
                queue.append(dest)
    if len(order) != len(nodes):
        errors.append("cycle detected: this bounded renderer cannot route loopbacks safely")
    if len(order) == len(nodes) and starts:
        seen = set()
        q = deque(starts)
        while q:
            key = q.popleft()
            if key in seen:
                continue
            seen.add(key)
            q.extend(flows[fid]["tgt"] for fid in outgoing[key])
        for key in sorted(nodes.keys() - seen):
            errors.append(f"{key}: unreachable from start")
        reaches_end = set(ends)
        q = deque(ends)
        while q:
            key = q.popleft()
            for fid in incoming[key]:
                prev = flows[fid]["src"]
                if prev not in reaches_end:
                    reaches_end.add(prev)
                    q.append(prev)
        for key in sorted(nodes.keys() - reaches_end):
            errors.append(f"{key}: cannot reach any end event")
    return {"ok": not errors, "errors": sorted(set(errors)),
            "node_count": len(nodes), "flow_count": len(flows), "lane_count": len(lanes),
            "order": order, "ranks": rank}


def compile_bpmn(ir: dict[str, Any]) -> bytes:
    report = audit_ir(ir)
    if not report["ok"]:
        raise ValueError("BPMN model invalid: " + "; ".join(report["errors"]))
    def q(ns: str, tag: str) -> str:
        return "{" + ns + "}" + tag
    defs = ET.Element(q(BPMN, "definitions"), id="Definitions_" + ir["process"]["id"],
                      targetNamespace="https://angent.dev/bpmn")
    process = ET.SubElement(defs, q(BPMN, "process"), id=ir["process"]["id"],
                            name=ir["process"]["title"], isExecutable="false")
    nodes = {node["id"]: node for node in ir["nodes"]}
    flow_by_src: dict[str, list[str]] = defaultdict(list)
    flow_by_dst: dict[str, list[str]] = defaultdict(list)
    for flow in ir["flows"]:
        flow_by_src[flow["src"]].append(flow["id"])
        flow_by_dst[flow["tgt"]].append(flow["id"])
    if ir.get("lanes"):
        lane_set = ET.SubElement(process, q(BPMN, "laneSet"), id="Lanes_" + ir["process"]["id"])
        for lane in ir["lanes"]:
            element = ET.SubElement(lane_set, q(BPMN, "lane"), id=lane["id"], name=lane["name"])
            for node in ir["nodes"]:
                if node["lane"] == lane["id"]:
                    ET.SubElement(element, q(BPMN, "flowNodeRef")).text = node["id"]
    for node in ir["nodes"]:
        kind = node["kind"]
        attrs = {"id": node["id"], "name": node["name"]}
        if kind == "gateway":
            attrs["gatewayDirection"] = (
                "Diverging" if len(flow_by_src[node["id"]]) >= 2 else "Converging")
        element = ET.SubElement(process, q(BPMN, NODE_TAGS[kind]), attrs)
        for fid in flow_by_dst[node["id"]]:
            ET.SubElement(element, q(BPMN, "incoming")).text = fid
        for fid in flow_by_src[node["id"]]:
            ET.SubElement(element, q(BPMN, "outgoing")).text = fid
    for flow in ir["flows"]:
        attrs = {"id": flow["id"], "sourceRef": flow["src"], "targetRef": flow["tgt"]}
        if flow.get("name"):
            attrs["name"] = flow["name"]
        ET.SubElement(process, q(BPMN, "sequenceFlow"), attrs)
    diagram = ET.SubElement(defs, q(BPMNDI, "BPMNDiagram"),
                             id="Diagram_" + ir["process"]["id"])
    plane = ET.SubElement(diagram, q(BPMNDI, "BPMNPlane"),
                          id="Plane_" + ir["process"]["id"],
                          bpmnElement=ir["process"]["id"])
    lane_ids = [l["id"] for l in ir.get("lanes", [])]
    col_width = 280
    row_height = 156
    top = 80
    left = 60
    # Topological longest-path ranks alone put sibling nodes in the SAME lane
    # at the same coordinates (a split into decline and continue, for example).
    # Reserve each lane/rank cell, then propagate any displacement downstream.
    predecessor: dict[str, list[str]] = defaultdict(list)
    for flow in ir["flows"]:
        predecessor[flow["tgt"]].append(flow["src"])
    assigned: dict[str, int] = {}
    occupancy: dict[str, set[int]] = defaultdict(set)
    for node_id in report["order"]:
        lane = nodes[node_id].get("lane", "_default")
        rank = max([report["ranks"][node_id]] +
                   [assigned[source] + 1 for source in predecessor[node_id]])
        while rank in occupancy[lane]:
            rank += 1
        assigned[node_id] = rank
        occupancy[lane].add(rank)
    maxrank = max(assigned.values()) if nodes else 0
    bounds: dict[str, tuple[int, int, int, int]] = {}
    for node in ir["nodes"]:
        width, height = SHAPES[node["kind"]]
        index = lane_ids.index(node["lane"]) if lane_ids else 0
        x = left + index * col_width + (col_width - width) // 2
        y = top + assigned[node["id"]] * row_height + (72-height)//2
        bounds[node["id"]] = (x, y, width, height)
    if lane_ids:
        for i, lane in enumerate(ir["lanes"]):
            shape = ET.SubElement(plane, q(BPMNDI, "BPMNShape"),
                                  id=lane["id"] + "_di", bpmnElement=lane["id"],
                                  isHorizontal="false")
            ET.SubElement(shape, q(DC, "Bounds"),
                          x=str(left + i*col_width-10), y="35",
                          width=str(col_width+20),
                          height=str((maxrank+1)*row_height+80))
    for node in ir["nodes"]:
        x, y, width, height = bounds[node["id"]]
        shape = ET.SubElement(plane, q(BPMNDI, "BPMNShape"),
                              id=node["id"] + "_di", bpmnElement=node["id"])
        ET.SubElement(shape, q(DC, "Bounds"), x=str(x), y=str(y),
                      width=str(width), height=str(height))
    for flow in ir["flows"]:
        sx, sy, sw, sh = bounds[flow["src"]]
        dx, dy, dw, dh = bounds[flow["tgt"]]
        ax, ay = sx+sw//2, sy+sh
        bx, by = dx+dw//2, dy
        # Route using a narrow gutter NEXT TO the destination lane. A
        # mid-point horizontal segment can cut through another branching task
        # placed on an intervening row; the gutter avoids that collision.
        src_lane = lane_ids.index(nodes[flow["src"]]["lane"]) if lane_ids else 0
        dst_lane = lane_ids.index(nodes[flow["tgt"]]["lane"]) if lane_ids else 0
        destination_left = left + dst_lane * col_width
        if dst_lane < src_lane:
            gutter_x = destination_left + col_width - 18
        elif dst_lane > src_lane:
            gutter_x = destination_left + 18
        else:
            gutter_x = destination_left + col_width - 18
        from_gap = ay + 18
        to_gap = by - 18
        if to_gap <= from_gap:
            raise ValueError("Layout row spacing insufficient for safe routing")
        points = [(ax, ay), (ax, from_gap), (gutter_x, from_gap),
                  (gutter_x, to_gap), (bx, to_gap), (bx, by)]
        edge = ET.SubElement(plane, q(BPMNDI, "BPMNEdge"),
                             id=flow["id"]+"_di", bpmnElement=flow["id"])
        last = None
        for x,y in points:
            if (x,y) != last:
                ET.SubElement(edge, q(DI, "waypoint"), x=str(x), y=str(y))
                last = (x,y)
    ET.indent(defs, space="  ")
    output = ET.tostring(defs, encoding="utf-8", xml_declaration=True)
    geometry = audit_geometry(output)
    if not geometry["ok"]:
        raise ValueError("BPMN layout has collisions: " + "; ".join(geometry["errors"]))
    return output




def audit_geometry(xml: bytes) -> dict[str, Any]:
    """Reject BPMN DI shape overlaps and connectors cutting through other nodes."""
    root = ET.fromstring(xml)
    q = lambda ns, tag: "{" + ns + "}" + tag
    lane_ids = {n.get("id") for n in root.iter(q(BPMN, "lane"))}
    boxes: dict[str, tuple[float,float,float,float]] = {}
    for shape in root.iter(q(BPMNDI, "BPMNShape")):
        key = shape.get("bpmnElement")
        if key in lane_ids:
            continue
        bounds = shape.find(q(DC, "Bounds"))
        if bounds is None or not key:
            continue
        boxes[key] = tuple(float(bounds.get(k, "0")) for k in ("x","y","width","height"))
    problems: list[str] = []
    keys = sorted(boxes)
    for i,key in enumerate(keys):
        ax,ay,aw,ah = boxes[key]
        if aw <= 0 or ah <= 0:
            problems.append(key + ": nonpositive bounding box")
        for other in keys[i+1:]:
            bx,by,bw,bh = boxes[other]
            if min(ax+aw,bx+bw) > max(ax,bx) and min(ay+ah,by+bh) > max(ay,by):
                problems.append(key + " overlaps " + other)
    flow_refs = {f.get("id"): (f.get("sourceRef"), f.get("targetRef"))
                 for f in root.iter(q(BPMN, "sequenceFlow"))}
    for edge in root.iter(q(BPMNDI, "BPMNEdge")):
        flow_id = edge.get("bpmnElement", "")
        endpoints = flow_refs.get(flow_id, ())
        points = [(float(p.get("x","0")),float(p.get("y","0")))
                  for p in edge.findall(q(DI,"waypoint"))]
        if len(points) < 2:
            problems.append(flow_id + ": fewer than two waypoints")
        for a,b in zip(points, points[1:]):
            (x1,y1),(x2,y2) = a,b
            if x1 != x2 and y1 != y2:
                problems.append(flow_id + ": nonorthogonal segment")
                continue
            for node,(x,y,w,h) in boxes.items():
                if node in endpoints:
                    continue
                if x1 == x2:
                    hit = x < x1 < x+w and max(min(y1,y2),y) < min(max(y1,y2),y+h)
                else:
                    hit = y < y1 < y+h and max(min(x1,x2),x) < min(max(x1,x2),x+w)
                if hit:
                    problems.append(flow_id + ": connector intersects " + node)
    return {"ok": not problems, "errors": sorted(set(problems)),
            "checked_nodes": len(boxes), "checked_flows": len(flow_refs)}

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--output", type=Path)
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    try:
        ir = json.loads(args.input.read_text(encoding="utf-8"))
        result = audit_ir(ir)
        if not result["ok"]:
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 1
        if args.check:
            print(json.dumps({k:v for k,v in result.items() if k not in ("order","ranks")},
                             ensure_ascii=False))
            return 0
        if args.output is None:
            p.error("--output required unless --check")
        output = compile_bpmn(ir)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(output)
        print(json.dumps({"ok": True, "output": str(args.output),
                          "bytes": len(output), "verified_with_external_modeler": False,
                          "diagram_layout": "deterministic-basic"}))
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
