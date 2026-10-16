# Figma Kit Adapter (ANGENT Hub)

Choose these capabilities only when diagram modeling, editable Figma objects or a stakeholder prototype truly adds value. `figma-activity`, `figma-erd`, etc. provide Figma-target method-specific semantics, not replacement for BA or Engineer's general diagram/code methods.

## Live host verification

1. Determine actual Figma file/document, page and user-authorized edit scope.
2. Inspect available native Figma connector/MCP tool operations. If unavailable, stop at an offline structured model or another explicitly requested fallback artifact; never state the Figma file changed.
3. Read current object IDs, design variables and connected graph metadata before modifying.
4. Make bounded native edits; inspect the returned nodes, links, component variants and layout (including screenshots when available).
5. Check source business model and unexpected collateral changes, and report evidence or remaining uncertainty.

The kit may render offline diagrams without native Figma, so the manifest allows portable instructions, but **native operations and portable output are not interchangeable evidence**. Plugin and MCP availability are observed per session, never inferred from bundled Skill source. Do not embed unreviewed external global system prompts into ANGENT or run arbitrary scripts from a page.
