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

## Representative evidence interpretation

The Atlas example has 58 source-linked BA artifact rows including six UN, four BO, six CAP and eight FR. The parser can prove four of eight FRs have explicit downstream test artifacts, but no production test execution or customer approval. Display **4/8 structurally linked** and **executed: unknown/not-proven**, not "50% quality" or "50% of the system works."

## Outcome

Deliver the smallest understandable view that answers what is complete, what is only proposed, what is blocked, why it matters and what action is next. State source scope, timestamps/revisions, uncovered requirements and limits. ANGENT Root keeps continuity and final recommendations; BA supplies disciplined indicators; Execution owns authorized writes and provider read-back. There is no compulsory singleton \`docs/_shared/dashboard.html\` or auto-regeneration of \`feature-list.md\`.
