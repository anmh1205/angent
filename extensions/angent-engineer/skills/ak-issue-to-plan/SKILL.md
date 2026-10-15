---
name: ak-issue-to-plan
description: Convert an issue into a validated implementation plan by reading the issue, scouting the codebase, resolving design uncertainty and producing auditable phases.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Issue to Plan — Portable Fallback

Use for GitHub/Jira/other issue records that need to become an implementation-ready plan.

## Workflow

1. Read the issue and linked evidence.
2. Extract acceptance criteria, constraints and ambiguity.
3. Scout the codebase and relevant AGENTS.md.
4. Brainstorm only if a material design choice is still open.
5. Resolve or explicitly preserve blocking uncertainty.
6. Create a plan in the project's **authoritative planning source** (an existing issue/spec/plan or project files), with phases, dependencies and verification; avoid competing stores.
7. Validate the plan against the original issue.
8. Optionally publish/link the plan in the issue when authorized.

Do not hard-require an HTML/wiki rendering format.

The plan and issue link must have an explicit canonical owner. When the issue/spec is itself authoritative, develop and link the implementation reasoning there instead of generating redundant phase files. Strategic trade-offs and unresolved decisions remain with ANGENT Reasoning.

## Stable 2.19.0 issue audit and stop gate
Use a specific GitHub issue at an observed revision and recover linked discussions, accepted outcome, actual constraints and DONE tests. Map the issue against current repository ownership, instructions, code and tests. Differentiate confirmed gaps, design alternatives and unanswered stakeholder decisions. Use bounded advice/brainstorm for unresolved architectural choices, not silent assumptions.

Produce a phased **durable plan** in the source actually owned by this project, with affected source/test paths, exact inputs/outputs, dependencies, risk, migration/rollback where relevant and verification evidence. Reconcile its acceptance criteria with the original issue before claiming readiness. **Stop at the plan's decision gate**; this workflow does not implement. Comment/link to the issue only if explicitly authorized and only after confirming current provider state. A plan artifact or issue comment is not proof of completed code.
