#!/usr/bin/env python3
"""Compile scoped BA graph models into D2 source; optionally render with real D2 CLI.

This is NOT an implementation of arbitrary D2 syntax or a generic graph drawing
engine. Rejected semantics must not be silently converted into a plausible image.
"""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from typing import Any

TYPE = {"activity", "erd", "architecture"}
DIRECTION = {"right", "down", "left", "up"}
ACTIVITY_KINDS = {"start", "end", "task", "decision"}
ARCH_KINDS = {"service", "database", "queue", "user", "external", "device", "boundary"}
FIELD_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")
FIELD_TYPES = re.compile(r"^[A-Za-z][A-Za-z0-9_(), .-]{0,80}$")
CONSTRAINTS = {"pk": "primary_key", "fk": "foreign_key", "unique": "unique"}
SHAPE = {"start": "circle", "end": "circle", "task": "rectangle",
         "decision": "diamond", "service": "rectangle", "database": "cylinder",
         "queue": "queue", "user": "person", "external": "rectangle",
         "device": "rectangle", "boundary": "rectangle"}
SVG = "{http://www.w3.org/2000/svg}svg"


def _string(value: Any, limit: int = 240) -> bool:
    return isinstance(value, str) and bool(value.strip()) and len(value) <= limit


def _text(value: str) -> str:
    """JSON quoted D2 label; newline and reserved delimiters cannot alter syntax."""
    return json.dumps(value, ensure_ascii=False)


