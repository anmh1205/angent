---
name: ak-bootstrap
description: Take a new project from an accepted outcome through stack/design decisions, implementation, verification, review, and optional authorized delivery.
metadata: {port: angent-fallback, mode: adapted}
---

# Bootstrap — Portable Fallback

Use for a new project or substantial greenfield subsystem.

Use `ak-cook` for an existing project with a clear bounded change, and `ak-plan` when the user wants only a plan.

## Modes

- **auto** — after the opening contract is sufficiently established, continue through authorized runnable work and stop only at real decision/authority/safety/blocker boundaries;
- **full** — explicitly surface missing material requirements, stack, and design decisions before implementation.

Do not invent deprecated fast/parallel modes. Parallelism is a planning/execution property used only when independent work and the active harness justify it.

## Workflow

1. Lock the project contract: outcome, constraints, non-goals, acceptance evidence, delivery boundary.
2. Inspect the actual destination/Git state; reuse an existing project rather than re-scaffolding it.
3. Research only material current/versioned choices.
4. Select stack/design consistent with accepted constraints and existing preferences.
5. Produce visual/interface evidence when the product surface warrants it.
6. Implement through the project/fallback implementation workflow; size the implementation plan to the work rather than forcing a separate plan phase.
7. Run project-native tests and independent code review.
8. For a web surface, run combined UX/AX enhancement when it adds value and authority permits the selected mode.
9. Release/deploy only when the accepted contract explicitly includes delivery.
10. Finish with documentation/onboarding impact and an evidence-bounded handoff.

A complete bootstrap is a working verified foundation at the authorized endpoint, not merely a scaffold.

Blocking test/review/UX findings remain blockers. Do not weaken the gate to call the project done.
