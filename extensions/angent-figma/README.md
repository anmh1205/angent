# ANGENT Figma — diagram and canvas methods

**Scope:** 12 methods, six substantial adaptations of the MIT [Reqwise Figma MCP](https://github.com/hoangpm96/reqwise-figma-mcp) skills and six independently authored methods for use case, BPMN, journey, persona, design system and demo. Attribution and original MIT license: THIRD_PARTY_NOTICES.md.

## Runtime truth

The six free Reqwise kinds (activity, userflow, state, sequence, erd, sitemap) can be prepared as portable semantic models, validated structurally and compiled to the public MIT figma_diagram request shape by scripts/to_reqwise_payload.py. That script defaults to dryRun and NEVER contacts Figma. The result is a request proposal, not evidence of a live canvas mutation.

For actual Figma operations, follow mcp/SETUP.md; inspect figma_status for live connection, file/page/session and version, then send authorized calls and verify by Figma read-back and layout audit. Without these tools, provide model/diagram source only.

Pro-only capabilities are not in Reqwise's public MIT runtime. Their six ANGENT methods specify semantics, quality gates and authorized tooling options. They **do not** currently constitute a proprietary-equivalent Pro server, screen generator, component library, BPMN DI engine or video recorder. Do not report them as such. Art direction belongs to angent-frontend; UX and code specialization may come from Engineer; Root retains decisions and permission checks.

See ../../hub/research/ba-figma-parity.md for the actual capability limits and verified source.

## Source-to-Figma identity integrity

The Reqwise OSS request compiler can verify a diagram model's source_refs against an existing BA artifact graph, without importing a second project-memory system:

    python extensions/angent-figma/scripts/to_reqwise_payload.py extensions/angent-figma/examples/rental-fleet-activity.json --evidence-graph extensions/angent-ba/examples/rental-fleet-traceability.json

This returns source_link_check=ids-resolved-only and writes_performed=false. It neither verifies business-semantic correspondence nor calls Figma. Before claiming a canvas edit, check actual MCP availability and perform authorized provider read-back. Cross-kit reference integrity is tested in tests/test_ba_figma_trace_chain.py.

## Editable application screens versus diagram models

The BA extension now includes extensions/angent-ba/scripts/build_figma_screens.py, which converts its source screen model to a proposed Reqwise figma_write editable FRAME/TEXT scene tree. It is a local generator tested against the real control inventory. It DOES NOT invoke a live Figma bridge, wire prototype interactions, preserve existing frames automatically, or prove visual layout until real canvas read-back. It complements, rather than duplicates, the six OSS figma_diagram adapters.

Use ANGENT Root/Execution to confirm target file/page, read existing nodes, obtain required permission and invoke the actual provider. Report the exact node IDs and screenshot/layout audit afterward; otherwise report no Figma edits.

## Native Figma Plugin API target (separate from Reqwise)

The BA kit now provides **two distinct executable-code candidates** from the same accepted screen model:

- Reqwise sandbox: build_figma_screens.py emits figma_write code using Reqwise's proprietary-to-it sandbox proxy figma.create(tree).
- Official Figma Plugin API: build_figma_native.py emits figma-native-plugin.js using **figma.createFrame(), figma.createText(), await figma.loadFontAsync() and native node read-back**. This is suitable for an authorized Figma host supporting direct asynchronous Plugin API JS, including an available Figma use_figma-style interface.

Generate a native candidate from the accepted screen model:

    python extensions/angent-ba/scripts/build_figma_native.py extensions/angent-ba/examples/authentication-screen-model.json --output out/figma-native

The generated script is deliberately **not run** by Python. Choose and inspect the correct Figma file/page first, check the actual connected tool's code contract and permissions, then invoke authorized JS in its supported context. Its preflight checks all existing screen names and control labels before making changes. Exact matching frames are left unchanged; conflicting frames prevent all new changes. Newly created frames are read back by native ID and rolled back on a detected write/read-back failure where possible. Node names serve as a conservative handoff identity; they are not guaranteed unique across unrelated Figma files.

A Node.js API-shaped mock regression at tests/test_ba_figma_native.py checks creation, idempotency, conflict detection and best-effort rollback. **Mock success is not evidence of real Figma compatibility, successful typography, visual fidelity or a verified customer canvas**; an authorized real Figma run with screenshot and read-back is still the acceptance criterion. Official references: https://developers.figma.com/docs/plugins/api/properties/figma-createframe/ and https://developers.figma.com/docs/plugins/api/properties/figma-loadfontasync/.

