#!/usr/bin/env python3
"""Produce a read-only provenance-aware reverse specification preview.

Input is a reviewed claim ledger, NOT an automatic code or document scanner.
Neither writing HTML nor source identity establishes stakeholder approval.
"""
from __future__ import annotations
import argparse
import html
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
from typing import Any

ID=re.compile(r"^[A-Za-z][A-Za-z0-9-]{1,99}$")
LEVELS=("SOURCE-OBSERVED","INFERRED","UNCONFIRMED","CONTRADICTORY","APPROVED-DECISION")

def validate(data:Any)->dict[str,Any]:
    errors=[]
    if not isinstance(data,dict):
        return {"ok":False,"errors":["Root must be a JSON object"]}
    sources=data.get("sources")
    claims=data.get("claims")
    if not isinstance(sources,list) or not sources or not isinstance(claims,list) or not claims:
        return {"ok":False,"errors":["sources and claims must be nonempty arrays"]}
    sourceids=set()
    for i,source in enumerate(sources):
        if not isinstance(source,dict):
            errors.append(f"sources[{i}]: invalid source")
            continue
        sid=source.get("id")
        if not isinstance(sid,str) or not ID.fullmatch(sid) or sid in sourceids:
            errors.append(f"sources[{i}]: invalid or repeated ID")
        else:sourceids.add(sid)
        for field in ("uri","revision"):
            if not isinstance(source.get(field),str) or not source[field].strip():
                errors.append(f"sources[{i}]: missing {field}")
    ids=set()
    for i,claim in enumerate(claims):
        if not isinstance(claim,dict):
            errors.append(f"claims[{i}]: invalid claim")
            continue
        cid=claim.get("id")
        if not isinstance(cid,str) or not ID.fullmatch(cid) or cid in ids:
            errors.append(f"claims[{i}]: missing/duplicate ID")
            continue
        ids.add(cid)
        if claim.get("confidence") not in LEVELS:
            errors.append(f"{cid}: invalid confidence level")
        if not isinstance(claim.get("statement"),str) or not claim["statement"].strip():
            errors.append(f"{cid}: missing concrete claim")
        refs=claim.get("source_refs")
        if (not isinstance(refs,list) or not refs or
            not all(isinstance(x,str) and x in sourceids for x in refs)):
            errors.append(f"{cid}: absent or unresolved source references")
            refs=[]
        elif len(set(refs))!=len(refs):
            errors.append(f"{cid}: duplicate source reference")
        if claim.get("confidence")=="CONTRADICTORY" and len(set(refs))<2:
            errors.append(f"{cid}: contradiction requires two distinct source witnesses")
        if claim.get("confidence")=="APPROVED-DECISION":
            did=claim.get("decision_id")
            if (not isinstance(did,str) or not ID.fullmatch(did) or
                not isinstance(claim.get("approval_source"),str) or
                claim["approval_source"] not in refs):
                errors.append(f"{cid}: approval needs stable decision ID and cited approval source")
        if claim.get("confidence")!="APPROVED-DECISION":
            if not isinstance(claim.get("next_verification"),str) or not claim["next_verification"].strip():
                errors.append(f"{cid}: unresolved claim requires a verification action")
        for field in ("conflicting_claim","impact"):
            if field in claim and not isinstance(claim[field],str):
                errors.append(f"{cid}: invalid {field}")
    return {"ok":not errors,"errors":sorted(set(errors)),
            "claim_count":len(ids),"source_count":len(sourceids),
            "confidence_breakdown":{level:sum(isinstance(x,dict) and x.get("confidence")==level for x in claims)
                                    for level in LEVELS},
            "approval_source_checked":"citation-ID-only; stakeholder authority not independently verified"}

def e(value:Any)->str:
    return html.escape(str(value),quote=True)

def link(uri:str)->str|None:
    # Explicitly allow only absolute HTTP(S). Local files are described without
    # clickable links to avoid unsafe path traversal and file-origin surprises.
    try:
        url=urlsplit(uri)
        if url.scheme in ("http","https") and url.netloc and not url.username and not url.password:
            return uri
    except ValueError:
        pass
    return None

