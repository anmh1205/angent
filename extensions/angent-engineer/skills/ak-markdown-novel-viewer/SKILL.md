---
name: ak-markdown-novel-viewer
description: Read long Markdown and plan directories through a trusted localhost browser reader with outline, Mermaid and safe file/server boundaries.
metadata: {port: angent-fallback, mode: degraded}
---

# Markdown Novel Viewer — Portable Fallback

Stable Engineer 2.19.0 Markdown Novel Viewer is **a Node-powered local HTTP reader**, not just a Markdown-to-HTML conversion. It includes a file/directory browser, chapter navigation, a calm typography theme, Mermaid support, plan navigation, keyboard shortcuts, responsive display, process management and multiple server helpers/tests. These scripts/runtime are not copied into this fallback.

## Native preflight

Inspect the installed skill's package scripts, dependencies and `package.json`; if available, follow actual CLI help. Stable source options include `--file`, `--dir`, `--port` (source default 3456), `--host` (prefer localhost), `--open`, `--background` and `--stop`. Server lifecycle/start/stop and package installation are **real process effects**; do not run them under a read-only or output-only request without permission.

## Safe reader

- Resolve the selected Markdown file or directory under an approved source root. Directory navigation and the source's `/view?file=...` route require careful path canonicalization to prevent path traversal, symlink escape and exposure of private files outside the allowed root.
- Default bind to `127.0.0.1`; do not expose `0.0.0.0` or tunnel a private document to the internet as a convenience.
- Render Markdown semantics faithfully: prose/heading hierarchy, tables, fenced code, links, images, Mermaid as supported by the actual renderer, and plan/phase navigation where available. Avoid executing untrusted scripts/inline HTML from source text.
- Use a readable line length, responsive font/spacing, keyboard navigation and high-contrast light/dark themes. Preserve source as read-only, unless an explicit editor was requested.
- If automatic reload/background lifecycle is requested, verify the server PID and stop mechanism; never claim it exists based on a browser tab.

## Portable rendering

If native Node viewer is absent, use a real Markdown renderer/document preview with direct file or restricted local HTML output. This can meet the reading goal but is **not** the full package's HTTP routes, live reload, directory browser, Mermaid parser and navigation parity.

Inspect the final display when the host can view it; show exact accessible URL/file only after it exists. Do not claim private-source protection merely because the browser is on localhost.

**Capability:** VERIFIED_DEGRADED until a real viewer/runtime is available and exercised.
