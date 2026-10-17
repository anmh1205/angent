---
name: ba-roadmap
description: Produce a decision-grounded product roadmap with source-backed priority, actual capacity constraints, alternative scenarios and dependency-aware milestones.
---

# Product roadmap: sequencing justified by evidence, not fabricated scores

**Method origin:** Independently adapted from the MIT [Dev BA Kit Roadmap method](https://github.com/nv-minh/dev-ba-kit/blob/main/skills/roadmap/SKILL.md), Edward Ngo (2026). The IIBA BACCM and public product-analysis practices emphasize value for stakeholders in context, while roadmap sequencing also depends on the organization's change capacity and external dependencies.

## Input hierarchy

Read the accepted product vision, opportunity findings, current feature map and CAP/BO/UN decisions, existing roadmap, delivery capacity and commitments, actual blockers, release gates and provider/customer deadlines. Identify which commitments are already made; a scoring spreadsheet cannot erase legal, safety or operational prerequisites. Separate current shipped features, in-progress items, validated future opportunities and untested ideas.

## Decision procedure

1. Build a candidate table with stable feature/CAP IDs and the actual BO/value they serve. Drop duplicates and note incompatible alternative implementations rather than ranking them as independent must-do features.
2. Define a common scoring unit only when data supports it. For RICE, **Reach** is users/events per same time horizon, **Impact** is a declared common unit, **Confidence** a proportion 0–1, and **Effort** person-time or a consistent relative unit. Do not combine an unnormalized 1–5 "reach" with a percentage for some rows and treat the results as comparable.
3. Compute \`(Reach × Impact × Confidence) / Effort\` only for candidates with sourced numbers and a stated horizon/unit. Missing or weakly supported inputs must remain unscored/low-confidence, not arbitrary zero or invented point estimates. Record source and uncertainty for each value.
4. Evaluate constraints **separately from the score**: skills and team capacity, test environment, regulatory/safety/privacy requirements, integration availability, device lead time, operational support and external stakeholder readiness.
5. Build a dependency graph with typed prerequisites (technology, data, people, vendor, compliance and validated customer needs). Detect cycles or impossible ordering before assigning dates. A dependency from a feature to its own downstream release is an error, not evidence of readiness.
6. Construct a Now/Next/Later roadmap for uncertain planning or dated milestones when actual capacity and deadlines justify dates. "Now" is a meaningful active commitment only when owner, capacity, scope and next acceptance checkpoint are grounded; distinguish candidate from committed.
7. For each proposed milestone define scope (CAP IDs), outcome, verifiable acceptance, owner, dependencies, status and an explicit contingency/rollback decision. Schedule uncertainty should remain visible rather than being represented as an exact delivery date.
8. Compare at least two relevant scenarios when the business decision warrants it: earliest customer feedback versus risk reduction, or build versus integrate. Explain what priority changes under different reach/cost assumptions.
9. On updates, reconcile actual progress from Jira/Git/deploy provider facts if connected. An issue marked Done is not automatically delivered to customers; a test in a mock environment is not release evidence. Preserve prior decision history and explain changes, rather than silently recomputing a new score order.

## What to deliver

A coherent roadmap document or management summary: intended value and planning horizon; sourced scoring table or justified unscored candidates; ranked recommendations; a dependency-aware Now/Next/Later or milestone view; risks and capacity constraints; explicit decision log; major assumptions; next review trigger. Only add a diagram when its dependencies or timeline are too complex for readable prose. Retain the existing project layout instead of imposing \`docs/_product/roadmap.md\`.

## Example

For a hypothetical rental-vehicle system, an operator may value access control, telemetry freshness and ECU fault diagnostics. Customer onboarding and reliable device installation may be prerequisites before rollout, regardless of a high estimated feature score. If no verified reach/impact/capacity data exists, recommend a bounded pilot and decision gates, not fictional quarterly delivery dates.

## Acceptance and authority

Every prioritized item should have an identifiable sponsor/customer value, scored or explicitly unscored evidence, relevant dependencies, feasible ownership and a reason why that order produces better outcomes. ANGENT Root holds task and business decision authority; BA provides specialist prioritization and dependency analysis; Execution performs only authorized edits; Quality checks math/evidence and user-facing readability.
