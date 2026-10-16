#!/usr/bin/env python3
"""Render a verified BA evidence graph as a self-contained, read-only HTML page."""
import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlsplit
from validate_artifacts import audit

def escape(obj):
    return html.escape(str(obj),quote=True)

def safe_link(uri):
    if not isinstance(uri,str):return None
    try:
        parts=urlsplit(uri)
        if parts.scheme in ("https","http") and parts.netloc and not parts.username and not parts.password:
            return uri
    except ValueError:
        pass
    return None

def render(graph,title="BA evidence"):
    report=audit(graph)
    if not report["ok"]:
        raise ValueError("Invalid graph: "+"; ".join(report["errors"]))
    sources={x["id"]:x for x in graph["sources"]}
    cards=[]
    for obj in sorted(graph["artifacts"],key=lambda x:(x.get("kind",""),x["id"])):
        refitems=[]
        for sid in obj.get("source_refs",[]):
            source=sources[sid]
            url=safe_link(source["uri"])
            label=escape(sid+": "+source["uri"])
            refitems.append("<a rel='noopener noreferrer' href='"+escape(url)+"'>"+label+"</a>" if url else label)
        deps=" ".join("<a href='#"+escape(x)+"'>"+escape(x)+"</a>" for x in obj.get("depends_on",[])) or "none"
        status=escape(obj.get("status","unknown"))
        card="<article id='"+escape(obj["id"])+"'><h2>"+escape(obj["id"])+": "+escape(obj["title"])+"</h2>"
        card+="<p><strong>Type:</strong> "+escape(obj["kind"])+"; <strong>Status:</strong> "+status+"</p>"
        card+="<p>"+escape(obj.get("description",""))+"</p><p><strong>Depends on:</strong> "+deps+"</p>"
        card+="<details><summary>Evidence sources ("+str(len(refitems))+")</summary><ul>"
        card+="".join("<li>"+x+"</li>" for x in refitems)+"</ul></details></article>"
        cards.append(card)
    cv=report["coverage"]
    score=str(cv["traced_to_test"])+"/"+str(cv["functional_requirements"]) if cv["functional_requirements"] else "not scoped"
    css="body{max-width:900px;margin:auto;padding:2rem;font:16px/1.65 system-ui}article{border:1px solid #8b9299;border-radius:10px;padding:1rem;margin:1rem 0}a{color:inherit;overflow-wrap:anywhere}summary{cursor:pointer}:focus-visible{outline:3px solid #3663c5}h2{font-size:1.1rem}@media(max-width:600px){body{padding:1rem}}"
    return "<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>"+escape(title)+"</title><style>"+css+"</style></head><body><header><h1>"+escape(title)+"</h1><p>Read-only project evidence index. This HTML does not establish execution or business approval.</p><p>FR to test traceability: "+escape(score)+"</p></header><main>"+"".join(cards)+"</main><footer>Checked structural links only; semantic correctness and live provider status require separate verification.</footer></body></html>"

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input",type=Path)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--title",default="BA evidence")
    a=p.parse_args()
    try:
        graph=json.loads(a.input.read_text(encoding="utf-8"))
        html_text=render(graph,a.title)
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(html_text,encoding="utf-8")
    except (OSError,ValueError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}));return 1
    print(json.dumps({"ok":True,"path":str(a.output),"read_only":True}))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
