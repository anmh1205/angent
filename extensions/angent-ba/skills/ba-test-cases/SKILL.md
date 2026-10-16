---
name: ba-test-cases
description: Business analysis test-cases specialist.
---

# ANGENT BA: test-cases

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/test-cases/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions.


# /test-cases — Full test cases (steps/data/expected)

## Goal

Expand each `CHK-` row into one or more `TC-{NNN}` test cases — numbered steps, concrete test data, and the expected observable outcome (+ error code/message where applicable). **Single output**: `docs/{feature}/test/testcases/{feature}-testcase-index.md` (type `test-cases-index`).

## Constraints

- **Group B** (`feature-bootstrap.md` canonical example): no `test/checklist/{feature}-checklist-index.md` → **refuse + route `/test-checklist`**. Expanding nothing = fabricating tests.
- **Mint `TC-{NNN}`** (`test-conventions.md`) — 3-digit, path-scoped, max+1, never reused.
- **One CHK → one or more TC** — a boundary `CHK-` expands to the at/below/above triple as separate `TC-` rows; an error `CHK-` to one `TC-` per `E-` code it covers. Every `TC-` links back via the `Expands CHK` column.
- **Test data is sourced** — values come from the spec/AC (BR thresholds, E- messages); unknown values → ask or OQ, never invented.
- **One action per step** — numbered steps, each a single click/enter/submit; no prose padding.
- **Expected = observable** — the outcome a tester sees + the exact error wording/code where applicable.
- **Fill the checklist's `TC` column** — after generating, write the `TC-` back into the checklist row (the reverse pointer `/gap` joins on).
- **Validate before done** — doc-validate (step 8).

## Inputs

```
/test-cases <feature>                # expand every CHK- with no TC yet
/test-cases <feature> --chk CHK-003  # one checklist row
```

## Approach

1. **Gate.** No checklist → refuse + route `/test-checklist` (standard group-B message). Read the checklist (every `CHK-`, its `Covers`, layer) + the spec/AC for the source values (boundaries, error messages).
2. **Expansion plan** — per uncovered `CHK-`: how many `TC-` (boundary → 3, error → 1 per E-, functional → 1); note the test data needed per case.
3. **Fact-list** — per planned `TC-`: the steps, the data (sourced), the expected (+ E- code).
4. **Ask data gaps** — any value the spec/AC doesn't pin (one batched round); "skip" → mark the case `data: TBD`.
5. **Assign `TC-` IDs** — scan the existing testcase index for max.
6. **Draft** per the template — rows with Title / Expands CHK / Steps / Test data / Expected / Status.
7. **L1 plan preview** — TC count + per-CHK expansion breakdown + data-gaps flagged.
10. **Output report** — TC generated + data-gaps + next (`/gap` to prove AC→CHK→TC coverage).

## Gotchas

- **No checklist = no test cases** — this is the canonical group-B refusal; don't soften it. Generating tests from FRs directly skips the outline and produces uneven coverage.
- **Boundary triple is non-negotiable** — a ≤ 50k rule tested only at 40k leaves the edge ambiguous; the at/below/above cases are why `/test-cases` exists over a flat generator.
- **Expected wording must match the spec** — the `E-` message in the test case is the exact string the user sees; paraphrasing it breaks the tester.
- **Don't renumber** — a `TC-` retired by a changed requirement keeps its number; new cases take max+1.
