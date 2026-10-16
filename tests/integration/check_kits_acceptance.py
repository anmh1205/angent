#!/usr/bin/env python3
"""Acceptance smoke across independent BA evidence, API, visual and Figma adapters.

Run the actual existing scripts in one invocation; this is a read-only test
orchestrator, NOT another ANGENT Hub/runtime or product workflow engine.
All models are explicitly synthetic or open-source worked examples.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[2]
BA=ROOT/"extensions/angent-ba"
FIGMA=ROOT/"extensions/angent-figma"
sys.path.insert(0,str(BA/"scripts"))
sys.path.insert(0,str(FIGMA/"scripts"))

from extract_markdown_graph import collect
from validate_artifacts import audit
from render_preview import render as render_preview
from compare_artifact_revisions import compare
from build_bruno import compile_collection
from audit_api_contract import audit_contract
from build_d2 import compile_source
from to_reqwise_payload import compile_model
from build_wireframe import render as render_wireframe
from build_playwright import generate_files
from build_next_prototype import generate_files as generate_next
from build_figma_screens import compile_screens


def run_script(path:Path,arguments:list[str])->dict:
    result=subprocess.run([sys.executable,str(path)]+arguments,cwd=ROOT,
                          capture_output=True,text=True,errors="replace",timeout=180)
    lines=result.stdout.strip().splitlines()
    try:
        report=json.loads(lines[-1])
    except (ValueError,IndexError):
        report={}
    return {"ok":result.returncode==0 and bool(report.get("ok")),"exit":result.returncode,
            "report":report,"stderr":result.stderr[-1000:]}


def check(chrome:Path|None,bru:Path|None,d2:Path|None,require_runtime:bool)->dict:
    if require_runtime and not all((chrome,bru,d2)):
        raise ValueError("--require-runtime needs --chrome, --bru and --d2")
    project=BA/"examples"
    feat=project/"docs/atlas-re"
    sources={
        "urd":feat/"atlas-re-urd.md",
        "brd":feat/"atlas-re-brd.md",
        "prd":feat/"atlas-re-prd.md",
        "srs":feat/"srs/atlas-re-spec.md",
        "checklist":feat/"test/checklist/atlas-re-checklist-index.md",
        "cases":feat/"test/testcases/atlas-re-testcase-index.md",
        "stories":feat/"userstories/atlas-re-story-index.md",
        "usecases":feat/"usecases/atlas-re-usecase-index.md"
    }
    atlas=collect(sources,project)
    if not audit(atlas["graph"])["ok"] or atlas["coverage"]["traced_to_test"]!=4 or len(atlas["graph"]["artifacts"])!=58 or
            atlas["lifecycle"]["fr_with_complete_structural_chain"]!=4):
        raise ValueError("Atlas source-indexed BA baseline unexpectedly changed")
    page=render_preview(atlas["graph"],"Atlas source evidence")
    if page.count("<article ")!=58 or "4/8" not in page:
        raise ValueError("Atlas preview does not match actual artifact count/coverage")
    revised=deepcopy(atlas["graph"])
    original=revised["artifacts"][0]
    original["title"]=original["title"]+" (proposed revision)"
    impact=compare(atlas["graph"],revised)
    if not impact["ok"] or not impact["modified"]:
        raise ValueError("BA change comparison did not register the revised source")
    graph=json.loads((BA/"examples/rental-fleet-traceability.json").read_text(encoding="utf8"))
    if not audit(graph)["ok"]:
        raise ValueError("Synthetic fleet BA graph invalid")
    ids={item["id"] for item in graph["artifacts"]}
    activity=json.loads((BA/"examples/d2-activity.json").read_text(encoding="utf8"))
    d2script=compile_source(activity,evidence_ids=ids)
    if "FR-IVTS-01" not in d2script:
        raise ValueError("D2 lost evidence identity")
    figma=json.loads((FIGMA/"examples/rental-fleet-activity.json").read_text(encoding="utf8"))
    figma_request=compile_model(figma,evidence_ids=ids)
    if figma_request["writes_performed"] or figma_request["source_link_check"]!="ids-resolved-only":
        raise ValueError("Figma payload must stay dry-run, with explicit ID limits")
    api=json.loads((BA/"examples/synthetic-fleet-api-tests.json").read_text(encoding="utf8"))
    openapi=json.loads((BA/"examples/synthetic-fleet-openapi.json").read_text(encoding="utf8"))
    contract=audit_contract(openapi,api)
    if not contract["ok"]:
        raise ValueError("OpenAPI contract mismatch: "+str(contract["errors"]))
    bruno=compile_collection(api,api_contract=openapi,evidence_ids=ids)
    if len(bruno)!=7:
        raise ValueError("Unexpected Bruno output file count")
    screen=json.loads((BA/"examples/authentication-screen-model.json").read_text(encoding="utf8"))
    generated=generate_files(screen)
    if len(json.loads(generated["traceability.json"])["cases"])!=7:
        raise ValueError("Source-driven browser test count mismatch")
    if "<script" not in render_wireframe(screen,"prototype"):
        raise ValueError("Prototype renderer unexpectedly lost script support")
    figma_screens=compile_screens(screen)
    next_files=generate_next(screen)
    next_model=json.loads(next_files["model.json"])
    if next_model!=screen:
        raise ValueError("Next.js prototype lost source model identity")
    if figma_screens["writes_performed"] or figma_screens["runtime_status"]!="not-run":
        raise ValueError("Screen-to-Figma candidate cannot claim native canvas effects")
    if [x["source_id"] for x in figma_screens["screens"]] != [x["id"] for x in screen["screens"]]:
        raise ValueError("Figma screen ID inventory disagrees with source")
    for source_screen,scene in zip(screen["screens"],figma_screens["screens"]):
        actual=[c["children"][0]["characters"].removeprefix("☐ ")
                for c in scene["figma_tree"]["children"] if c["name"].startswith("control:")]
        expected=[control["label"] for control in source_screen["controls"]]
        if actual!=expected:
            raise ValueError("Figma editable text controls disagree with source labels")
    runtime={}
    if chrome:
        runtime["playwright"]=run_script(ROOT/"tests/integration/check_generated_playwright.py",
                                          ["--chrome",str(chrome)])
    if bru:
        runtime["bruno"]=run_script(ROOT/"tests/integration/check_bruno_cli.py",
                                      ["--cli",str(bru)])
    if d2:
        runtime["d2"]=run_script(ROOT/"tests/integration/check_d2_cli.py",["--d2",str(d2)])
    passed=all(report["ok"] for report in runtime.values())
    if require_runtime:
        passed=passed and len(runtime)==3
    return {"ok":passed,"atlas":{"artifacts":58,"fr":8,"explicit_tc_links":4,
                                  "full_upstream_chains":8,"complete_structural_chains":4,
                                  "test_execution":"not-proven","preview_entries":58,
                                  "revision_diff":"observed"},
            "synthetic_fleet":{"d2_source":True,"reqwise_request":"dry-run",
                               "contract_checked":True,"bruno_request_count":4,
                               "real_fleet_or_figma_writes":False},
            "synthetic_auth":{"generated_browser_cases":7,"backend_requests":0,
                              "html_prototype":True,"next_source_matches":True,
                              "figma_candidate_screens":len(figma_screens["screens"]),
                              "figma_candidate_controls":sum(len(x["controls"]) for x in figma_screens["screens"]),
                              "figma_canvas_writes":False},
            "runtime":runtime,"limitations":"Two distinct example domains; no claim of semantic parity between Atlas, Fleet and Authentication",
            "merge_performed":False}

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--chrome",type=Path)
    p.add_argument("--bru",type=Path)
    p.add_argument("--d2",type=Path)
    p.add_argument("--require-runtime",action="store_true")
    args=p.parse_args()
    try:
        result=check(args.chrome,args.bru,args.d2,args.require_runtime)
    except (OSError,ValueError,TypeError,subprocess.TimeoutExpired) as exc:
        result={"ok":False,"error":str(exc)}
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result["ok"] else 1

if __name__=="__main__":
    raise SystemExit(main())
