# ANGENT Figma specialist kit

Twelve original specialist methods cover use case, userflow, activity, BPMN, sequence, state, ERD, journey, sitemap, persona, design system and demonstrable UI flows. The scope is informed by public Reqwise Pro features, **not** a reconstruction of its inaccessible source files or a claim of proprietary parity.

The portable layer is a specialist instruction library and structured diagram-model verifier; it can prepare diagrams/specifications without a live Figma connection. **Actual editing, node creation, variables, exports and videos depend on a verified native Figma tool.** Do not claim canvas mutations from generated instructions alone.

## Hub relationship

`angent-frontend` owns visual art direction and accepted aesthetic; `angent-engineer` can own systemic UI/UX and application code; `angent-ba` establishes requirements and business process semantics. `angent-figma` translates accepted models into editable Figma structures using a live adapter when available. ANGENT Root owns selection, permission, real tool calls and final verification.

## Tool boundary

Use host Figma plugin or a separately configured MCP server only after checking actual capabilities. An optional reference implementation exists under the MIT [Reqwise Figma MCP project](https://github.com/hoangpm96/reqwise-figma-mcp). Nothing in this extension automatically installs or starts that tool; review its source, license and runtime setup before adoption.

`scripts/validate_diagram_model.py` validates simple graph models offline. It does not render Figma node content or prove diagram appearance, BPMN interchange or accessibility.
