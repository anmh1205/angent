# Readable, semantic diagram styling

**Provenance:** Adapted from MIT Dev BA Kit / rules/diagram-style.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. Styling decisions are subordinate to an existing brand/design system.

## Visual hierarchy

Prioritize node/edge identity and reading order above decoration. Use actor/system boundaries, ownership, external integrations and error decisions consistently within a diagram. Labels must remain readable at the target display size, including mobile-width document previews if relevant.

Color must never be the **only** carrier of meaning. Use shape, text, grouping and connectors so diagrams remain understandable in grayscale or high-contrast conditions. Avoid an arbitrary multi-color icon palette when simple shapes suffice.

## Suitable source and renderer

D2 layout is determined by the official D2 engine and its supported shape properties. The portable JSON-to-D2 generator currently encodes semantic node kinds and limited layout inputs; it is not a full theme/token engine. Do not promise styles that build_d2.py does not emit.

Mermaid and PlantUML theme syntax differs from D2 and must be validated by a real renderer if applied. Figma node properties should derive from the actual file's variables/styles/components when available; an unrelated static palette is a proposal, not the project's design system.

## Distinguish scope and trust

An external system can be shown with a dashed boundary and explicit owner. A database needs a data-store identity, not an icon that obscures column or key labels. An authorization decision should include readable guarded edges; a red fill is insufficient by itself.

For dense diagrams, split by a meaningful bounded context or level. Do not hide critical negative paths to make the image cleaner. Enforce readable line routing, visible arrowheads and sufficient spacing after rendering.

## Review procedure

Render with an actually available engine, inspect concrete SVG/canvas output, compare node and edge inventories to the model, check clipped/overlapping text and verify source/provenance labels. Record the renderer version and any unresolved visual defect.

A syntactically correct D2 or BPMN file may still be visually poor. It is better to report that limitation than to claim “production-ready diagrams” from a passing parser.
