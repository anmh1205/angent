---
name: ba-figma
description: Translate accepted screen wireframes into editable Figma frames through an actual authorized provider, with verified node-level read-back.
---

# Wireframe-to-Figma screen handoff

**Origin:** Adapted from the MIT Dev BA Kit Figma wireframe workflow by Edward Ngo (https://github.com/nv-minh/dev-ba-kit/blob/main/skills/figma/SKILL.md), supplemented with Reqwise OSS's actual Figma MCP reference (https://github.com/hoangpm96/reqwise-figma-mcp/blob/main/docs/TOOLS.md). The commercial AI4BA/Reqwise Pro binaries were not available or copied.

## Domain boundary: screen delivery versus diagrams

\`ba-figma\` carries approved **screens and controls** from \`ba-wireframe-ascii\`, \`ba-wireframe-html\` or an accepted screen model into editable Figma frames. The six Reqwise OSS \`figma_diagram\` types (userflow, activity, state, sequence, ERD, sitemap) are **diagram models**, not a general \`wireframe → app screen\` compiler. Do not call \`figma_diagram\` to create a login form and then claim it faithfully implemented screen layouts. Use Figma provider-native frame and node operations only when live, permitted and documented.

## Source-to-canvas mapping

1. Read accepted feature scope, screen inventory, selected variant, SRS/FR/AC, userflow and existing Figma design system. Preserve screen IDs/names, control labels, role/permission states and the intended device width. Do not assume an ASCII sketch is the best authoritative source when a later approved screen revision exists.
2. Create a screen mapping inventory: source screen ID → Figma target file/page → existing frame node ID (when any), width, components, actions, error/empty/loading states, source revision and intended update type. The output is a proposed frame map, not yet a Figma change.
3. Read the actual Figma file first through the connected provider: inspect file/page, existing frames, variables, text styles, component instances and library constraints. If the connected tool cannot read frames or write editable nodes, stop the **native edit** and provide the screen specification for a capable host rather than inventing links.
4. Decide shape and component reuse before creation. Prefer existing design tokens, components and auto-layout settings where supported. Controls must preserve labels, statuses and keyboard/accessibility notes. The BA specialist does not override ANGENT Frontend's accepted visual direction.
5. Compute per-screen change intent: create, reconcile existing node, leave unchanged, manual repair. Avoid regenerating duplicate frames on a repeated run. The source screen ID and exact Figma node ID together establish identity; title similarity alone does not.
6. Before consequential writes, apply ANGENT Execution's current authorization and scope rules. For approved operations, use the **actual** Figma adapter that is available (the Reqwise \`figma_write\` sandbox or a different documented Figma provider). Never invent tool names or assume an available Figma connector supports every node-level action. Confirm Figma text font loading and provider-specific batching.
7. Read back actual frame IDs, editable node types, texts and component references. Compare control inventory against source, check frame count, visibility and constraints; run a real layout/screenshot review if the host supports it. Record only returned, verified URLs. A frame created but missing half its controls has not passed.
8. After read-back, update an existing authorized wireframe/index document with the actual Figma URL/node ID, without overwriting other links or creating a hidden synchronization database. If no existing index exists, supply links in the task result; do not invent a compulsory path.
9. Report created/updated/skipped/failed frames, exact checked revision and any unsynchronized states. A dry-run manifest, exported PNG or a \`figma_diagram\` response is **not** equivalent to an editable screen.

## When Figma is unavailable

Prepare a precise screen-to-node mapping, list provider prerequisites and retain any approved HTML prototype. Do not fabricate URLs, claim a mock Figma session or automatically upload restricted screens to an external renderer.

## Test criteria

For each screen: correct actor permission, one stable frame mapping, source-equivalent content/control count, interaction and error states, usable type sizes and contrast, no clipped content at target width, editable node read-back and preservation of unrelated existing frames. A successful write message alone is not enough.

**ANGENT ownership:** Root chooses scope and retains user approval, BA owns requirement-to-screen semantics, Frontend owns visual design when needed, Figma specialist handles real diagram/model-specific construction, Execution controls external effects and Quality verifies.
