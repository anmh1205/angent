#!/usr/bin/env python3
"""Verify source-code witness locations against an immutable Git commit.

Strictly read-only and scoped to explicit BA evidence/paths. Matching a code
fragment is NOT a conclusion of implementation correctness or deployment.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from typing import Any
from validate_artifacts import audit

SHA=re.compile(r"^[0-9a-f]{40}$")
REL=re.compile(r"^[A-Za-z0-9_./-]{1,240}$")
ID=re.compile(r"^[A-Za-z][A-Za-z0-9-]{1,120}$")

def git(repo:Path,*args:str)->str:
    run=subprocess.run(["git","-C",str(repo),*args],capture_output=True,
                       text=True,errors="replace",timeout=20)
    if run.returncode:
        raise ValueError("Git source read failed: "+run.stderr[-400:].strip())
    return run.stdout

def inspect(repo:Path,revision:str,ledger:Any,graph:dict)->dict[str,Any]:
    if not isinstance(revision,str) or not SHA.fullmatch(revision):
        raise ValueError("Expected full 40-hex commit SHA")
    if not isinstance(ledger,dict) or not isinstance(ledger.get("witnesses"),list) or not ledger["witnesses"]:
        raise ValueError("Need nonempty explicit source witness list")
    verdict=audit(graph)
    if not verdict["ok"]:
        raise ValueError("Invalid BA source graph: "+"; ".join(verdict["errors"]))
    repo=repo.resolve()
    if Path(git(repo,"rev-parse","--show-toplevel").strip()).resolve()!=repo:
        raise ValueError("Repository root must be the actual Git root")
    if git(repo,"cat-file","-t",revision).strip()!="commit":
        raise ValueError("Revision is not a Git commit")
    known={x["id"] for x in graph["artifacts"]}
    verified=[]
    seen=set()
    cache={}
    for item in ledger["witnesses"]:
        if not isinstance(item,dict):
            raise ValueError("Witness must be an object")
        rid,path=item.get("requirement_id"),item.get("path")
        first,last=item.get("line_start"),item.get("line_end")
        needle=item.get("expected_excerpt")
        if not isinstance(rid,str) or not ID.fullmatch(rid) or rid not in known:
            raise ValueError("Unknown BA requirement witness ID")
        if not isinstance(path,str) or not REL.fullmatch(path) or path.startswith(("/", "./")) or (
            ".." in path.split("/") or "\\" in path or "//" in path or ":" in path):
            raise ValueError("Unsafe or invalid Git source path")
        if isinstance(first,bool) or isinstance(last,bool) or not isinstance(first,int) or not isinstance(last,int) or not (1<=first<=last<=100000) or last-first>250:
            raise ValueError("Invalid bounded source line range")
        if not isinstance(needle,str) or not needle or len(needle)>450 or "\x00" in needle:
            raise ValueError("Expected nonempty bounded excerpt")
        key=(rid,path,first,last)
        if key in seen:raise ValueError("Duplicate code witness")
        seen.add(key)
        if path not in cache:
            cache[path]=git(repo,"show",revision+":"+path).splitlines()
        lines=cache[path]
        if last>len(lines):
            raise ValueError("Witness line range exceeds committed file")
        excerpt="\n".join(lines[first-1:last])
        if needle not in excerpt:
            raise ValueError("Expected excerpt absent from pinned source: "+rid+" "+path)
        fingerprint=hashlib.sha256(excerpt.encode("utf8")).hexdigest()
        if item.get("sha256") is not None and item["sha256"]!=fingerprint:
            raise ValueError("Pinned code excerpt fingerprint mismatch: "+rid+" "+path)
        verified.append({"requirement_id":rid,"path":path,"lines":[first,last],
                         "observed_excerpt":needle,"sha256":fingerprint,
                         "source_verified":True,"semantic_alignment":"not-assessed"})
    refs={x["requirement_id"] for x in verified}
    return {"ok":True,"revision":revision,"witnesses":verified,
            "verified_count":len(verified),"linked_requirement_ids":sorted(refs),
            "unwitnessed_fr_ids":sorted(x["id"] for x in graph["artifacts"]
                                      if x["kind"]=="FR" and x["id"] not in refs),
            "source_verification":"pinned-git-blob-excerpt",
            "semantic_alignment":"not-assessed","runtime_execution":"not-run",
            "deployment_verified":False,"writes_performed":False}

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger",type=Path)
    parser.add_argument("--repo",required=True,type=Path)
    parser.add_argument("--revision",required=True)
    parser.add_argument("--evidence-graph",required=True,type=Path)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    try:
        data=json.loads(args.ledger.read_text(encoding="utf8"))
        graph=json.loads(args.evidence_graph.read_text(encoding="utf8"))
        report=inspect(args.repo,args.revision,data,graph)
        if args.output:
            if args.output.exists():raise ValueError("Output exists, refusing to overwrite")
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    except (OSError,ValueError,TypeError,subprocess.TimeoutExpired) as exc:
        report={"ok":False,"error":str(exc)}
    print(json.dumps(report,ensure_ascii=False))
    return 0 if report["ok"] else 1

if __name__=="__main__":
    raise SystemExit(main())
