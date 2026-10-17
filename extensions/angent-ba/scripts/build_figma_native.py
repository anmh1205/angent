#!/usr/bin/env python3
"""Generate source-bound native Figma Plugin API code, without touching Figma.

The output is executed only later by an authorized native Figma host. It is
NOT interchangeable with Reqwise's proprietary figma.create() sandbox proxy.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any
from build_figma_screens import compile_screens

TEMPLATE = Path(__file__).resolve().parents[1] / "templates/figma-native-plugin.js"
MARKER = "__ANGENT_SCREEN_SPEC_JSON__"

def files(model: dict[str, Any], evidence_ids: set[str] | None = None) -> dict[str, str]:
    plan = compile_screens(model, evidence_ids=evidence_ids)
    screen_specs = [
        {"id":s["source_id"], "name":s["figma_tree"]["name"],
         "title":s["source_name"],
         "controls":[{"id":c["id"], "type":c["type"], "label":c["label"]}
                     for c in s["controls"]]}
        for s in plan["screens"]
    ]
    template = TEMPLATE.read_text(encoding="utf8")
    if template.count(MARKER) != 2:
        raise ValueError("Native Figma template marker count mismatch")
    # First marker is the literal mention in comment. Replace only the source.
    source = template.replace("= " + MARKER + ";",
                              "= " + json.dumps(screen_specs, ensure_ascii=True, separators=(",", ":")) + ";")
    if "= " + MARKER + ";" in source:
        raise ValueError("Native Figma template placeholder was not substituted")
    return {
        "figma-native-plan.json":json.dumps(plan, ensure_ascii=False, indent=2) + "\n",
        "figma-native-plugin.js":source
    }

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("model",type=Path)
    p.add_argument("--output",required=True,type=Path)
    p.add_argument("--evidence-graph",type=Path)
    args=p.parse_args()
    try:
        model=json.loads(args.model.read_text(encoding="utf8"))
        ids=None
        if args.evidence_graph:
            from validate_artifacts import audit
            graph=json.loads(args.evidence_graph.read_text(encoding="utf8"))
            result=audit(graph)
            if not result["ok"]:
                raise ValueError("Evidence graph invalid: " + "; ".join(result["errors"]))
            ids={node["id"] for node in graph["artifacts"]}
        generated=files(model, ids)
        if args.output.exists() and any(args.output.iterdir()):
            raise ValueError("Refusing to overwrite an existing native Figma handoff")
        args.output.mkdir(parents=True,exist_ok=True)
        for path,content in generated.items():
            (args.output/path).write_text(content, encoding="utf8")
        print(json.dumps({"ok":True,"outputs":list(generated),"screens":len(model["screens"]),
                          "writes_performed":False,"native_runtime":"not-run",
                          "evidence_check":"ids-resolved-only" if ids is not None else "not-performed"}))
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
