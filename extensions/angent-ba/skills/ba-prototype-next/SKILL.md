---
name: ba-prototype-next
description: Specialized ANGENT business-analysis procedure for prototype-next.
---

# Build a reviewable Next.js prototype from accepted BA flows

## Distinction

A prototype demonstrates decisions and user paths; it is **not** proof that backend logic, data persistence, authentication or security is production-ready. Use an authorized existing Next.js repo if one exists, rather than installing a different stack or rewriting the project's agreed UI foundation.

## Build procedure

1. Read the accepted screen inventory, userflow, wireframe, SRS, error matrix and style constraints. Capture a screen-state matrix: route, user role, inputs, validation, loading, empty, success, error, denied and expired-session states.
2. Inspect package.json, router type (App Router or Pages Router), TypeScript, components, tokens, styling, test tooling, images and lockfile. Respect the current project baseline; ask only if a consequential platform choice is unsettled.
3. Define route contracts before styling. For each action record trigger, locally simulated state transition, data mutation (in-memory/mock), validation outcome and accessibility focus target. Mark real integrations as mocks visibly in the code and demo notes.
4. Implement screen components by reusing existing primitives; avoid duplicating form validation rules across pages. Maintain explicit fixture lifecycle and a reset action so reviewers can reproduce scenarios.
5. Implement all mapped alternate outcomes, including invalid input, authorization denial, stale session, network error, duplicate submit, interrupted flow and recovery; do not show a visual screen disconnected from any navigation.
6. Verify keyboard labels, semantic forms, tab order, announcements, zoom and responsive widths. No fake submit success that silently accepts all inputs.
7. Execute the existing install/build/typecheck/test commands if the host permits; inspect rendered routes in a browser at representative viewports. Record command, exit code, environment, scope and observed failure.
8. Deliver the file diff, route map, state coverage table, screenshots or browser references where available, setup command and explicit unimplemented backend boundaries.

## Core acceptance

Every route in the flow loads, required transitions are reachable, fixture reset works, no unsupported data claim is shown, no browser errors occur in tested paths, and build/runtime status is reported from actual execution. If tooling is absent, produce a design specification rather than asserting a runnable prototype.

## Example

An email-login prototype must expose wrong-password, locked-account, session timeout and transient network error as distinct states where the accepted SRS distinguishes them. It must not invent a threshold or reveal whether an email exists if the policy forbids account enumeration.


## ANGENT cooperation

ANGENT Root/Reasoning owns interpretation and decisions; Authoring owns narrative quality; Execution handles authorized external effects; Quality verifies the outcome. Method selection is optional and context-dependent, never a forced workflow.
