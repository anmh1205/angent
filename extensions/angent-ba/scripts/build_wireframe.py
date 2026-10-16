#!/usr/bin/env python3
"""Generate standalone static BA wireframes or explicitly mocked interactive prototypes.

The renderer does not call APIs, authenticate users or persist data. JSON input
is validated before either output; script payload data is escaped.
"""
from __future__ import annotations

import argparse
from collections import deque
import html
import json
from pathlib import Path
import re
from typing import Any

KEY = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,63}$")
INPUTS = {"text", "email", "password", "checkbox"}
TYPES = INPUTS | {"button", "submit", "note"}
ERROR = ("status", "error")


def check_model(data: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict):
        return {"ok": False, "errors": ["Model must be an object"], "warnings": []}
    screens = data.get("screens")
    scenarios = data.get("scenarios")
    start = data.get("start")
    if not isinstance(screens, list) or not screens:
        return {"ok": False, "errors": ["screens must be a nonempty array"], "warnings": []}
    if not isinstance(scenarios, list) or not scenarios or not all(
        isinstance(s, str) and KEY.fullmatch(s) for s in scenarios
    ) or len(set(scenarios)) != len(scenarios):
        errors.append("scenarios must be unique nonempty identifiers")
        scenarios = []
    if not isinstance(data.get("title"), str) or not data["title"].strip():
        errors.append("title must be nonempty")
    by_id: dict[str, dict[str, Any]] = {}
    for index, screen in enumerate(screens):
        if not isinstance(screen, dict):
            errors.append(f"screens[{index}] must be an object")
            continue
        sid = screen.get("id")
        if not isinstance(sid, str) or not KEY.fullmatch(sid):
            errors.append(f"screens[{index}]: invalid screen id")
            continue
        if sid in by_id:
            errors.append(f"screens[{index}]: duplicate screen id {sid}")
            continue
        by_id[sid] = screen
        if not isinstance(screen.get("title"), str) or not screen["title"].strip():
            errors.append(f"{sid}: title required")
        controls = screen.get("controls")
        if not isinstance(controls, list) or not controls:
            errors.append(f"{sid}: controls must be nonempty array")
            continue
        seen = set()
        for j, control in enumerate(controls):
            if not isinstance(control, dict):
                errors.append(f"{sid}.controls[{j}]: not object")
                continue
            cid = control.get("id")
            kind = control.get("type")
            if not isinstance(cid, str) or not KEY.fullmatch(cid):
                errors.append(f"{sid}.controls[{j}]: invalid control id")
                continue
            if cid in seen:
                errors.append(f"{sid}: duplicate control id {cid}")
            seen.add(cid)
            if not isinstance(kind, str) or kind not in TYPES:
                errors.append(f"{sid}.{cid}: unsupported control type")
            if not isinstance(control.get("label"), str) or not control["label"].strip():
                errors.append(f"{sid}.{cid}: missing accessible label")
            refs = control.get("requirements", [])
            if not isinstance(refs, list) or any(not isinstance(r, str) or not r for r in refs):
                errors.append(f"{sid}.{cid}: requirements must be a string list")
            if kind == "button":
                action = control.get("action")
                if not isinstance(action, dict) or action.get("type") != "navigate" or not isinstance(action.get("target"), str):
                    errors.append(f"{sid}.{cid}: button must navigate to an explicit screen")
            if kind == "submit":
                outcomes = control.get("outcomes")
                if not isinstance(outcomes, dict) or not outcomes:
                    errors.append(f"{sid}.{cid}: submit must specify mock outcomes")
                else:
                    if set(outcomes) != set(scenarios):
                        errors.append(f"{sid}.{cid}: outcome keys must match scenarios")
                    for name, outcome in outcomes.items():
                        if not isinstance(outcome, dict) or outcome.get("type") not in ("navigate", "error"):
                            errors.append(f"{sid}.{cid}: invalid outcome {name}")
                        elif outcome["type"] == "navigate" and not isinstance(outcome.get("target"), str):
                            errors.append(f"{sid}.{cid}: missing target for outcome {name}")
                        elif outcome["type"] == "error" and (not isinstance(outcome.get("message"), str) or not outcome["message"].strip()):
                            errors.append(f"{sid}.{cid}: missing error message for {name}")
    if not isinstance(start, str) or start not in by_id:
        errors.append("start must identify a declared screen")
    graph: dict[str, set[str]] = {sid: set() for sid in by_id}
    for sid, screen in by_id.items():
        if not isinstance(screen.get("controls"), list):
            continue
        for control in screen["controls"]:
            if not isinstance(control, dict):
                continue
            targets = []
            if control.get("type") == "button":
                action = control.get("action")
                if isinstance(action, dict):
                    targets.append(action.get("target"))
            if control.get("type") == "submit" and isinstance(control.get("outcomes"), dict):
                for result in control["outcomes"].values():
                    if isinstance(result, dict) and result.get("type") == "navigate":
                        targets.append(result.get("target"))
            for target in targets:
                if target not in by_id:
                    errors.append(f"{sid}.{control.get('id')}: unknown target {target!r}")
                else:
                    graph[sid].add(target)
    if isinstance(start, str) and start in graph:
        queue = deque([start])
        visited = set()
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            queue.extend(graph[current] - visited)
        for sid in sorted(set(by_id) - visited):
            errors.append(f"{sid}: unreachable screen")
    return {"ok": not errors, "errors": sorted(set(errors)),
            "warnings": sorted(set(warnings)), "screens": len(by_id),
            "scenario_count": len(scenarios)}


