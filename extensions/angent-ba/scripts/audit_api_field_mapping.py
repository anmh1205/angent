#!/usr/bin/env python3
"""Audit and execute a deterministic OpenAPI-to-UI data field mapping on fixtures.

No network/provider access or code injection. Does not infer application mapping
from field names or claim to verify production frontend binding.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from typing import Any
from audit_api_contract import _response_schema, _schema_property, _match_scalar, _kind, VERSION

IDENT=re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
REF=re.compile(r"^(?:FR|BR|AC|NFR|CAP)-[A-Za-z0-9][A-Za-z0-9-]*$")
RESERVED={"__proto__","prototype","constructor"}
ALLOWED_TYPES={"string","integer","number","boolean","null"}
ALLOWED_TRANSFORMS={"copy","enum"}

def dotted(path:Any)->list[str]:
    if not isinstance(path,str) or len(path)>120:
        raise ValueError("Invalid dotted field path")
    parts=path.split(".")
    if not parts or len(parts)>8 or any(not IDENT.fullmatch(p) or p in RESERVED for p in parts):
        raise ValueError("Invalid/reserved dotted field path: "+str(path))
    return parts

def lookup(data:Any,parts:list[str])->Any:
    current=data
    for p in parts:
        if not isinstance(current,dict) or p not in current:
            raise ValueError("Source fixture field missing: "+".".join(parts))
        current=current[p]
    return current

def place(data:dict,parts:list[str],value:Any)->None:
    current=data
    for p in parts[:-1]:
        if p in current and not isinstance(current[p],dict):
            raise ValueError("Output path collides with scalar: "+".".join(parts))
        current=current.setdefault(p,{})
    if parts[-1] in current:
        raise ValueError("Duplicate output path: "+".".join(parts))
    current[parts[-1]]=value

def perform(contract:Any,mapping:Any,evidence_ids:set[str]|None=None)->dict[str,Any]:
    if (not isinstance(contract,dict) or not isinstance(contract.get("openapi"),str)
            or not VERSION.fullmatch(contract["openapi"])):
        raise ValueError("An inspected OpenAPI 3.1 JSON contract is required")
    if not isinstance(mapping,dict) or not isinstance(mapping.get("operation"),dict):
        raise ValueError("Mapping needs an explicit operation")
    op=mapping["operation"]
    path,method,status=op.get("path"),op.get("method"),op.get("expected_status")
    if not isinstance(path,str) or not path.startswith("/") or "?" in path or not isinstance(method,str):
        raise ValueError("Operation path and method must be exact OpenAPI fields")
    if isinstance(status,bool) or not isinstance(status,int) or status<100 or status>599:
        raise ValueError("Expected HTTP status must be integer")
    paths=contract.get("paths")
    if not isinstance(paths,dict):
        raise ValueError("OpenAPI paths must be an object")
    path_item=paths.get(path)
    if path_item is not None and not isinstance(path_item,dict):
        raise ValueError("OpenAPI path item must be an object")
    operation=(path_item or {}).get(method.lower())
    if not isinstance(operation,dict):
        raise ValueError("No such OpenAPI operation "+method+" "+path)
    schema=_response_schema(contract,operation,status)
    if not isinstance(schema,dict) or schema.get("type")!="object":
        raise ValueError("Expected response has no supported object schema")
    refs=mapping.get("source_refs",[])
    if not isinstance(refs,list) or any(not isinstance(x,str) or not REF.fullmatch(x) for x in refs):
        raise ValueError("Invalid source requirement ID")
    if len(set(refs))!=len(refs):
        raise ValueError("Duplicate source requirement")
    if evidence_ids is not None and (not refs or any(x not in evidence_ids for x in refs)):
        raise ValueError("Unresolved or absent BA source evidence IDs")
    sample=mapping.get("sample_response")
    types=mapping.get("ui_field_types")
    expected=mapping.get("expected_ui")
    items=mapping.get("fields")
    if not isinstance(sample,dict) or not isinstance(types,dict) or not isinstance(expected,dict):
        raise ValueError("Need JSON source sample, UI field type contract and expected UI fixture")
    if not isinstance(items,list) or not items or len(items)>120:
        raise ValueError("Need a nonempty bounded field mapping")
    output={}
    observed=[]
    target_keys=set()
    for i,item in enumerate(items):
        if not isinstance(item,dict):
            raise ValueError("Invalid mapping entry at "+str(i))
        source=item.get("source")
        target=item.get("target")
        sp,tp=dotted(source),dotted(target)
        if target in target_keys:
            raise ValueError("Duplicate destination: "+target)
        target_keys.add(target)
        field_schema,reason=_schema_property(contract,schema,sp)
        if field_schema is None:
            raise ValueError("OpenAPI source field is not supported: "+source+" ("+reason+")")
        value=lookup(sample,sp)
        if not _match_scalar(value,field_schema,contract):
            raise ValueError("Source sample violates its OpenAPI schema: "+source)
        transform=item.get("transform","copy")
        if transform not in ALLOWED_TRANSFORMS:
            raise ValueError("Unsupported field transform: "+str(transform))
        if transform=="enum":
            cases=item.get("cases")
            if not isinstance(value,str) or not isinstance(cases,dict) or value not in cases:
                raise ValueError("Enum transform lacks explicit source value: "+source)
            if not all(isinstance(k,str) and isinstance(v,(str,int,float,bool)) for k,v in cases.items()):
                raise ValueError("Enum transform cases must be scalar")
            result=cases[value]
        else:
            if "cases" in item:
                raise ValueError("copy transform cannot declare enum cases")
            result=value
        target_type=types.get(target)
        if target_type not in ALLOWED_TYPES:
            raise ValueError("Missing or unsupported UI field type: "+target)
        actual=_kind(result)
        if not (actual==target_type or
                (target_type=="number" and actual in ("integer","number"))):
            raise ValueError("Destination value contradicts UI field contract: "+target)
        place(output,tp,result)
        observed.append({"from":source,"to":target,"transform":transform,
                         "source_schema_type":field_schema.get("type"),
                         "ui_type":target_type})
    if set(types)!=target_keys:
        raise ValueError("UI contract contains unmapped or missing destinations")
    if output!=expected:
        raise ValueError("Mapped output differs from explicitly expected UI fixture")
    return {"ok":True,"operation":op,"field_count":len(items),
            "fields":observed,"mapped_fixture":output,
            "source_link_check":"ids-resolved-only" if evidence_ids is not None else "not-performed",
            "scope":"provided OpenAPI 3.1 response sample and explicit UI field contract",
            "live_api_calls":0,"browser_bindings_verified":False,
            "writes_performed":False}

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mapping",type=Path)
    parser.add_argument("--openapi",required=True,type=Path)
    parser.add_argument("--evidence-graph",type=Path)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    try:
        mapping=json.loads(args.mapping.read_text(encoding="utf8"))
        contract=json.loads(args.openapi.read_text(encoding="utf8"))
        ids=None
        if args.evidence_graph:
            from validate_artifacts import audit
            graph=json.loads(args.evidence_graph.read_text(encoding="utf8"))
            validation=audit(graph)
            if not validation["ok"]:
                raise ValueError("Invalid source graph: "+"; ".join(validation["errors"]))
            ids={x["id"] for x in graph["artifacts"]}
        result=perform(contract,mapping,ids)
        if args.output:
            if args.output.exists():
                raise ValueError("Refusing to overwrite existing result")
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    except (OSError,ValueError,TypeError) as exc:
        result={"ok":False,"error":str(exc)}
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result["ok"] else 1

if __name__=="__main__":
    raise SystemExit(main())
