---
name: ba-ac
description: Business analysis ac specialist.
---

# ANGENT BA: ac

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/ac/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Run extensions/angent-ba/scripts/validate_documents.py only where its documented input is compatible; for Mermaid, D2, PlantUML or BPMN use an actual available compiler, renderer and semantic review. Treat references to original Claude-only engines as source architecture examples until those dependencies are installed and verified.


# /ac — Acceptance criteria (Given-When-Then, in-place)

## Goal

Make every story verifiable — a complete Given-When-Then set per story covering the happy path, each linked `E-` error, and each `BR-` boundary, written INTO the story's `## Acceptance Criteria` section. **No new files** — this skill only edits `us-{NNN}.md`.

## Constraints

- **Group B** (`feature-bootstrap.md`) — no `us-*.md` → **refuse + route to `/userstory`**.
- **Pure edit skill — always L2** (`approval-gate.md`): every change is shown as a diff against the story file; there is no L1 create path.
- **Mint `AC-{NNN}`** — 3-digit, scoped WITHIN each story file (`AC-001` in us-001 and `AC-002` in us-003 don't collide — path-scoped per `naming-conventions.md`), max+1 per story, existing ACs never renumbered.
- **Coverage rule** — per story: ≥1 AC for the happy path, ≥1 per linked `E-` code, ≥1 per `BR-` boundary the story touches (test the edge: at/below/above the threshold). A story ending with <2 ACs must carry an OQ explaining why.
- **Given-When-Then discipline** — Given = observable state, When = one action, Then = observable outcome. No "should", no UI pixel talk, no implementation ("the query returns…").
- **Source-bound** — thresholds/values come from the spec (BR-/E- rows) or the interview; unknown boundary values become OQs in the story, never invented numbers.
- **Validate before done** — BA Markdown validation on the userstories dir (step 7).

## Inputs

```
/ac <feature>              # sweep every story, fill gaps
/ac <feature> us-003       # one story only
```

## Approach

1. **Gate.** No stories → refuse + route `/userstory`. Read the story index + target `us-*.md` files + `srs/{feature}-spec.md` (E- and BR- rows are the AC checklist).
2. **Gap analysis per story** — existing ACs vs the coverage rule: which happy path, E- code, or BR- boundary has no criterion yet. Stories already complete → skip (report as such).
3. **Interview only true gaps** (one batched round): boundary values the spec doesn't pin down, expected outcomes for ambiguous error paths. No-re-ask what spec/story already answer.
4. **Draft ACs** — per gap, numbered `AC-{next}` within that story; boundary rules get the at/below/above triple where meaningful.
5. **proposed change diff** — per story: the exact `## Acceptance Criteria` section diff + a one-line coverage summary (happy ✓ · E-xxx ✓/✗ · BR-xxx ✓/✗).
9. **Output report** — per-story coverage table + next (`/test-checklist`, wave 4).

## AC shape reference (Claude composes it, do NOT hard-paste)

```markdown
- AC-003: Given a VALIDATED claim of exactly 50,000 USD, when tier routing runs, then it lands in the handler-tier queue (BR boundary: ≤ 50k).
- AC-004: Given the approver also validated this claim, when they submit a decision, then the system blocks it and names the validator (E-atlas-re-001).
```

## proposed change diff (per story)

> **us-{NNN}** — coverage before: happy {✓/✗} · errors {n}/{m} · boundaries {n}/{m} → after: all ✓ ({K} ACs added).
> ```diff
> {the section diff}
> ```
> Apply? (Y / edit / skip)

## Gotchas

- **One When per AC** — "when the user logs in and approves and…" is a scenario, not a criterion; split it.
- **Boundaries need three cases** — a "≤ 50k" rule is only pinned by at/below/above; one case leaves the edge ambiguous.
- **AC ≠ test case** — no test data tables, no step-by-step clicks; that detail is `/test-cases`' job (wave 4).
- **Respect story scope** — an AC that needs behavior from another story belongs there; note it, don't absorb it.