def render(data:dict[str,Any],title:str="Reverse specification evidence")->str:
    report=validate(data)
    if not report["ok"]:
        raise ValueError("; ".join(report["errors"]))
    sources={x["id"]:x for x in data["sources"]}
    nav=[]
    cards=[]
    for item in data["claims"]:
        cid=item["id"]
        nav.append('<li><a href="#'+e(cid)+'">'+e(cid)+": "+e(item["confidence"])+'</a></li>')
        links=[]
        for ref in item["source_refs"]:
            source=sources[ref]
            source_text=e(ref)+": "+e(source["uri"])+" @ "+e(source["revision"])
            safe=link(source["uri"])
            if safe:
                source_text='<a href="'+e(safe)+'" rel="noopener noreferrer">'+source_text+'</a>'
            links.append('<li>'+source_text+'</li>')
        detail=('<p><strong>Possible conflict:</strong> '+e(item["conflicting_claim"])+'</p>'
                if item.get("conflicting_claim") else "")
        review=('<p><strong>Next evidence:</strong> '+e(item["next_verification"])+'</p>'
                if item.get("next_verification") else "")
        approval=('<p><strong>Decision:</strong> '+e(item.get("decision_id",""))+'</p>'
                  if item["confidence"]=="APPROVED-DECISION" else "")
        impact=('<p><strong>Impact if wrong:</strong> '+e(item["impact"])+'</p>'
                if item.get("impact") else "")
        cards.append('<article id="'+e(cid)+'"><h2>'+e(cid)+'</h2><p class="confidence"><strong>Evidence: '+e(item["confidence"])+'</strong></p>'
                     +'<p>'+e(item["statement"])+'</p>'+detail+review+approval+impact
                     +'<details open><summary>Source evidence ('+str(len(links))+')</summary><ul>'
                     +''.join(links)+'</ul></details></article>')
    css=("body{font:16px/1.55 system-ui;margin:0 auto;max-width:960px;padding:2rem;color:#18252c;background:#f7f8f8}"
         "article{background:white;border:1px solid #a1abb0;padding:1rem 1.3rem;margin:1.4rem 0;border-radius:.55rem}"
         "a{color:#15598a;overflow-wrap:anywhere}nav{padding:1rem;background:white;border:1px solid #b0b8bd}"
         "h1{font-size:1.6rem}h2{font-size:1.15rem}.confidence{font-size:.85rem}li{margin:.3rem 0}"
         ":focus-visible{outline:3px solid #155c93;outline-offset:3px}"
         "@media(max-width:600px){body{padding:.9rem}article{padding:.9rem}}")
    csp="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'"
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            +'<meta http-equiv="Content-Security-Policy" content="'+e(csp)+'"><title>'+e(title)+'</title><style>'+css+'</style></head><body>'
            +'<header><h1>'+e(title)+'</h1><p>Reconstructed evidence for review. Neither source observations nor claims of approval prove deployed behavior.</p>'
            +'<p>Total claims: '+str(report["claim_count"])+'; none automatically promoted to accepted requirements.</p></header>'
            +'<nav aria-label="Evidence claims"><h2>Claim index</h2><ul>'+''.join(nav)+'</ul></nav><main>'
            +''.join(cards)+'</main><footer>Confidence is a source class, not a numeric probability or a verified production result.</footer></body></html>')

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",type=Path)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--title",default="Reverse specification evidence")
    args=parser.parse_args()
    try:
        data=json.loads(args.input.read_text(encoding="utf8"))
        page=render(data,args.title)
        if args.output.exists():raise ValueError("Refusing to overwrite existing preview")
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(page,encoding="utf8")
        print(json.dumps({"ok":True,"output":str(args.output),"read_only":True,
                          "claims":len(data["claims"]),"network_calls":0,"provider_writes":0}))
        return 0
    except (OSError,ValueError,TypeError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1
if __name__=="__main__":
    raise SystemExit(main())
