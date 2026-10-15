---
name: ak-frontend-development
description: Implement React/TypeScript frontend behavior using the project's actual component, routing, data, state and styling contracts with complete UI states and browser-aware verification.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Frontend Development — Portable Fallback

Use for React/TypeScript component/application implementation.

The pinned upstream package contains project-specific MUI/TanStack conventions. The portable fallback preserves the underlying engineering capability while **deriving exact libraries/patterns from the current project** instead of forcing those package-specific defaults.

Read `references/react-project-adaptation.md`.

## Contract

Resolve:
- user-visible behavior;
- component/public APIs;
- route/query/cache/server contracts;
- auth/permissions;
- design tokens/shared primitives;
- loading/empty/error/success states;
- keyboard/pointer/responsive behavior;
- file/dependency/network/process authority;
- required verification.

## Workflow

1. Inspect `AGENTS.md`, package/framework versions, current component/data/router/styling patterns and tests.
2. Identify component/state ownership and server/client boundary.
3. Reuse project primitives/tokens/query keys/router conventions before adding alternatives.
4. Implement all relevant UI/data states, not only happy-path render.
5. Keep asynchronous mutation/error/rollback/cache behavior explicit.
6. Preserve accessibility and responsive behavior.
7. Add/update tests at the cheapest layer that establishes behavior.
8. Run type/build/test and browser/render checks proportional to the change.
9. Measure before applying non-trivial performance optimizations.
10. Report package/lock/generated-file impact and any runtime/browser verification gap.

## Effects

Package installation, dev servers, browser automation and calls to live APIs can produce network/process/remote-data effects.

Do not infer permission for those effects from an implementation request. Resolve endpoint/account/fixture and authority when material.

## Boundary

Use Frontend Design for visual concept/fidelity decisions and UI Styling for component-level styling-system work.

Do not hard-code upstream-specific MUI/TanStack aliases/patterns into an unrelated project.

A source-level implementation is not visually verified when rendered inspection is available but not performed.
