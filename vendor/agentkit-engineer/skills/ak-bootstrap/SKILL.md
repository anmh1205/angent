---
name: ak-bootstrap
description: Take a new project from an accepted outcome through research, stack/design decisions, implementation, verification, review, UX/AX enhancement where applicable, and optional authorized delivery.
metadata: {port: angent-fallback, mode: adapted}
---

# Bootstrap — Portable Fallback

Use for a new project or substantial greenfield subsystem.

Use `ak-cook` for an existing project with a clear bounded change, `ak-brainstorm` when direction is not yet settled, and `ak-plan` when the requested endpoint is only a plan.

## Modes

Preserve the current stable intent of the four modes:

- **auto** — default; after the opening contract is locked, make ordinary research/stack/design decisions autonomously and continue through authorized implementation/verification, stopping at real authority/safety/spend/credential boundaries;
- **full** — surface missing material requirements and pause for material stack/design decisions that the user has not already settled;
- **fast** — reduce research/setup overhead by grouping independent research where safe, while preserving implementation, test, review, and authority gates;
- **parallel** — build a dependency graph and use non-overlapping implementation ownership only when the active harness can support the required isolation/delegation honestly.

`--ask` changes how the opening contract is resolved; it is not a mode.

Options such as YAGNI or stronger review depth may compose only when the current installed upstream/fallback workflow supports them. Do not reconstruct unknown flags from memory.

Modes change effort/routing, not effect authority.

## Workflow

1. Lock the project contract: outcome, constraints, non-goals, acceptance criteria, definition of done, surfaces, and delivery boundary.
2. Inspect the actual destination/Git state; reuse an existing project rather than re-scaffolding or resetting it.
3. Research only material current/versioned choices at the depth implied by the selected mode.
4. Select stack/design consistent with accepted constraints and established project/user decisions.
5. Produce design/interface evidence where the product surface warrants it.
6. Implement through the project/fallback implementation workflow; do not add a ceremonial planning phase when the accepted contract already provides enough structure.
7. Run project-native tests and independent code review; blocking findings return to implementation/diagnosis rather than being waived.
8. For a web surface, run the combined UX/AX workflow when the selected mode/current contract calls for it and the required browser/vision/discovery checks are available; missing checks remain visible gaps.
9. Release/deploy only when the accepted contract explicitly includes delivery and the concrete provider effects remain authorized.
10. Finish with documentation/onboarding impact, verified endpoint state, remaining risks, and an evidence-bounded handoff.

## Parallel/runtime boundary

Parallel mode requires separable dependencies and exclusive/non-overlapping ownership.

Worktrees or separate workers reduce edit collisions; they are not OS sandboxes.

If the active harness lacks the delegation/isolation needed for the requested parallel semantics, do not pretend parallel execution occurred. Choose an explicitly accepted sequential/degraded route or return the capability gap.

## Completion

A complete bootstrap is a working foundation at the authorized endpoint, not merely a scaffold, passing build, or attractive screenshot.

Keep blocking test, review, UX/AX, onboarding, and delivery findings visible according to the accepted contract.

Automatic execution never grants unrelated authority over credentials, destructive actions, spend, publication, push, or deployment.
