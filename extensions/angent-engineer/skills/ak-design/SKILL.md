---
name: ak-design
description: Design brand identities, logos, campaign graphics, posters, banners, social assets, icons and visual presentation systems from authentic brand evidence and production-aware visual principles.
license: MIT
metadata: {port: angent-fallback, mode: degraded, baseline: "AgentKit Engineer 2.19.0"}
---

# Design — Portable Fallback

Use for brand/graphic visual systems and assets. Use Frontend Design/UI Styling for application UI implementation.

The pinned upstream package contains bundled style datasets and generator scripts for several asset classes. The portable fallback preserves the **design workflow, deliverable knowledge and quality gates**, but does not pretend those packaged generators/datasets exist. Use a harness-native image/design capability when available or report the generation boundary.

## Load progressively

- `references/deliverable-routing.md` — logo/identity/banner/social/poster/icon/slides/campaign distinctions.
- `references/brand-system.md` — identity principles, tokens and system coherence.
- `references/brand-asset-authenticity.md` — existing-brand source-of-truth and rights boundary.
- `references/asset-production.md` — dimensions, export, print/digital constraints and generation.
- `references/design-review.md` — concept/craft/production critique.

## Brief

Resolve:
- artifact/deliverable;
- communication objective;
- audience/context;
- required copy/content;
- quantity/variants;
- physical/digital medium and exact dimensions;
- existing brand assets/source of truth;
- output formats/editability;
- rights/licensing/provider boundary for external/generated assets.

Do not fabricate an official logo, font, brand color or product asset because it is easy to generate.

## Workflow

1. Inspect authentic existing brand/reference assets and production constraints.
2. Route to the correct deliverable semantics.
3. Form the actual visual thesis from product meaning and audience recognition. Explain **which shape/composition mechanism communicates it**, not just which style adjective it resembles.
4. Explore materially different **concepts**, not merely palette/font changes or small geometric variations of one untested premise. When the user explicitly wants to preserve a chosen form, explore within that constraint instead.
5. Judge concepts against communication fit, distinctiveness, optical balance and real target reproduction; distinguish weak underlying symbol design from a production/detail defect. Select by evidence and accepted direction rather than personal preference.
6. Build reusable typography/color/grid/shape/image rules when the requested scope is a system.
7. Produce representative assets through the available design/image/vector/render capability.
8. Inspect the **exported/rendered result at real target size**, not only source/design canvas.
9. Iterate on causal concept/hierarchy/craft issues before micro-polish.
10. Document reusable identity rules only when future consistency requires them.

## Deliverable expectations

### Logo / mark
Test recognizability, silhouette, small size, monochrome, light/dark, lockups and production/vector suitability. Do not force initials/letters when another concept communicates better.

### CIP / identity
Extend an accepted identity into coherent typography, color roles, grid, imagery/icon language and representative applications. Mockups are evidence of application, not a substitute for actual reusable identity rules.

### Banner / social / poster
Design for the exact aspect ratio/viewing context. Preserve one focal hierarchy, safe zones, legibility, realistic copy and export fidelity.

### Icon
Verify viewBox/vector validity when SVG, optical alignment, clarity at requested sizes, color behavior and accessibility naming when used in UI.

### Slides
Treat a deck as a sequence of visual arguments, not independent decorated pages. Use the slide/presentation capability when the requested deliverable is an editable deck.

## Generated assets

When an external image/design model is used:
- provider/model availability is a runtime fact;
- never expose API keys;
- keep brand-critical text/logos controlled when generative text fidelity is unreliable;
- record provider/model only when needed for reproducibility;
- inspect text, anatomy, trademarks, logos and artifacts before delivery.

A generated draft is not accepted merely because the generation call succeeded.

## Boundary

The fallback does **not** claim parity with upstream bundled logo/CIP/poster/icon search datasets or generator scripts. Those are a real capability difference.

It does preserve the ability to reason about and direct the asset workflow using available harness-native generation/rendering tools.
