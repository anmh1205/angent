---
name: ak-ui-styling
description: Implement or refine component-level React UI styling with the project's actual tokens/primitives, responsive behavior, interaction states and accessibility, including safe shadcn/Tailwind adaptation when present.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# UI Styling — Portable Fallback

Use for component/system styling implementation. Use UI/UX Pro Max for product-level design reasoning; Frontend Design when a whole visual direction/reference implementation is primary.

## Load progressively

- `references/component-system.md` — variants, primitives and reuse.
- `references/theming-accessibility.md` — tokens, light/dark, contrast and focus.
- `references/mutation-and-visual-gates.md` — package/config/file boundaries and render verification.

## Prepare

Inspect:
- framework/version;
- component system (including shadcn/Radix when present);
- Tailwind/CSS version/config;
- semantic tokens/theme source;
- aliases/file ownership;
- protected/generated files;
- supported breakpoints/states.

Define what files, package manifests, lockfiles, global CSS and config may change.

Do not initialize/overwrite a component system merely because a helper could.

## Workflow

1. Map the request to existing primitives/tokens/variants.
2. Define default, hover, focus, active/pressed, disabled, loading, empty/error and dark/light states that apply.
3. Use semantic HTML/accessible primitives before decoration.
4. Add reusable variants when reuse is real; avoid page-local copy/paste forks.
5. Implement responsive behavior based on content/task constraints.
6. Preserve visible focus, contrast, touch target, labels/error semantics and reduced motion.
7. Render/test representative states and viewports.
8. Remove conflicting one-off overrides when the design system should own the behavior.

## shadcn/Tailwind path

When the project uses them:
- inspect `components.json`, existing generated components, Tailwind version/config and package manager;
- preview/limit component-generation scope when possible;
- do not overwrite an existing customized component/config without explicit intent;
- remember package CLIs can use network, lifecycle scripts and modify lockfiles/dependencies.

Use current project-native commands, not hard-coded upstream helper scripts.

## Completion

Report changed components/tokens/config/dependencies plus rendered/accessibility verification.

A reference recommendation without runtime/render evidence is not proof that the implemented UI is correct.