def e(s: Any) -> str:
    return html.escape(str(s), quote=True)


CSS = """
:root{font-family:system-ui,sans-serif;line-height:1.5;color:#172027;background:#f3f5f6}
*{box-sizing:border-box}
body{margin:0}.shell{max-width:1060px;margin:auto;padding:1.5rem}
header{padding-bottom:1rem;border-bottom:1px solid #c5cdd1;margin-bottom:1.5rem}
h1{font-size:1.4rem}h2{font-size:1.2rem;margin-top:0}
.note{font-size:.87rem;color:#485765}.warning{padding:.85rem;border:2px dashed #60737e;background:white}
.screen{background:white;border:1px solid #a9b6bb;border-radius:.8rem;padding:1.4rem;max-width:520px;margin:1.3rem 0;box-shadow:0 3px 8px #17202711}
label{font-size:.94rem;display:block;margin-top:1rem;font-weight:600}
input{font:inherit;padding:.65rem;width:100%;border:1px solid #60737e;border-radius:.4rem;margin-top:.3rem}
input[type=checkbox]{width:auto;min-width:1.2rem;min-height:1.2rem}
button,select{font:inherit;padding:.65rem;border:1px solid #364854;border-radius:.4rem;background:white;color:#172027;cursor:pointer}
button[type=submit]{background:#172027;color:white}
button{margin:.5rem .5rem .1rem 0}
button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #1269b5;outline-offset:3px}
.small{font-size:.82rem;color:#485765}
.alert{padding:.7rem;border-left:4px solid #ad3030;background:#fff1f1;color:#792525;margin-top:1rem}
.simulation{border:1px solid #74858f;padding:1rem;margin-bottom:1.2rem;background:#e7edf0}
.simulation label{display:inline;margin:0 .6rem 0 0}
.control-ref{font-size:.76rem;color:#50606a}
@media(max-width:600px){.shell{padding:.8rem}.screen{padding:1rem}}
"""

