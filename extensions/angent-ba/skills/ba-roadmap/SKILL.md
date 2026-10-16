---
name: ba-roadmap
description: Business analysis roadmap specialist.
---

# ANGENT BA: roadmap

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/roadmap/SKILL.md

## Portability and authority

Use domain-specific steps below as methodological guidance; do not assume the original Claude-specific scripts, hooks, subagents, slash commands, filesystem paths, and approval levels exist. ANGENT Root owns intent and routing, Execution owns all provider mutation and read-back, and Quality owns outcome verification. Never claim original tools ran if unavailable. Retain current project IDs and explicitly distinguish facts, assumptions and approvals.


# /roadmap — Product roadmap (RICE-lite + plan + dependencies)

## Goal

Turn the Feature Map into a prioritized plan — RICE-lite scores per feature (Reach · Impact · Confidence · Effort), a Now/Next/Later or by-quarter plan, a dependency map, and a decisions log. **Single output**: `docs/_product/roadmap.md` (type `roadmap`, frontmatter has `format`).

## Constraints

- **Singleton** — `docs/_product/roadmap.md`; re-run = update mode (L2 diff). Frontmatter `format:` records the chosen shape.
- **Group C** (`feature-bootstrap.md`) — no product PRD yet → friendly message: "No Feature Map yet — run `/prd` first, or list your features now and I'll score them" (a Map-less roadmap from a live list is valid).
- **One-way read** — consumes `docs/_product/prd.md`'s Feature Map (+ each feature's `CAP-` priorities if PRDs exist). Never edits the PRD; PRD changes → re-run `/roadmap` to sync (`resolve-oqs.md`: no OQ cascade into this file).
- **RICE-lite discipline** — Reach/Impact/Confidence on the agreed scale (1-5 or %), Effort in relative units; **every score's basis comes from the user or a doc** — no invented scores. Score = (R×I×C)/E, computed, shown per row.
- **Now means committed** — "Now" items should have (or be about to get) a `/prd-epic`; flag "Now" features with no PRD.
- **Dependencies are typed** — tech / data / team / vendor, per row.
- **Validate before done** — doc-validate (step 8).

## Inputs

```
/roadmap                              # default format: now-next-later
/roadmap --format quarter             # by-quarter plan
```

## Approach

1. **Load the Feature Map** from `docs/_product/prd.md` (or take a live list — group C fallback). Existing roadmap → update mode, Read fully first.
2. **Score interview (one batched round per gap):** per feature — Reach basis · Impact on which product goal · Confidence + why · Effort relative to a named anchor feature. Skip rows the user already scored.
3. **Fact-list** — every score + basis; sequencing constraints; dependency claims.
4. **Compute + draft** per the template — RICE table sorted by score · the plan (Now/Next/Later or quarters; note where the plan order deviates from score order and why) · dependency map (typed) · decisions log (append-mode across runs).
5. **L1 plan preview** — top-3 by score + any score-vs-plan deviations + "Now without PRD" flags.
6. **Write.**
9. **Output report** — the plan summary + suggested next (`/prd-epic` for un-specced "Now" items, `/timeline` for a visual).

## Gotchas

- **Score ≠ plan** — dependencies and strategy legitimately reorder; the deviation note is what makes the roadmap defensible.
- **Effort needs an anchor** — "3" means nothing; "3× the size of {shipped-feature}" survives review.
- **Don't cascade OQs here** — this file is derived; questions belong in the PRD/feature docs, and the fix is a re-run.
- **Decisions log is append-only across runs** — it's the "why did we demote X in July" memory; never rewrite old rows.
