#!/usr/bin/env python3
"""Compile a bounded API test plan into a Git-friendly Bruno .bru collection.

Only declarative requests, JSON payloads and type-safe assertions are emitted.
No requests execute, secrets are never embedded, and only localhost is a
default target. Validate the generated collection with a real Bruno parser/CLI.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from typing import Any

IDENT = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,79}$")
PATH = re.compile(r"^/[A-Za-z0-9_/{}/.?=&%:~-]{0,499}$")
FIELD = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*$")
METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}
SCALAR = (str, bool, int, float)
REPLACE = re.compile(r"\{\{([A-Za-z][A-Za-z0-9_]*)\}\}")

def fail(message: str) -> None:
    raise ValueError(message)

def clean_string(value: Any, where: str, limit: int = 160) -> str:
    if not isinstance(value, str) or not 1 <= len(value) <= limit or any(c in value for c in ("\n","\r","{","}")):
        fail(where + ": invalid metadata string")
    return value

def validate(plan: Any) -> list[dict]:
    if not isinstance(plan, dict):
        fail("Plan must be JSON object")
    name=clean_string(plan.get("name"),"name")
    cases=plan.get("scenarios")
    if not isinstance(cases,list) or not cases:
        fail("nonempty scenarios list required")
    if len(cases)>200:
        fail("maximum 200 requests per collection")
    seen=set()
    accepted=[]
    for i,item in enumerate(cases):
        if not isinstance(item,dict):
            fail(f"scenarios[{i}]: object required")
        key=item.get("id")
        if not isinstance(key,str) or not IDENT.fullmatch(key):
            fail(f"scenarios[{i}]: invalid ID")
        if key in seen:
            fail("duplicate scenario ID: "+key)
        seen.add(key)
        title=clean_string(item.get("name"),f"scenarios[{i}].name")
        method=item.get("method")
        if method not in METHODS:
            fail(f"{key}: unsupported method")
        path=item.get("path")
        if not isinstance(path,str) or not PATH.fullmatch(path) or ".." in path:
            fail(f"{key}: invalid path, use a local baseUrl variable")
        if path.count("{{")!=path.count("}}") or "{{{" in path or "}}}" in path:
            fail(f"{key}: malformed interpolation")
        residue=REPLACE.sub("",path)
        if "{" in residue or "}" in residue:
            fail(f"{key}: unrecognized interpolation variable")
        status=item.get("expected_status")
        if type(status) is not int or not 100<=status<=599:
            fail(f"{key}: HTTP status between 100 and 599 required")
        auth=item.get("auth","none")
        if auth not in ("none","bearer"):
            fail(f"{key}: auth must be none or bearer")
        body=item.get("body")
        if body is not None and method=="GET":
            fail(f"{key}: GET cannot carry JSON body in this bounded compiler")
        if body is not None and not isinstance(body,(dict,list)):
            fail(f"{key}: JSON body must be object or array")
        checks=item.get("body_checks",{})
        if not isinstance(checks,dict):
            fail(f"{key}: body_checks must be object")
        for field,expected in checks.items():
            if not isinstance(field,str) or not FIELD.fullmatch(field):
                fail(f"{key}: unsupported JSON property expression {field!r}")
            if not (expected is None or type(expected) in SCALAR):
                fail(f"{key}: body check must compare scalar or null")
        accepted.append({"id":key,"name":title,"method":method,"path":path,"expected_status":status,
                         "auth":auth,"body":body,"body_checks":checks})
    return accepted

def bru(item: dict, seq:int) -> str:
    method=item["method"].lower()
    bodykind="json" if item["body"] is not None else "none"
    lines=["meta {","  name: "+item["id"]+" - "+item["name"],"  type: http",
           "  seq: "+str(seq),"}","",method+" {",
           "  url: {{baseUrl}}"+item["path"],"  body: "+bodykind,
           "  auth: "+item["auth"],"}",""]
    if item["auth"]=="bearer":
        lines+=["auth:bearer {","  token: {{authToken}}","}",""]
    if item["body"] is not None:
        payload=json.dumps(item["body"],ensure_ascii=False,indent=2,allow_nan=False)
        lines+=["headers {","  Content-Type: application/json","}","",
                "body:json {",payload,"}",""]
    lines+=["tests {",
            '  test("HTTP '+str(item["expected_status"])+'", function () {',
            "    expect(res.getStatus()).to.equal("+str(item["expected_status"])+");","  });"]
    for field,expected in item["body_checks"].items():
        rendered=json.dumps(expected,ensure_ascii=False,allow_nan=False)
        expression="res.getBody()"+"".join("["+json.dumps(part)+"]" for part in field.split("."))
        lines+=['  test("Response '+field+' matches contract", function () {',
                "    expect("+expression+").to.deep.equal("+rendered+");","  });"]
    lines+=["}",""]
    return "\n".join(lines)

def compile_plan(plan:dict) -> dict[str,str]:
    accepted=validate(plan)
    name=clean_string(plan["name"],"name")
    result={"bruno.json":json.dumps({"version":"1","name":name,"type":"collection"},
                                    ensure_ascii=False,indent=2)+"\n"}
    for seq,item in enumerate(accepted,1):
        result["requests/"+item["id"]+".bru"]=bru(item,seq)
    # This environment is an explicit localhost fixture, never a production target.
    result["environments/Local.bru"]="vars {\n  baseUrl: http://127.0.0.1:8765\n}\n"
    result["README.md"]=("# "+name+"\n\nGenerated **requests only**; nothing has been executed or verified against the API. "+
        "Set the baseUrl in environments/Local.bru to an authorized test target before running. "+
        "Keep authToken in a secret manager or CLI environment, never in this repository. "+
        "Run the Bruno CLI and inspect both request and assertion results; an expected HTTP status is not proof "+
        "that data side effects were verified.\n")
    return result

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input",type=Path)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    try:
        plan=json.loads(a.input.read_text(encoding="utf-8"))
        outputs=compile_plan(plan)
        if a.output.exists() and any(a.output.iterdir()):
            fail("Output directory is nonempty: refusing to overwrite existing collection")
        a.output.mkdir(parents=True,exist_ok=True)
        root=a.output.resolve()
        for name,content in outputs.items():
            dest=(root/name).resolve()
            if not dest.is_relative_to(root):
                fail("Unsafe output path")
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_text(content,encoding="utf-8")
    except (OSError,ValueError,TypeError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1
    print(json.dumps({"ok":True,"collection":str(a.output),"requests":len(plan["scenarios"]),
                      "executed":False},ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
