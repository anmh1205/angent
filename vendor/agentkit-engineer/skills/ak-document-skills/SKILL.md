---
name: ak-document-skills
description: Route Word, PDF, PowerPoint and spreadsheet tasks to real native format skills/tools with source fidelity, editable structure and rendered quality gates.
metadata: {port: angent-fallback, mode: adapted}
---

# Document Skills — Portable Format Router

The stable Engineer 2.19.0 Document Skills entrypoint is a **thin index** into a large package (about 130 Word/PDF/presentation/spreadsheet references and scripts). It is not a generic one-command document converter. In ANGENT, route to the host's **actually installed** document-specific capabilities; a standalone Markdown fallback is not a replacement for all bundled parsers and Office renderers.

## Route by destination

- **DOCX**: semantic paragraphs, styles/sections, tables, footnotes, headers/footers, tracked/revision behavior and editable fields. Follow the installed document authoring skill.
- **PDF**: distinguish text-extractable from scanned PDF; preserve page geometry, embedded fonts, searchable text and visual page review. Use the installed PDF skill/renderer; OCR only as a last resort.
- **PPTX/slides**: preserve editable object hierarchy, speaker notes, slide masters/themes, visual hierarchy and the requested presentation flow; inspect rendered slides for clipping and overlap.
- **XLSX/spreadsheet**: preserve values/formulas, references, named ranges, data types, date/number formats, tables/charts, workbook links and recalculation state. Use spreadsheet-native tooling rather than converting through PDF or document editors.

## Common workflow

1. Determine input source, required format, editability and what must remain unchanged. Inspect source with structured APIs before considering OCR or visual inference.
2. Choose the corresponding native format skill or connected editor; read its actual operating instructions and tool capabilities. Never infer tool support solely from this entrypoint.
3. Modify only the requested semantic structure; retain data/formula correctness, citations, objects and links.
4. Save the requested real artifact through an available authorized file workflow, then reopen it and validate machine-readable structure **and** rendered output at representative pages/slides/sheets.
5. Distinguish produced file, inspected structure, visually reviewed render and user-visible download link as separate facts. A filename without a real backing file is not a deliverable.

## Important boundary

Destination conversion cannot silently discard tables, figures, formulas, diagram editability or long-form explanation. If a format cannot represent a key requirement faithfully, communicate the trade-off and choose a supported output with user authority. The large upstream reference/script pack is optional when capable host-native engines are available, not proven present by identity matching.
