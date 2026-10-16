#!/usr/bin/env python3
"""Run real Chrome interactions for the standalone prototype; requires Playwright.

Only a fixture is tested; it deliberately sends no authentication/API traffic.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_wireframe import render

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chrome",type=Path,default=None)
    parser.add_argument("--screenshot-dir",type=Path,default=None)
    args=parser.parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(json.dumps({"ok":False,"error":"playwright not installed; browser test NOT RUN"}))
        return 2
    model=json.loads((ROOT/"extensions/angent-ba/examples/authentication-screen-model.json").read_text(encoding="utf8"))
    if args.screenshot_dir:
        args.screenshot_dir.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        output=Path(tmp)/"authentication.html"
        output.write_text(render(model,"prototype"),encoding="utf8")
        with sync_playwright() as p:
            kwargs={"headless":True}
            if args.chrome:
                kwargs["executable_path"]=str(args.chrome)
            browser=p.chromium.launch(**kwargs)
            page=browser.new_page(viewport={"width":390,"height":844})
            errors=[]
            external_requests=[]
            page.on("pageerror",lambda err:errors.append(str(err)))
            page.on("request",lambda req:external_requests.append(req.url) if req.url.startswith(("https:","http:")) else None)
            page.goto(output.as_uri())
            assert page.locator('[data-screen-id="login"]').count()==1,"Initial login screen absent"
            assert page.get_by_label("Email address").count()==1
            assert page.get_by_label("Password").count()==1
            # Required-field validation: no submission without accepted inputs.
            page.get_by_role("button",name="Sign in").click()
            assert page.locator('[data-screen-id="login"]').count()==1
            assert page.get_by_label("Email address").evaluate("(el)=>el.validity.valueMissing")
            page.get_by_label("Email address").fill("tester@example.test")
            page.get_by_label("Password").fill("not-a-real-password")
            outcomes={"invalid":"Invalid credentials (mock).",
                      "locked":"Account temporarily locked (mock).",
                      "offline":"Network unavailable — try again (mock)."}
            for scenario,message in outcomes.items():
                page.get_by_label("Mock response").select_option(scenario)
                page.get_by_role("button",name="Sign in").click()
                assert page.get_by_role("alert").inner_text()==message,(scenario,page.get_by_role("alert").inner_text())
                assert page.locator('[data-screen-id="login"]').count()==1
            page.get_by_label("Mock response").select_option("success")
            page.get_by_role("button",name="Sign in").click()
            assert page.locator('[data-screen-id="home"]').count()==1
            assert "no authentication token" in page.locator("#app").inner_text()
            if args.screenshot_dir:
                page.screenshot(path=str(args.screenshot_dir/"authenticated-mock.png"))
            page.get_by_role("button",name="Return to sign in").click()
            page.get_by_role("button",name="Forgot password").click()
            assert page.locator('[data-screen-id="recovery"]').count()==1
            assert page.get_by_label("Recovery email").count()==1
            page.get_by_role("button",name="Return to sign in").click()
            assert page.locator('[data-screen-id="login"]').count()==1
            assert not external_requests,external_requests
            assert not errors,errors
            # Injection text from the source JSON remains data, never executable JS.
            model["screens"][0]["title"]='</script><script>window.__executed=true</script>'
            attack=Path(tmp)/"injection.html"
            attack.write_text(render(model,"prototype"),encoding="utf8")
            page.goto(attack.as_uri())
            assert page.locator('[data-screen-id="login"]').count()==1
            assert page.evaluate("() => window.__executed === undefined")
            assert not errors,errors
            browser.close()
    print(json.dumps({"ok":True,"engine":"Chrome/Playwright",
                      "tested":["required validation","invalid","locked","offline","success",
                                "home navigation","recovery navigation","no external requests","HTML injection"],
                      "authentication_calls":0,"screenshots":str(args.screenshot_dir) if args.screenshot_dir else None}))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
