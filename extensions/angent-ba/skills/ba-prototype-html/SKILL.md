---
name: ba-prototype-html
description: Business analysis prototype-html specialist.
---

# ANGENT BA: prototype-html

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/prototype-html/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions.


# /prototype-html — Clickable multi-screen prototype

## Goal

Produce ONE self-contained, clickable HTML prototype — `docs/{feature}/html-design/{feature}-prototype.html` — where every navigable control moves the user to its target screen (`#{slug}` anchors), covering all flows. Referenced back from `{feature}-wireframe-index.md` column `HTML prototype` as `{feature}-prototype.html#{slug}`.

## Constraints

- **Group B** (`feature-bootstrap.md`): needs ASCII screens in `ascii-wireframe/{flow-slug}.md` (preferred) OR HTML wireframes — missing both → refuse + route to `/user-flow` + `/wireframe-ascii`.
- **No L3** — HTML; review from the file (L1/L2).
- **Navigation must actually work** — the defining feature: a button whose Description said "Nav → [4]" must jump to `#s4`. Broken/dead links are BLOCKING.
- **Self-contained** — inline CSS + the minimal JS for screen switching (anchor + optional show/hide); no CDN, no build step, double-click to run.
- **One screen = one state** (`ba-conventions.md` §8) — error/empty/loading states are their own screens or clearly toggled views, not a busy combo.
- **Device frame** — inherit from `userflow.md`'s `primary_device` (no re-ask — it's settled); the prototype renders at that width.
- **Idempotent** — re-run → L2 diff (regenerate from current wireframes).
- **Template** — `@./resources/prototype.html`.
- **Index update** — set the `HTML prototype` column in `{feature}-wireframe-index.md`.

## Inputs

```
/prototype-html <feature>          # all flows → one clickable file
```

## Approach

1. **Gate.** No ASCII screens AND no HTML wireframes → refuse + route `/user-flow` + `/wireframe-ascii`. Read the wireframes (content) + `userflow.md` (the navigation edges — what links to what).
2. **Build the nav map** — every control with a `Nav →` in its Description becomes a working link to `#s{n}`; every error-path edge too.
3. **Draft `{feature}-prototype.html`** — all screens as sections (`id="s{n}"`), inline CSS, the minimal JS to switch screens on click; device-width frame; B&W neutral (this is interaction, not visual design).
4. **L1 plan preview** — flow/screen count + nav edges wired + any dead-end found (must be resolved or explicitly an exit).
6. **Index update** — `{feature}-wireframe-index.md` column `HTML prototype` → `{feature}-prototype.html#{slug}` per screen.
7. **Output report** — open path + nav coverage + dead-ends (none expected).

## Gotchas

- **A prototype with broken links is worse than no prototype** — it looks done but misleads; verify every edge before reporting done.
- **Don't add visual polish here** — colors, real typography, images belong to the real frontend or `/figma`; the prototype proves *flow*, not *look*.
- **State screens count** — if the spec has an error state for a form, it's a screen in the prototype, not a hidden assumption.
- **Reuse wireframe content** — drifting from the ASCII/HTML wireframes here means three sources of truth; re-sync instead.
