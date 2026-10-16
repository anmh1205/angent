---
name: ba-prd-epic
description: Business analysis prd-epic specialist.
---

# ANGENT BA: prd-epic

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/prd-epic/SKILL.md

## Portability and authority

Use domain-specific steps below as methodological guidance; do not assume the original Claude-specific scripts, hooks, subagents, slash commands, filesystem paths, and approval levels exist. ANGENT Root owns intent and routing, Execution owns all provider mutation and read-back, and Quality owns outcome verification. Never claim original tools ran if unavailable. Retain current project IDs and explicitly distinguish facts, assumptions and approvals.


# /prd-epic — Feature PRD (capabilities)

## Goal

Define WHAT we'll build for one feature — capabilities prioritized P0/P1/P2 that mint **`CAP-{feature}-{NN}`** IDs covering the BRD's `BO-` objectives, plus goals/non-goals, user types, out-of-scope, release plan, and dependencies. **Single output**: `docs/{feature}/{feature}-prd.md`.

## Constraints

- **1 fixed output** — `docs/{feature}/{feature}-prd.md` (type `prd`, FULL frontmatter).
- **Feature missing → group A** (`feature-bootstrap.md`). BRD missing but feature exists → soft note (Covers column stays empty until `/brd` runs).
- **Section names are load-bearing** — Goals · Non-goals · User Types · Capabilities · Out of scope · Release plan · Dependencies (the `resolve-oqs.md` topic map scans them).
- **Mint `CAP-` IDs** — `CAP-{feature}-{NN}`, max+1. Every capability: priority (P0/P1/P2) + the `BO-` it covers + a one-line user-visible statement.
- **Capability ≠ implementation** — "user can retry a failed payment" (capability), not "add a retry queue" (design). P0 = the feature is pointless without it.
- **The discovery question set** — when interviewing: problem recap · target users · what must be true at launch (P0 probe) · nice-to-have (P1/P2 probe) · explicit non-goals · sequencing constraints. One batched round.
- **Inherit OQs** — from BRD/URD (`resolve-oqs.md` Phase E).
- **Validate before done** — BA Markdown validation (step 9).

## Inputs

```
/prd-epic <feature>          # reads {feature}-brd.md + upstream chain
/prd-epic <new-feature>      # group A: interview + create
```

## Approach

1. **Resolve feature.** Read `{feature}-brd.md` (objectives to cover) + `{feature}-urd.md` (user types come from personas) if present.
2. **Gather.** Gaps → the discovery question set (one batched round).
3. **Fact-list** — every capability candidate + its origin + the BO it serves.
4. **Assign IDs + priorities** — `CAP-{feature}-{NN}`; challenge every P0 ("is the feature truly pointless without this?").
5. **Draft** per the template — goals/non-goals first (they fence the capability list), then the capabilities table, user types (from personas), OOS, release plan (phases reference CAP IDs), dependencies, OQs.
6. **scoped change preview** — CAP count by priority + BO coverage + any uncovered BO- called out.
7. **Write** — `links:` → BRD (+ URD).
11. **Output report** — priority breakdown + next step (`/srs {feature}`).

## Gotchas

- **Everything-is-P0 disease** — if >60% of capabilities are P0, re-ask the "pointless without it" question per row; a PRD with no P1/P2 gives the roadmap nothing to sequence.
- **Non-goals are a gift** — every explicit non-goal kills a future scope debate; push for at least 2.
- **Release plan references CAP IDs** — phases with prose-only content can't be traced by `/gap`.
- **Do not rename sections** — the OQ cascade greps them.
