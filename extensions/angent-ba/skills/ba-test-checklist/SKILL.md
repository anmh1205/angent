---
name: ba-test-checklist
description: Business analysis test-checklist specialist.
---

# ANGENT BA: test-checklist

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/test-checklist/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Use the real BA Markdown validator only for completed documents and report the result. For HTML/prototype/API use the actual browser, contract runner or test tool when authorized; generating source is not equivalent to successful execution. Other original Claude-only helper script names describe possible implementations, not installed ANGENT commands.


# /test-checklist — Test coverage outline

## Goal

Derive the test-coverage outline from `srs/{feature}-spec.md` (FR/BR/E), the stories' acceptance criteria (`AC-`), and the use cases' extensions — one `CHK-{NNN}` row per testable thing, classified by layer. **Single output**: `docs/{feature}/test/checklist/{feature}-checklist-index.md` (type `test-checklist-index`).

## Constraints

- **Group B\*** (`feature-bootstrap.md`): `srs/{feature}-spec.md` missing → refuse + route `/srs`. AC files missing → soft warn (the checklist can derive from FRs/E-, but coverage of AC is the stronger path).
- **Mint `CHK-{NNN}`** (`test-conventions.md`) — 3-digit, path-scoped, max+1, never reused.
- **Every row covers something** — `Covers` cites the AC/FR/BR/E it verifies; a row with no source is a fabrication → drop it or send back to `/srs`.
- **Layer classification** — functional / boundary / error / non-functional (the value of the checklist is the *categorized* outline, not a flat list).
- **Boundary awareness** — a BR threshold (e.g. ≤ 50k) → one boundary `CHK-` that `/test-cases` will expand to the at/below/above triple.
- **Error coverage** — every `E-` code → at least one `CHK-` (error layer).
- **The `TC` column starts empty** — `/test-cases` fills it; this skill owns the outline, not the steps.
- **Validate before done** — BA Markdown validation (step 8).

## Inputs

```
/test-checklist <feature>          # derive from spec + AC + UC extensions
```

## Approach

1. **Gate.** Spec missing → refuse + route `/srs`. Read the spec (FR/BR/E rows), the story ACs, and the UC extensions (failure branches → error-layer checks).
2. **Derive candidates** — per FR: the happy-path check + any boundary (BR threshold) + any error (E- code); per AC: a check verifying it; per NFR: a non-functional check where measurable.
3. **Fact-list** — every candidate + its source (FR/BR/E/AC) + its layer.
4. **Assign `CHK-` IDs** — scan the existing checklist for max; classify each row's layer.
5. **Draft** the checklist per the template — rows grouped by layer, `Covers` filled, `TC` empty, `Status: draft`.
6. **scoped change preview** — row count by layer + coverage map (which FRs/ACs/E- are covered, which aren't).
9. **Output report** — layer breakdown + uncovered FR/E/AC (so the user knows the outline's edges) + next (`/test-cases`).

## Gotchas

- **Don't write steps here** — steps/data/expected are `/test-cases`' job; a checklist row is a one-line "what to test", not a procedure.
- **Boundary = one row, not three** — the at/below/above split happens at the case level; the checklist just flags "test the 50k boundary".
- **E- coverage is mandatory** — an error code with no CHK- is a documented error nobody tests; surface it in the report.
- **AC is the richest source** — if stories have ACs, derive from them first (they're already Given-When-Then); FRs are the fallback.
