---
name: ak-ui-styling
description: Style product interfaces using the project's component system while preserving accessibility, tokens, responsiveness and component consistency.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# UI Styling — Portable Fallback

## Load progressively

- `references/component-system.md` — variants, primitives and reuse.
- `references/theming-accessibility.md` — tokens, dark/light, contrast and focus.

## Workflow

1. Inspect existing design tokens/components.
2. Map the requested UI to existing primitives.
3. Add variants rather than copy/paste one-off styles when reuse is real.
4. Preserve semantic structure and accessibility.
5. Handle responsive states and content overflow.
6. Preview real screens.
7. Remove inconsistent local styling when a system token/variant should own it.

Do not create new colors/radii/shadows merely to make a page look different.
