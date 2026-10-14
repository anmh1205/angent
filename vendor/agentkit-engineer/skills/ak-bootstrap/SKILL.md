---
name: ak-bootstrap
description: Bootstrap a new project from an accepted product contract through evidence-grounded stack/design decisions, planning, implementation, testing, review and onboarding.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Bootstrap — Portable Fallback

Use for a new project or substantial greenfield subsystem, not for a bounded change to an established project.

Read `references/project-bootstrap.md`.

## Opening contract

Before Git initialization, research, scaffolding or design, establish:
- product outcome and intended users;
- required surfaces (web/mobile/CLI/API/MCP/library/etc.);
- constraints: stack, compatibility, security, licensing, delivery;
- explicit non-goals;
- observable acceptance criteria/definition of done;
- authority for Git initialization, external research, provider/deployment effects.

Reuse an accepted brief when it already contains these fields. Ask only about missing decisions that materially change the product or safety.

## Modes

- **full** — research material choices and keep meaningful user decision gates.
- **auto** — explicit opt-in to continue through authorized routine decisions; design/authority boundaries still stop.
- **fast** — use established requirements/stack where possible; skip low-value research, not acceptance/review.
- **parallel** — research/implementation branches may run concurrently only with proven independence.

Modes change effort and interaction, not requested scope or effect authority.

## Workflow

1. Inspect destination and existing files before scaffolding; do not reset/recreate an existing project blindly.
2. Initialize Git only when appropriate and authorized.
3. Research only material open questions.
4. Select stack/architecture from the contract and evidence.
5. Create interface/design evidence appropriate to the product surface.
6. Produce/accept the implementation plan for the stable-2.19 workflow and hand it to Cook.
7. Implement through Cook; do not bypass its testing/review semantics.
8. Run independent code review and repair blocking findings.
9. Update only documentation needed for setup, architecture/contracts and onboarding.
10. Verify a thin end-to-end user/client path plus project-native checks.
11. Release/deploy only if the accepted contract explicitly includes it and provider authority is available.
12. Finish with onboarding, known constraints and unresolved decisions.

The stable public documentation may evolve orchestration details independently of the pinned package. This fallback follows the pinned 2.19.0 package semantics unless the baseline is intentionally refreshed.

## Output

A good bootstrap ends with a working, tested, reviewed and understandable foundation—not merely a folder scaffold or generated boilerplate.
