---
name: ak-document-skills
description: Route creation, editing and inspection of DOCX, PDF, PPTX and XLSX artifacts to the active format-specific capabilities with destination-aware verification.
metadata: {port: angent-fallback, mode: adapted}
---

# Document Skills — Portable Fallback

This is a format router and quality layer, not one monolithic conversion script.

## Load progressively

- `references/docx.md` — structured documents.
- `references/pdf.md` — PDF creation/inspection/render checks.
- `references/slides.md` — presentation narrative/layout.
- `references/spreadsheets.md` — formulas, tables, charts and workbook integrity.

## Route

Use the active harness' native document/PDF/presentation/spreadsheet capability.

Do not use a generic document converter when a structured editor is available.

## Common workflow

1. Identify required destination and editability.
2. Read the source using the most structured representation available.
3. Preserve semantic structure while adapting to destination constraints.
4. Generate/edit with the format-specific tool.
5. Read back/render the result.
6. Verify content, hierarchy, tables/media, links and layout.

## Boundary

If a requested feature cannot be represented faithfully in the destination, return to Authoring/Format for an alternative rather than silently dropping information.

Avoid OCR unless the source cannot expose text/structure otherwise.
