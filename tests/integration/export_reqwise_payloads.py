#!/usr/bin/env python3
"""Export all six ANGENT/Reqwise OSS examples for live upstream schema verification."""
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
FIGMA=ROOT/"extensions/angent-figma"
sys.path.insert(0,str(FIGMA/"scripts"))
from to_reqwise_payload import compile_model

def export():
    payloads=[]
    for kind in ("activity","sequence","state","erd","userflow","sitemap"):
        name="rental-fleet-"+kind+".json"
        model=json.loads((FIGMA/"examples"/name).read_text(encoding="utf-8"))
        value=compile_model(model)
        if value["arguments"]["type"] != kind or not value["arguments"]["spec"]["options"]["dryRun"]:
            raise ValueError("Unsafe or mismatched payload "+kind)
        payloads.append(value)
    return payloads

if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("Usage: python tests/integration/export_reqwise_payloads.py out.json")
    path=Path(sys.argv[1])
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(export(),ensure_ascii=False,indent=2),encoding="utf-8")
    print("Exported six dry-run payloads:",path)
