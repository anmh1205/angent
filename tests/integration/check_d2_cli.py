#!/usr/bin/env python3
"""Real D2 0.9+ CLI smoke for activity, ERD and logical architecture.

All source models are synthetic. Generated files are isolated, no external
services or user projects are mutated. Renderer failure is a test failure.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_d2 import compile_source, render_svg, validate

SVG="{http://www.w3.org/2000/svg}"

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--d2",default="d2",help="Path to D2 CLI")
    p.add_argument("--keep",type=Path,help="Optional output directory; must be empty")
    args=p.parse_args()
    temp=None
    if args.keep is None:
        temp=tempfile.TemporaryDirectory()
        target=Path(temp.name)
    else:
        target=args.keep
        if target.exists() and any(target.iterdir()):
            print(json.dumps({"ok":False,"error":"Output directory must be empty"}))
            return 1
        target.mkdir(parents=True,exist_ok=True)
    try:
        reports=[]
        for kind in ("activity","erd","architecture"):
            source=ROOT/"extensions/angent-ba/examples"/f"d2-{kind}.json"
            data=json.loads(source.read_text(encoding="utf8"))
            check=validate(data)
            if not check["ok"]:
                raise ValueError(kind+" invalid: "+"; ".join(check["errors"]))
            d2file=target/(kind+".d2")
            d2file.write_text(compile_source(data),encoding="utf8")
            svgfile=target/(kind+".svg")
            render=render_svg(d2file,svgfile,args.d2)
            if not render["ok"]:
                raise ValueError(kind+" failed D2 CLI: "+str(render))
            root=ET.parse(svgfile).getroot()
            viewbox=root.attrib.get("viewBox","")
            items=[float(x) for x in viewbox.replace(","," ").split()]
            if len(items)!=4 or items[2]<=100 or items[3]<=100:
                raise ValueError(kind+": blank/invalid SVG viewBox")
            texts=["".join(node.itertext()) for node in root.iter(SVG+"text")]
            if len(texts)<len(data["nodes"]):
                raise ValueError(kind+": too few label text nodes in rendered SVG")
            expected=[n["label"] for n in data["nodes"]]
            for label in expected:
                if not any(label in value for value in texts):
                    raise ValueError(kind+": missing rendered label "+label)
            for field in ("script","foreignObject"):
                if list(root.iter(SVG+field)):
                    raise ValueError(kind+": unexpected active SVG element "+field)
            reports.append({"diagram":kind,"nodes":len(data["nodes"]),"edges":len(data["edges"]),
                            "svg_bytes":svgfile.stat().st_size,"viewBox":viewbox,"labels_verified":len(expected)})
        print(json.dumps({"ok":True,"renderer":"D2 CLI","diagrams":reports,"runtime_verified":True},ensure_ascii=False))
        return 0
    except (OSError,ValueError,ET.ParseError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1
    finally:
        if temp is not None:
            temp.cleanup()

if __name__=="__main__":
    raise SystemExit(main())
