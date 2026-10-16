---
name: ba-srs
description: Business analysis srs specialist.
---

# ANGENT BA: srs

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/srs/SKILL.md

## Portability and authority

Use domain-specific steps below as methodological guidance; do not assume the original Claude-specific scripts, hooks, subagents, slash commands, filesystem paths, and approval levels exist. ANGENT Root owns intent and routing, Execution owns all provider mutation and read-back, and Quality owns outcome verification. Never claim original tools ran if unavailable. Retain current project IDs and explicitly distinguish facts, assumptions and approvals.


# /srs — Software Requirements Specification (orchestrator)

## Goal

Specify EXACTLY what the system must do — Section 2 Functional Requirements (`FR-`), Section 3 NFRs (`NFR-`), Section 4 Business Rules (`BR-`), Section 5 Error Matrix (`E-`) — each testable and traced to a `CAP-`. **Single output**: `docs/{feature}/srs/{feature}-spec.md` (type `srs`, FULL frontmatter). After the spec, offer the diagram menu (`/sequence` `/state` `/erd` `/user-flow`…) — each menu item is its own skill run.

## Constraints

- **1 fixed output** — `docs/{feature}/srs/{feature}-spec.md`. Diagrams do NOT embed here — they live in `srs/{feature}-flows.md` / `-states.md` / `-erd.md` via their own skills.
- **Orchestrator special case** (`feature-bootstrap.md`): spec missing → group A for the spec itself (derive slug + interview Batch 1-2 + create `srs/`); the menu items stay group B (they need the just-written spec).
- **Sub-agents return content, never write** (`approval-gate.md` §sub-agents) — every Write goes through this orchestrator's L1 gate.
- **Testable phrasing** — every FR: "The system shall {observable behavior} when {condition}" (or equivalent); reject vague verbs (support/handle/manage) in favor of observable outcomes. Every FR row: Covers (CAP-) + Priority + Source.
- **Mint 4 ID families** — `FR-/NFR-/BR-/E-{feature}-{NNN}`, 3-digit, max+1 each, never renumber.
- **Error Matrix is first-class** — every FR with a failure mode gets an `E-` row (condition · system behavior · user sees · related FR). An SRS with 12 FRs and 1 error row is under-specified.
- **PRD missing → soft note** (Covers column empty until `/prd-epic` runs); feature missing → group A.
- **Inherit OQs** (`resolve-oqs.md` Phase E) — from PRD/BRD/URD chain; own OQs in the "Open Questions" section.
- **Validate before done** — BA Markdown validation (step 9).

## Inputs

```
/srs <feature>                  # full spec (create or update)
/srs <feature> --section 5      # revisit one section (e.g. Error Matrix)
/srs <new-feature>              # group A: interview Batch 1-2 + create
```

## Approach

1. **Resolve feature + mode.** Read the chain: `{feature}-prd.md` (CAPs to cover) → `{feature}-brd.md` (business rules to formalize) → `{feature}-urd.md` (actors from personas). Existing spec → update mode.
2. **Interview Batch 1 (frame):** actors + system boundary · the main scenarios per P0 capability. **Batch 2 (behavior):** per scenario — trigger, observable outcome, failure modes, business rules touched, data touched. No-re-ask what the chain already answers.
3. **Fact-list** — every behavior/rule/error + origin (PRD/BRD/interview); each CAP → its FR candidates.
4. **Assign IDs** — FR/NFR/BR/E per section, scanning the existing spec for max.
5. **Draft** per the template — Overview + actors · Section 2 FRs (testable, Covers CAP-) · Section 3 NFRs (category + measure) · Section 4 BRs (formalized from BRD + interview) · Section 5 Error Matrix (linked to FRs) · data notes · diagram links · OQs.
6. **scoped change preview** — per-section counts + CAP coverage + uncovered CAPs called out. `--section` mode → preview only that section's diff.
7. **Write** — `links:` → PRD (+ BRD/URD).
11. **Diagram menu** — offer per `doc-selection.md`/`diagram-selection.md`: flows (`/sequence`, `/activity-swimlane`), lifecycle (`/state`), data (`/erd`, `/dbdiagram`), screens (`/user-flow`, wave 2). Each item runs as its own skill with this spec as source.
12. **Output report.**

## Gotchas

- **"Support X" is not a requirement** — rewrite to the observable behavior ("shall return the refund status within 2s of the request").
- **The Error Matrix is where specs earn their keep** — happy paths survive contact with users; error rows are what devs and testers actually need.
- **NFRs need a measure** — "fast" is not an NFR; "p95 < 500ms at 100 rps" is.
- **BR here is system-enforceable** — BRD-level policy became `BR-` rows only when the system enforces them.
- **Do not embed diagrams** — link `srs/{feature}-flows.md` etc.; the merged-file convention keeps the spec reviewable.
