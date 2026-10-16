#!/usr/bin/env python3
"""Read-only requirement handoff evidence audit across BA's full project lifecycle.

Unlike a fixed document workflow, inspect only actually supplied artifact kinds.
A missing downstream kind means "not inspected", never "passed" or "failed".
Linked test artifacts are NOT execution evidence or stakeholder acceptance.
"""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
import json
from pathlib import Path
from typing import Any

from validate_artifacts import audit, canonical

# Stage contracts describe evidence handoffs, not required document filenames.
# The final TEST stage means TC artifact existence, NOT a passing test run.
STAGES: tuple[tuple[str, str, str], ...] = (
    ("need_to_objective", "NEED", "BUSINESS_OBJECTIVE"),
    ("objective_to_capability", "BUSINESS_OBJECTIVE", "CAPABILITY"),
    ("capability_to_requirement", "CAPABILITY", "FR"),
    ("functional_requirement_to_test", "FR", "TEST"),
    ("quality_requirement_to_test", "NFR", "TEST"),
    ("business_rule_to_test", "BR", "TEST"),
    ("error_behavior_to_test", "ERROR", "TEST"),
    ("acceptance_to_test", "ACCEPTANCE", "TEST"),
    ("checklist_to_test", "CHECKLIST", "TEST"),
)
# Only these kinds may supply the FR-to-test verification path.
# A story referencing a broad FR must not imply the story's tests cover the FR.
VERIFICATION_HOPS = frozenset({"ERROR","ACCEPTANCE","CHECKLIST","TEST"})


def _shortest_path(start: str, target_kind: str, nodes: dict[str, dict],
                   outgoing: dict[str, list[str]], allowed: frozenset[str] | None) -> list[str] | None:
    visited = {start}
    pending = deque([[start]])
    while pending:
        path = pending.popleft()
        for candidate in sorted(outgoing.get(path[-1], [])):
            if candidate in visited or candidate not in nodes:
                continue
            kind = canonical(nodes[candidate]["kind"])
            if allowed is not None and kind not in allowed:
                continue
            new_path = path + [candidate]
            if kind == target_kind:
                return new_path
            visited.add(candidate)
            pending.append(new_path)
    return None


def inspect(graph: Any, *, require_known_handoffs: bool = False) -> dict[str, Any]:
    validated = audit(graph)
    if not validated["ok"]:
        return {"ok": False, "errors": validated["errors"], "warnings": validated.get("warnings", []),
                "scope": "invalid evidence graph", "writes_performed": False}
    nodes = {entry["id"]: entry for entry in graph["artifacts"]}
    by_kind: dict[str, list[str]] = defaultdict(list)
    forward: dict[str, list[str]] = defaultdict(list)
    for entry in graph["artifacts"]:
        key = entry["id"]
        by_kind[canonical(entry["kind"])].append(key)
        for dep in entry["depends_on"]:
            forward[dep].append(key)
    for keys in by_kind.values():
        keys.sort()
    results = []
    all_gaps: list[dict] = []
    not_inspected = []
    for stage, source_kind, target_kind in STAGES:
        src = by_kind.get(source_kind, [])
        dst = by_kind.get(target_kind, [])
        if not src or not dst:
            results.append({"stage": stage, "state": "not-inspected",
                            "source_kind": source_kind, "target_kind": target_kind,
                            "source_count": len(src), "target_count": len(dst),
                            "verified_links": 0, "missing": [],
                            "reason": ("no source artifacts" if not src else "no target artifacts in inspected corpus")})
            not_inspected.append(stage)
            continue
        witnessed = {}
        missing = []
        for key in src:
            # For early lifecycle a DIRECT downstream relation is required:
            # no accidental completion from unrelated artifact families.
            allowed = VERIFICATION_HOPS if target_kind=="TEST" else frozenset({target_kind})
            path = _shortest_path(key, target_kind, nodes, forward, allowed)
            if path is None:
                missing.append(key)
                all_gaps.append({"stage": stage, "source_id": key,
                                 "finding": "no explicit source-to-target evidence link",
                                 "status": "review-required-not-a-release-verdict"})
            else:
                witnessed[key] = path
        results.append({"stage":stage,"state":"inspected",
                        "source_kind":source_kind,"target_kind":target_kind,
                        "source_count":len(src),"target_count":len(dst),
                        "verified_links":len(witnessed),
                        "missing":missing,
                        "witness_paths":witnessed,
                        "meaning":"structural provenance only; not semantically validated"})
    unapproved = sorted(entry["id"] for entry in graph["artifacts"]
                        if str(entry.get("status","unverified")).lower() in ("draft","unverified","proposed"))
    # Graph self-assertions of "passed" do NOT establish a run: this command
    # has no execution receipt, independently checked result or provider.
    tests = [entry for entry in graph["artifacts"] if canonical(entry["kind"])=="TEST"]
    unexecuted = sorted(entry["id"] for entry in tests)
    claimed_executed = sorted(entry["id"] for entry in tests
                              if str(entry.get("verification_status","not-executed")).lower()
                              in ("executed","passed","success"))
    unversioned_sources = sorted(source["id"] for source in graph["sources"]
                                 if not str(source.get("revision","")).strip())
    return {
        "ok": not (require_known_handoffs and all_gaps),
        "mode":"read-only-structural-assurance",
        "artifact_count":len(nodes),
        "source_count":len(graph["sources"]),
        "stages":results,
        "known_handoff_gaps":all_gaps,
        "not_inspected_stages":not_inspected,
        "unapproved_or_draft_artifact_ids":unapproved,
        "test_artifacts_without_execution_evidence":unexecuted,
        "test_artifacts_claimed_executed_but_unverified":claimed_executed,
        "source_revision_not_established":unversioned_sources,
        "confidence":"structural links only; no assertion of business validity, test execution or provider writes",
        "writes_performed":False,
    }


def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("graph",type=Path,help="Existing ANGENT BA artifact graph JSON")
    p.add_argument("--require-known-handoffs",action="store_true",
                   help="Exit nonzero if a link is missing where BOTH artifact kinds were inspected")
    p.add_argument("--output",type=Path,help="Write report to a NEW file, never overwrite")
    args=p.parse_args()
    try:
        graph=json.loads(args.graph.read_text(encoding="utf-8"))
        result=inspect(graph,require_known_handoffs=args.require_known_handoffs)
        content=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
        if args.output:
            if args.output.exists():
                raise ValueError("Refusing to overwrite previous review report")
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(content,encoding="utf-8")
        print(content)
        return 0 if result["ok"] else 1
    except (OSError,ValueError,TypeError) as exc:
        print(json.dumps({"ok":False,"errors":[str(exc)]}))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
