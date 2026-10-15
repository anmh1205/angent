---
name: ak-excalidraw
description: Author editable Excalidraw architectural diagrams with real MCP canvas or file-based scene JSON, grounded source relations, export and visual verification.
metadata: {port: angent-fallback, mode: degraded}
---

# Excalidraw — Portable Fallback

Use when the user needs an **editable Excalidraw diagram**, not a flattened vector illustration. Stable Engineer 2.19.0 offers two modes: live Excalidraw MCP canvas (when connected), and file-based `.excalidraw` JSON rendered through a real browser/Playwright backend. Both require observed runtime capability; generic Mermaid/SVG is a different output contract.

Read `references/diagram-model.md` and `references/layout-validation.md` for the semantic model and layout discipline.

## Capability selection

**Live canvas:** Discover the actual MCP canvas tool and its guide. Verify it can read/write the intended document before editing; do not print upstream `mcp__excalidraw__read_diagram_guide` as though it were a portable host tool. Use actual canvas coordinates/IDs and read back elements.

**File-based:** Create a valid Excalidraw scene with the required `type`, `version`, `elements`, `appState` and `files` schema as supported by the destination. Include stable element IDs, bindings, positioning, consistent grouping and embedded assets when required. Use a real Excalidraw-compatible viewer or renderer; SVG/XML or Markdown alone does **not** satisfy the editable deliverable.

**Auto-diagram from code:** Scout actual project boundary, component/module owners, public contracts, data/trigger directions and error flows. Group unrelated components, represent precise topology, and cite source paths separately. Do not draw a package tree as architectural behavior. The upstream's discovery/diagram-size quotas are pragmatic heuristics, not universal proof of completeness.

## Visual encoding and review

Before producing elements, choose a diagram form that **conveys the mechanism**: fan-out for dispatch, convergence for aggregation, timeline for ordered events, loop for feedback, tree for hierarchy, side-by-side for comparison, zones for trust/ownership. Decisions are diamonds; mere labels usually need no box.

Plan generous text and connector corridors, one primary reading direction, edge labels/arrowheads and a restrained role palette; don't invent relationships because the layout seems sparse. Render/read back each meaningful revision and check text clipping, collisions, connector anchoring, arrows passing through unrelated nodes, viewport balance and missing assets. Fix visible defects, then export PNG/SVG if requested/available. A parsable JSON scene alone is **not** a verified image.

**Capability:** VERIFIED_DEGRADED without an accessible canvas/scene renderer. If the runtime supports only SVG or Mermaid, explicitly label a non-Excalidraw substitute and do not represent it as editable Excalidraw source.
