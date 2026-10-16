#!/usr/bin/env python3
"""Check BA BPMN exports against official OMG BPMN 2.0.2 normative XSDs.

Supply original official BPMN20, Semantic, BPMNDI, DC, DI XSDs from
https://www.omg.org/spec/BPMN/2.0.2/ in one local directory.
Optional lxml is required ONLY for this integration test.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_bpmn import compile_bpmn,audit_ir,BPMN


def check(schema_dir:Path)->dict:
    required=("BPMN20.xsd","Semantic.xsd","BPMNDI.xsd","DC.xsd","DI.xsd")
    missing=[name for name in required if not (schema_dir/name).is_file()]
    if missing:
        raise ValueError("Missing OMG XSD files: "+", ".join(missing))
    try:
        from lxml import etree
    except ImportError as exc:
        raise ValueError("lxml package required for actual XSD validation") from exc
    parser=etree.XMLParser(resolve_entities=False,no_network=True)
    schema=etree.XMLSchema(etree.parse(str(schema_dir/"BPMN20.xsd"),parser))
    model=json.loads((ROOT/"extensions/angent-ba/examples/atlas-re/bpmn/claim-approval.ir.json").read_text(encoding="utf8"))
    semantic=audit_ir(model)
    if not semantic["ok"]:
        raise ValueError("BA BPMN IR invalid: "+"; ".join(semantic["errors"]))
    result=compile_bpmn(model)
    parsed=etree.fromstring(result,parser=parser)
    if not schema.validate(parsed):
        raise ValueError("Official OMG 2.0.2 validation failed: "+str(schema.error_log)[:2000])
    broken=etree.fromstring(result,parser=parser)
    first=broken.find(".//{"+BPMN+"}sequenceFlow")
    if first is None or "sourceRef" not in first.attrib:
        raise ValueError("Expected sequenceFlow sourceRef")
    del first.attrib["sourceRef"]
    mutation_caught=not schema.validate(broken)
    if not mutation_caught:
        raise ValueError("Official OMG XSD failed to reject a missing sequenceFlow sourceRef")
    return {"ok":True,"schema":"OMG BPMN 2.0.2 normative local files",
            "source":"synthetic Atlas claim-approval","generated_bytes":len(result),
            "nodes":semantic["node_count"],"flows":semantic["flow_count"],
            "mutation_caught":mutation_caught,
            "engine_executable":False,"external_modeler_import_checked":False,
            "network_requests_sent":0}


def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--schema-dir",required=True,type=Path)
    args=p.parse_args()
    try:
        result=check(args.schema_dir.resolve())
    except Exception as exc:
        # Missing external schema files and XML parse failures are failures,
        # never silent skips or invented successful validation.
        result={"ok":False,"error":str(exc)}
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result["ok"] else 1

if __name__=="__main__":
    raise SystemExit(main())
