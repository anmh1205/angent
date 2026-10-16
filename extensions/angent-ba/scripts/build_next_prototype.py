#!/usr/bin/env python3
"""Build a REAL isolated Next.js App Router mock from an accepted BA screen model.

Produces runnable Next/React sources; does not install packages, contact APIs,
provision accounts, or claim a compiled build without a separate real test.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any
from build_wireframe import check_model

APP_LAYOUT="""import './globals.css';

export const metadata = {
  title: 'ANGENT BA prototype — simulated',
  description: 'Stakeholder mock prototype; no real authentication or APIs'
};

export default function RootLayout({ children }) {
  return <html lang="en"><body>{children}</body></html>;
}
"""
ROOT_PAGE="""import { redirect } from 'next/navigation';
import model from '../model.json';

export default function IndexPage() {
  redirect('/' + encodeURIComponent(model.start));
}
"""
SCREEN_PAGE=r"""'use client';
import { useEffect, useRef, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import model from '../../model.json';

const screens = Object.fromEntries(model.screens.map(item => [item.id, item]));

export default function ScreenPage() {
  const params = useParams();
  const router = useRouter();
  const sid = Array.isArray(params.screen) ? '' : params.screen;
  const screen = Object.hasOwn(screens, sid) ? screens[sid] : null;
  const heading = useRef(null);
  const [scenario, setScenario] = useState(model.scenarios[0]);
  const [message, setMessage] = useState('');

  useEffect(() => {
    setMessage('');
    heading.current?.focus();
  }, [sid]);

  function navigate(target) {
    // Only use validated, predeclared screen IDs; never push arbitrary input.
    if (Object.hasOwn(screens, target)) router.push('/' + encodeURIComponent(target));
  }

  function reset() {
    if (typeof window !== 'undefined') {
      sessionStorage.removeItem('angent-review-demo');
    }
    setScenario(model.scenarios[0]);
    setMessage('');
    navigate(model.start);
  }

  if (!screen) return <main><h1>Unknown prototype screen</h1><button onClick={reset}>Reset demo</button></main>;
  const submit = screen.controls.find(c => c.type === 'submit');

  function onSubmit(event) {
    event.preventDefault();
    if (!submit || !event.currentTarget.reportValidity()) return;
    const result = submit.outcomes[scenario];
    if (!result) return;
    if (result.type === 'error') {
      setMessage(result.message);
      return;
    }
    setMessage('');
    if (typeof window !== 'undefined') {
      // DEMO STATE ONLY. A client-controlled flag is never authorization.
      sessionStorage.setItem('angent-review-demo', 'mock-transition');
    }
    navigate(result.target);
  }

  return (
    <main className="shell">
      <header>
        <h1>{model.title}</h1>
        <p className="notice"><strong>Simulation only.</strong> No real credentials, backend request,
          authorization or account/session token is created. The review flag is client-controlled.
        </p>
        <button type="button" onClick={reset}>Reset demo</button>
      </header>
      <section className="screen" data-screen-id={screen.id}>
        <h2 tabIndex={-1} ref={heading}>{screen.title}</h2>
        <p className="description">{screen.description}</p>
        {submit && (
          <div className="simulation">
            <label htmlFor="mock-scenario">Mock response</label>
            <select id="mock-scenario" value={scenario}
                    onChange={event => setScenario(event.target.value)}>
              {model.scenarios.map(value => <option key={value} value={value}>{value}</option>)}
            </select>
          </div>
        )}
        <form onSubmit={onSubmit}>
          {screen.controls.map(control => {
            const fieldId = screen.id + '-' + control.id;
            if (control.type === 'note') {
              return <p key={control.id} className="note">{control.label}</p>;
            }
            if (control.type === 'button') {
              return <button key={control.id} type="button"
                             onClick={() => navigate(control.action.target)}>{control.label}</button>;
            }
            if (control.type === 'submit') {
              return <button key={control.id} type="submit">{control.label}</button>;
            }
            if (control.type === 'checkbox') {
              return <div key={control.id} className="field">
                <label htmlFor={fieldId}>{control.label}</label>
                <input id={fieldId} type="checkbox" required={Boolean(control.required)} />
              </div>;
            }
            return <div key={control.id} className="field">
              <label htmlFor={fieldId}>{control.label}</label>
              <input id={fieldId} type={control.type} required={Boolean(control.required)}
                     placeholder={control.placeholder || ''} autoComplete="off" />
              {control.requirements?.length > 0 &&
                <p className="source">{control.requirements.join(', ')}</p>}
            </div>;
          })}
        </form>
        {message && <p className="error" role="alert">{message}</p>}
      </section>
    </main>
  );
}
"""
CSS="""*{box-sizing:border-box}body{margin:0;background:#f0f3f5;color:#1d2932;font:16px/1.5 system-ui,sans-serif}
.shell{max-width:960px;margin:auto;padding:2rem}header{padding-bottom:1rem;border-bottom:1px solid #b7c2c8}
h1{font-size:1.6rem}h2{font-size:1.25rem;margin-top:0}p{overflow-wrap:anywhere}
.notice{border:2px dashed #6f7e89;background:white;padding:.9rem;max-width:620px}
.screen{margin:1.3rem 0;padding:1.4rem;border:1px solid #b7c2c8;border-radius:.7rem;background:white;max-width:580px}
label{display:block;font-weight:600;margin:.7rem 0 .25rem}input,select{display:block;width:100%;border:1px solid #697b88;border-radius:.35rem;padding:.65rem;font:inherit}
input[type=checkbox]{width:1.3rem;height:1.3rem}.field{margin:1rem 0}
button{font:inherit;border:1px solid #31444f;background:#fff;padding:.65rem 1rem;border-radius:.35rem;cursor:pointer;margin:.6rem .6rem .2rem 0}
button[type=submit]{background:#263744;color:white}.description,.note{color:#394954}
.source{font-size:.8rem;color:#536675;margin:.1rem 0}.simulation{background:#e7eef2;padding:1rem}
.error{border-left:4px solid #a72a2a;background:#fff3f3;color:#772525;padding:.8rem}
:focus-visible{outline:3px solid #125eaa;outline-offset:3px}
@media(max-width:600px){.shell{padding:.8rem}.screen{padding:1rem}}
"""
README="""# ANGENT BA Next.js review prototype

Generated from a validated source screen model. This is a **mock stakeholder review**, never a production login, API client or authorization implementation.

Requires Node 20.9+ (Next 16). Inside a disposable/authorized working directory:

    npm install
    npm run build
    npm run start

Open localhost:3000; use the Mock response selector and Reset demo. State in sessionStorage is a **client-controlled demo flag only**, not authentication. All screen IDs, labels, branches and requirement references come from model.json. No external APIs or real credentials are used.

Before delivering this prototype, execute a real build and click through normal/error/recovery routes at desktop and mobile sizes, verify keyboard labels and compare the screens with the approved business source. Do not report a build/test result merely because the source files were generated.
"""

def generate_files(model:dict[str,Any])->dict[str,str]:
    report=check_model(model)
    if not report["ok"]:
        raise ValueError("Invalid BA screen model: "+"; ".join(report["errors"]))
    # A real product project may have an entirely different Next/router/components
    # contract. This generator only creates an isolated mock project.
    for screen in model["screens"]:
        for control in screen["controls"]:
            if control.get("type")=="password" and "test_value" in control:
                raise ValueError("Never embed password test values in generated frontend sources")
    package={"name":"angent-ba-next-review","version":"0.0.0","private":True,
             "scripts":{"dev":"next dev","build":"next build","start":"next start"},
             "dependencies":{"next":"16.4.2","react":"19.2.0","react-dom":"19.2.0"}}
    manifest={"type":"angent-ba-next-prototype-v1","execution_status":"not-run",
              "simulation_only":True,"network_api_calls":0,
              "screens":[s["id"] for s in model["screens"]],
              "mock_scenarios":list(model["scenarios"]),
              "limitations":["No real authentication or route security",
                             "No backend API calls, persistent domain entities or OAuth",
                             "Client sessionStorage flag is only a synthetic review state"]}
    return {"package.json":json.dumps(package,indent=2)+"\n",
            "model.json":json.dumps(model,ensure_ascii=False,indent=2)+"\n",
            "review-manifest.json":json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",
            "app/layout.jsx":APP_LAYOUT,
            "app/page.jsx":ROOT_PAGE,
            "app/[screen]/page.jsx":SCREEN_PAGE,
            "app/globals.css":CSS,
            "README.md":README}

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input",type=Path)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    try:
        data=json.loads(a.input.read_text(encoding="utf8"))
        files=generate_files(data)
        if a.output.exists() and any(a.output.iterdir()):
            raise ValueError("Refuse to overwrite a nonempty Next.js project directory")
        for path,body in files.items():
            target=a.output/path
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(body,encoding="utf8")
        print(json.dumps({"ok":True,"output":str(a.output),"files":len(files),
                          "screens":len(data["screens"]),"compile_status":"not-run",
                          "browser_status":"not-run","api_requests_sent":0}))
        return 0
    except (OSError,ValueError,TypeError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
