#!/usr/bin/env python3
"""Conservatively compare explicit Bruno tests to a scoped OpenAPI 3.1 JSON contract.

This is a subset implementation: inline JSON object response bodies, simple
properties/required/enum/const, local JSON-pointer $ref and bearer security.
Unsupported oneOf/anyOf/allOf and remote references fail closed.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from typing import Any
from build_bruno import validate as validate_bruno

URI_VARIABLE=re.compile(r"\{\{([A-Za-z_][A-Za-z0-9_]*)\}\}")
VERSION=re.compile(r"^3\.1(?:\.\d+)?$")


def _resolve_local(document:dict, value:Any, seen:frozenset[str] = frozenset())->dict:
    """Resolve bounded local OpenAPI $refs, rejecting cycles and remote fetches."""
    if not isinstance(value,dict):
        raise ValueError("Expected OpenAPI schema/response object")
    if any(k in value for k in ("allOf","oneOf","anyOf")):
        raise ValueError("Schema composition is unsupported; explicit review required")
    if "$ref" not in value:
        return value
    ref=value["$ref"]
    if not isinstance(ref,str) or not ref.startswith("#/") or ref.startswith("#//"):
        raise ValueError("Only local #/ JSON-pointer references are supported")
    if ref in seen or len(seen)>=12:
        raise ValueError("Recursive or excessively deep OpenAPI $ref: "+ref)
    target=document
    for raw in ref[2:].split("/"):
        if re.search(r"~(?![01])",raw):
            raise ValueError("Invalid JSON-pointer escape")
        part=raw.replace("~1","/").replace("~0","~")
        if not isinstance(target,dict) or part not in target:
            raise ValueError("Unresolved local OpenAPI $ref: "+ref)
        target=target[part]
    return _resolve_local(document,target,seen|{ref})


def _kind(value:Any)->str:
    if value is None:return "null"
    if isinstance(value,bool):return "boolean"
    if isinstance(value,int):return "integer"
    if isinstance(value,float):return "number"
    if isinstance(value,str):return "string"
    if isinstance(value,list):return "array"
    if isinstance(value,dict):return "object"
    return "unsupported"


def _match_scalar(value:Any,schema:dict,document:dict)->bool:
    schema=_resolve_local(document,schema)
    kind=schema.get("type")
    allowed=[kind] if isinstance(kind,str) else kind
    if not isinstance(allowed,list) or not allowed or any(
        not isinstance(x,str) or x not in ("string","integer","number","boolean","null")
        for x in allowed):
        raise ValueError("Unsupported scalar JSON Schema type")
    actual=_kind(value)
    matched=any(
        actual==option or (option=="number" and actual in ("integer","number")) or
        (option=="integer" and actual=="number" and float(value).is_integer())
        for option in allowed
    )
    if not matched:return False
    if not matched:return False
    def json_equal(a,b):
        # JSON Schema uses mathematical numeric equality, but never equates bool with 1/0.
        if isinstance(a,bool) or isinstance(b,bool):
            return type(a) is type(b) and a==b
        return a==b
    if "const" in schema and not json_equal(value,schema["const"]):
        return False
    if "enum" in schema and not any(json_equal(value,x) for x in schema["enum"]):
        return False
    if actual in ("integer","number"):
        # JSON Schema: bool is not numeric, an integral float is an integer.
        for prop in ("minimum","maximum","exclusiveMinimum","exclusiveMaximum"):
            if prop in schema:
                limit=schema[prop]
                if isinstance(limit,bool) or not isinstance(limit,(int,float)):
                    raise ValueError("Invalid numeric schema bound")
                if prop=="minimum" and value<limit:return False
                if prop=="maximum" and value>limit:return False
                if prop=="exclusiveMinimum" and value<=limit:return False
                if prop=="exclusiveMaximum" and value>=limit:return False
    if actual=="string":
        for prop in ("minLength","maxLength"):
            if prop in schema:
                limit=schema[prop]
                if isinstance(limit,bool) or not isinstance(limit,int) or limit<0:
                    raise ValueError("Invalid string schema length bound")
                if prop=="minLength" and len(value)<limit:return False
                if prop=="maxLength" and len(value)>limit:return False
    # Explicitly reject constraints not evaluated by this conservative subset.
    unknown=set(schema)&{"pattern","format","multipleOf","not","if","then","else","dependentSchemas","contentEncoding","contentMediaType"}
    if unknown:
        raise ValueError("Unsupported scalar JSON Schema constraint: "+", ".join(sorted(unknown)))
    return True


def _schema_property(document:dict,schema:dict,path:list[str])->tuple[dict|None,str]:
    current=_resolve_local(document,schema)
    for key in path:
        if current.get("type")!="object":
            return None,"parent is not a resolved object"
        props=current.get("properties")
        if not isinstance(props,dict) or key not in props:
            return None,"property "+key+" is not declared"
        current=_resolve_local(document,props[key])
    type_value=current.get("type")
    allowed=[type_value] if isinstance(type_value,str) else type_value
    if not isinstance(allowed,list) or not allowed or any(
        not isinstance(k,str) or k not in ("string","integer","number","boolean","null")
        for k in allowed):
        return None,"property is not a supported scalar type"
    return current,""


def _response_schema(document:dict,operation:dict,status:int)->dict|None:
    responses=operation.get("responses",{})
    if not isinstance(responses,dict):
        raise ValueError("operation.responses must be an object")
    key=str(status)
    if key not in responses:
        wildcard=str(status//100)+"XX"
        key=wildcard if wildcard in responses else "default"
    if key not in responses:
        raise ValueError("expected HTTP "+str(status)+" is not in operation.responses (exact, range or default)")
    response=_resolve_local(document,responses[key])
    content=response.get("content",{})
    if not isinstance(content,dict):
        return None
    app=content.get("application/json")
    if not isinstance(app,dict):
        return None
    return _resolve_local(document,app.get("schema"))



def audit_contract(contract:Any,model:Any)->dict[str,Any]:
    errors:list[str]=[]
    warnings:list[str]=[]
    report=validate_bruno(model)
    if not report["ok"]:
        return {"ok":False,"errors":["Invalid Bruno test model: "+e for e in report["errors"]]}
    if not isinstance(contract,dict) or not isinstance(contract.get("openapi"),str) or not VERSION.fullmatch(contract["openapi"]):
        return {"ok":False,"errors":["Expected a JSON OpenAPI 3.1 document; this checker does not support Swagger 2 or OpenAPI 3.0"]}
    paths=contract.get("paths")
    if not isinstance(paths,dict):
        return {"ok":False,"errors":["OpenAPI paths must be an object"]}
    declared_security=contract.get("security",[])
    if not isinstance(declared_security,list):
        errors.append("security must be an array")
        declared_security=[]
    for item in model["requests"]:
        ident=item["id"]
        route=item["path"].split("?",1)[0]
        route=URI_VARIABLE.sub(lambda m:"{"+m.group(1)+"}",route)
        operation=(paths.get(route) or {}).get(item["method"].lower())
        if not isinstance(operation,dict):
            errors.append(ident+": "+item["method"]+" "+route+" is not declared")
            continue
        security=operation.get("security",declared_security)
        if not isinstance(security,list) or any(not isinstance(x,dict) for x in security):
            errors.append(ident+": invalid security alternatives")
            continue
        # OpenAPI: OR between alternatives; AND between schemes in one entry.
        # [] or an empty alternative {} permits anonymous access.
        anonymous=not security or any(not option for option in security)
        specs=contract.get("components",{}).get("securitySchemes",{})
        if not isinstance(specs,dict):
            errors.append(ident+": invalid securitySchemes object")
            continue
        bearer_possible=False
        for alternative in security:
            if not alternative:
                continue
            if any(not isinstance(name,str) or name not in specs or
                   not isinstance(scopes,list) for name,scopes in alternative.items()):
                errors.append(ident+": security references undeclared schemes or invalid scopes")
                continue
            if len(alternative)==1:
                key=next(iter(alternative))
                scheme=specs[key]
                if isinstance(scheme,dict) and scheme.get("type")=="http" and scheme.get("scheme")=="bearer":
                    bearer_possible=True
        if item.get("auth","none")=="none" and not anonymous:
            errors.append(ident+": contract requires auth but the Bruno test has auth none")
        if item.get("auth")=="bearer" and not bearer_possible:
            errors.append(ident+": bearer-only auth is not a valid OpenAPI security alternative")
        expected=item["expected_status"]
        try:
            schema=_response_schema(contract,operation,expected)
        except ValueError as exc:
            errors.append(ident+": "+str(exc))
            continue
        expected_fields=item.get("expected_json",{})
        if expected_fields and (not isinstance(schema,dict) or schema.get("type")!="object"):
            errors.append(ident+": expected JSON fields require a supported object response schema")
            continue
        for field,value in expected_fields.items():
            try:
                property_schema,why=_schema_property(contract,schema,field.split("."))
                if property_schema is None:
                    errors.append(ident+": "+field+" "+why)
                elif not _match_scalar(value,property_schema,contract):
                    errors.append(ident+": "+field+" value contradicts declared type, const or enum")
            except ValueError as exc:
                errors.append(ident+": "+field+" "+str(exc))
        try:
            requestbody=_resolve_local(contract,operation["requestBody"]) if "requestBody" in operation else None
        except ValueError as exc:
            errors.append(ident+": "+str(exc))
            continue
        body=item.get("body_json")
        if requestbody is None and body is not None:
            errors.append(ident+": test sends a JSON body but OpenAPI has no requestBody")
        if isinstance(requestbody,dict) and requestbody.get("required") and body is None:
            errors.append(ident+": missing required JSON requestBody")
        if body is not None and isinstance(requestbody,dict):
            try:
                schema_in=_resolve_local(contract,requestbody.get("content",{}).get("application/json",{}).get("schema"))
            except ValueError as exc:
                errors.append(ident+": "+str(exc))
                continue
            if schema_in.get("type")!="object" or not isinstance(body,dict):
                errors.append(ident+": only supported JSON object requestBody schemas are accepted")
            else:
                for key in schema_in.get("required",[]):
                    if key not in body:errors.append(ident+": missing required body property "+str(key))
                for key,value in body.items():
                    declared=(schema_in.get("properties") or {}).get(key)
                    if declared is None:
                        if schema_in.get("additionalProperties") is False:
                            errors.append(ident+": undeclared body property "+key)
                        else:
                            warnings.append(ident+": body property "+key+" is not explicitly modeled")
                    else:
                        try:
                            if not isinstance(declared,dict) or not _match_scalar(value,declared,contract):
                                errors.append(ident+": body property "+key+" contradicts type/enum/const")
                        except ValueError as exc:
                            errors.append(ident+": body property "+key+" "+str(exc))
        if not item.get("requirements"):
            warnings.append(ident+": no BA source requirement linked")
    return {"ok":not errors,"errors":sorted(set(errors)),"warnings":sorted(set(warnings)),
            "requests_checked":len(model["requests"]),"contract_version":contract["openapi"],
            "source_contract_check":"static-openapi-subset-with-local-refs-security-and-status",
            "execution_status":"not-run","writes_performed":False}


def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract",type=Path)
    parser.add_argument("test_model",type=Path)
    args=parser.parse_args()
    try:
        contract=json.loads(args.contract.read_text(encoding="utf8"))
        model=json.loads(args.test_model.read_text(encoding="utf8"))
        report=audit_contract(contract,model)
    except (OSError,ValueError,TypeError) as exc:
        report={"ok":False,"errors":[str(exc)]}
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if report["ok"] else 1

if __name__=="__main__":
    raise SystemExit(main())
