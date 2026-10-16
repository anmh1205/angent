---
name: ba-figma
description: Business analysis figma specialist.
---

# ANGENT BA: figma

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/figma/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Use the real BA Markdown validator only for completed documents and report the result. For HTML/prototype/API use the actual browser, contract runner or test tool when authorized; generating source is not equivalent to successful execution. Other original Claude-only helper script names describe possible implementations, not installed ANGENT commands.


# /figma — Push wireframes to Figma frames

## Goal

Create/update Figma frames from the feature's wireframes (ASCII content as the source of truth) via the Figma MCP, and record each frame's URL into the `Figma` column of `docs/{feature}/ascii-wireframe/{feature}-wireframe-index.md`. **No local output file** — Figma is the artifact; the index is the pointer.

## Constraints

- **External-write — hard gate** (`approval-gate.md` external-write class, same shape as `/sync-confluence`): preview every frame's contents + the target Figma file/page, get an explicit **Y** before any MCP write. No auto-approve.
- **Figma MCP must be authenticated** — if the MCP is not connected/authenticated, STOP and tell the user how to connect it; do not fabricate URLs or fall back to a local file.
- **Group B** (`feature-bootstrap.md`): needs wireframes — ASCII screens preferred (`ascii-wireframe/{flow-slug}.md`), else HTML wireframes; missing both → refuse + route `/wireframe-ascii`.
- **One Figma frame per screen** — frame name = `[n] {screen-name}`; group frames by flow (a Figma section/page per flow when the tool supports it).
- **Content parity** — the Figma frames mirror the wireframes (same controls, same `[n]`); the index's `Figma` column holds the frame URL per screen.
- **No local file** (`naming-conventions.md` line 46) — only the index is edited (the `Figma` column).
- **Idempotent** — re-run updates existing frames (URLs stable); new screens get new frames.

## Inputs

```
/figma <feature>                  # all flows
/figma <feature> --flow <slug>    # one flow
```

## Approach

1. **Gate.** No wireframes → refuse + route `/wireframe-ascii`. Verify the Figma MCP is authenticated (probe a read-only call); if not → STOP with connect instructions.
2. **Read the wireframes** for the target flow(s) — every screen `[n]`, its controls, the device width.
3. **Draft the frame plan** — per screen: frame name `[n] {name}`, width (device), the controls to place, the target Figma file/page (from memory or ask once).
4. **L1 preview (hard gate)** — list every frame + target + a note that this WRITES to Figma; get explicit **Y**.
5. **On Y → MCP writes** — create/update each frame; collect the returned frame URLs.
6. **Edit the index** — write each URL into the `Figma` column of its screen row; tick `updated`.
8. **Output report** — frames pushed + the Figma file link + next (`/prototype-html` for a local clickable demo).

## Gotchas

- **Never invent a Figma URL** — if a write fails or returns nothing, leave the cell empty and report it; a fake URL breaks the index contract silently.
- **Content parity, always** — the Figma frame is a render of the wireframe, not a redesign; if the wireframe changed, re-sync the frame.
- **One source of screen truth** — the ASCII wireframe + its `[n]`; Figma frames follow those numbers, never the reverse.
- **MCP availability varies** — in headless/CI contexts the Figma MCP may be absent; this skill is interactive-only by nature.
