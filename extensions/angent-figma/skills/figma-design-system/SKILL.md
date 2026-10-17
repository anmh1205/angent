---
name: figma-design-system
description: Specialized design-system analysis and editable Figma delivery when runtime support is proven.
---

# Maintain a real Figma design system instead of drawing decoration

## Responsibility
ANGENT Frontend handles art direction and accepted brand expression; Engineer handles systemic UX/accessibility; this method maps an agreed system to Figma variables, styles, reusable component sets and documented usage. A new design system must not overwrite an existing accepted one.

## Discovery and tokens
1. Inspect existing Figma library, components, variant sets, variables and style bindings using real read tools. Also inspect code design tokens if a codebase is authorized; reconcile token identity rather than guessing equality from color swatches.
2. Define semantic tokens for foreground/background, border, intent, state and density, plus primitive palettes, typography scale, radii, spacing, elevation and breakpoints. Keep an explicit role for light/dark mode and brand-specific variants.
3. Establish variable collections/modes and alias graphs, documenting intended consumers and avoiding cycles. In Figma Plugin API, variables live under figma.variables; evaluate current API/version before scripting changes.
4. Define component anatomy and responsive constraints before creating variants: Button, Input, Select, Checkbox, Radio, Textarea, Dialog, Table, Navigation, Toast and states. Maintain names, stable keys, component properties, variants, slots and instances.
5. Perform accessibility checks against WCAG 2.2 AA for target context: ordinary text contrast 4.5:1, large text 3:1; evaluate component states, focus visibility, accessible labels and minimum target size. Color contrast alone does not certify WCAG compliance.
6. Implement native Figma changes only with actual authorized tools. Create/update variables and components incrementally; read back property definitions, instances, bound variables and component references. Avoid destructive library reshaping without versioned diff and approval.
7. Compare implemented layout on representative widths and zoom levels. Detect text clipping, overflow, disconnected autolayout, variable mismatch and state inconsistencies. Record failures and remediation evidence.
8. For source code alignment, maintain an explicit mapping table between code component props and Figma component properties; do not infer that two-way syncing exists in the installed tools.

## Deliverable
Token catalogue with value/alias/mode, component inventory with variants/props/states, Figma node IDs and verified read-back where present, usage examples and accessibility/responsive audit evidence.

## Pro caveat
The public MIT Reqwise package does not ship Pro component generation or a code-Figma 1:1 synchronizer. A native tool must demonstrably exist or the result remains a specification, not an editable Figma library.

## Technical references
https://developers.figma.com/docs/plugins/working-with-variables/
https://developers.figma.com/docs/plugins/working-with-component-properties/
https://www.w3.org/TR/WCAG22/


## ANGENT coordination

ANGENT Root owns task/authority, BA owns business evidence, Engineer/Frontend provide independent UX or visual specialization when genuinely needed, and Execution/Quality own tool effects and read-back.
