# React / TypeScript project adaptation

## Discover before prescribing

Inspect:
- React/framework version;
- build tooling;
- TypeScript settings;
- router;
- server/client rendering model;
- query/data library;
- form/validation library;
- component/design system;
- CSS/styling stack;
- testing/browser tools;
- import/file organization conventions.

Use those project contracts unless the task explicitly changes them.

## Components

Prefer:
- explicit props/types;
- semantic component ownership;
- existing primitives/variants;
- predictable state boundaries;
- cleanup for effects/subscriptions;
- lazy/code splitting when evidence shows a useful boundary.

Do not add memoization/callback wrappers automatically. Optimize from render/profile/contract evidence.

## Data and mutations

Preserve:
- canonical query/cache keys;
- request/response schema;
- loading/empty/error states;
- cancellation/race handling when material;
- optimistic update rollback and cache reconciliation;
- auth/permission failure behavior.

Do not point tests at production/live mutation endpoints without explicit authority.

## Routing

Use the installed router/framework idioms and exact version.

Check:
- route params/query validation;
- loader/data dependencies;
- auth/permission gates;
- not-found/error boundaries;
- navigation state.

## Accessibility and UI state

Keyboard/focus, labels/errors, semantic roles, touch targets, responsive overflow and reduced motion belong to implementation, not only visual review.

## Performance

Measure before optimizing:
- rerender cost;
- expensive computation;
- bundle/code split;
- network waterfalls;
- image/font assets;
- list virtualization;
- browser main thread.

A generic "useMemo/useCallback everywhere" policy can add complexity without improving performance.
