---
name: ba-urd
description: Business analysis urd specialist.
---

# ANGENT BA: urd

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/urd/SKILL.md

## Portability and authority

Use domain-specific steps below as methodological guidance; do not assume the original Claude-specific scripts, hooks, subagents, slash commands, filesystem paths, and approval levels exist. ANGENT Root owns intent and routing, Execution owns all provider mutation and read-back, and Quality owns outcome verification. Never claim original tools ran if unavailable. Retain current project IDs and explicitly distinguish facts, assumptions and approvals.


# /urd — User Requirements Document

## Goal

Capture WHO the users are and WHAT they need — personas, context of use, and a needs table that mints **`UN-{feature}-{NNN}`** IDs (the root of the traceability spine: UN → BO → CAP → FR). **Single output**: `docs/{feature}/{feature}-urd.md`.

## Constraints

- **1 fixed output** — `docs/{feature}/{feature}-urd.md` (type `urd`, FULL frontmatter).
- **Feature arg required in spirit** — missing/new feature → group A (`feature-bootstrap.md`): derive slug, interview user needs, create on Write.
- **Read upstream first** — `docs/{feature}/brainstorms/*.md` if present: personas and pains often already exist there; inherit unresolved OQs (`resolve-oqs.md` Phase E). No-re-ask.
- **Mint `UN-` IDs** — `UN-{feature}-{NNN}`, 3-digit, max+1, never reused. Every need row cites its source (brainstorm section, interview answer, research doc).
- **User altitude** — needs are phrased from the user's world ("needs to see the refund status without calling support"), NOT solution language ("needs a status API"). Solutioning belongs downstream.
- **No fabricated personas** — no source + no answer → OQ, not an invented persona.
- **Idempotent** — re-run → update mode (L2 diff); new needs append with the next `UN-` number.
- **Validate before done** — doc-validate (step 9).

## Inputs

```
/urd <feature>              # existing feature (reads its brainstorms)
/urd <new-feature>          # group A: interview user needs + create
```

## Approach

1. **Resolve feature.** Existing → read `brainstorms/*.md` + any prior URD. New → group A.
2. **Gather.** From the brainstorm: affected users → persona candidates; pains → need candidates. Gaps → one batched interview: personas (who, context, goals, frustrations) · context of use (where/when/on what) · needs per persona · environment constraints.
3. **Fact-list** — every persona + need + its source; unresolved upstream OQs to inherit.
4. **Assign IDs** — `UN-{feature}-{NNN}` per need, scanning the existing URD for max.
5. **Draft** per the template: personas table · context of use · needs table (ID/persona/statement/priority/source) · environment & constraints · assumptions · OQs (own + inherited, marked with origin).
6. **L1 plan preview** — persona count + need count + inherited OQ count.
7. **Write** — with frontmatter `links:` pointing at the source brainstorm(s).
10. **Output report** — needs minted + next step (`/brd {feature}`).

## Gotchas

- **Needs ≠ features** — "needs to export a monthly report" is a need; "needs an Export button" is a solution. Push solution phrasing down to the PRD/SRS.
- **Persona sprawl** — >4 personas usually means the feature is too broad; suggest splitting the feature instead of padding the table.
- **ID discipline** — never renumber existing `UN-`s on update; deleted needs keep their number retired.
- **Priority is the user's voice** — P0 = the persona cannot do their job without it, not "we want it first".
