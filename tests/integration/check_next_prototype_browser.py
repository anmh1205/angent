#!/usr/bin/env python3
"""Browser acceptance for actual built Next.js App Router BA mock.

Uses an isolated installed/build project; no cloud deployment or real auth.
Optional --project points at a separately generated/built test project (this
script reads it but never rewrites source or installs dependencies there).
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
from urllib.parse import urlsplit
from urllib.request import urlopen

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_next_prototype import generate_files

def _assert_generated_project(project:Path, model:dict)->None:
    if not (project/".next").is_dir() or not (project/"node_modules/next").is_dir():
        raise ValueError("No actual installed and built Next.js project at "+str(project))
    expected=generate_files(model)
    for name in ("model.json","app/[screen]/page.jsx","review-manifest.json"):
        candidate=project/name
        if not candidate.is_file() or candidate.read_text(encoding="utf8")!=expected[name]:
            raise ValueError("Project source does not match current generator: "+name)

def _create_and_build(model:dict,folder:Path)->None:
    for name,source in generate_files(model).items():
        file=folder/name
        file.parent.mkdir(parents=True,exist_ok=True)
        file.write_text(source,encoding="utf8")
    npm="npm.cmd" if os.name=="nt" else "npm"
    for args in ([npm,"install","--no-audit","--no-fund"],[npm,"run","build"]):
        process=subprocess.run(args,cwd=folder,capture_output=True,text=True,errors="replace",timeout=210)
        if process.returncode:
            raise ValueError("Next install/build failed: "+str(args)+"\n"+
                             (process.stdout+process.stderr)[-1400:])

def _free_port()->int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1",0))
        return int(sock.getsockname()[1])

def _test_browser(url:str,chrome:Path|None)->dict:
    from playwright.sync_api import sync_playwright,expect
    seen=[]
    page_errors=[]
    with sync_playwright() as play:
        config={"headless":True}
        if chrome: config["executable_path"]=str(chrome)
        browser=play.chromium.launch(**config)
        try:
            for width,height in ((390,844),(1366,850)):
                page=browser.new_page(viewport={"width":width,"height":height})
                def protect(route):
                    parsed=urlsplit(route.request.url)
                    if parsed.hostname not in ("127.0.0.1","localhost"):
                        seen.append(route.request.url)
                        route.abort()
                    else:
                        route.continue_()
                page.route("**/*",protect)
                page.on("pageerror",lambda e:page_errors.append(str(e)))
                try:
                    response=page.goto(url,wait_until="networkidle")
                    if response is None:
                        raise AssertionError("No real Next.js HTTP response")
                    expect(page.locator('[data-screen-id="login"]')).to_have_count(1)
                    expect(page.get_by_text("Simulation only.",exact=False)).to_be_visible()
                    page.get_by_role("button",name="Sign in",exact=True).click()
                    expect(page.get_by_label("Email address")).to_have_attribute("required","")
                    expect(page.locator('[data-screen-id="login"]')).to_have_count(1)
                    page.get_by_label("Email address").fill("not-an-email")
                    page.get_by_label("Password").fill("fixture-password")
                    page.get_by_role("button",name="Sign in",exact=True).click()
                    assert page.get_by_label("Email address").evaluate("(e)=>e.validity.typeMismatch")
                    page.get_by_label("Email address").fill("test@example.test")
                    for state,expected in (
                        ("invalid","Invalid credentials (mock)."),
                        ("locked","Account temporarily locked (mock)."),
                        ("offline","Network unavailable — try again (mock).")
                    ):
                        page.get_by_label("Mock response").select_option(state)
                        page.get_by_role("button",name="Sign in",exact=True).click()
                        expect(page.locator(".screen [role=alert]")).to_have_text(expected)
                    page.get_by_label("Mock response").select_option("success")
                    page.get_by_role("button",name="Sign in",exact=True).click()
                    expect(page.locator('[data-screen-id="home"]')).to_have_count(1)
                    expect(page.locator("h2")).to_be_focused()
                    expect(page.get_by_text("Mock sign-in succeeded; no authentication token was issued.")).to_be_visible()
                    page.get_by_role("button",name="Return to sign in").click()
                    expect(page.locator('[data-screen-id="login"]')).to_have_count(1)
                    page.get_by_role("button",name="Forgot password").click()
                    expect(page.locator('[data-screen-id="recovery"]')).to_have_count(1)
                    expect(page.locator("h2")).to_be_focused()
                    page.get_by_role("button",name="Reset demo").click()
                    expect(page.locator('[data-screen-id="login"]')).to_have_count(1)
                    expect(page.locator("h2")).to_be_focused()
                    assert not page_errors,page_errors
                    # Check that layout does not leak horizontally at viewport.
                    dimensions=page.evaluate("({doc:document.documentElement.scrollWidth, viewport:window.innerWidth})")
                    if dimensions["doc"]>dimensions["viewport"]+1:
                        raise AssertionError("Horizontal clipping at "+str(width)+": "+str(dimensions))
                finally:
                    page.close()
        finally:
            browser.close()
    if seen:
        raise ValueError("Unexpected external browser network request: "+str(seen[:4]))
    return {"ok":True,"viewports":["390x844","1366x850"],
            "mock_scenarios":["invalid","locked","offline","success"],
            "navigation":["login","home","recovery","reset"],
            "format_and_required_validation":True,"external_http_requests":0,
            "browser_errors":page_errors}

def smoke(project:Path,chrome:Path|None,model:dict)->dict:
    _assert_generated_project(project,model)
    port=_free_port()
    node="node.exe" if os.name=="nt" else "node"
    binary=project/"node_modules/next/dist/bin/next"
    command=[node,str(binary),"start","-p",str(port),"-H","127.0.0.1"]
    flags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name=="nt" else 0
    process=subprocess.Popen(command,cwd=project,stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,
                             creationflags=flags)
    try:
        endpoint="http://127.0.0.1:"+str(port)
        ready=False
        for _ in range(80):
            if process.poll() is not None:
                raise ValueError("Next.js server exited before becoming ready")
            try:
                with urlopen(endpoint,timeout=1) as res:
                    ready=res.status in (200,307,308)
                    if ready:break
            except OSError:
                pass
            time.sleep(.25)
        if not ready:
            raise ValueError("Next.js localhost server never became ready")
        details=_test_browser(endpoint,chrome)
        details.update({"real_next_server":True,"runtime":"Next App Router production build",
                        "backend_api_calls_claimed":0,"writes_to_figma":False})
        return details
    finally:
        process.terminate()
        try:
            process.wait(timeout=7)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--project",type=Path,help="Preinstalled and production-built generated project")
    p.add_argument("--chrome",type=Path,help="Real Chrome/Chromium executable")
    args=p.parse_args()
    model=json.loads((ROOT/"extensions/angent-ba/examples/authentication-screen-model.json").read_text(encoding="utf8"))
    tmp=None
    try:
        if args.project:
            project=args.project.resolve()
        else:
            tmp=tempfile.TemporaryDirectory()
            project=Path(tmp.name)
            _create_and_build(model,project)
        result=smoke(project,args.chrome,model)
    except Exception as exc:
        result={"ok":False,"error":str(exc)[:1800]}
    finally:
        if tmp:tmp.cleanup()
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result["ok"] else 1

if __name__=="__main__":
    raise SystemExit(main())
