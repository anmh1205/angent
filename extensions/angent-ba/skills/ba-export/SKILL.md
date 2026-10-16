---
name: ba-export
description: Export actual reviewed Markdown BA documents as provenance-linked MD, HTML and DOCX with optional real PDF engine.
---

# Stakeholder document export with real file verification

**Source methodology:** Maintained adaptation of MIT Dev BA Kit (Edward Ngo), https://github.com/nv-minh/dev-ba-kit/blob/main/skills/export/SKILL.md. Portable exporter is an independent ANGENT implementation.

## Prepare the export

1. Identify an explicitly authorized feature or stakeholder scope; read the actual accepted documents and their revision. Select only the relevant files in narrative order: buyer/problem, URD, business objectives, feature PRD, SRS/error paths, use cases/AC, tests and outstanding decisions.
2. Validate document sources for stale template tokens, invalid links, missing referenced files and source conflicts. An export is a snapshot, not a new source of truth or a substitute for peer review.
3. Choose format and audience. The command accepts **explicit Markdown paths** under a root, records SHA-256 of each, and never silently scans a vault or pulls hidden documents.
4. Generate the *actual file*. For HTML, DOCX and PDF, an installed Pandoc CLI is required; HTML is sandboxed with raw HTML/TeX disabled and a conservative CSP. DOCX is verified as a real OOXML archive; PDF requires an available PDF engine and is accepted only if the output has a PDF header.
5. Run a real viewer/open/read-back check. Confirm section order, source links, typography, tables, Vietnamese text and any needed accessible navigation. A successful Pandoc exit is not enough for a high-stakes stakeholder document.
6. Report the exact output file, format, source revisions/hash list, commands, checks that ran, failures and excluded materials. Never publish a sensitive export to a provider not authorized by the user.

## Commands from ANGENT repository root

    python extensions/angent-ba/scripts/build_export.py docs/atlas-re/atlas-re-urd.md docs/atlas-re/atlas-re-brd.md docs/atlas-re/atlas-re-prd.md --root extensions/angent-ba/examples --format html --title "Atlas decision review" --output out/atlas-review.html

Replace the example file paths with the user's **existing, inspected source files**. The same command supports --format md, html, docx or pdf and matching file extensions. It will reject existing output files rather than overwriting without a diff.

Optional real tool regression:

    python tests/integration/check_ba_export.py --chrome PATH_TO_CHROME --pandoc PATH_TO_PANDOC

This integration currently verifies real Markdown, HTML and Word files plus a Chrome review using synthetic Atlas documents. **PDF has not been runtime-verified** in that test host, so it must not be claimed as supported without an installed PDF engine and an actual file check.

## What is and is not proven

SHA-256 records the exact exported Markdown inputs; it does not prove stakeholder approval. A DOCX can be valid but editorially poor. HTML is a read-only document export, not an app dashboard. This helper is not a live Confluence/Jira sync, mass attachment collector or document editing backend. ANGENT Root and Quality retain final writing and format decisions; Execution controls actual file/provider effects.
