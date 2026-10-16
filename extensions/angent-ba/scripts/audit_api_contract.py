#!/usr/bin/env python3
"""Conservatively compare explicit Bruno tests to a scoped OpenAPI 3.1 JSON contract.

This is a subset implementation: inline JSON object response bodies, simple
properties/required/enum/const and bearer security. Unsupported $ref, oneOf,
anyOf, nullable composition etc fail closed instead of asserting parity.
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


def _kind(value:Any)->str:
    if value is None:return "null"
    if isinstance(value,bool):return "boolean"
    if isinstance(value,int):return "integer"
    if isinstance(value,float):return "number"
    if isinstance(value,str):return "string"
    if isinstance(value,list):return "array"
    if isinstance(value,dict):return "object"
    return "unsupported"


def _match_scalar(value:Any,schema:dict)->bool:
    kind=schema.get("type")
    if not isinstance(kind,str):
        return False
    if kind=="number":
        matched=_kind(value) in ("integer","number")
    else:
        matched=_kind(value)==kind
    if not matched:return False
    if "const" in schema and value!=schema["const"]:return False
    if "enum" in schema and value not in schema["enum"]:return False
    return True


def _schema_property(schema:dict,path:list[str])->tuple[dict|None,str]:
    current=schema
    for key in path:
        if not isinstance(current,dict) or "allOf" in current or "oneOf" in current or "anyOf" in current or "$ref" in current:
            return None,"unsupported composition"
        if current.get("type")!="object":
            return None,"parent is not an inline object"
        current=(current.get("properties") or {}).get(key)
        if current is None:
            return None,"property "+key+" is not declared"
    if not isinstance(current,dict) or "$ref" in current or "allOf" in current or "oneOf" in current or "anyOf" in current:
        return None,"unsupported scalar schema"
    return current,""


def _response_schema(operation:dict,status:int)->dict|None:
    responses=operation.get("responses",{})
    response=responses.get(str(status))
    if not isinstance(response,dict) or "$ref" in response:
        return None
    content=response.get("content",{})
    if not isinstance(content,dict):
        return None
    app=content.get("application/json")
    if not isinstance(app,dict):
        return None
    return app.get("schema")


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
        if not isinstance(security,list):
            errors.append(ident+": invalid security definition")
            security=[]
        if security and item.get("auth","none")=="none":
            errors.append(ident+": contract requires auth but the Bruno test has auth none")
        if item.get("auth")=="bearer":
            specs=contract.get("components",{}).get("securitySchemes",{})
            if not any(isinstance(v,dict) and v.get("type")=="http" and v.get("scheme")=="bearer"
                       for v in specs.values()):
                errors.append(ident+": bearer auth is not defined in the OpenAPI security schemes")
        expected=item["expected_status"]
        schema=_response_schema(operation,expected)
        if str(expected) not in operation.get("responses",{}):
            errors.append(ident+": expected HTTP "+str(expected)+" is not in operation.responses")
            continue
        expected_fields=item.get("expected_json",{})
        if expected_fields and (not isinstance(schema,dict) or schema.get("type")!="object"):
            errors.append(ident+": expected JSON fields require an inline object response schema")
            continue
        for field,value in expected_fields.items():
            property_schema,why=_schema_property(schema,field.split("."))
            if property_schema is None:
                errors.append(ident+": "+field+" "+why)
            elif not _match_scalar(value,property_schema):
                errors.append(ident+": "+field+" value contradicts declared type, const or enum")
        requestbody=operation.get("requestBody")
        body=item.get("body_json")
        if requestbody is None and body is not None:
            errors.append(ident+": test sends a JSON body but OpenAPI has no requestBody")
        if isinstance(requestbody,dict) and requestbody.get("required") and body is None:
            errors.append(ident+": missing required JSON requestBody")
        if body is not None and isinstance(requestbody,dict):
            schema_in=requestbody.get("content",{}).get("application/json",{}).get("schema")
            if not isinstance(schema_in,dict) or schema_in.get("type")!="object" or not isinstance(body,dict):
                errors.append(ident+": only inline JSON object requestBody schemas are supported")
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
                    elif not isinstance(declared,dict) or not _match_scalar(value,declared):
                        errors.append(ident+": body property "+key+" contradicts type/enum/const")
        if not item.get("requirements"):
            warnings.append(ident+": no BA source requirement linked")
    return {"ok":not errors,"errors":sorted(set(errors)),"warnings":sorted(set(warnings)),
            "requests_checked":len(model["requests"]),"contract_version":contract["openapi"],
            "source_contract_check":"static-inline-openapi-subset",
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
