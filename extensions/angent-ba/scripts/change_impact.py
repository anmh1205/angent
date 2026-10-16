#!/usr/bin/env python3
"""Compute reverse dependency impact of a proposed change; read-only."""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
import json
from pathlib import Path
from validate_artifacts import audit


def impact(data: dict, changed: list[str]) -> dict:
    checked = audit(data)
    if not checked["ok"]:
        return {"ok": False, "errors": checked["errors"]}
    by_id = {node["id"]: node for node in data["artifacts"]}
    missing = sorted(set(changed) - set(by_id))
    if missing:
        return {"ok": False, "errors": ["Unknown changed artifact: " + x for x in missing]}
    rev: dict[str, set[str]] = defaultdict(set)
    for node in data["artifacts"]:
        for dep in node["depends_on"]:
            rev[dep].add(node["id"])
    frontier = deque(sorted(set(changed)))
    seen = set(frontier)
    ancestors = {k: [] for k in frontier}
    while frontier:
        item = frontier.popleft()
        for nxt in sorted(rev[item]):
            if nxt not in seen:
                seen.add(nxt)
                ancestors[nxt] = ancestors[item] + [item]
                frontier.append(nxt)
    affected = sorted(seen - set(changed))
    return {"ok": True, "changed": sorted(set(changed)), "affected": affected,
            "impact_paths": {k: ancestors[k] + [k] for k in affected},
            "writes_performed": False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("changed", nargs="+")
    args = parser.parse_args()
    try:
        source = json.loads(args.input.read_text(encoding="utf-8"))
        report = impact(source, args.changed)
    except (OSError, ValueError) as exc:
        report = {"ok": False, "errors": [str(exc)]}
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
