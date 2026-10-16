---
name: angent-frontend-design
description: Choose and realize a cohesive frontend visual direction for a real product screen or website, including typography, layout, color, motion and verified imagery; use after ANGENT has established the task and design constraints.
---

# ANGENT Frontend — visual direction and implementation judgment

This is a **specialist extension of ANGENT**, not a parallel root agent, design-system replacement or standalone plugin. ANGENT decides when the task requires visual art direction. Do not invoke for unrelated coding, generic technical explanation or product-workflow diagnosis that belongs to `ak-ui-ux-pro-max`.

## Understand the product and design baseline

Before proposing styles, identify the real user task, page/screen, audience, brand voice, existing design system, approved visual references and framework constraints. Inspect existing UI/code or screenshots when available. Determine whether the request is a fresh visual concept, an in-system screen, a redesign, or a fidelity repair. A strong current style is a constraint to preserve, not an invitation to re-theme every page.

Aesthetic distinctiveness must improve orientation, character and legibility. Do not require unusual fonts, asymmetric layouts, a signature gimmick, expensive animation or any predetermined visual trend. Design direction is a choice justified by the product, not a random style name.

## Select and apply a coherent art direction

Read `references/aesthetic-directions.md` when visual exploration or style translation matters. Use the reference catalogue as a **vocabulary of mechanisms**, not a menu that must be exhausted. When the choice is open, compare a few genuinely distinct directions against brand, audience, accessibility, expected content density and maintenance. Then choose one coherent basis (or retain the established system), describing its typography hierarchy, spatial rhythm, grid behavior, color relationships, surface treatment, imagery and interaction character.

Translate the selected direction into implementation decisions:
- layout and typography for the actual content hierarchy, including empty/loading/error and long-copy states;
- semantic components and tokens aligned with the existing design system;
- responsive behavior across relevant widths and input methods; no overflow or clipped content;
- contrast, keyboard/focus behavior, hit targets, accessible semantics, reduced-motion alternatives;
- motion only where it clarifies hierarchy, feedback or identity within performance constraints.

If the request is to **implement**, apply the selected art direction using the project's real framework and components, not only a prompt or attractive HTML excerpt. Delegate technical implementation to existing Engineer capabilities when useful; no code or external effect without task authority.

## Imagery and visual evidence

Read `references/imagery-and-verification.md` when imagery or visual proof matters. Match assets to the product and context: real photograph, genuine product/UI imagery, purpose-built illustration or no image. Verify external assets and their reuse constraints; never fabricate working image URLs or claim a generated prompt is an image. Distinguish illustrative mockups from real implementation evidence.

## Verification and boundaries

Inspect the rendered interface when the runtime permits. Compare it to the requested baseline at relevant viewport widths and interactive states; check accessibility and performance implications. If only source/code is accessible, state the missing rendered verification. A polished hero cannot compensate for broken navigation, forms, loading states or mobile usability.

Pass final observations through ANGENT Reasoning/Quality. This extension contributes visual expertise, not an independent approval gate, model persona or new workflow controller.
