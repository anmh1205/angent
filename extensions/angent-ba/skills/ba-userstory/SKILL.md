---
name: ba-userstory
description: Business analysis userstory specialist.
---

# ANGENT BA: userstory

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/userstory/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Run extensions/angent-ba/scripts/validate_documents.py only where its documented input is compatible; for Mermaid, D2, PlantUML or BPMN use an actual available compiler, renderer and semantic review. Treat references to original Claude-only engines as source architecture examples until those dependencies are installed and verified.


# /userstory — INVEST user stories (backlog slices)

## Goal

Slice the SRS's FRs into INVEST stories — As a / I want / So that + context + linked requirements + inline Acceptance Criteria — one `us-{NNN}.md` per story (zero frontmatter), with `docs/{feature}/userstories/{feature}-story-index.md` (type `userstory-index`) as the single source of metadata, status, and jira-key.

## Constraints

- **Group B** (`feature-bootstrap.md`) — `srs/{feature}-spec.md` missing → **refuse + route to `/srs`** (standard message). Slicing without FRs = fabrication. UC files missing → soft warn only (stories can slice FRs directly).
- **Content/metadata split** (`naming-conventions.md`) — `us-{NNN}.md` is **zero frontmatter**, prose sections only (User Story / Context / Linked Requirements / Acceptance Criteria inline / UI refs / Error refs / Dependencies / OQs). Status, priority, FR links, screens, jira-key live in the index table ONLY.
- **Mint `US-{NNN}`** — 3-digit, path-scoped (feature implied by folder), max+1 across the index, never renumbered.
- **INVEST discipline** — each story independently valuable and small enough for a sprint; an FR too big for one story → split by scenario/persona; several trivial FRs → one story may cover them (the index maps both ways).
- **Every story links ≥1 FR** — a story with no FR source is invented scope → refuse or send back to `/srs`.
- **AC section seeded, not padded** — 1-2 obvious Given-When-Then per story now; `/ac` is the dedicated pass for full criteria.
- **Validate before done** — BA Markdown validation on the userstories dir (step 9).

## Inputs

```
/userstory <feature>                    # slice all uncovered FRs into stories
/userstory <feature> --from FR-{feature}-004   # stories for one FR only
```

## Approach

1. **Gate.** `srs/{feature}-spec.md` missing → refuse + route `/srs` (group B). Present → Read it (FRs, E- codes, priorities) + `{feature}-urd.md` (personas) + UC index (screens) + existing story index (coverage + max US number).
2. **Slice plan.** Map uncovered FRs → story candidates: persona (from URD) + want (the FR's observable behavior) + so-that (the need/objective upstream). Note split/merge decisions per INVEST.
3. **Fact-list** — per story: FRs covered, persona source, screen refs (if wireframes exist), E- codes touched.
4. **Draft `us-{NNN}.md`** per story — story sentence, context (why this slice), linked requirements (wikilinks to spec anchors), 1-2 seed ACs (`AC-001`, `AC-002` scoped per story), UI refs, error refs, dependencies (other US), OQs.
5. **Update the index** — one row per story: ID/title/persona/FR/screens/priority(from FR)/status `draft`/jira-key `—`/updated.
6. **scoped change preview** — the slice plan (story list + FR coverage map + split/merge notes).
8. **Coverage check** — every targeted FR now maps to ≥1 story; report any FR left uncovered (with reason) rather than silently skipping.
11. **Output report** — coverage + next (`/ac` for full criteria; `/jira` in wave 6).

## Story shape reference (Claude composes it, do NOT hard-paste)

```markdown
# US-001 — Approver decides a claim within their tier

**As an** approver, **I want** validated claims routed to me only when the amount is within my authority, **so that** small claims stop waiting on the Head of Claims.

## Context
Slice of the tier-routing capability; the queue view is US-002.

## Linked Requirements
[[docs/atlas-re/srs/atlas-re-spec.md#FR-atlas-re-006|FR-atlas-re-006]] · BR-atlas-re-001

## Acceptance Criteria
- AC-001: Given a VALIDATED claim of 40k USD, when routing runs, then it lands in a handler-tier queue.
- AC-002: Given a claim of 300k USD, when routing runs, then it lands in the committee queue.

## UI refs · Error refs · Dependencies · OQs
Screens: (pending wireframes) · Errors: E-atlas-re-002 · Depends: US-002 · OQ: committee quorum
```

## Gotchas

- **Story ≠ FR restated** — the story adds persona intent and slice rationale; if it reads identically to the FR, the slice is wrong (too big or too mechanical).
- **Index is the write surface for status** — never edit status/priority inside `us-*.md`; tools (jira sync, dashboard) read the index only.
- **Cross-story dependencies are a warning sign** — a chain of `Depends:` usually means the slicing follows architecture, not user value; re-slice by scenario.
- **Don't pad ACs here** — `/ac` interviews properly; two obvious seeds beat six guessed ones.
