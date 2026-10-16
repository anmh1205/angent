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

ID = re.compile(r"^(?:UN|BO|CAP|FR|NFR|BR|E|AC|CHK|TC|US|UC)-[A-Za-z0-9][A-Za-z0-9-]*$")
LINKED_ID = re.compile(r"^\[([A-Za-z0-9-]+)\]\([^)]+\)$")
REF = re.compile(r"\b(?:CAP|BO|UN|FR|NFR|BR|E|UC|US|AC|CHK|TC)-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\b")
HEADERS = {"UN":("Need statement",),"BO":("Objective","Covers needs"),"CAP":("Capability","Covers"),"AC":("Criterion",),
           "FR":("Requirement","Covers"),
           "NFR":("Requirement",),
           "BR":("Rule","Applies to"),
           "E":("Condition","Related FR"),
           "CHK":("What to test","Covers","TC"),
           "TC":("Title","Expands CHK"),
           "US":("Title","FR"),"UC":("Slug","Covers FR") }
KIND = {"UN":"NEED","BO":"BUSINESS_OBJECTIVE","CAP":"CAPABILITY","AC":"ACCEPTANCE",
        "FR":"FR","NFR":"NFR","BR":"BR","E":"ERROR","CHK":"CHECKLIST","TC":"TEST",
        "US":"STORY","UC":"USECASE"}
LINK_CELLS = {"UN":[],"BO":["Covers needs"],"CAP":["Covers"],"AC":["Covers","Related FR","FR","US"],
              "FR":["Covers"], "BR":["Applies to"], "E":["Related FR"],
              "CHK":["Covers"], "TC":["Expands CHK"],
              "US":["FR"],"UC":["Covers FR"]}
DISPLAY_CELLS = {"UN":"Need statement","BO":"Objective","CAP":"Capability","AC":"Criterion","FR":"Requirement","NFR":"Requirement","BR":"Rule","E":"Condition",
                 "CHK":"What to test","TC":"Title",
                 "US":"Title","UC":"Slug"}


def _cells(line: str) -> list[str]:
    # Split Markdown table delimiters but preserve escaped literals.
    return [x.strip().replace("\\|","|") for x in re.split(r"(?<!\\)\|",line.strip().strip("|"))]


def _is_separator(row: list[str]) -> bool:
    return bool(row) and all(bool(re.fullmatch(r":?-{3,}:?", x.strip())) for x in row)


