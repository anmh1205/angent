---
name: ak-markdown-novel-viewer
description: Present long Markdown in a calm browser reading view for editorial review, with a portable fallback to any available Markdown/HTML preview surface.
metadata: {port: angent-fallback, mode: adapted}
---

# Markdown Reader — Portable Fallback

Use when long-form Markdown needs human reading/review rather than source editing.

## Behavior

Prefer a local read-only HTTP/HTML viewer with:
- readable measure and typography;
- heading navigation;
- code/table support;
- no mutation of source;
- automatic reload when useful.

If no viewer helper exists, render Markdown to HTML or use the harness' preview capability.

Do not persist private documents to a public hosting service merely for preview.
