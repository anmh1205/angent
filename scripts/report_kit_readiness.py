#!/usr/bin/env python3
"""Read-only BA/Figma release-evidence report. A green unit suite is not full parity.

Reads the 67-source capability inventory and 13 planned, *unexecuted* scenario
evaluations. No source modifications, provider calls or release decisions.
"""
from __future__ import annotations
import argparse
from collections import Counter,defaultdict
import json
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
ACCEPTED={"runtime-mock","source-validated","payload-verified"}
PENDING={"method","unverified","provider-blocked"}


def summarize(rows:Any,cases:Any)->dict:
    if not isinstance(rows,list) or not isinstance(cases,list):
        raise ValueError("Expected specialist inventory and scenario arrays")
    keys=[row.get("skill") for row in rows if isinstance(row,dict)]
    if len(rows)!=67 or len(set(keys))!=67 or not all(isinstance(k,str) for k in keys):
        raise ValueError("Inventory must enumerate 67 unique specialist IDs")
    assigned=[name for row in cases for name in row.get("skills",[])]
    if len(assigned)!=67 or sorted(assigned)!=sorted(keys):
        raise ValueError("Scenario coverage is incomplete or duplicates a specialist")
    bystage:dict[str,list[str]]=defaultdict(list)
    unverified:list[dict]=[]
    for row in rows:
        status=row.get("evidence")
        name=row["skill"]
        if status not in ACCEPTED|PENDING:
            raise ValueError("Unknown capability evidence tier for "+name)
        bystage[row["stage"]].append(name)
        refs=row.get("proof_refs")
        if not isinstance(refs,list) or (status in ACCEPTED and not refs):
            raise ValueError("Promoted evidence tier lacks proof path for "+name)
        if status in PENDING:
            unverified.append({"skill":name,"evidence":status,"acceptance_gap":row["remaining"]})
    recorded=sum(case.get("execution_status") not in (None,"not-run") for case in cases)
    counts=Counter(row["evidence"] for row in rows)
    return {
        "ok":True,"scope":"audit only; not a merge or release approval",
        "verified_capability_claims":0,
        "capability_records":len(rows),
        "method_or_provider_issues":len(unverified),
        "evidence_tiers":dict(sorted(counts.items())),
        "case_count":len(cases),
        "cases_pending":len(cases)-recorded,
        "cases_recorded_as_runs":recorded,
        "release_readiness":"NOT_YET_VERIFIED",
        "why_not_ready":[
            "No evaluated real ANGENT runs for every scenario with independently inspected output",
            "Offline source/runtime examples do not establish live Figma/Atlassian capabilities",
            "Unverified stakeholder requirements and real project behavior cannot be inferred from synthetic examples",
        ],
        "by_stage":{group:{"skills":len(values),"names":sorted(values)}
                    for group,values in sorted(bystage.items())},
        "unverified_methods_and_provider_capabilities":unverified,
        "writes_performed":False,"merged":False,
    }


def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--inventory",type=Path,default=ROOT/"hub/research/ba-figma-audit-67.json")
    p.add_argument("--scenarios",type=Path,default=ROOT/"evals/ba-figma/scenarios.json")
    args=p.parse_args()
    try:
        rows=json.loads(args.inventory.read_text(encoding="utf8"))
        cases=json.loads(args.scenarios.read_text(encoding="utf8"))
        report=summarize(rows,cases)
        print(json.dumps(report,ensure_ascii=False,indent=2))
        return 0
    except (ValueError,OSError,TypeError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
