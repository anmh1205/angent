#!/usr/bin/env python3
"""Build a scoped, evidence-linked BA artifact graph from real Markdown tables.

This is an extractor, not an AI inference engine. It reads only explicitly
declared ID/relationship columns and reports external/unresolved references.
Business-rule correctness and execution of test cases are NOT established.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
from typing import Any

from validate_artifacts import audit

ID = re.compile(r"^(?:FR|NFR|BR|E|CHK|TC)-[A-Za-z0-9][A-Za-z0-9-]*$")
REF = re.compile(r"\b(?:CAP|BO|UN|FR|NFR|BR|E|UC|US|AC|CHK|TC)-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\b")
HEADERS = {"FR":("Requirement","Covers"),
           "NFR":("Requirement",),
           "BR":("Rule","Applies to"),
           "E":("Condition","Related FR"),
           "CHK":("What to test","Covers","TC"),
           "TC":("Title","Expands CHK")}
KIND = {"FR":"FR","NFR":"NFR","BR":"BR","E":"ERROR","CHK":"CHECKLIST","TC":"TEST"}
LINK_CELLS = {"FR":["Covers"], "BR":["Applies to"], "E":["Related FR"],
              "CHK":["Covers"], "TC":["Expands CHK"]}
DISPLAY_CELLS = {"FR":"Requirement","NFR":"Requirement","BR":"Rule","E":"Condition",
                 "CHK":"What to test","TC":"Title"}


def _cells(line: str) -> list[str]:
    # Split Markdown table delimiters but preserve escaped literals.
    return [x.strip().replace("\\|","|") for x in re.split(r"(?<!\\)\|",line.strip().strip("|"))]


def _is_separator(row: list[str]) -> bool:
    return bool(row) and all(bool(re.fullmatch(r":?-{3,}:?", x.strip())) for x in row)


def markdown_tables(text: str) -> list[list[dict[str,str]]]:
    lines=text.replace("\r\n","\n").splitlines()
    result=[]
    i=0
    while i < len(lines):
        if not lines[i].strip().startswith("|"):
            i+=1
            continue
        block_start=i+1
        block=[]
        while i<len(lines) and lines[i].strip().startswith("|"):
            block.append(_cells(lines[i]))
            i+=1
        if len(block)<3 or not _is_separator(block[1]):
            continue
        keys=block[0]
        if len(set(keys))!=len(keys):
            raise ValueError("Duplicate Markdown table headers")
        rows=[]
        for offset,row in enumerate(block[2:]):
            if len(row)!=len(keys):
                raise ValueError("Malformed Markdown table: inconsistent column count")
            rows.append({**dict(zip(keys,row)),"__source_line":str(block_start+2+offset)})
        result.append(rows)
    return result


def _metadata(raw: str) -> dict[str,str]:
    if not raw.startswith("---\n"):
        return {}
    pos=raw.find("\n---\n",4)
    if pos<0:
        raise ValueError("Unterminated document frontmatter")
    data={}
    for line in raw[4:pos].splitlines():
        if line and not line[0].isspace() and ":" in line:
            key,value=line.split(":",1)
            data[key.strip()]=value.strip().strip('"')
    return data


def collect(paths: dict[str,Path], root: Path) -> dict[str,Any]:
    root=root.resolve()
    sources=[]
    candidates=[]
    for role,path in paths.items():
        path=path.resolve()
        if not path.is_relative_to(root):
            raise ValueError("Source path is outside project root: "+str(path))
        raw=path.read_text(encoding="utf-8")
        meta=_metadata(raw)
        source_id="SOURCE-"+role.upper()
        sources.append({"id":source_id,"uri":path.relative_to(root).as_posix(),
                        **({"revision":meta["updated"]} if meta.get("updated") else {})})
        seen_role=0
        for table in markdown_tables(raw):
            if not table or "ID" not in table[0]:
                continue
            for row in table:
                item_id=row.get("ID","").strip()
                if not ID.fullmatch(item_id):
                    continue
                kind=item_id.split("-",1)[0]
                if role=="srs" and kind not in ("FR","NFR","BR","E"):
                    continue
                if role=="checklist" and kind!="CHK":
                    continue
                if role=="cases" and kind!="TC":
                    continue
                if not all(key in row for key in HEADERS[kind]):
                    raise ValueError(f"{item_id}: missing necessary columns {HEADERS[kind]}")
                title=row.get(DISPLAY_CELLS[kind],"").strip()
                if not title:
                    raise ValueError(f"{item_id}: missing concrete statement/title")
                refs=[]
                for col in LINK_CELLS.get(kind,[]):
                    refs.extend(REF.findall(row.get(col,"")))
                candidates.append({
                    "id":item_id,"kind":KIND[kind],"title":title,
                    "status":row.get("Status",meta.get("status","unverified")),
                    "source_refs":[source_id],"potential_links":list(dict.fromkeys(refs)),
                    "source_location":{"uri":path.relative_to(root).as_posix(),"line":int(row["__source_line"])},
                    "properties":{k:v for k,v in row.items() if k not in ("ID","__source_line")},
                    **({"verification_status":"not-executed"} if kind=="TC" else {})
                })
                seen_role+=1
        if not seen_role:
            raise ValueError(role+": no recognizable requirement/checklist/test-case rows")
    all_ids=[x["id"] for x in candidates]
    dupe=[k for k,c in Counter(all_ids).items() if c>1]
    if dupe:
        raise ValueError("Duplicate artifact IDs across sources: "+", ".join(sorted(dupe)))
    ids=set(all_ids)
    artifacts=[]
    unresolved=[]
    for candidate in candidates:
        item=dict(candidate)
        links=item.pop("potential_links")
        item["depends_on"]=[x for x in links if x in ids]
        outside=[x for x in links if x not in ids]
        if outside:
            item["external_refs"]=outside
            unresolved.append({"artifact":item["id"],"referenced_ids":outside})
        artifacts.append(item)
    graph={"sources":sources,"artifacts":artifacts}
    report=audit(graph)
    if not report["ok"]:
        raise ValueError("Constructed graph invalid: "+"; ".join(report["errors"]))
    counts=dict(sorted(Counter(x["kind"] for x in artifacts).items()))
    return {"graph":graph,"coverage":report["coverage"],"counts":counts,
            "unresolved_external_refs":unresolved,
            "caveats":["A linked test artifact is not an executed test result.",
                       "A source status marked approved is not proof of deployed behavior.",
                       "References to CAP/AC/US outside inspected files are reported, not invented.",
                       "Only explicit Markdown table relationships are inferred by this extractor."]}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--srs",required=True,type=Path)
    p.add_argument("--checklist",type=Path)
    p.add_argument("--cases",type=Path)
    p.add_argument("--root",type=Path,default=Path("."))
    p.add_argument("--output",type=Path,required=True)
    opts=p.parse_args()
    paths={"srs":opts.srs}
    if opts.checklist: paths["checklist"]=opts.checklist
    if opts.cases: paths["cases"]=opts.cases
    try:
        report=collect(paths,opts.root)
        opts.output.parent.mkdir(parents=True,exist_ok=True)
        opts.output.write_text(json.dumps(report["graph"],ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        print(json.dumps({"ok":True,"output":str(opts.output),
                          "counts":report["counts"],"coverage":report["coverage"],
                          "unresolved_external_refs":report["unresolved_external_refs"],
                          "caveats":report["caveats"]},ensure_ascii=False,indent=2))
        return 0
    except (OSError,ValueError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)},ensure_ascii=False))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
