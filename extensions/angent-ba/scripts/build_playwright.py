#!/usr/bin/env python3
"""Generate runnable, local-only Playwright regression cases from a reviewed screen model.

No AI inference is performed. Tests cover declared navigation and mock-submit
outcomes, NOT production auth, backend side effects or missing business rules.
"""
from __future__ import annotations
import argparse
from collections import deque
import json
from pathlib import Path
import re
import sys
from typing import Any
from build_wireframe import check_model

REF = re.compile(r"^(?:FR|NFR|BR|AC|TC|CHK)-[A-Za-z0-9][A-Za-z0-9-]*$")
RUNNER = r'''#!/usr/bin/env python3
"""ANGENT-generated local-only Playwright test plan. No network API writes."""
import argparse
import json
from pathlib import Path
import sys

CASE_DATA = json.loads(CASE_JSON)
def run(prototype, chrome=None):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(json.dumps({"ok":False,"executed":False,"error":"Install the Python playwright package and Chrome first"}))
        return 2
    proto=Path(prototype).resolve()
    if not proto.is_file() or proto.suffix.lower()!=".html":
        print(json.dumps({"ok":False,"executed":False,"error":"A local HTML prototype file is required"}))
        return 2
    cases=CASE_DATA["cases"]
    failures=[]
    network_calls=[]
    with sync_playwright() as p:
        args={"headless":True}
        if chrome:
            args["executable_path"]=str(chrome)
        browser=p.chromium.launch(**args)
        try:
            for case in cases:
                page=browser.new_page(viewport={"width":390,"height":844})
                errors=[]
                page.on("pageerror",lambda err:errors.append(str(err)))
                def forbid_external(route):
                    network_calls.append(route.request.url)
                    route.abort()
                page.route("http://**/*",forbid_external)
                page.route("https://**/*",forbid_external)
                try:
                    page.goto(proto.as_uri())
                    for hop in case["path"]:
                        assert page.locator('[data-screen-id="'+hop["screen"]+'"]').count()==1
                        if hop["kind"]=="submit":
                            for field in hop["fields"]:
                                input_el=page.get_by_label(field["label"],exact=True)
                                if field["type"]=="checkbox":
                                    input_el.check()
                                else:
                                    input_el.fill(field["value"])
                            page.get_by_label("Mock response").select_option(hop["scenario"])
                        page.get_by_role("button",name=hop["label"],exact=True).click()
                        assert page.locator('[data-screen-id="'+hop["target"]+'"]').count()==1
                    assert page.locator('[data-screen-id="'+case["screen"]+'"]').count()==1
                    if case["kind"]=="navigate":
                        page.get_by_role("button",name=case["label"],exact=True).click()
                        assert page.locator('[data-screen-id="'+case["target"]+'"]').count()==1
                    else:
                        for field in case["fields"]:
                            input_el=page.get_by_label(field["label"],exact=True)
                            if field["type"]=="checkbox":
                                input_el.check()
                            else:
                                input_el.fill(field["value"])
                        page.get_by_label("Mock response").select_option(case["scenario"])
                        page.get_by_role("button",name=case["label"],exact=True).click()
                        if case["result"]=="navigate":
                            assert page.locator('[data-screen-id="'+case["target"]+'"]').count()==1
                            assert page.locator("h2").evaluate("(el)=>document.activeElement===el")
                        else:
                            assert page.get_by_role("alert").inner_text()==case["message"]
                    assert not errors,errors
                except Exception as exc:
                    failures.append({"id":case["id"],"error":str(exc)[:600]})
                finally:
                    page.close()
        finally:
            browser.close()
    good=not failures and not network_calls
    print(json.dumps({"ok":good,"executed":True,"cases":len(cases),
                      "passed":len(cases)-len(failures),"failed":failures,
                      "external_requests":network_calls,
                      "scope":"local HTML mock, not product backend"},
                     ensure_ascii=False))
    return 0 if good else 1

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prototype",type=Path,required=True)
    ap.add_argument("--chrome",type=Path)
    args=ap.parse_args()
    return run(args.prototype,args.chrome)

if __name__=="__main__":
    raise SystemExit(main())
'''

def path_to(button_graph: dict[str,list[dict]],start:str,target:str)->list[dict]|None:
    queue=deque([(start,[])])
    visited=set()
    while queue:
        current,path=queue.popleft()
        if current==target:
            return path
        if current in visited:
            continue
        visited.add(current)
        for edge in button_graph[current]:
            if edge["target"] not in visited:
                queue.append((edge["target"],path+[edge]))
    return None

