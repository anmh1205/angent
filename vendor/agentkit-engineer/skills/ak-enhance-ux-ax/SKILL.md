---
name: ak-enhance-ux-ax
description: Review an existing site or app for both human UX quality and AI/search discoverability, produce ranked fixes with a DONE contract, and optionally implement and verify them when authorized.
metadata: {port: angent-fallback, mode: adapted}
---

# Enhance UX/AX — Portable Fallback

Use for a combined review of:
- **UX** — clarity, hierarchy, brand recall, trust, interaction, responsiveness, accessibility and product feel;
- **AX** — whether agents/search systems can crawl, parse, quote, identify canonical content, and understand the public surface.

Read `references/review-contract.md`.

## Modes

### Default — review only

Inspect the actual product/code/rendered surface and produce ranked findings plus an explicit DONE contract.

Do not edit merely because tools are available.

### `--auto`

Only when implementation is authorized:
1. complete the review first;
2. implement ranked Must and Should items within scope;
3. verify build/lint/test and the affected rendered/discovery surfaces;
4. stop on destructive/irreversible changes that need separate authority.

### `--loop [N]`

Run bounded review → implement → verify rounds. Default to three only when the user invokes loop semantics without another limit.

Do not continue a round when there is no actionable evidence or when verification is blocked.

## Runtime boundary

Rendered UX review requires a real browser/rendered surface; screenshot critique requires vision.

AX checks require access to the reachable public/dev surface or its source/routes.

If a required check cannot run, record it as **not verified**, never as PASS.

Use existing design-system/template components before inventing replacements.

Use `ak-frontend-design` for UI-only design work and a dedicated SEO workflow when search-only analysis is the real outcome.