def markdown_tables(text: str) -> list[list[dict[str,str]]]:
    lines=text.replace("\r\n","\n").splitlines()
    # Exclude fenced code samples without shifting source-line references.
    # A table demonstrating requirement syntax is not accepted evidence.
    excluded=[False]*len(lines)
    active=None
    fence=re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
    for pos,line in enumerate(lines):
        found=fence.match(line)
        if active is not None:
            excluded[pos]=True
            if (found and found.group(1)[0]==active[0] and
                    len(found.group(1))>=active[1] and not found.group(2).strip()):
                active=None
            continue
        if found:
            excluded[pos]=True
            active=(found.group(1)[0],len(found.group(1)))
    result=[]
    i=0
    while i < len(lines):
        if excluded[i] or not lines[i].strip().startswith("|"):
            i+=1
            continue
        block_start=i+1
        block=[]
        while i<len(lines) and not excluded[i] and lines[i].strip().startswith("|"):
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
            if not table or ("ID" not in table[0] and not (role=="usecases" and "Slug" in table[0])):
                continue
            for row in table:
                item_id=row.get("ID","").strip()
                if role=="usecases" and "Slug" in row:
                    item_id=row["Slug"].strip()
                linked=LINKED_ID.fullmatch(item_id)
                if linked:
                    item_id=linked.group(1)
                if role=="usecases" and item_id.startswith("uc-"):
                    item_id="UC-"+item_id[3:]
                if not ID.fullmatch(item_id):
                    continue
                kind=item_id.split("-",1)[0]
                if role=="urd" and kind!="UN":
                    continue
                if role=="brd" and kind!="BO":
                    continue
                if role=="prd" and kind!="CAP":
                    continue
                if role=="criteria" and kind!="AC":
                    continue
                if role=="srs" and kind not in ("FR","NFR","BR","E"):
                    continue
                if role=="checklist" and kind!="CHK":
                    continue
                if role=="cases" and kind!="TC":
                    continue
                if role=="stories" and kind!="US":
                    continue
                if role=="usecases" and kind!="UC":
                    continue
                if not all(key in row for key in HEADERS[kind]):
                    raise ValueError(f"{item_id}: missing necessary columns {HEADERS[kind]}")
                title=row.get(DISPLAY_CELLS[kind],"").strip()
                if kind=="UC":
                    title=item_id[3:].replace("-"," ").capitalize()
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
    ancestry={item["id"]:set(item["depends_on"]) for item in artifacts}
    origins={item["id"]:item["kind"] for item in artifacts}
    requirements=sorted((x for x in artifacts if x["kind"]=="FR"),key=lambda x:x["id"])
    # Only a complete FR -> CAP -> BO -> UN ancestry chain counts.
    traced=[]
    for fr in requirements:
        caps=[cid for cid in ancestry[fr["id"]] if origins.get(cid)=="CAPABILITY"]
        meaningful=False
        for cap in caps:
            for bo in [bid for bid in ancestry.get(cap,set()) if origins.get(bid)=="BUSINESS_OBJECTIVE"]:
                if any(origins.get(u)=="NEED" for u in ancestry.get(bo,set())):
                    meaningful=True
                    break
            if meaningful: break
        if meaningful: traced.append(fr["id"])
    tested=set(requirement["id"] for requirement in requirements)-set(report["coverage"]["uncovered"])
    complete=sorted(tested&set(traced))
    # A per-FR witness is more useful than a single coverage percentage.
    # Only edges explicit in inspected source tables may appear in a proof.
    from collections import defaultdict, deque
    backlinks: dict[str, list[str]] = defaultdict(list)
    for child,parents in ancestry.items():
        for parent in parents:
            backlinks[parent].append(child)
    for values in backlinks.values():
        values.sort()
    byid={entry["id"]:entry for entry in artifacts}
    def upstream_proof(fr_id: str) -> list[str] | None:
        for cap in sorted(ancestry.get(fr_id,[])):
            if origins.get(cap)!="CAPABILITY":
                continue
            for bo in sorted(ancestry.get(cap,[])):
                if origins.get(bo)!="BUSINESS_OBJECTIVE":
                    continue
                for un in sorted(ancestry.get(bo,[])):
                    if origins.get(un)=="NEED":
                        return [un,bo,cap,fr_id]
        return None
    def test_proof(fr_id: str) -> list[str] | None:
        follow={"ERROR","E","AC","ACCEPTANCE","CHECKLIST","CHK","TEST","TC"}
        q=deque([(fr_id,[fr_id])])
        seen={fr_id}
        while q:
            current,path=q.popleft()
            for dependent in backlinks.get(current,[]):
                if dependent in seen or origins.get(dependent) not in follow:
                    continue
                witness=path+[dependent]
                if origins[dependent] in ("TEST","TC"):
                    return witness
                seen.add(dependent)
                q.append((dependent,witness))
        return None
    fr_witnesses=[]
    for fr in requirements:
        fid=fr["id"]
        up=upstream_proof(fid)
        down=test_proof(fid)
        test_artifact=byid[down[-1]] if down else None
        fr_witnesses.append({
            "id":fid,
            "source":fr.get("source_location"),
            "upstream_path":up,
            "test_path":down,
            "upstream_chain_present":up is not None,
            "test_artifact_linked":down is not None,
            "complete_structural_chain":up is not None and down is not None,
            "test_execution_status":test_artifact.get("verification_status","not-proven") if test_artifact else "no-test-artifact",
            "unresolved_references":fr.get("external_refs",[]),
        })
    lifecycle={"user_needs":counts.get("NEED",0),
               "business_objectives":counts.get("BUSINESS_OBJECTIVE",0),
               "capabilities":counts.get("CAPABILITY",0),
               "functional_requirements":len(requirements),
               "fr_traced_via_capability_objective_need":len(traced),
               "fr_linked_to_test_artifact":len(tested),
               "fr_with_complete_structural_chain":len(complete),
               "complete_fr_ids":complete,
               "missing_upstream_chain":sorted(set(x["id"] for x in requirements)-set(traced)),
               "missing_test_artifact":report["coverage"]["uncovered"],
               "per_requirement":fr_witnesses,
               "verification":"links only; no stakeholder or production evidence"}
    return {"graph":graph,"coverage":report["coverage"],"lifecycle":lifecycle,"counts":counts,
            "unresolved_external_refs":unresolved,
            "caveats":["A linked test artifact is not an executed test result.",
                       "A source status marked approved is not proof of deployed behavior.",
                       "References to CAP/AC/US outside inspected files are reported, not invented.",
                       "Only explicit Markdown table relationships are inferred by this extractor."]}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--srs",required=True,type=Path)
    p.add_argument("--urd",type=Path,help="Optional accepted user-needs index with UN IDs")
    p.add_argument("--brd",type=Path,help="Optional accepted business objectives index with BO IDs")
    p.add_argument("--prd",type=Path,help="Optional accepted feature capability index with CAP IDs")
    p.add_argument("--criteria",type=Path,help="Optional accepted AC table with Criterion column")
    p.add_argument("--checklist",type=Path)
    p.add_argument("--cases",type=Path)
    p.add_argument("--stories",type=Path,help="User story index table, when present")
    p.add_argument("--usecases",type=Path,help="Use-case index table, when present")
    p.add_argument("--root",type=Path,default=Path("."))
    p.add_argument("--output",type=Path,required=True)
    opts=p.parse_args()
    paths={"srs":opts.srs}
    for source_role in ("urd","brd","prd","criteria"):
        if getattr(opts,source_role): paths[source_role]=getattr(opts,source_role)
    if opts.checklist: paths["checklist"]=opts.checklist
    if opts.cases: paths["cases"]=opts.cases
    if opts.stories: paths["stories"]=opts.stories
    if opts.usecases: paths["usecases"]=opts.usecases
    try:
        report=collect(paths,opts.root)
        opts.output.parent.mkdir(parents=True,exist_ok=True)
        opts.output.write_text(json.dumps(report["graph"],ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        print(json.dumps({"ok":True,"output":str(opts.output),
                          "counts":report["counts"],"coverage":report["coverage"],"lifecycle":report["lifecycle"],
                          "unresolved_external_refs":report["unresolved_external_refs"],
                          "caveats":report["caveats"]},ensure_ascii=False,indent=2))
        return 0
    except (OSError,ValueError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)},ensure_ascii=False))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