def generate(model: Any, evidence_ids: set[str] | None = None) -> dict[str,Any]:
    outcome=check_model(model)
    if not outcome["ok"]:
        raise ValueError("Invalid screen model: "+"; ".join(outcome["errors"]))
    screens={s["id"]:s for s in model["screens"]}
    nav={}
    for s in model["screens"]:
        fields=[]
        for f in s["controls"]:
            if f["type"] in ("text","email","password","checkbox"):
                default={"email":"tester@example.test","password":"fixture-not-a-secret","text":"fixture"}.get(f["type"],"")
                if f["type"]=="password" and "test_value" in f:
                    raise ValueError("Do not embed custom password fixtures in generated scripts")
                val=f.get("test_value",default)
                if f["type"]!="checkbox" and (not isinstance(val,str) or not val):
                    raise ValueError("Invalid nonempty test_value for "+s["id"]+"."+f["id"])
                fields.append({"label":f["label"],"type":f["type"],"value":val})
        nav[s["id"]]=[{"screen":s["id"],"kind":"button","label":c["label"],"target":c["action"]["target"]}
                      for c in s["controls"] if c["type"]=="button"]
        for c in s["controls"]:
            if c["type"]=="submit":
                for scenario,result in c["outcomes"].items():
                    if result["type"]=="navigate":
                        nav[s["id"]].append({"screen":s["id"],"kind":"submit","label":c["label"],
                                            "target":result["target"],"scenario":scenario,"fields":fields})
    cases=[]
    covered=set()
    for s in model["screens"]:
        path=path_to(nav,model["start"],s["id"])
        if path is None:
            continue
        for c in s["controls"]:
            if c["type"] not in ("button","submit"):
                continue
            refs=c.get("requirements",[])
            if not isinstance(refs,list) or any(not isinstance(ref,str) or not REF.fullmatch(ref) for ref in refs):
                raise ValueError("Invalid source requirement reference for "+s["id"]+"."+c["id"])
            if evidence_ids is not None:
                for ref in refs:
                    if ref not in evidence_ids:
                        raise ValueError("Unresolved evidence requirement: "+ref)
            if c["type"]=="button":
                cases.append({"screen":s["id"],"kind":"navigate","label":c["label"],
                              "control":c["id"],"path":path,"target":c["action"]["target"],
                              "requirements":refs})
                covered.update((s["id"],c["action"]["target"]))
                continue
            fields=next((hop["fields"] for hop in nav[s["id"]] if hop["kind"]=="submit"),[])
            if not fields:
                fields=[{"label":x["label"],"type":x["type"],
                         "value": {"email":"tester@example.test","password":"fixture-not-a-secret","text":"fixture"}.get(x["type"],"")}
                        for x in s["controls"] if x["type"] in ("text","email","password","checkbox")]
            for scenario,result in c["outcomes"].items():
                case={"screen":s["id"],"kind":"submit","control":c["id"],
                      "label":c["label"],"scenario":scenario,"result":result["type"],
                      "path":path,"fields":fields,"requirements":refs}
                if result["type"]=="navigate":
                    case["target"]=result["target"]
                    covered.update((s["id"],result["target"]))
                else:
                    case["message"]=result["message"]
                cases.append(case)
        covered.add(s["id"])
    noncovered=sorted(set(screens)-covered)
    if noncovered:
        raise ValueError("Screens not covered by reachable navigations and mock outcomes: "+", ".join(noncovered))
    if not cases:
        raise ValueError("No testable actions")
    for index,item in enumerate(cases,1):
        item["id"]=f"TC-PROT-{index:04d}"
    return {"format":"angent-prototype-playwright-v1",
            "source_link_check":"ids-resolved-only" if evidence_ids is not None else "not-performed",
            "environment":"local-file-only","execution_status":"not-run",
            "cases":cases}

def generate_files(model:dict[str,Any],evidence_ids:set[str]|None=None)->dict[str,str]:
    suite=generate(model,evidence_ids=evidence_ids)
    encoded=json.dumps(json.dumps(suite,ensure_ascii=False,separators=(",",":")),ensure_ascii=False)
    script=RUNNER.replace("CASE_JSON",encoded)
    return {"test_prototype.py":script,"traceability.json":json.dumps(suite,ensure_ascii=False,indent=2)+"\n"}

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input",type=Path)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--evidence-graph",type=Path)
    args=p.parse_args()
    try:
        model=json.loads(args.input.read_text(encoding="utf8"))
        ids=None
        if args.evidence_graph:
            from validate_artifacts import audit
            graph=json.loads(args.evidence_graph.read_text(encoding="utf8"))
            result=audit(graph)
            if not result["ok"]:
                raise ValueError("Invalid evidence graph: "+"; ".join(result["errors"]))
            ids={a["id"] for a in graph["artifacts"]}
        output=generate_files(model,evidence_ids=ids)
        if args.output.exists() and any(args.output.iterdir()):
            raise ValueError("Refuse to overwrite nonempty output directory")
        for rel,value in output.items():
            target=args.output/rel
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(value,encoding="utf8")
        cases=json.loads(output["traceability.json"])["cases"]
        print(json.dumps({"ok":True,"generated":len(cases),"files":list(output),
                          "execution_status":"not-run","backend_requests":0,
                          "output":str(args.output)}))
        return 0
    except (OSError,ValueError,TypeError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
