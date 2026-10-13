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
6. Create a files-first plan with phases, dependencies and verification.
7. Validate the plan against the original issue.
8. Optionally publish/link the plan in the issue when authorized.

Do not hard-require an HTML/wiki rendering format.

The plan artifact and issue link are useful projections; strategic ownership remains with ANGENT Reasoning.
