---
name: ak-ui-ux-pro-max
description: Build or review a product UI decision system across hierarchy, layout, typography, color, interaction, accessibility, responsive behavior, forms/charts and performance; preserve approved rules and verify implementation.
metadata: {port: angent-fallback, mode: degraded, baseline: "AgentKit Engineer 2.19.0"}
---

# UI/UX Pro Max — Portable Fallback

Use for product-level UI/UX direction or comprehensive audit.

The pinned upstream capability includes bundled design-recommendation datasets/search tooling. This fallback preserves the **decision model, audit dimensions, persistence and verification workflow**, but does not claim access to the same packaged dataset/search engine.

## Workflow

1. Establish user/product task, surface, audience, brand/system constraints and acceptance evidence.
2. Inspect actual rendered UI plus relevant code/design tokens when available.
3. Reuse accepted product/design-system decisions before applying general guidance.
4. Analyze only dimensions relevant to the task:
   - information hierarchy/navigation;
   - layout/grid/density;
   - typography;
   - color/contrast/theme;
   - components/states;
   - forms/validation;
   - tables/charts/data density;
   - responsive/mobile behavior;
   - accessibility/keyboard/reduced motion;
   - interaction/feedback/motion;
   - performance/asset implications;
   - content clarity.
5. Separate **systemic design-system findings** from page-local issues.
6. Produce prioritized recommendations with rationale, examples and implementation consequences.
7. Persist approved master rules/page overrides only when the product needs durable design guidance.
8. After implementation, inspect rendered states again; a recommendation is not verification.

## Recommendation evidence

Bundled/static design knowledge is guidance, not a live standard.

When freshness matters—WCAG/browser/platform/framework guidance—use current authoritative sources.

When a strong reference/template exists, compare concrete component/page/state mechanisms instead of generic best-practice lists.

## Output

Return:
- chosen/recommended direction;
- system/tokens/rules affected;
- ranked systemic vs local findings;
- state/responsive/accessibility requirements;
- implementation guidance;
- verification plan/evidence;
- unresolved trade-offs.

## Degraded boundary

The fallback does not reproduce upstream packaged CSV/search recommendation datasets. Do not report exact "database recommendation parity."

Use project evidence, accepted references and current authoritative guidance instead.
