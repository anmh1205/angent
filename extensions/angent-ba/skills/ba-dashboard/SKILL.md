---
name: ba-dashboard
description: Source-driven BA dashboard method with independent decision evidence, output validation and safe provider boundaries.
---

# BA evidence dashboard: what is known, blocked and changing

**Source background:** Independent adaptation of MIT Dev BA Kit's dashboard method (Edward Ngo, 2026): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/dashboard/SKILL.md. The dashboard is a *read model* of actual documents and provider evidence, not a lifecycle controller or a new authoritative database.

## Establish provenance before metrics

1. Scope the question: feature readiness, document completeness, open business decisions, requirement/test coverage or observed delivery status. Choose only indicators that help the user's next decision; avoid decorative charts and false precision.
2. Read the accepted source set and revisions, current BA evidence graph if present and actual Jira/release/provider data **only if connected and authorized**. Do not assume \`activity.log\`, \`staleness.log\`, \`docs/feature-list.md\` or \`source_watermark\` exist.
3. Compute denominators from the documents actually inspected. Distinguish a missing artifact, an uninspected artifact, an accepted deferral and a broken source reference. A dashboard with a perfect 4/4 score based on four selected examples must not imply a project's remaining requirements were covered.
4. Present structural coverage across UN→BO→CAP→FR→AC/CHK/TC separately from execution evidence. A linked TC is **not** a passed test; a Jira issue closed is **not** a deployed capability; a mock CLI or prototype demonstration is **not** a production service.
5. List consequential open questions and source conflicts with owner, affected decision and next evidence. Never fabricate status transitions from dates or automatically mark a user question as resolved because a generated file exists.
6. Use current source/provider timestamps where available. When estimating staleness, state the actual method (document revision divergence, Git SHA or observed provider updated_at) rather than inventing a "fresh/stale" rule based on undocumented logs.
7. Where helpful, display a compact per-feature table: goal, source revision, FR total, explicit test links, *executed* test count, open policy decisions, provider/deployment status and material risk. Leave unmeasured cells as "unknown", not zero.
8. If HTML is requested, use a real authorized artifact renderer, with semantic headings, usable contrast and a local/no-external-resource policy for private data. The existing source graph has a tested offline HTML preview at \`extensions/angent-ba/scripts/render_preview.py\`; it does not independently implement a full multi-provider operations dashboard.
9. Read back the actual output where files/providers were modified, and preserve existing manual status notes. Regenerate only the authorized view, not the whole project index or accepted documentation.

## Indicator contracts before any chart

Each indicator needs a **named population**, an inspected-source snapshot, a calculation, its uncertainty and a decision it can inform. A denominator that excludes uninspected features is not representative of the entire product.

| Indicator | Numerator | Denominator | Boundary |
|---|---|---|---|
| Upstream functional lineage | FR with actual UN → BO → CAP → FR links | All inspected in-scope FR | Structural linkage is not a stakeholder-approved need |
| Linked test cases | FR linked through permissible evidence to TC | All inspected in-scope FR | Test linkage is not test execution |
| Executed passing tests | Tests with real-run evidence and expected observable result | All required release-scope cases | Version/environment and test mode must match release |
| Unresolved decisions | Explicit open material decisions with owners | Complete in-scope decision inventory | Unknown counts must stay unknown |
| Provider delivery state | Real Jira/release/deployment states retrieved live | Actual queried issue/release set | Approval, merge, deployment and rollout remain different |

With a denominator of zero report **N/A**, never 0% or 100%. Do not turn an unknown into a pass, a fail, or a fabricated zero. For multiple products report separate denominators rather than one blended percentage.

## Reproduce the source evidence

For Markdown tables that meet the supported BA contracts, run:

    python extensions/angent-ba/scripts/extract_markdown_graph.py --urd extensions/angent-ba/examples/docs/atlas-re/atlas-re-urd.md --brd extensions/angent-ba/examples/docs/atlas-re/atlas-re-brd.md --prd extensions/angent-ba/examples/docs/atlas-re/atlas-re-prd.md --srs extensions/angent-ba/examples/docs/atlas-re/srs/atlas-re-spec.md --checklist extensions/angent-ba/examples/docs/atlas-re/test/checklist/atlas-re-checklist-index.md --cases extensions/angent-ba/examples/docs/atlas-re/test/testcases/atlas-re-testcase-index.md --root extensions/angent-ba/examples --output output/atlas-source-evidence.json

    python extensions/angent-ba/scripts/validate_artifacts.py output/atlas-source-evidence.json --source-root extensions/angent-ba/examples

Inspect lifecycle.per_requirement and unresolved_external_refs with actual proof paths, not only totals. The extractor reads source tables and reports links; it does not make business decisions, run tests or prove deployment. Unsupported input document formats require a clearly identified manual audit or reviewed transcription.

## Interpret conflicts before recommending action

If FR lineage exists but no TC artifact does, call it a **test specification gap**, not a runtime bug. If a TC exists without execution evidence, mark **execution unknown**, never passed.

When Jira Done contradicts Git or runtime status, preserve the actual observations and their revisions; ask which gate Jira's status represents. Never translate issue status into customer rollout without evidence.

Separate business-approved temporary waivers, with accountable owners and scope, from tested acceptance criteria. An intentionally deferred diagram is not automatically a release blocker.

Present decision-changing gaps first: affected FR or BO IDs, source links, whose decision is needed, what test would resolve it and measurable consequences when known. Keep other metadata available for review without overwhelming the reader.

## Presentation acceptance

Prose and a small table are normally clearer than a chart. A chart is justified only if population, time basis, units and underlying source values are consistent. The chart cannot hide unknown evidence or turn counts into an invented quality score.

A second reviewer must be able to reproduce every material status from pinned source files or actual provider responses, identify its uncertainty, and understand whether the next action is stakeholder validation, source repair, test execution or deployment checking. An attractive preview that fails this reproducibility standard is not an accepted dashboard.

## Representative evidence interpretation

The Atlas example has 58 source-linked BA artifact rows including six UN, four BO, six CAP and eight FR. The parser can prove four of eight FRs have explicit downstream test artifacts, but no production test execution or customer approval. Display **4/8 structurally linked** and **executed: unknown/not-proven**, not "50% quality" or "50% of the system works."

## Outcome

Deliver the smallest understandable view that answers what is complete, what is only proposed, what is blocked, why it matters and what action is next. State source scope, timestamps/revisions, uncovered requirements and limits. ANGENT Root keeps continuity and final recommendations; BA supplies disciplined indicators; Execution owns authorized writes and provider read-back. There is no compulsory singleton \`docs/_shared/dashboard.html\` or auto-regeneration of \`feature-list.md\`.

## Current source evidence—not a made-up green dashboard

For a scoped existing graph, obtain current handoff metrics with:

    python extensions/angent-ba/scripts/audit_lifecycle_handoffs.py PROJECT_GRAPH.json

Display inspected stage counts and the actual numerator and denominator, explicitly label not-inspected stages, and keep approved/implemented/executed as separate signals. A linked test artifact is *not* a passing test. A provider status panel requires current Jira/build/deployment results, not derivation from document rows.
