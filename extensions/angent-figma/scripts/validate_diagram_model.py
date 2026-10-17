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
    "activity": {"start", "initial", "end", "final", "task", "action", "decision",
                 "fork", "join", "event", "external"},
    "userflow": {"start", "initial", "end", "final", "terminal", "external",
                 "screen", "task", "state", "decision"},
    "state": {"start", "initial", "end", "final", "state", "task", "decision",
              "choice", "fork", "join"},
    "sequence": {"actor", "external", "queue", "system", "db"},
    "sitemap": {"page", "section", "modal", "external"},
    "erd": {"entity"},
}
ACYCLIC = {"sitemap"}
VISUAL_CLASSES = {"happy", "error", "edge", "plain", "decision"}


def audit(model: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(model, dict):
        return {"ok": False, "errors": ["Diagram must be an object"], "warnings": []}
    kind = model.get("type")
    if not isinstance(kind, str) or kind not in TYPES:
        errors.append("Unsupported type")
        kind = "unknown"
    if "metadata" in model and not isinstance(model["metadata"], dict):
        errors.append("metadata must be an object")
    meta=model.get("metadata") if isinstance(model.get("metadata"),dict) else {}
    if "continuous" in meta and (kind != "state" or not isinstance(meta["continuous"],bool)):
        errors.append("metadata.continuous must be a boolean on state diagrams")
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
        if node_kind is not None and (not isinstance(node_kind, str) or
                                       (kind in NODE_KINDS and node_kind not in NODE_KINDS[kind])):
            errors.append(f"nodes[{i}]: unsupported {kind} node kind {node_kind!r}")
        for field in ("lane", "detail", "slug", "entry", "do", "exit"):
            if field in node and (not isinstance(node[field], str) or not node[field].strip()):
                errors.append(f"nodes[{i}]: {field} must be a nonempty string")
        if "cls" in node and (not isinstance(node["cls"],str) or node["cls"] not in VISUAL_CLASSES):
            errors.append(f"nodes[{i}]: unsupported visual class")
        if "screenId" in node:
            ref=node["screenId"]
            if kind=="sitemap":
                valid=(isinstance(ref,str) and bool(ref.strip())) or (
                    isinstance(ref,list) and bool(ref) and
                    all(isinstance(x,str) and bool(x.strip()) for x in ref) and
                    len(set(ref))==len(ref))
            else:
                valid=isinstance(ref,str) and bool(ref.strip())
            if not valid:
                errors.append(f"nodes[{i}]: invalid screenId reference")
    adj: dict[str, set[str]] = defaultdict(set)
    indeg = {key: 0 for key in by_id}
    for i, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"edges[{i}]: not an object")
            continue
        a, b = edge.get("from"), edge.get("to")
        # Do not silently stringify booleans/objects/numbers into a seemingly
        # meaningful business guard, event or message on the Figma canvas.
        for field in ("guard", "label", "note", "action"):
            if field in edge and (
                not isinstance(edge[field], str) or not edge[field].strip()
            ):
                errors.append(f"edges[{i}]: {field} must be a nonempty string")
        if "cls" in edge and (not isinstance(edge["cls"],str) or edge["cls"] not in VISUAL_CLASSES):
            errors.append(f"edges[{i}]: unsupported visual class")
        if (kind in ("activity","userflow") and "label" in edge and "guard" in edge
            and isinstance(edge["label"],str) and isinstance(edge["guard"],str)
            and edge["label"].strip()!=edge["guard"].strip()):
            errors.append(f"edges[{i}]: conflicting guard and label; Reqwise has one edge label")
        if not isinstance(a, str) or not isinstance(b, str) or a not in by_id or b not in by_id:
            errors.append(f"edges[{i}]: unknown endpoint")
            continue
        if b not in adj[a]:
            indeg[b] += 1
        adj[a].add(b)
        edge_types = ({"sync", "async", "return"} if kind == "sequence" else
                      {"forward", "return"} if kind in FLOW else None)
        if (edge_types is not None and "kind" in edge and
            (not isinstance(edge["kind"], str) or edge["kind"] not in edge_types)):
            errors.append(f"edges[{i}]: unsupported {kind} edge kind {edge['kind']!r}")
        if a == b and kind in ("activity", "sitemap"):
            warnings.append(f"{a}: self-loop needs explicit rationale")
    if not nodes:
        errors.append("Diagram is empty")
    if kind in FLOW:
        starts = sorted(key for key, node in by_id.items()
                        if isinstance(node.get("kind"), str) and
                        node.get("kind") in ("start", "initial"))
        ends = sorted(key for key, node in by_id.items()
                      if isinstance(node.get("kind"), str) and
                      node.get("kind") in FLOW_END[kind])
        # A handoff to an external party can legitimately terminate the team's
        # activity without inventing an internal completion event.
        external_exits = (sorted(key for key, node in by_id.items()
                                 if node.get("kind") == "external" and not adj[key])
                          if kind == "activity" else [])
        terminals = sorted(set(ends + external_exits))
        # A persistent session, switch or process may legitimately have no
        # final state, but this must be a documented design decision.
        continuous = kind == "state" and meta.get("continuous") is True and not terminals
        if continuous:
            warnings.append("state: explicitly continuous lifecycle without final; review termination policy")
        if len(starts) != 1:
            errors.append(f"{kind}: expected exactly one start/initial node")
        if not terminals and not continuous:
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
            if key not in terminals and not adj[key]:
                errors.append(f"{kind}: dead end {key}")
        # Reachable retry cycles are legitimate only when they have a possible
        # route to a terminal. A connected, closed cycle must not pass merely
        # because a different branch reaches an end.
        reverse: dict[str, set[str]] = defaultdict(set)
        for src, targets in adj.items():
            for dst in targets:
                reverse[dst].add(src)
        can_finish = set(terminals)
        pending = deque(terminals)
        while pending:
            for previous in sorted(reverse[pending.popleft()]):
                if previous not in can_finish:
                    can_finish.add(previous)
                    pending.append(previous)
        if not continuous:
            for key in sorted(reached - can_finish):
                errors.append(f"{kind}: no path from {key} to a terminal")
        for key, node in by_id.items():
            if node.get("kind") in ("decision", "choice"):
                outgoing = [edge for edge in edges if isinstance(edge, dict) and edge.get("from") == key]
                if len(outgoing) < 2:
                    errors.append(f"{kind}: decision {key} needs two or more branches")
                if kind == "state":
                    # In a UML choice node, at most one outgoing transition
                    # may be the implicit else branch. Events are not guards.
                    conditions = [e.get("guard") for e in outgoing]
                    missing = sum(not isinstance(x, str) or not x.strip() for x in conditions)
                    if missing > 1:
                        errors.append(f"{kind}: choice {key} has multiple unguarded branches")
                    supplied = [x.strip() for x in conditions if isinstance(x, str) and x.strip()]
                    if len(set(supplied)) != len(supplied):
                        errors.append(f"{kind}: choice {key} has duplicate branch guards")
                else:
                    conditions = [e.get("guard") or e.get("label") for e in outgoing]
                    if any(not isinstance(value, str) or not value.strip() for value in conditions):
                        errors.append(f"{kind}: decision {key} has an unlabeled branch")
                    elif len({value.strip() for value in conditions}) != len(conditions):
                        errors.append(f"{kind}: decision {key} has duplicate branch conditions")
    if kind == "state":
        for i,edge in enumerate(edges):
            if not isinstance(edge,dict) or edge.get("from") not in by_id:
                continue
            origin=by_id[edge["from"]]
            if (origin.get("kind") not in ("initial","start","choice","decision","fork","join")
                and not edge.get("label") and not edge.get("guard")
                and not origin.get("do")):
                warnings.append(
                    f"state: transitions[{i}] lacks event/guard and originating do activity; review trigger"
                )
    if kind in ACYCLIC:
        for key, degree in sorted(indeg.items()):
            if degree > 1:
                errors.append(f"sitemap: page {key} has multiple parents")
        roots = [k for k, deg in indeg.items() if deg == 0]
        if len(roots) != 1:
            errors.append("sitemap: expected one hierarchy root")
        visited: set[str] = set()
        for root in roots:
            if root in visited:
                continue
            visited.add(root)
            active = {root}
            frames = [(root, iter(sorted(adj[root])))]
            while frames:
                node, children = frames[-1]
                child = next(children, None)
                if child is None:
                    frames.pop()
                    active.remove(node)
                    continue
                if child in active:
                    errors.append(f"sitemap: cycle involving {child}")
                    continue
                if child in visited:
                    continue
                visited.add(child)
                active.add(child)
                frames.append((child, iter(sorted(adj[child]))))
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
        # Message IDs are positional only by default. Explicit stable IDs are
        # supported for meaningful alt/opt/loop/par/break fragment references.
        ids = set()
        for i, edge in enumerate(edges):
            if not isinstance(edge,dict):
                continue
            msgid = edge.get("id", f"message-{i+1}")
            if (not isinstance(msgid,str) or not msgid.strip() or
                any(ch.isspace() for ch in msgid)):
                errors.append(f"sequence: edges[{i}] invalid message ID")
                continue
            if msgid in ids:
                errors.append(f"sequence: duplicate message ID {msgid}")
            ids.add(msgid)
            if not edge.get("label"):
                warnings.append(f"sequence: edges[{i}] has no message label")
        fragments = model.get("fragments", [])
        if not isinstance(fragments,list):
            errors.append("sequence: fragments must be an array")
        else:
            for i, fragment in enumerate(fragments):
                if not isinstance(fragment,dict):
                    errors.append(f"sequence: fragments[{i}] must be an object")
                    continue
                fkind=fragment.get("kind")
                if fkind not in ("alt","opt","loop","par","break"):
                    errors.append(f"sequence: fragments[{i}] unsupported fragment kind")
                if not isinstance(fragment.get("label"),str) or not fragment["label"].strip():
                    errors.append(f"sequence: fragments[{i}] needs a meaningful label")
                branches=[("messages",fragment.get("messages"))]
                if "else" in fragment:
                    alternate=fragment["else"]
                    if fkind!="alt":
                        errors.append(f"sequence: fragments[{i}] else is only meaningful for alt")
                    if not isinstance(alternate,dict):
                        errors.append(f"sequence: fragments[{i}] else must be an object")
                    else:
                        if "label" in alternate and (
                            not isinstance(alternate["label"],str) or not alternate["label"].strip()
                        ):
                            errors.append(f"sequence: fragments[{i}] else label must be nonempty text")
                        branches.append(("else.messages",alternate.get("messages")))
                branch_refs=[]
                for name, refs in branches:
                    if (not isinstance(refs,list) or not refs or
                        any(not isinstance(x,str) or not x.strip() for x in refs)):
                        errors.append(f"sequence: fragments[{i}] {name} needs message IDs")
                        continue
                    if len(set(refs))!=len(refs):
                        errors.append(f"sequence: fragments[{i}] {name} repeats a message")
                    missing=sorted(set(refs)-ids)
                    if missing:
                        errors.append(f"sequence: fragments[{i}] {name} refers to unknown messages: "+", ".join(missing))
                    branch_refs.extend(refs)
                if len(branch_refs)!=len(set(branch_refs)):
                    errors.append(f"sequence: fragments[{i}] message occurs in both branches")
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
