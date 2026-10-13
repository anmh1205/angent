---
name: ak-stitch
description: Use Google Stitch when available for AI-assisted UI exploration/export, with a portable fallback to ANGENT design and frontend implementation workflows.
license: MIT
metadata: {port: angent-fallback, mode: degraded}
---

# Stitch — Portable Fallback

Read `references/import-normalization.md`.

## Native path

If Google Stitch is available, use its current official workflow for design generation/export.

## Fallback path

Use:
- AI Artist/visual generation for concept exploration;
- Frontend Design for system extraction;
- UI Styling/Frontend Development for production implementation.

## Rule

Generated UI is a draft/reference, not production architecture.

Normalize tokens/components/state behavior into the project's design system.

Do not claim Stitch-specific exports when the provider is unavailable.