JS = r"""
"use strict";
const model = JSON.parse(document.getElementById("model-json").textContent);
const screens = Object.fromEntries(model.screens.map(s => [s.id, s]));
const app = document.getElementById("app");
const scenario = document.getElementById("scenario");
const mark = (tag, text, cls) => {
  const el = document.createElement(tag);
  if (text !== undefined) el.textContent = String(text);
  if (cls) el.className = cls;
  return el;
};
for (const value of model.scenarios) {
  const option = mark("option", value);
  option.value = value;
  scenario.append(option);
}
function render(id) {
  const screen = screens[id];
  if (!screen) return;
  history.replaceState(null, "", "#" + encodeURIComponent(id));
  const section = mark("section", undefined, "screen");
  section.dataset.screenId = id;
  section.append(mark("h2", screen.title));
  if (screen.description) section.append(mark("p", screen.description, "note"));
  const form = document.createElement("form");
  form.noValidate = false;
  form.addEventListener("submit", event => event.preventDefault());
  const alert = mark("div", "", "alert");
  alert.setAttribute("role", "alert");
  alert.hidden = true;
  for (const ctrl of screen.controls) {
    const key = id + "--" + ctrl.id;
    if (["text","email","password","checkbox"].includes(ctrl.type)) {
      const label = mark("label", ctrl.label);
      label.setAttribute("for", key);
      const input = document.createElement("input");
      input.type = ctrl.type;
      input.id = key;
      input.name = ctrl.id;
      input.required = !!ctrl.required;
      if (ctrl.placeholder && ctrl.type !== "checkbox") input.placeholder = ctrl.placeholder;
      form.append(label, input);
      if (ctrl.requirements && ctrl.requirements.length)
        form.append(mark("p", "Requirements: " + ctrl.requirements.join(", "), "control-ref"));
    } else if (ctrl.type === "note") {
      form.append(mark("p", ctrl.label, "note"));
    } else if (ctrl.type === "button") {
      const btn = mark("button", ctrl.label);
      btn.type = "button";
      btn.addEventListener("click", () => render(ctrl.action.target));
      form.append(btn);
    } else if (ctrl.type === "submit") {
      const btn = mark("button", ctrl.label);
      btn.type = "submit";
      btn.addEventListener("click", event => {
        if (!form.reportValidity()) {
          event.preventDefault();
          return;
        }
        event.preventDefault();
        const outcome = ctrl.outcomes[scenario.value];
        if (outcome.type === "navigate") {
          render(outcome.target);
        } else {
          alert.textContent = outcome.message;
          alert.hidden = false;
        }
      });
      form.append(btn);
    }
  }
  section.append(form, alert);
  app.replaceChildren(section);
}
render(model.start);
"""


def shell(title: str, body: str, *, script: str = "") -> str:
    head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            "<title>" + e(title) + "</title><style>" + CSS + "</style></head>")
    return head + '<body><div class="shell">' + body + "</div>" + script + "</body></html>"


def render(data: dict[str, Any], mode: str) -> str:
    result = check_model(data)
    if not result["ok"]:
        raise ValueError("; ".join(result["errors"]))
    title = data["title"]
    notice = '<p class="warning">BA design review only. All responses are simulated; no identity checks, API calls or data persistence.</p>'
    if mode == "wireframe":
        sections = []
        for screen in data["screens"]:
            controls = []
            for c in screen["controls"]:
                label = e(c["label"])
                refs = ", ".join(c.get("requirements", []))
                if c["type"] in INPUTS:
                    controls.append("<label>" + label + "<input type='" + e(c["type"]) +
                                    "' placeholder='" + e(c.get("placeholder", "")) + "' disabled></label>")
                else:
                    controls.append("<p><strong>" + e(c["type"]) + ":</strong> " + label + "</p>")
                if refs:
                    controls.append('<p class="control-ref">Requirements: ' + e(refs) + "</p>")
            sections.append('<section class="screen" id="' + e(screen["id"]) + '"><h2>' +
                            e(screen["title"]) + '</h2><p class="note">' +
                            e(screen.get("description", "")) + "</p>" +
                            "".join(controls) + "</section>")
        return shell(title, "<header><h1>" + e(title) + "</h1>" + notice +
                     "</header><main>" + "".join(sections) + "</main>")
    if mode != "prototype":
        raise ValueError("Mode must be wireframe or prototype")
    data_json = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    data_json = data_json.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    main = ("<header><h1>" + e(title) + "</h1>" + notice + "</header>"
            '<aside class="simulation"><label for="scenario">Mock response</label>'
            '<select id="scenario" aria-label="Mock response"></select>'
            '<p class="small">Select an artificial response, then submit the form. No real credentials are checked.</p></aside>'
            '<main id="app" aria-live="polite"></main>')
    script = '<script type="application/json" id="model-json">' + data_json + "</script>" + "<script>" + JS + "</script>"
    return shell(title, main, script=script)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("--mode", choices=("wireframe", "prototype"), required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.model.read_text(encoding="utf-8"))
        page = render(data, args.mode)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(page, encoding="utf-8")
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1
    print(json.dumps({"ok": True, "output": str(args.output),
                      "mode": args.mode, "writes_to_backend": False,
                      "requires_browser_review": True}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
