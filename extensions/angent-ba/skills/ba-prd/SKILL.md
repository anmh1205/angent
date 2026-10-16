---
name: ba-prd
description: Business analysis prd specialist.
---

# ANGENT BA: prd

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/prd/SKILL.md

## Portability and authority

Use domain-specific steps below as methodological guidance; do not assume the original Claude-specific scripts, hooks, subagents, slash commands, filesystem paths, and approval levels exist. ANGENT Root owns intent and routing, Execution owns all provider mutation and read-back, and Quality owns outcome verification. Never claim original tools ran if unavailable. Retain current project IDs and explicitly distinguish facts, assumptions and approvals.


# /prd — Product PRD (project-level singleton)

## Goal

Define the WHOLE product once — pitch, problem, users, value, goals, themes, the **Feature Map** (the canonical feature list `/roadmap` prioritizes and feature slugs are born from), metrics, constraints, risks. **Single output**: `docs/_product/prd.md` (type `prd-product`, NO `feature` field — project-level).

## Constraints

- **Singleton** — `docs/_product/prd.md`; a second run = update mode (L2 diff), never a second file.
- **Group C** (`feature-bootstrap.md`) — runs BEFORE any feature exists; an empty vault is a valid starting state, no routing needed.
- **Product altitude** — themes and the Feature Map, not capability detail. One line per feature in the Map; detail belongs to that feature's `/prd-epic`.
- **The Feature Map is the contract** — slug (kebab-case, per `naming-conventions.md`) + theme + one-line purpose + status. `/roadmap` reads it one-way; feature folders adopt these slugs.
- **Own OQs only** — Section 11; the product PRD is the product-level root, nothing cascades in (`resolve-oqs.md`). Cascade scans stay within this file.
- **No fabricated market claims** — metrics targets and user segments need a stated basis or become OQs.
- **Validate before done** — doc-validate (step 8).

## Inputs

```
/prd                # create (interview) or open update mode if it exists
/prd --update       # explicit update mode (L2 diff per section)
```

## Approach

1. **Mode.** `docs/_product/prd.md` exists → update (Read fully first, no-re-ask). Else → create.
2. **Interview (one batched round):** the pitch in one sentence · the problem + who has it · segments + their core job · what makes this valuable · product goals · theme candidates · known features (seed the Map — include existing `docs/*/` folders) · metrics + basis · constraints/risks.
3. **Fact-list** — every claim + origin.
4. **Draft** per the template — Sections 1-11; Feature Map rows get valid slugs (existing folders keep theirs).
5. **L1 plan preview** — theme + Feature Map summary.
6. **Write** — no `feature:` in frontmatter; `links: []` or pointers to research docs.
10. **Output report** — Feature Map + next steps (`/roadmap`, `/prd-epic {slug}`).

## Gotchas

- **"PRD for {feature}" → `/prd-epic`** — this skill only does the product singleton; redirect immediately, don't create a second product PRD.
- **Feature Map slugs are forever** — folders get created from them; renaming later means moving `docs/{slug}/`. Spend the extra minute on slug quality.
- **Metrics without a basis** — a target pulled from air becomes the team's OKR; make the basis explicit or file an OQ.
- **Roadmap sync is one-way** — editing the Feature Map does not auto-update `roadmap.md`; re-run `/roadmap` (per `resolve-oqs.md`).