def _id(value: str) -> str:
    # Encodes source identities into safe D2 keys, retaining labels separately.
    return "n_" + hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def validate(model: Any) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(model, dict):
        return {"ok": False, "errors": ["Diagram must be an object"]}
    kind = model.get("type")
    if not isinstance(kind, str) or kind not in TYPE:
        errors.append("Unsupported diagram type")
    if not _string(model.get("title")):
        errors.append("Diagram title must be nonempty")
    if not isinstance(model.get("direction", "right"), str) or model.get("direction", "right") not in DIRECTION:
        errors.append("Invalid direction")
    nodes, edges = model.get("nodes"), model.get("edges")
    if not isinstance(nodes, list) or not nodes or not isinstance(edges, list):
        return {"ok": False, "errors": errors + ["Nonempty nodes and edges array required"]}
    if len(nodes) > 250 or len(edges) > 600:
        errors.append("Diagram exceeds bounded size")
    byid: dict[str, dict] = {}
    groups: set[str] = set()
    for i, item in enumerate(nodes):
        if not isinstance(item, dict) or not _string(item.get("id"), 96):
            errors.append(f"nodes[{i}]: invalid node ID")
            continue
        key = item["id"]
        if key in byid:
            errors.append(f"nodes[{i}]: duplicate node ID {key}")
            continue
        byid[key] = item
        if not _string(item.get("label")):
            errors.append(f"nodes[{i}]: missing label")
        if kind == "activity" and (not isinstance(item.get("kind"), str) or item.get("kind") not in ACTIVITY_KINDS):
            errors.append(f"{key}: unsupported activity kind")
        if kind == "architecture" and (not isinstance(item.get("kind"), str) or item.get("kind") not in ARCH_KINDS):
            errors.append(f"{key}: unsupported architecture kind")
        if kind == "erd":
            if item.get("kind") != "entity":
                errors.append(f"{key}: ERD node must be an entity")
            attrs = item.get("attributes")
            if not isinstance(attrs, list) or not attrs:
                errors.append(f"{key}: missing nonempty attributes")
                continue
            colnames=set()
            for j, attr in enumerate(attrs):
                if not isinstance(attr, dict):
                    errors.append(f"{key}.attributes[{j}]: invalid attribute")
                    continue
                name, datatype = attr.get("name"), attr.get("type")
                if not isinstance(name, str) or not FIELD_RE.fullmatch(name):
                    errors.append(f"{key}.attributes[{j}]: unsafe field name")
                elif name in colnames:
                    errors.append(f"{key}: duplicate column {name}")
                colnames.add(name)
                if not isinstance(datatype, str) or not FIELD_TYPES.fullmatch(datatype):
                    errors.append(f"{key}.attributes[{j}]: invalid data type")
                val=attr.get("key")
                if val is not None and (not isinstance(val,str) or val not in CONSTRAINTS):
                    errors.append(f"{key}.attributes[{j}]: unsupported constraint")
            if not item.get("external") and not any(isinstance(a, dict) and a.get("key")=="pk" for a in attrs):
                errors.append(f"{key}: non-external entity requires primary key")
        if kind in ("activity","architecture"):
            group = item.get("lane" if kind=="activity" else "group")
            if group is not None:
                if not _string(group, 80):
                    errors.append(f"{key}: invalid lane/group")
                else:
                    groups.add(group)
    adj: dict[str, list[str]] = defaultdict(list)
    outgoing: dict[str,list[dict]] = defaultdict(list)
    for i, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"edges[{i}]: invalid edge")
            continue
        a,b = edge.get("from"),edge.get("to")
        if not isinstance(a,str) or not isinstance(b,str) or a not in byid or b not in byid:
            errors.append(f"edges[{i}]: unknown endpoint")
            continue
        adj[a].append(b)
        outgoing[a].append(edge)
        if "label" in edge and not _string(edge["label"], 160):
            errors.append(f"edges[{i}]: invalid edge label")
        if kind=="activity" and byid[a].get("kind")=="decision" and not _string(edge.get("guard"), 90):
            errors.append(f"edges[{i}]: decision branch requires guard")
        if kind=="erd":
            ca,cb=edge.get("fromField"),edge.get("toField")
            if not isinstance(ca,str) or not isinstance(cb,str) or not FIELD_RE.fullmatch(ca) or not FIELD_RE.fullmatch(cb):
                errors.append(f"edges[{i}]: ERD requires safe fromField/toField")
                continue
            for key,col in ((a,ca),(b,cb)):
                attrs=byid[key].get("attributes",[])
                if not isinstance(attrs,list) or col not in {x.get("name") for x in attrs if isinstance(x,dict)}:
                    errors.append(f"edges[{i}]: field {key}.{col} not declared")
            if not _string(edge.get("cardinality"),40):
                errors.append(f"edges[{i}]: missing cardinality")
        if kind=="architecture":
            if not _string(edge.get("protocol"), 80):
                errors.append(f"edges[{i}]: missing protocol/trust-flow meaning")
    if kind=="activity":
        starts=[k for k,n in byid.items() if n.get("kind")=="start"]
        ends=[k for k,n in byid.items() if n.get("kind")=="end"]
        if len(starts)!=1: errors.append("Activity requires exactly one start")
        if not ends: errors.append("Activity requires terminal end")
        if groups and any(not n.get("lane") for n in byid.values()):
            errors.append("All activity nodes need lanes when swimlanes are enabled")
        for key,node in byid.items():
            k=node.get("kind")
            if k=="decision" and len(outgoing[key])<2:
                errors.append(f"{key}: decision needs at least two guarded branches")
            if k=="end" and outgoing[key]:
                errors.append(f"{key}: end must have no outgoing edge")
            if k!="end" and not outgoing[key]:
                errors.append(f"{key}: nonterminal node has no exit")
        if starts:
            seen=set()
            queue=deque(starts)
            while queue:
                cur=queue.popleft()
                if cur in seen:continue
                seen.add(cur)
                queue.extend(adj[cur])
            for key in sorted(byid.keys()-seen):
                errors.append(f"{key}: unreachable from start")
    return {"ok": not errors, "errors": sorted(set(errors)), "node_count": len(byid),
            "edge_count": len(edges), "type": kind, "group_count":len(groups),
            "rendered": False}


