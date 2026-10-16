#!/usr/bin/env python3
"""Validate portable diagram graph structure; never claims Figma rendering."""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
import json
from pathlib import Path
from typing import Any

TYPES = {"usecase", "userflow", "activity", "bpmn", "sequence", "state", "erd",
         "journey", "sitemap", "persona", "design-system", "demo"}
# Pro-only "demo" has no fixed graph/terminal semantics in the public OSS kit.
FLOW = {"activity", "userflow", "state"}
FLOW_END = {
    "activity": {"end", "final"},
    "userflow": {"end", "final", "terminal", "external"},
    "state": {"end", "final"},
}
# These are the portable adapter's supported kinds, not an assertion about
# every possible shape in a proprietary Reqwise Pro runtime.
NODE_KINDS = {
    "activity": {"start", "initial", "end", "final", "task", "action", "decision"},
    "userflow": {"start", "initial", "end", "final", "terminal", "external",
                 "screen", "task", "state", "action", "decision"},
    "state": {"start", "initial", "end", "final", "state", "task", "decision", "choice"},
    "sequence": {"actor", "external", "queue", "system", "db"},
    "sitemap": {"page", "section", "modal", "external"},
    "erd": {"entity"},
}
ACYCLIC = {"sitemap"}


def audit(model: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(model, dict):
        return {"ok": False, "errors": ["Diagram must be an object"], "warnings": []}
    kind = model.get("type")
    if not isinstance(kind, str) or kind not in TYPES:
        errors.append("Unsupported type")
        kind = "unknown"
    nodes, edges = model.get("nodes"), model.get("edges")
    if not isinstance(nodes, list) or not isinstance(edges, list):
        return {"ok": False, "errors": errors + ["nodes and edges must be arrays"], "warnings": warnings}
    by_id = {}
    for i, node in enumerate(nodes):
        if not isinstance(node, dict) or not isinstance(node.get("id"), str) or not node["id"].strip():
            errors.append(f"nodes[{i}]: missing ID")
            continue
        key = node["id"]
        if any(ch.isspace() for ch in key):
            errors.append(f"nodes[{i}]: ID cannot contain whitespace")
        if key in by_id:
            errors.append(f"nodes[{i}]: duplicate ID {key}")
        by_id[key] = node
        if not isinstance(node.get("label"), str) or not node["label"].strip():
            errors.append(f"nodes[{i}]: empty label")
        node_kind = node.get("kind")
        if node_kind is not None and kind in NODE_KINDS and node_kind not in NODE_KINDS[kind]:
            errors.append(f"nodes[{i}]: unsupported {kind} node kind {node_kind!r}")
    adj: dict[str, set[str]] = defaultdict(set)
    indeg = {key: 0 for key in by_id}
    for i, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"edges[{i}]: not an object")
            continue
        a, b = edge.get("from"), edge.get("to")
        if not isinstance(a, str) or not isinstance(b, str) or a not in by_id or b not in by_id:
            errors.append(f"edges[{i}]: unknown endpoint")
            continue
        if b not in adj[a]:
            indeg[b] += 1
        adj[a].add(b)
        if a == b and kind in ("activity", "sitemap"):
            warnings.append(f"{a}: self-loop needs explicit rationale")
    if not nodes:
        errors.append("Diagram is empty")
    if kind in FLOW:
        starts = sorted(key for key, node in by_id.items()
                        if node.get("kind") in ("start", "initial"))
        ends = sorted(key for key, node in by_id.items()
                      if node.get("kind") in FLOW_END[kind])
        if len(starts) != 1:
            errors.append(f"{kind}: expected exactly one start/initial node")
        if not ends:
            errors.append(f"{kind}: missing terminal outcome")
        for key in starts:
            if indeg[key]:
                errors.append(f"{kind}: initial node {key} has incoming edges")
        for key in ends:
            if adj[key]:
                errors.append(f"{kind}: terminal node {key} has outgoing edges")
        reached = set(starts)
        q = deque(starts)
        while q:
            for nxt in sorted(adj[q.popleft()]):
                if nxt not in reached:
                    reached.add(nxt)
                    q.append(nxt)
        for key in sorted(by_id.keys() - reached):
            errors.append(f"{kind}: unreachable node {key}")
        for key in sorted(reached):
            if key not in ends and not adj[key]:
                errors.append(f"{kind}: dead end {key}")
        # Reachable retry cycles are legitimate only when they have a possible
        # route to a terminal. A connected, closed cycle must not pass merely
        # because a different branch reaches an end.
        reverse: dict[str, set[str]] = defaultdict(set)
        for src, targets in adj.items():
            for dst in targets:
                reverse[dst].add(src)
        can_finish = set(ends)
        pending = deque(ends)
        while pending:
            for previous in sorted(reverse[pending.popleft()]):
                if previous not in can_finish:
                    can_finish.add(previous)
                    pending.append(previous)
        for key in sorted(reached - can_finish):
            errors.append(f"{kind}: no path from {key} to a terminal")
        for key, node in by_id.items():
            if node.get("kind") == "decision":
                outgoing = [edge for edge in edges if isinstance(edge, dict) and edge.get("from") == key]
                if len(outgoing) < 2:
                    errors.append(f"{kind}: decision {key} needs two or more branches")
                conditions = [e.get("guard") or (e.get("label") if kind == "userflow" else None)
                              for e in outgoing]
                if any(not isinstance(value, str) or not value.strip() for value in conditions):
                    errors.append(f"{kind}: decision {key} has an unlabeled branch")
                elif len({value.strip() for value in conditions}) != len(conditions):
                    errors.append(f"{kind}: decision {key} has duplicate branch conditions")
    if kind in ACYCLIC:
        for key, degree in sorted(indeg.items()):
            if degree > 1:
                errors.append(f"sitemap: page {key} has multiple parents")
        roots = [k for k, deg in indeg.items() if deg == 0]
        if len(roots) != 1:
            errors.append("sitemap: expected one hierarchy root")
        visited: set[str] = set()
        def walk(k: str, visiting: set[str]):
            if k in visiting:
                errors.append(f"sitemap: cycle involving {k}")
                return
            if k in visited:
                return
            visited.add(k)
            for nxt in sorted(adj[k]):
                walk(nxt, visiting | {k})
        for root in roots:
            walk(root, set())
        for key in sorted(by_id.keys() - visited):
            errors.append(f"sitemap: unreachable node {key}")
    if kind == "erd":
        for i, edge in enumerate(edges):
            if not isinstance(edge, dict):
                continue
            for name in ("from", "to"):
                if edge.get(name) in by_id and by_id[edge[name]].get("kind") != "entity":
                    errors.append(f"erd: edges[{i}] connects a non-entity node")
            if not edge.get("cardinality"):
                warnings.append(f"erd: edges[{i}] missing cardinality")
    if kind == "sequence":
        for i, edge in enumerate(edges):
            if isinstance(edge, dict) and edge.get("from") in by_id and edge.get("to") in by_id:
                if not edge.get("label"):
                    warnings.append(f"sequence: edges[{i}] has no message label")
    return {"ok": not errors, "errors": sorted(set(errors)), "warnings": sorted(set(warnings)),
            "type": kind, "node_count": len(nodes), "edge_count": len(edges),
            "rendered_or_written_to_figma": False}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    opts = p.parse_args()
    try:
        payload = json.loads(opts.input.read_text(encoding="utf-8"))
        report = audit(payload)
    except (OSError, ValueError) as exc:
        report = {"ok": False, "errors": [str(exc)]}
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
