---
name: ak-frontend-design
description: Turn an approved brief, screenshot or video reference into a distinctive implementation-ready or working frontend interface with explicit aesthetic direction, complete states, accessibility and rendered visual verification.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Frontend Design — Portable Fallback

Use when visual fidelity/interface craft is a primary outcome.

Use Frontend Development when the main problem is component behavior, routing, data/state integration. Use UI/UX Pro Max for product-level design reasoning/audit.

## Load progressively

- `references/design-system-audit.md` — extract/reuse current/template grammar.
- `references/craft-direction.md` — prevent generic mode-collapse and define a coherent visual thesis.
- `references/states-responsive.md` — interaction/accessibility/responsive completeness.
- `references/reference-replication.md` — learn from screenshot/live/template evidence.
- harness-native image/media/browser capability when required.

## Brief and evidence

Resolve:
- user/audience task;
- content/information hierarchy;
- brand/reference assets and permission to reproduce;
- framework/component system;
- target viewport/browser/device;
- interaction and responsive states;
- editable file boundary;
- acceptance evidence.

For screenshot/video replication, identify the source viewport/state and whether the goal is faithful reproduction or an approved redesign.

## Decision procedure

1. Inspect current product/template/design system and rendered state.
2. Extract visual grammar: layout, type, color roles, surfaces, radius/depth, imagery, iconography, density, motion.
3. State one visual thesis/direction derived from the content/brand instead of falling back to a category stereotype.
4. Identify the memorable/focal element and the main hierarchy.
5. Map complete UI states and responsive behavior before polishing.
6. Reuse strong primitives/patterns before inventing local components.
7. Implement/prototype using the actual stack when code delivery is in scope.
8. Render at representative viewports and inspect actual pixels/interaction/accessibility.
9. Fix systematic design errors first, local polish second.
10. Run the craft/accessibility self-review before delivery.

## Anti-template discipline

Avoid generic "AI-made" composition caused by mode collapse:
- same centered hero/card-grid structure for unrelated products;
- decoration standing in for hierarchy;
- fake status/meta labels;
- arbitrary gradients/glass/cards;
- copy/template placeholders;
- repeated page sections with identical composition.

This is not a lexical/style blacklist. Existing brand requirements or a justified product pattern can override a default heuristic.

The test is whether the visual form follows the actual content, brand and interaction job.

## Accessibility and interaction

At minimum consider:
- semantic structure;
- keyboard/focus-visible;
- pointer/touch targets;
- contrast;
- reduced motion;
- loading/empty/error/success/permission states;
- long/realistic content;
- mobile/tablet/desktop re-composition.

Responsive design may change hierarchy/navigation, not only shrink columns.

## Reference replication

Compare the **rendered local result** with the supplied reference at matching states/viewports.

Reuse design mechanisms (layout/state/component grammar) rather than only matching colors. Respect licensing and avoid copying irrelevant structure/content.

## Completion

Deliver:
- implemented/prototyped interface or implementation-ready guidance as requested;
- extracted/created system decisions;
- state/responsive matrix;
- rendered visual evidence when tools exist;
- accessibility checks;
- known gaps when browser/image/render capability is unavailable.

Source code that "looks right" without rendered inspection is not visual verification.
