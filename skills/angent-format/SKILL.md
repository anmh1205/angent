---
name: angent-format
description: Render established ANGENT content faithfully for the destination, preserving semantic representations and verifying the final render.
---

# ANGENT Format — Destination Fidelity

Format owns destination mechanics: hierarchy, blocks, code/equations, citations, links, figures, tables, page breaks and final render/readback verification.

Read `representation.md`.

Authoring owns wording and representation intent. If a destination limitation requires a meaning change, return it rather than silently rewriting.

Preserve semantic structure: do not flatten an explanatory relation into bullets merely for scanability or convert a real procedure/table into prose for stylistic consistency.

Strip transport-only metadata and raw internal citation tokens. A successful API write, raw Mermaid source, placeholder or URL is not proof of correct rendering.

Inspect the actual destination when possible.
