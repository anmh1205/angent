---
name: ba-reverse-doc
description: Business analysis reverse-doc specialist.
---

# ANGENT BA: reverse-doc

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/reverse-doc/SKILL.md

## Portability and authority

Use domain-specific steps below as methodological guidance; do not assume the original Claude-specific scripts, hooks, subagents, slash commands, filesystem paths, and approval levels exist. ANGENT Root owns intent and routing, Execution owns all provider mutation and read-back, and Quality owns outcome verification. Never claim original tools ran if unavailable. Retain current project IDs and explicitly distinguish facts, assumptions and approvals.


# /reverse-doc — Reconstruct BA docs from legacy sources

## Goal

Read legacy sources (docx/pdf/images/code/emails) and reconstruct the business logic as a `docs/{feature}/reverse-{feature}.md` (type `reverse-feature`) — a 12-section framework + Section 0 (source map + 3-level confidence ✅/🔵/🟡). Produces a `docs/.reverse-plan.md` (type `reverse-plan`) conversion plan first. **Never overwrites** the official `urd/brd/srs` — it sits alongside, as a reverse-engineered view.

## Constraints

- **Group A-variant** (`feature-bootstrap.md`): derives the slug from the SOURCE (not from interviewing the user); can create MULTIPLE features at once; asks only about GAPS (where the source is missing), never interviews the business from scratch.
- **scan-project shape, 2 HARD STOPs** — Phase 1: read sources → cluster into features → write `.reverse-plan.md` (HARD STOP, confirm). Phase 2: generate the reverse docs per confirmed plan (HARD STOP only if a gap blocks generation).
- **3-level confidence on every claim** (`naming-conventions.md` line 66): ✅ directly stated in source · 🔵 inferred from source · 🟡 gap/assumption (must become an OQ). No claim without a confidence marker.
- **No fabrication** — anything not in the source is 🟡 + an OQ, never a confident ✅. This is the skill's defining discipline.
- **Provenance per section** — Section 0 records which source(s) fed which section, so an auditor can trace back.
- **Alongside, not replacing** — `reverse-{feature}.md` is a reconstruction; the official `urd/brd/srs` (if they exist) stay untouched. The user may later promote reverse content into them via `/cr` or manual edit.
- **Temp convert files** under `docs/.reverse-convert/` are scratch (gitignored/cleaned); only the reverse docs + plan persist.
- **Validate before done** — doc-validate (step 9).

## Inputs

```
/reverse-doc ./legacy/claim-system-spec.docx --feature claim-legacy
/reverse-doc ./legacy/*.pdf ./src/claims/           # cluster sources → propose features
```

## Approach

1. **Read the sources** — extract text/structure (docx/pdf via available tooling; code via Read/Grep; images via the vision/OCR available). Note per-source: what it covers, its authority (a signed spec > an email).
2. **Cluster → features** — group source content by business domain; propose feature slugs (from the source, not invented). Write `docs/.reverse-plan.md`: the feature list + per-feature source map + the clarifying questions for gaps. **HARD STOP** — confirm the plan before generating.
3. **On confirm → per feature** draft `reverse-{feature}.md`: Section 0 (source map + confidence legend) + the 12 sections (problem/users/objectives/scope/rules/data/flows/states/errors/screens/OQs/…), every claim tagged ✅/🔵/🟡.
4. **Gap interview** — only the 🟡 items the source can't resolve; one batched round; unresolved → OQ in the doc.
5. **L1 plan preview** (per feature) — section coverage + confidence mix (✅/🔵/🟡 counts) + OQ count.
7. **If a gap blocks a section** → HARD STOP, ask; never fill with a guess.
9. **Output report** — features reconstructed + confidence mix + next (`/srs` to formalize from the reverse view; `/scan-project` if code needs architecture diagrams).

## Gotchas

- **Confidence honesty is the whole skill** — a reconstruction full of ✅ that were actually 🔵/🟡 is worse than useless; it looks authoritative and isn't. When unsure, drop a level.
- **Source authority matters** — a vendor's signed spec is ✅-grade; a Slack screenshot is 🔵 at best; tag accordingly.
- **Don't promote silently** — moving reverse content into the official urd/brd/srs is a `/cr` (it changes the source of truth); keep them separate until then.
- **Images need OCR/vision** — if neither is available, the section stays 🟡 with an OQ rather than skipped.
