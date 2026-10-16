---
name: ba-gap
description: Business analysis gap specialist.
---

# ANGENT BA: gap

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/gap/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions.


# /gap — Cross-doc traceability matrix + coverage report

## Goal

Walk the entire ID spine across the vault, compute coverage, and write one report: `docs/_shared/traceability.md` (type `traceability`) — the gaps, orphans, uncited error codes, and stale chains. Read-only analysis; the **only** write is that report (L1-gated per `approval-gate.md`'s named exception).

## Constraints

- **Group C** (`feature-bootstrap.md`): empty vault → friendly abort ("Start with `/brainstorm` or `/urd`"). `--feature <slug>` scopes the walk to one feature.
- **Read-only on the docs it scans** — never edits URDs/SRSes/stories; it reports gaps, the owning skill fills them.
- **Parse the 3 surfaces** (`traceability.md`): frontmatter `links:`, body wikilinks, and index tables (usecase-index, story-index, wireframe-index) — content files are zero-frontmatter, so the join goes via indexes + body.
- **Emit exactly the coverage rules** in `traceability.md` §"Coverage rules": UN-without-BO, BO-without-CAP, CAP-without-FR, FR-without-UC/US, US-without-AC, US-without-≥2-AC, AC-without-CHK/TC, E-uncited, orphan-doc, stale-chain, CR-apply-order-gap.
- **No fabrication** — every finding cites the concrete ID/path; never invent a "missing" ID that doesn't exist upstream (only report breaks in the *declared* chain).
- **Idempotent** — re-run regenerates the report (L2 diff).
- **Validate before done** — doc-validate on the report (step 7).

## Inputs

```
/gap                          # whole vault
/gap --feature atlas-re       # one feature
```

## Approach

1. **Scope.** Empty vault → friendly abort. `--feature` → that folder; else every `docs/{feature}/`.
2. **Index the IDs** — scan each doc for its IDs (UN/BO/CAP/FR/NFR/BR/E/UC/US/AC/CHK/TC/CR) and its `links:` + body wikilinks + index-table rows. Build the graph.
3. **Run the coverage rules** (`traceability.md`) — for each, collect the violations with their concrete IDs.
4. **Stale check** — compare `links:` target `updated:` vs the doc's own (via `staleness.log` if present).
5. **Draft `traceability.md`** — the spine diagram + a findings table per rule (ID + where + suggested owner skill) + an orphan-doc list + a CR-apply-order check.
6. **L1 plan preview** — finding counts per rule + the worst gaps called out.
9. **Output report** — the gap summary + the single highest-leverage fix per category.

## Gotchas

- **Coverage ≠ quality** — `/gap` proves the chain is *complete*, not that it's *correct*; correctness is `/doc-review`'s job.
- **Don't chase 100%** — a deliberately deferred need (UN with no BO, phased out) is a finding, not a defect; the report lists it, the user decides.
- **E-uncited is the sneaky one** — error codes defined in the SRS but referenced nowhere are the most common real gap; they're why this skill exists.
- **The index tables are the cheap join** — prefer them over re-parsing every zero-frontmatter content file; body wikilinks are the fallback.
