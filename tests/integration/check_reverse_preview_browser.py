#!/usr/bin/env python3
"""Read a generated reverse evidence preview in real Chrome; no external requests."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from render_reverse_preview import render

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--chrome",type=Path)
    a=p.parse_args()
    try:
        from playwright.sync_api import sync_playwright,expect
    except ImportError:
        print(json.dumps({"ok":False,"error":"Real Playwright browser not installed","executed":False}))
        return 2
    model=json.loads((ROOT/"extensions/angent-ba/examples/reverse-evidence-synthetic.json").read_text(encoding="utf8"))
    with tempfile.TemporaryDirectory() as tmp:
        output=Path(tmp)/"reverse-evidence.html"
        output.write_text(render(model),encoding="utf8")
        with sync_playwright() as p:
            kwargs={"headless":True}
            if a.chrome:kwargs["executable_path"]=str(a.chrome)
            browser=p.chromium.launch(**kwargs)
            try:
                page=browser.new_page(viewport={"width":390,"height":844})
                outbound=[]
                errors=[]
                page.on("request",lambda req: outbound.append(req.url) if req.url.startswith(("http://","https://")) else None)
                page.on("pageerror",lambda err:errors.append(str(err)))
                page.goto(output.as_uri())
                expect(page.locator("article")).to_have_count(3)
                expect(page.get_by_role("navigation",name="Evidence claims")).to_be_visible()
                expect(page.get_by_text("Archived document says 404, current code path emits 403")).to_be_visible()
                page.get_by_role("link",name="RCL-003: CONTRADICTORY").click()
                if not page.url.endswith("#RCL-003"):
                    raise ValueError("Evidence navigation anchor did not resolve")
                good=not outbound and not errors
                print(json.dumps({"ok":good,"rendered":True,"claims":3,
                                  "external_requests":outbound,"javascript_errors":errors,
                                  "source_content_is_synthetic":True},ensure_ascii=False))
                return 0 if good else 1
            finally:
                browser.close()

if __name__=="__main__":
    raise SystemExit(main())
