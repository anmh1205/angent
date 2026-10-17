---
name: ba-gap
description: Source-driven BA gap method with independent decision evidence, output validation and safe provider boundaries.
---

# Evidence-based BA coverage and gap analysis

**Method origin:** Independently adapted from MIT Dev BA Kit \`gap\` by Edward Ngo (2026): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/gap/SKILL.md. Source-of-truth and document naming follow the actual product, not a required Claude vault.

## Coverage is not correctness

A gap audit identifies absent or weak relationships among stakeholder needs (UN), objectives (BO), capabilities (CAP), verifiable requirements (FR/NFR/BR), use cases/stories, acceptance (AC), checklist (CHK), test cases (TC) and business decisions. A mathematically complete graph cannot show whether the underlying business assumptions are correct. Conversely, a deliberate product deferral is not necessarily a defect.

## Choose the inspection boundary

1. Confirm the requested feature/product scope and accepted source revisions. Inspect current URD/BRD/PRD/SRS, user stories/use cases, acceptance, test cases and relevant provider issue data **only when accessible**. Avoid a whole-repo scan for a single decision.
2. Collect explicit stable IDs, source files, document links and provenance. Distinguish named sources that were not inspected from documents that truly do not exist. Do not create missing FR/CAP/TC IDs to improve a score.
3. Use the existing BA source graph, if available, without inventing a second registry. The portable extractor supports real Markdown index tables and reports unresolved references. For example:

    python extensions/angent-ba/scripts/extract_markdown_graph.py --urd extensions/angent-ba/examples/docs/atlas-re/atlas-re-urd.md --brd extensions/angent-ba/examples/docs/atlas-re/atlas-re-brd.md --prd extensions/angent-ba/examples/docs/atlas-re/atlas-re-prd.md --srs extensions/angent-ba/examples/docs/atlas-re/srs/atlas-re-spec.md --checklist extensions/angent-ba/examples/docs/atlas-re/test/checklist/atlas-re-checklist-index.md --cases extensions/angent-ba/examples/docs/atlas-re/test/testcases/atlas-re-testcase-index.md --root extensions/angent-ba/examples --output out/atlas-evidence.json

4. Validate graph direction and existence with \`extensions/angent-ba/scripts/validate_artifacts.py\`. Test artifacts point upstream to requirements, not the reverse; a story covering a group of FRs does not prove every individual FR has a corresponding tested behavior.
5. Assess gaps **per relationship**, not from a single global percentage: UN with no BO; BO with no CAP; CAP with no FR; FR with no explicit behavior/test witness; important rule/error without an acceptance or failure case; missing actor/permission; stale source; orphaned decision; changing implementation without review.
6. Verify source content where a relationship matters. A TC that mentions an FR identifier but tests an unrelated status can be a *semantic mismatch*, even though the graph edge is valid. Do not auto-declare compliance from ID matching.
7. Assign finding severity by actual consequence: safety/privacy/financial exposure, business decision block, release dependency or documentation usability. Separate "not reviewed", "not implemented", "deliberately deferred" and "uncertain evidence".
8. Derive a small, actionable reconciliation plan: affected IDs, current vs expected relation, exact source/revision, owner, decision needed and next verification. Preserve existing source material and report contradictions without unapproved mutation.

## How to report

Give the inspected scope and source inventory, a stage-by-stage structural coverage summary, decisive risks, explicit broken chains with shortest proof path, and prioritized next actions. For the shipped Atlas worked example, eight FRs trace upstream through CAP/BO/UN, while only **four** reach a TC artifact. These are declared link counts, not passing test results. A missing TC link must not be silently recast as a release blocker if the FR was intentionally deferred.

ANGENT Root decides whether to run this specialist; Quality compares the report to the actual user's goals. The method performs read-only analysis unless a specific target artifact is requested and authorized. It does not require \`docs/_shared/traceability.md\`, invented \`staleness.log\` files or a fixed Claude L1 gate.

## One read-only handoff audit across inspected stages

When the project already has an accepted artifact graph, run the **distributed** BA assurance command rather than manually inferring nine percentages:

    python extensions/angent-ba/scripts/audit_lifecycle_handoffs.py PATH_TO_ACTUAL_GRAPH.json --output NEW_REVIEW_REPORT.json

For a team that explicitly requires every *inspected* stage to have an evidence link, enable \`--require-known-handoffs\`. The optional strict flag returns nonzero only for gaps where both the source and target artifact kinds exist. If the corpus lacks an entire downstream source, the tool reports **not-inspected**, not passed and not definitively failed. Keep intentional deferrals, planned stories and incomplete stakeholder interviews outside any manufactured release verdict.

The report gives source IDs, shortest witnessed paths, uncovered upstream IDs, unapproved/draft records and test cases with **no execution evidence**. Neither a traced TC nor an approved document status proves the test ran or the solution works. If stakeholders want a business-validation verdict, inspect their actual decisions and observed customer outcomes separately.
