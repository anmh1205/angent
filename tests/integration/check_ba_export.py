#!/usr/bin/env python3
"""Generate real MD/HTML/DOCX via local Pandoc and inspect HTML in Chrome."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_export import export

def main()->int:
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument("--chrome",type=Path)
    a.add_argument("--pandoc",default="pandoc")
    args=a.parse_args()
    docs=["docs/atlas-re/atlas-re-urd.md","docs/atlas-re/atlas-re-brd.md","docs/atlas-re/atlas-re-prd.md"]
    source=ROOT/"extensions/angent-ba/examples"
    try:
        from playwright.sync_api import sync_playwright,expect
        with tempfile.TemporaryDirectory() as tmp:
            temp=Path(tmp)
            manifest=[]
            for fmt in ("md","html","docx"):
                data,manifest=export(source,docs,"Atlas decision review",fmt,pandoc=args.pandoc)
                output=temp/("review."+fmt)
                output.write_bytes(data)
                if fmt=="docx":
                    with zipfile.ZipFile(output) as docx:
                        xml=docx.read("word/document.xml").decode("utf8")
                        if "Atlas" not in xml or "Business Objectives" not in xml:
                            raise ValueError("DOCX missing actual business headings")
            with sync_playwright() as p:
                opts={"headless":True}
                if args.chrome:
                    opts["executable_path"]=str(args.chrome)
                browser=p.chromium.launch(**opts)
                try:
                    page=browser.new_page(viewport={"width":390,"height":844})
                    requests=[]
                    errors=[]
                    page.on("request",lambda req:requests.append(req.url) if req.url.startswith(("http://","https://")) else None)
                    page.on("pageerror",lambda e:errors.append(str(e)))
                    page.goto((temp/"review.html").as_uri())
                    expect(page.get_by_role("heading",name="Atlas decision review")).to_be_visible()
                    if "Business Objectives" not in page.locator("body").inner_text():
                        raise ValueError("Business goals missing from rendered stakeholder HTML")
                    if requests or errors:
                        raise ValueError("External requests or script errors: "+str((requests,errors)))
                finally:browser.close()
            return_report={"ok":True,"formats":["md","html","docx"],
                           "source_files":len(manifest),"source_hashes":[m["sha256"][:16] for m in manifest],
                           "read_only_input":True,"chrome_rendered":True,"external_http_requests":0,
                           "pdf":"tested separately with Chromium in check_ba_chromium_pdf.py"}
            print(json.dumps(return_report))
            return 0
    except Exception as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
