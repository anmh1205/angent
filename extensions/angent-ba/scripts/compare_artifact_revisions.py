#!/usr/bin/env python3
"""Compare two validated BA evidence graph revisions and derive review impacts.

Output shows *documented changes*, NOT implementation drift or approval.
Source freshness changes trigger re-review but never auto-edit other artifacts.
"""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
import json
from pathlib import Path
from typing import Any
from validate_artifacts import audit


def _reverse(graph: dict) -> dict[str,set[str]]:
    rev=defaultdict(set)
    for node in graph["artifacts"]:
        for dep in node["depends_on"]:
            rev[dep].add(node["id"])
    return rev


def _impacts(graph:dict,roots:set[str]) -> dict[str,list[str]]:
    rev=_reverse(graph)
    known={node["id"] for node in graph["artifacts"]}
    queue=deque(sorted(known & roots))
    paths={key:[key] for key in queue}
    while queue:
        node=queue.popleft()
        for dependent in sorted(rev[node]):
            if dependent not in paths:
                paths[dependent]=paths[node]+[dependent]
                queue.append(dependent)
    return {key:value for key,value in sorted(paths.items()) if key not in roots}


def compare(before: Any, after: Any) -> dict[str,Any]:
    for name,graph in (("before",before),("after",after)):
        report=audit(graph)
        if not report["ok"]:
            raise ValueError(name+" graph invalid: "+"; ".join(report["errors"]))
    old={x["id"]:x for x in before["artifacts"]}
    new={x["id"]:x for x in after["artifacts"]}
    old_sources={x["id"]:x for x in before["sources"]}
    new_sources={x["id"]:x for x in after["sources"]}
    old_ids=set(old)
    new_ids=set(new)
    added=sorted(new_ids-old_ids)
    removed=sorted(old_ids-new_ids)
    modified=[]
    for ident in sorted(old_ids & new_ids):
        a,b=old[ident],new[ident]
        keys=sorted(set(a)|set(b))
        details={}
        for key in keys:
            if a.get(key)!=b.get(key):
                details[key]={"before":a.get(key),"after":b.get(key)}
        if details:
            modified.append({"id":ident,"fields":details})
    source_changes=[]
    for sid in sorted(set(old_sources)|set(new_sources)):
        if old_sources.get(sid)==new_sources.get(sid):
            continue
        impacted=sorted({entry["id"] for entry in before["artifacts"]+after["artifacts"]
                         if sid in entry.get("source_refs",[])})
        source_changes.append({"id":sid,"before":old_sources.get(sid),
                               "after":new_sources.get(sid),"referencing_artifacts":impacted})
    semantic_change=set(added+removed+[item["id"] for item in modified])
    source_review_roots=set().union(*(set(c["referencing_artifacts"]) for c in source_changes)) if source_changes else set()
    roots=semantic_change|source_review_roots
    affected={}
    for name,graph in (("before",before),("after",after)):
        for ident,path in _impacts(graph,roots).items():
            paths=affected.setdefault(ident,[])
            if path not in paths:
                paths.append(path)
    for iden in roots:
        affected.pop(iden,None)
    return {"ok":True,
            "baseline":{"before_artifacts":len(old),"after_artifacts":len(new),
                        "before_sources":len(old_sources),"after_sources":len(new_sources)},
            "added":added,"removed":removed,"modified":modified,
            "source_changes":source_changes,"direct_review":sorted(roots),
            "dependent_review":{ident:sorted(paths) for ident,paths in sorted(affected.items())},
            "review_required":sorted(roots|set(affected)),
            "scope":"document/evidence graph revision comparison, not source-code implementation drift",
            "approval_status":"not-established","writes_performed":False}

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("before",type=Path)
    p.add_argument("after",type=Path)
    p.add_argument("--output",type=Path,help="Optional new JSON report; must not exist")
    args=p.parse_args()
    try:
        old=json.loads(args.before.read_text(encoding="utf8"))
        new=json.loads(args.after.read_text(encoding="utf8"))
        report=compare(old,new)
        content=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
        if args.output:
            if args.output.exists():
                raise ValueError("Refuse to overwrite existing comparison report")
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(content,encoding="utf8")
        print(content)
        return 0
    except (OSError,ValueError,TypeError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)},ensure_ascii=False))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
