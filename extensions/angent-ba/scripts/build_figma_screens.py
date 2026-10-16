#!/usr/bin/env python3
"""Convert accepted BA screen models to editable Reqwise figma_write node trees.

Output is a dry-run source file, NOT a Figma write. Requires an authorized,
connected Reqwise OSS server/plugin to execute and independently read back.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any
from build_wireframe import check_model

CONTROL_FIELD={"email":"Email input","text":"Text input","password":"Password input",
               "checkbox":"Checkbox","note":"Note","submit":"Submit","button":"Button"}

def _text(name:str,content:str,size:int=14)->dict:
    return {"type":"TEXT","name":name,"characters":content,"fontSize":size}

def _control(control:dict)->dict:
    kind=control["type"]
    label=control["label"]
    cid=control["id"]
    flags=[]
    if control.get("required"):flags.append("required")
    if kind in ("email","password","text"):
        flags.append(CONTROL_FIELD[kind])
        # No test values, credentials, or actual input contents enter Figma.
        children=[_text("label:"+cid,label)]
        children.append({"type":"FRAME","name":"input-outline:"+cid,
                         "height":42,"width":330,"fill":"#ffffff",
                         "stroke":"#637482","cornerRadius":6})
        if control.get("placeholder") and kind!="password":
            children.append(_text("placeholder:"+cid,control["placeholder"],12))
    elif kind=="checkbox":
        children=[_text("label:"+cid,("☐ "+label))]
    else:
        children=[_text("label:"+cid,label)]
    return {"type":"FRAME","name":"control:"+kind+":"+cid,
            "layoutMode":"VERTICAL","itemSpacing":6,
            "padding":8,"width":350,
            "fill":"#f3f5f7" if kind in ("submit","button") else "#ffffff",
            "children":children}

def compile_screens(model:Any)->dict[str,Any]:
    checked=check_model(model)
    if not checked["ok"]:
        raise ValueError("Invalid BA screen model: "+"; ".join(checked["errors"]))
    screens=[]
    for screen in model["screens"]:
        sid=screen["id"]
        controls=screen["controls"]
        name="ANGENT BA / "+sid+" / "+screen["title"]
        children=[_text("screen:title",screen["title"],20)]
        if screen.get("description"):
            children.append(_text("screen:description",screen["description"],13))
        for control in controls:
            children.append(_control(control))
        names=["control:"+x["type"]+":"+x["id"] for x in controls]
        screens.append({
            "source_id":sid,
            "source_name":screen["title"],
            "controls":[{"id":x["id"],"type":x["type"],"label":x["label"],
                         "requirements":x.get("requirements",[]),
                         "action":x.get("action"),
                         "outcomes":x.get("outcomes")}
                        for x in controls],
            "figma_tree":{"type":"FRAME","name":name,"width":390,
                          "layoutMode":"VERTICAL","padding":20,"itemSpacing":12,
                          "fill":"#ffffff","children":children},
            "expected_figma_nodes":{"root_name":name,"control_names":names},
        })
    return {"format":"angent-ba-figma-screen-tree-v1","scope":"editable source-screen low-fidelity frames",
            "runtime_status":"not-run","writes_performed":False,
            "sources":{"model_title":model["title"],"screen_count":len(screens)},
            "screens":screens,
            "limitations":["No real canvas edit or Figma URL until native provider call and read-back",
                           "Frames are editable visuals, not wired prototype reactions or functioning forms",
                           "Original source control behavior is metadata; text-only controls are not functional",
                           "No existing frame update/idempotent merge without provider identity/revision"]}

def generate_js(compiled:dict[str,Any])->str:
    # JS is for the Reqwise OSS figma_write sandbox, NOT official Figma Plugin API.
    data=[{"id":item["source_id"],"tree":item["figma_tree"],
           "expected":item["expected_figma_nodes"]} for item in compiled["screens"]]
    literal=json.dumps(data,ensure_ascii=True,separators=(",",":"))
    return """// ANGENT BA candidate for Reqwise figma_write({code}).
// CALL ONLY AFTER root/provider authorization, figma_status and figma_rules.
// A rerun can create duplicates: first compare existing frame node IDs.
// This is NOT a Figma plugin source file or a standalone Node.js program.
const planned = """+literal+""";
const output = [];
for (const item of planned) {
  // figma.create is the documented Reqwise sandbox proxy operation.
  const result = await figma.create(item.tree);
  if (!result || !result.id) {
    console.log(JSON.stringify({ok:false,writes:output,error:"Missing Figma node ID"}));
    throw new Error("Figma create response missing node ID");
  }
  output.push({source_screen_id:item.id,figma_node_id:result.id,
               expected_root_name:item.expected.root_name,
               expected_controls:item.expected.control_names});
}
console.log(JSON.stringify({ok:true,writes:output,
  status:"WRITE_REQUESTED_NOT_YET_READ_BACK",
  next:"figma_read get_nodes + layout_audit + screenshot; compare labels"}));
"""

def files(model:dict[str,Any])->dict[str,str]:
    compiled=compile_screens(model)
    return {"figma-screen-plan.json":json.dumps(compiled,ensure_ascii=False,indent=2)+"\n",
            "figma-write.js":generate_js(compiled)}

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input",type=Path)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    try:
        input_model=json.loads(args.input.read_text(encoding="utf8"))
        outputs=files(input_model)
        if args.output.exists() and any(args.output.iterdir()):
            raise ValueError("Refusing to overwrite existing output directory")
        args.output.mkdir(parents=True,exist_ok=True)
        for name,body in outputs.items():
            (args.output/name).write_text(body,encoding="utf8")
        plan=json.loads(outputs["figma-screen-plan.json"])
        print(json.dumps({"ok":True,"screens":len(plan["screens"]),
                          "controls":sum(len(x["controls"]) for x in plan["screens"]),
                          "files":list(outputs),
                          "provider_writes":0,"runtime_status":"not-run"},ensure_ascii=False))
        return 0
    except (OSError,TypeError,ValueError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)},ensure_ascii=False))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
