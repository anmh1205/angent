#!/usr/bin/env python3
"""Generate Bruno API test collections from reviewed, explicit contracts.

This command only writes files; it never sends network requests. It does NOT
turn a fake environment or missing test execution into a passing test.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from typing import Any

IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
TEST_ID = re.compile(r"^TC-[A-Za-z0-9][A-Za-z0-9-]*$")
REQUIREMENT_ID = re.compile(r"^(?:FR|BR|NFR|AC|CHK)-[A-Za-z0-9][A-Za-z0-9-]*$")
NAME = re.compile(r"^[A-Za-z0-9 _.,:/()\-]{1,100}$")
METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}
FIELD = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*$")
SENSITIVE_KEY = re.compile(r"(?:password|secret|token|api[_-]?key|credential)", re.I)
FORBIDDEN_PROPERTY = {"__proto__", "constructor", "prototype"}
PLACEHOLDER = re.compile(r"\{\{([A-Za-z_][A-Za-z0-9_]*)\}\}")


def validate(model: Any, evidence_ids: set[str] | None = None) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(model, dict):
        return {"ok": False, "errors": ["Root must be object"]}
    label = model.get("name")
    if not isinstance(label, str) or not NAME.fullmatch(label):
        errors.append("Collection name has invalid characters")
    environ = model.get("environment")
    if not isinstance(environ, dict) or not environ:
        errors.append("environment object required")
        environ = {}
    for key, value in environ.items():
        if not isinstance(key, str) or not IDENT.fullmatch(key):
            errors.append("Invalid environment variable name")
        if not isinstance(value, str) or not value or "\n" in value or "\r" in value or "{" in value or "}" in value:
            errors.append(f"Invalid environment value for {key}")
        if isinstance(key,str) and SENSITIVE_KEY.search(key):
            errors.append(f"Secret-like environment key {key} cannot be written to a collection")
    if not isinstance(environ.get("baseUrl"), str) or not environ["baseUrl"].startswith(("http://","https://")):
        errors.append("environment.baseUrl must be a declared HTTP(S) target")
    requests = model.get("requests")
    if not isinstance(requests, list) or not requests:
        return {"ok": False, "errors": errors + ["requests must be nonempty array"]}
    seen = set()
    for i, request in enumerate(requests):
        if not isinstance(request, dict):
            errors.append(f"requests[{i}]: expected object")
            continue
        testid = request.get("id")
        refs = request.get("requirements", [])
        if not isinstance(refs, list) or not all(isinstance(v,str) and REQUIREMENT_ID.fullmatch(v) for v in refs):
            errors.append(f"requests[{i}]: invalid requirement reference list")
            refs = []
        elif len(set(refs)) != len(refs):
            errors.append(f"requests[{i}]: duplicate requirement references")
        if evidence_ids is not None:
            for requirement in refs:
                if requirement not in evidence_ids:
                    errors.append(f"requests[{i}]: unresolved evidence requirement {requirement}")
        method = request.get("method")
        path = request.get("path")
        if not isinstance(testid, str) or not TEST_ID.fullmatch(testid):
            errors.append(f"requests[{i}]: invalid test ID")
            continue
        if testid in seen:
            errors.append(f"{testid}: duplicate test ID")
        seen.add(testid)
        if not isinstance(request.get("name"), str) or not NAME.fullmatch(request["name"]):
            errors.append(f"{testid}: invalid test name")
        if not isinstance(method, str) or method not in METHODS:
            errors.append(f"{testid}: invalid HTTP method")
        if not isinstance(path, str) or not path.startswith("/") or path.startswith("//") or "\\" in path or "\r" in path or "\n" in path or "://" in path or ".." in path:
            errors.append(f"{testid}: invalid path")
        else:
            missing = [p for p in PLACEHOLDER.findall(path) if p not in environ]
            if missing:
                errors.append(f"{testid}: undefined path variables: "+",".join(missing))
            if "{" in PLACEHOLDER.sub("",path) or "}" in PLACEHOLDER.sub("",path):
                errors.append(f"{testid}: unsupported variable syntax")
        expected = request.get("expected_status")
        if isinstance(expected, bool) or not isinstance(expected, int) or not (100 <= expected <= 599):
            errors.append(f"{testid}: invalid expected status")
        fields = request.get("expected_json",{})
        if not isinstance(fields, dict):
            errors.append(f"{testid}: expected_json must be an object")
        else:
            for field, value in fields.items():
                if (not isinstance(field, str) or not FIELD.fullmatch(field)
                        or any(segment in FORBIDDEN_PROPERTY for segment in field.split("."))):
                    errors.append(f"{testid}: invalid assertion field")
                if not (value is None or isinstance(value,(str,int,float,bool))):
                    errors.append(f"{testid}: assertion values must be JSON scalars")
        if request.get("auth","none") not in ("none","bearer"):
            errors.append(f"{testid}: auth must be none or bearer")
        headers = request.get("headers",{})
        if not isinstance(headers, dict):
            errors.append(f"{testid}: headers must be an object")
        else:
            for key,value in headers.items():
                if not isinstance(key,str) or not re.fullmatch(r"[A-Za-z0-9-]+",key):
                    errors.append(f"{testid}: invalid header name")
                if not isinstance(value,str) or "\r" in value or "\n" in value or "{" in PLACEHOLDER.sub("",value) or "}" in PLACEHOLDER.sub("",value):
                    errors.append(f"{testid}: invalid header value")
                if isinstance(key,str) and key.lower() in ("authorization","x-api-key"):
                    errors.append(f"{testid}: secrets must be supplied through runtime auth, not persisted headers")
        body = request.get("body_json")
        if body is not None and method not in ("POST","PUT","PATCH","DELETE"):
            errors.append(f"{testid}: GET cannot have JSON body in this generator")
        if body is not None and not isinstance(body,(dict,list)):
            errors.append(f"{testid}: body_json must be an object or array")
    return {"ok": not errors, "errors": sorted(set(errors)),
            "tests": len(seen), "network_requests_sent": 0}


def render_request(request: dict, seq: int) -> str:
    method = request["method"]
    expected = request["expected_status"]
    lines = ["meta {", "  name: "+request["name"], "  type: http",
             "  seq: "+str(seq), "}", "",
             method.lower()+" {",
             "  url: {{baseUrl}}"+request["path"],
             "  body: "+"json" if request.get("body_json") is not None else "  body: none",
             "  auth: "+request.get("auth","none"), "}", ""]
    if request.get("auth")=="bearer":
        lines.extend(["auth:bearer {","  token: {{authToken}}","}",""])
    headers = request.get("headers") or {}
    if headers or request.get("body_json") is not None:
        lines.append("headers {")
        for key, value in sorted(headers.items()):
            lines.append("  "+key+": "+value)
        if request.get("body_json") is not None and not any(k.lower()=="content-type" for k in headers):
            lines.append("  Content-Type: application/json")
        lines.extend(["}",""])
    if request.get("body_json") is not None:
        lines.append("body:json {")
        lines.extend("  "+line for line in json.dumps(request["body_json"],ensure_ascii=False,indent=2).splitlines())
        lines.extend(["}",""])
    lines.extend(["tests {",
                  '  test('+json.dumps(request["id"]+" status",ensure_ascii=False)+', function () {',
                  "    expect(res.getStatus()).to.eql("+str(expected)+");",
                  "  });"])
    for field, value in sorted((request.get("expected_json") or {}).items()):
        expression="res.getBody()"+"".join("["+json.dumps(part)+"]" for part in field.split("."))
        lines.extend(["  test("+json.dumps(request["id"]+" "+field,ensure_ascii=False)+", function () {",
                      "    expect("+expression+").to.deep.equal("+json.dumps(value,ensure_ascii=False,allow_nan=False)+");",
                      "  });"])
    lines.extend(["}",""])
    return "\n".join(lines)


def compile_collection(data: dict, evidence_ids: set[str] | None = None,
                       api_contract: dict | None = None) -> dict[str,str]:
    report=validate(data, evidence_ids=evidence_ids)
    if not report["ok"]:
        raise ValueError("; ".join(report["errors"]))
    if api_contract is not None:
        from audit_api_contract import audit_contract
        check=audit_contract(api_contract,data)
        if not check["ok"]:
            raise ValueError("OpenAPI contract mismatch: "+"; ".join(check["errors"]))
    files: dict[str,str] = {}
    files["bruno.json"]=json.dumps({"version":"1","name":data["name"],"type":"collection",
                                     "ignore":["node_modules",".git"]},ensure_ascii=False,indent=2)+"\n"
    env = ["vars {"]
    for key, value in sorted(data["environment"].items()):
        env.append("  "+key+": "+value)
    env.extend(["}",""])
    files["environments/Mock.bru"]="\n".join(env)
    files["traceability.json"]=json.dumps({
        "format":"angent-ba-api-test-traceability-v1",
        "source_evidence_id_check":"performed" if evidence_ids is not None else "not-performed",
        "execution_status":"not-run",
        "tests":[{"id":request["id"],"requirements":request.get("requirements",[]),
                  "source_link_state":("missing" if not request.get("requirements") else
                                       "ids-resolved-only" if evidence_ids is not None else "not-checked")}
                 for request in data["requests"]]
    },ensure_ascii=False,indent=2)+"\n"
    for i, request in enumerate(data["requests"],1):
        files["requests/"+request["id"]+".bru"]=render_request(request,i)
    return files


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model",type=Path)
    parser.add_argument("--output",required=True,type=Path)
    parser.add_argument("--evidence-graph",type=Path,help="Optional already-inspected BA artifact graph for ID validation")
    parser.add_argument("--openapi",type=Path,help="Optional OpenAPI 3.1 JSON contract; rejects unverified statuses/fields")
    args=parser.parse_args()
    try:
        data=json.loads(args.model.read_text(encoding="utf8"))
        evidence_ids=None
        if args.evidence_graph:
            from validate_artifacts import audit
            graph=json.loads(args.evidence_graph.read_text(encoding="utf8"))
            check=audit(graph)
            if not check["ok"]:
                raise ValueError("Evidence graph invalid: "+"; ".join(check["errors"]))
            evidence_ids={entry["id"] for entry in graph["artifacts"]}
        contract=json.loads(args.openapi.read_text(encoding="utf8")) if args.openapi else None
        generated=compile_collection(data,evidence_ids=evidence_ids,api_contract=contract)
        if args.output.exists() and any(args.output.iterdir()):
            raise ValueError("Output directory must be empty to avoid overwriting existing tests")
        for rel, content in generated.items():
            target=args.output/rel
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(content,encoding="utf8")
    except (ValueError,OSError,TypeError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1
    print(json.dumps({"ok":True,"files":len(generated),"requests":len(data["requests"]),
                      "network_requests_sent":0,"execution_status":"not-run",
                      "contract_check":"checked-subset" if args.openapi else "not-performed",
                      "output":str(args.output)}))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
