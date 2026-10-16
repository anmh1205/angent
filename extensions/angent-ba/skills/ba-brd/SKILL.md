---
name: ba-brd
description: Business analysis brd specialist.
---

# ANGENT BA: brd

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/brd/SKILL.md

## Portability and authority

Use domain-specific steps below as methodological guidance; do not assume the original Claude-specific scripts, hooks, subagents, slash commands, filesystem paths, and approval levels exist. ANGENT Root owns intent and routing, Execution owns all provider mutation and read-back, and Quality owns outcome verification. Never claim original tools ran if unavailable. Retain current project IDs and explicitly distinguish facts, assumptions and approvals.


# /brd — Business Requirements Document

## Goal

Make the business case — objectives with measurable success criteria that mint **`BO-{feature}-{NN}`** IDs covering the URD's `UN-` needs, plus business scope, business rules, cost-benefit, and risks. **Single output**: `docs/{feature}/{feature}-brd.md`.

## Constraints

- **1 fixed output** — `docs/{feature}/{feature}-brd.md` (type `brd`, FULL frontmatter).
- **Feature missing → group A** (`feature-bootstrap.md`): derive slug + interview + create. URD missing but feature exists → proceed with a soft note ("BO- rows will have empty Covers-needs until /urd runs") — the BRD can legitimately come first in some engagements.
- **Section names are load-bearing** — Executive Summary · Business Objectives & Success Measures · Business Scope · Business Rules · Cost-Benefit · Risks. `resolve-oqs.md` §3.5.3's topic map scans these exact names for OQ cascade; do not rename.
- **Mint `BO-` IDs** — `BO-{feature}-{NN}` (2-digit ok), max+1. Every objective row: measurable success measure + target + the `UN-` needs it covers.
- **Money altitude, no fabricated figures** — cost/benefit estimates carry a `basis` column; no basis from the user → OQ, never an invented number (`ba-conventions.md` §3).
- **Inherit OQs** — from the URD + brainstorms (`resolve-oqs.md` Phase E); mark origins.
- **Idempotent** — re-run → versioned diff update.
- **Validate before done** — BA Markdown validation (step 9).

## Inputs

```
/brd <feature>              # reads {feature}-urd.md + brainstorms if present
/brd <new-feature>          # group A: interview the business case + create
```

## Approach

1. **Resolve feature.** Read `{feature}-urd.md` (needs to cover) + `brainstorms/*.md` (problem framing) if present.
2. **Gather.** Gaps → one batched interview: why now (the business driver) · objectives + how each is measured · in/out of scope + dependencies · known business rules · cost/benefit items with their basis · risks.
3. **Fact-list** — every objective/figure/rule + its origin; inherited OQs.
4. **Assign IDs** — `BO-{feature}-{NN}`, covering `UN-` refs per row.
5. **Draft** per the template — the six load-bearing sections + OQs.
6. **scoped change preview** — BO count + UN coverage + risk count + any uncovered UN- called out.
7. **Write** — `links:` → the URD + brainstorm(s).
11. **Output report** — coverage summary + next step (`/prd-epic {feature}`).

## Gotchas

- **A success measure is not a feature** — "increase self-service refunds to 80%" is a measure; "add a refund button" belongs in the PRD.
- **Cost-benefit honesty** — a table full of confident numbers with no basis column filled is worse than OQs; stakeholders will hold the BRD to those numbers.
- **Business Rules here are business-level** — policy ("refunds over $500 need manager approval"), not system behavior; system-level `BR-` IDs are minted later by `/srs`.
- **Do not rename sections** — the OQ cascade greps them.
