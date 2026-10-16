#!/usr/bin/env python3
"""Compile original portable model to Reqwise MIT figma_diagram arguments.

This produces a payload, NOT a native tool invocation. Confirm the installed
MCP schema/version using figma_docs and live tool availability before calling.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any
from validate_diagram_model import audit

SUPPORTED = {"activity", "userflow", "state", "sequence", "erd", "sitemap"}
VALID_RANKDIR = {"TB", "LR"}


def compile_model(model: dict[str, Any], *, ready_to_write: bool = False) -> dict[str, Any]:
    checked = audit(model)
    if not checked["ok"]:
        raise ValueError("Model failed structural check: " + "; ".join(checked["errors"]))
    kind = model["type"]
    if kind not in SUPPORTED:
        raise ValueError(f"Reqwise OSS diagram adapter does not support type {kind!r}")
    nodes = model["nodes"]
    edges = model["edges"]
    meta = model.get("metadata") if isinstance(model.get("metadata"), dict) else {}
    title = meta.get("title") or meta.get("artifact_id") or f"ANGENT {kind}"
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Model title must be nonempty")
    options = {"dryRun": not ready_to_write, "verify": True, "checkFirst": True, "crossCheck": True}
    if "rankdir" in meta:
        if meta["rankdir"] not in VALID_RANKDIR:
            raise ValueError("rankdir must be TB or LR")
        options["rankdir"] = meta["rankdir"]
    spec: dict[str, Any] = {"title": title.strip(), "options": options}
    if kind == "activity":
        lanes = sorted({n["lane"] for n in nodes if n.get("lane")})
        if lanes:
            if any(not n.get("lane") for n in nodes):
                raise ValueError("An activity with lanes requires an owner for every node")
            if "rankdir" not in meta:
                raise ValueError("Choose rankdir TB or LR before laying out swimlanes")
            spec["lanes"] = [{"id": s, "label": s} for s in lanes]
        mapping = {"task": "action", "initial": "start", "final": "end"}
        spec["nodes"] = [{"id": n["id"], "label": n["label"],
                           "kind": mapping.get(n.get("kind"), n.get("kind", "action")),
                           **({"lane": n["lane"]} if n.get("lane") else {})} for n in nodes]
        spec["edges"] = [
            {"from": e["from"], "to": e["to"],
             **({"label": str(e.get("guard") or e.get("label"))} if e.get("guard") or e.get("label") else {}),
             **({"kind": e["kind"]} if e.get("kind") in ("forward", "return") else {})} for e in edges
        ]
    elif kind == "userflow":
        mapping = {"start": "state", "initial": "state", "end": "terminal", "final": "terminal", "task": "screen"}
        spec["nodes"] = [{"id": n["id"], "label": n["label"], "kind": mapping.get(n.get("kind"), n.get("kind","screen")),
                           **({"screenId": n["screenId"]} if n.get("screenId") else {})} for n in nodes]
        spec["edges"] = [{"from": e["from"], "to": e["to"],
                           **({"label": str(e.get("guard") or e.get("label"))} if e.get("guard") or e.get("label") else {})}
                          for e in edges]
    elif kind == "state":
        mapping = {"start": "initial", "end": "final", "decision": "choice", "task": "state"}
        spec["states"] = [{"id": n["id"], "label": n["label"],
                            "kind": mapping.get(n.get("kind"), n.get("kind", "state"))} for n in nodes]
        spec["transitions"] = [{"from": e["from"], "to": e["to"],
                                **({"guard": str(e["guard"])} if e.get("guard") else {}),
                                **({"event": str(e["label"])} if e.get("label") else {})} for e in edges]
    elif kind == "sequence":
        if any(not e.get("label") for e in edges):
            raise ValueError("Every sequence message needs a meaningful label")
        pmap = {"db":"db","actor":"actor","external":"external","queue":"queue","system":"system"}
        spec["participants"] = [{"id": n["id"], "name": n["label"],
                                  "kind": pmap.get(n.get("kind"), "system")} for n in nodes]
        spec["messages"] = [{"id": f"message-{i+1}", "from": e["from"], "to": e["to"],
                             "label": e["label"], "kind": e.get("kind", "sync") if e.get("kind") in ("sync","async","return") else "sync"}
                            for i, e in enumerate(edges)]
    elif kind == "sitemap":
        roots = {n["id"] for n in nodes}
        parents: dict[str, str] = {}
        for e in edges:
            if e["to"] in parents:
                raise ValueError("Sitemap is a containment tree: a child cannot have two parents")
            parents[e["to"]] = e["from"]
        if len(roots - set(parents)) != 1:
            raise ValueError("Sitemap needs exactly one root")
        spec["pages"] = [{"id": n["id"], "label": n["label"],
                          **({"parent": parents[n["id"]]} if n["id"] in parents else {}),
                          "kind": n["kind"] if n.get("kind") in ("page","section","modal","external") else "page"} for n in nodes]
    elif kind == "erd":
        entities = []
        for n in nodes:
            attributes = n.get("attributes")
            if not isinstance(attributes, list) or not attributes:
                raise ValueError(f"ERD entity {n['id']} needs actual column definitions")
            for attr in attributes:
                if not isinstance(attr, dict) or not attr.get("name"):
                    raise ValueError(f"ERD entity {n['id']} has an unnamed column")
            if not n.get("external") and not any(a.get("key") in ("pk","pfk") for a in attributes):
                raise ValueError(f"ERD entity {n['id']} needs a primary key or external=true")
            entities.append({"id": n["id"], "name": n["label"], "attributes": attributes,
                             **({"external": True} if n.get("external") else {})})
        spec["entities"] = entities
        relations = []
        for e in edges:
            if not e.get("fromField") or not e.get("toField"):
                raise ValueError(f"ERD relationship {e['from']}->{e['to']} must name both columns")
            a = next(x for x in entities if x["id"] == e["from"])
            b = next(x for x in entities if x["id"] == e["to"])
            if e["fromField"] not in {x["name"] for x in a["attributes"]}:
                raise ValueError(f"Unknown ERD source column {e['fromField']}")
            if e["toField"] not in {x["name"] for x in b["attributes"]}:
                raise ValueError(f"Unknown ERD target column {e['toField']}")
            relations.append({"from": e["from"], "to": e["to"],
                              "fromField": e["fromField"], "toField": e["toField"],
                              **({"fromCard": e["fromCard"]} if e.get("fromCard") else {}),
                              **({"toCard": e["toCard"]} if e.get("toCard") else {}),
                              **({"label": e["label"]} if e.get("label") else {})})
        spec["relations"] = relations
    return {"tool": "figma_diagram", "arguments": {"type": kind, "spec": spec},
            "writes_performed": False, "requires_live_mcp": True,
            "dry_run": not ready_to_write, "upstream_model": "Reqwise Figma MCP MIT tool shape"}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--emit-write-payload", action="store_true", help="Only generates a prospective payload; it NEVER writes to Figma")
    args = p.parse_args()
    try:
        model = json.loads(args.input.read_text(encoding="utf-8"))
        result = compile_model(model, ready_to_write=args.emit_write_payload)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
