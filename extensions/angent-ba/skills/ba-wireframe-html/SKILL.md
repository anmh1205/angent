---
name: ba-wireframe-html
description: Business analysis wireframe-html specialist.
---

# ANGENT BA: wireframe-html

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/wireframe-html/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Use the real BA Markdown validator only for completed documents and report the result. For HTML/prototype/API use the actual browser, contract runner or test tool when authorized; generating source is not equivalent to successful execution. Other original Claude-only helper script names describe possible implementations, not installed ANGENT commands.


# /wireframe-html — B&W static HTML wireframes

## Goal

Render each flow as a standalone B&W static HTML file (`docs/{feature}/html-wireframe/{flow-slug}.html`, device-width frames, screens wrap automatically, each screen `id="s{n}"` for deep-linking), plus the **entry point** `docs/{feature}/html-wireframe/{feature}-wireframe.html` (sidebar TOC: flow → screen, an Overview tab that is a clickable flow map, iframes loading each flow) and the metadata index `docs/{feature}/html-wireframe/{feature}-wireframe-html-index.md` (type `wireframe-html-index`).

## Constraints

- **Group B\*** (`feature-bootstrap.md`): `srs/{feature}-userflow.md` (`stage: approved`) missing → refuse + route `/user-flow`. ASCII screens present → reuse their content 1:1 (renderer on par); missing → still works, draws from the userflow directly.
- **No L3** (`approval-gate.md`) — HTML can't render in chat; review from the file in a browser. L1 (create) / L2 (update) only.
- **B&W, no color, no JS for the per-flow files** (`naming-conventions.md` line 50) — pure static; the only JS lives in the entry `{feature}-wireframe.html` (TOC + iframe switching). Light/dark theming is out of scope.
- **Device width = frame width** — mobile 375 / tablet 768 / desktop 1024; `responsive` only if the user chose it AND you emit real breakpoints. Confirm the device (AskUserQuestion, pre-suggest from `primary_device`) — never guess.
- **Renderer on par with `/wireframe-ascii`** — same screens, same `[n]`, same 5-column description intent; the ASCII content is the source of truth, HTML is the fidelity pass.
- **Self-contained** — no CDN, inline CSS; opens by double-click. Each screen `id="s{n}"` matches the ASCII deep-links.
- **Idempotent** — re-run → versioned diff; entry + index regenerated.
- **Validate before done** — BA Markdown validation on the metadata index (step 9).

## Inputs

```
/wireframe-html <feature>                  # all flows, or prompt for one
/wireframe-html <feature> --flow <slug>    # one flow
```

## Approach

1. **Gate.** `userflow.md` (`stage: approved`) missing → refuse + route `/user-flow`. Read it + the ASCII `{flow}.md` if present (content source of truth).
2. **Confirm device** (pre-suggest from `primary_device`).
3. **Per flow → `{flow-slug}.html`** — device-width frame per screen, the controls as neutral B&W boxes/labels, `id="s{n}"`, wrap screens vertically. Reuse ASCII content exactly; this is fidelity, not redesign.
4. **Entry `{feature}-wireframe.html`** (Phase G.5) — sidebar TOC (flow → screen), Overview tab = clickable flow map (anchors to each `id="s{n}"`), iframe loading each flow file. Self-contained.
5. **Index `{feature}-wireframe-html-index.md`** — Flows table (flow / file / screens / device / updated).
6. **scoped change preview** — flows + screens + device + entry created.
9. **Output report** — entry path (double-click to open) + next (`/prototype-html` for click-through, `/figma` to push frames).

## Gotchas

- **Don't redesign in HTML** — if the ASCII and the HTML disagree, the ASCII is right; fix the HTML, never the other way silently.
- **Per-flow files stay JS-free** — the entry file is the only place with JS; mixing JS into per-flow files breaks the "static, opens anywhere" promise.
- **`id="s{n}"` is the deep-link contract** — `/prototype-html` and `/export` anchor to it; don't renumber.
- **B&W is deliberate** — color/branding is a design decision, not a wireframe one; `/figma` or the real frontend owns that.