def compile_source(model: dict[str,Any]) -> str:
    report=validate(model)
    if not report["ok"]:
        raise ValueError("; ".join(report["errors"]))
    kind=model["type"]
    ids={node["id"]:_id(node["id"]) for node in model["nodes"]}
    groups={}
    for node in model["nodes"]:
        name = node.get("lane" if kind=="activity" else "group")
        if name is not None:
            groups[name]="g_"+hashlib.sha256(name.encode("utf8")).hexdigest()[:16]
    lines=["# ANGENT BA D2 diagram: "+str(kind),
           "# Source is independent and proposed; SVG requires a separately checked D2 CLI.",
           "direction: "+model.get("direction","right")]
    for group,ident in sorted(groups.items()):
        lines.extend([ident+": "+_text(group)+" {", "  shape: rectangle", "}"])
    paths={}
    for node in model["nodes"]:
        ident=ids[node["id"]]
        group=node.get("lane" if kind=="activity" else "group")
        full=groups[group]+"."+ident if group in groups else ident
        paths[node["id"]]=full
        if kind=="erd":
            lines.append(ident+": "+_text(node["label"])+" {")
            lines.append("  shape: sql_table")
            for col in node["attributes"]:
                field=col["name"]
                dtype=col["type"]
                if col.get("key") in CONSTRAINTS:
                    lines.append("  "+_text(field)+": "+_text(dtype)+" {")
                    lines.append("    constraint: "+CONSTRAINTS[col["key"]])
                    lines.append("  }")
                else:
                    lines.append("  "+_text(field)+": "+_text(dtype))
            lines.append("}")
        else:
            shape=SHAPE[node["kind"]]
            if group in groups:
                # Define children via qualified paths, not by re-opening groups.
                lines.append(full+": "+_text(node["label"])+" {")
            else:
                lines.append(ident+": "+_text(node["label"])+" {")
            lines.append("  shape: "+shape)
            lines.append("}")
    for edge in model["edges"]:
        if kind=="erd":
            a=paths[edge["from"]]+"."+_text(edge["fromField"])
            b=paths[edge["to"]]+"."+_text(edge["toField"])
            label=edge["cardinality"]
        else:
            a,b=paths[edge["from"]],paths[edge["to"]]
            label=edge.get("guard") or edge.get("protocol") or edge.get("label")
        lines.append(a+" -> "+b+(": "+_text(label) if label else ""))
    return "\n".join(lines)+"\n"


def render_svg(d2file: Path, svgfile: Path, executable: str = "d2") -> dict[str,Any]:
    cmd=shutil.which(executable)
    if not cmd:
        return {"ok":False,"rendered":False,"error":"D2 CLI is unavailable; only .d2 generated"}
    if not d2file.is_file() or svgfile.resolve()==d2file.resolve():
        return {"ok":False,"rendered":False,"error":"Invalid render paths"}
    if svgfile.exists():
        return {"ok":False,"rendered":False,"error":"Refusing to overwrite existing SVG"}
    try:
        proc=subprocess.run([cmd,str(d2file),str(svgfile)],timeout=90,capture_output=True,text=True,errors="replace")
    except (OSError,subprocess.TimeoutExpired) as exc:
        return {"ok":False,"rendered":False,"error":str(exc)}
    if proc.returncode:
        return {"ok":False,"rendered":False,"exit_code":proc.returncode,
                "error":(proc.stderr or proc.stdout)[-2500:]}
    if not svgfile.is_file() or svgfile.stat().st_size<100:
        return {"ok":False,"rendered":False,"error":"Renderer exited but no nonempty SVG"}
    try:
        root=ET.parse(svgfile).getroot()
        if root.tag!=SVG:
            raise ValueError("Rendered file has no SVG root")
    except (ValueError,ET.ParseError,OSError) as exc:
        return {"ok":False,"rendered":False,"error":"Invalid SVG: "+str(exc)}
    return {"ok":True,"rendered":True,"svg":str(svgfile),
            "bytes":svgfile.stat().st_size,"exit_code":proc.returncode}


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input",type=Path)
    ap.add_argument("--output",required=True,type=Path)
    ap.add_argument("--svg",type=Path,help="Render SVG using real D2 CLI")
    ap.add_argument("--d2",default="d2",help="D2 executable path")
    args=ap.parse_args()
    try:
        data=json.loads(args.input.read_text(encoding="utf8"))
        output=compile_source(data)
        if args.output.exists():
            raise ValueError("Refusing to overwrite existing D2 output")
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(output,encoding="utf8")
    except (OSError,TypeError,ValueError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1
    result={"ok":True,"d2":str(args.output),"rendered":False,"model_type":data["type"]}
    if args.svg:
        result=render_svg(args.output,args.svg,args.d2)
        result["d2"]=str(args.output)
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__=="__main__":
    raise SystemExit(main())
