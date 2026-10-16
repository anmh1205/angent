# Figma Kit Adapter (ANGENT Hub)

**Repository-only verification:** Any `tests/` command below requires the GitHub source checkout. Release ZIPs intentionally ship the supported `extensions/.../scripts/` executables, but not the development test suite. When using an installed package, run its bundled generator and verify actual output; check out the source only for the additional regression tests.


Choose these capabilities only when diagram modeling, editable Figma objects or a stakeholder prototype truly adds value. `figma-activity`, `figma-erd`, etc. provide Figma-target method-specific semantics, not replacement for BA or Engineer's general diagram/code methods.

## Live host verification

1. Determine actual Figma file/document, page and user-authorized edit scope.
2. Inspect available native Figma connector/MCP tool operations. If unavailable, stop at an offline structured model or another explicitly requested fallback artifact; never state the Figma file changed.
3. Read current object IDs, design variables and connected graph metadata before modifying.
4. Make bounded native edits; inspect the returned nodes, links, component variants and layout (including screenshots when available).
5. Check source business model and unexpected collateral changes, and report evidence or remaining uncertainty.

The kit may render offline diagrams without native Figma, so the manifest allows portable instructions, but **native operations and portable output are not interchangeable evidence**. Plugin and MCP availability are observed per session, never inferred from bundled Skill source. Do not embed unreviewed external global system prompts into ANGENT or run arbitrary scripts from a page.

## Native Figma Plugin API target (separate from Reqwise)

The BA kit now provides **two distinct executable-code candidates** from the same accepted screen model:

- Reqwise sandbox: build_figma_screens.py emits figma_write code using Reqwise's proprietary-to-it sandbox proxy figma.create(tree).
- Official Figma Plugin API: build_figma_native.py emits figma-native-plugin.js using **figma.createFrame(), figma.createText(), await figma.loadFontAsync() and native node read-back**. This is suitable for an authorized Figma host supporting direct asynchronous Plugin API JS, including an available Figma use_figma-style interface.

Generate a native candidate from the accepted screen model:

    python extensions/angent-ba/scripts/build_figma_native.py extensions/angent-ba/examples/authentication-screen-model.json --output out/figma-native

The generated script is deliberately **not run** by Python. Choose and inspect the correct Figma file/page first, check the actual connected tool's code contract and permissions, then invoke authorized JS in its supported context. Its preflight checks all existing screen names and control labels before making changes. Exact matching frames are left unchanged; conflicting frames prevent all new changes. Newly created frames are read back by native ID and rolled back on a detected write/read-back failure where possible. Node names serve as a conservative handoff identity; they are not guaranteed unique across unrelated Figma files.

A Node.js API-shaped mock regression at tests/test_ba_figma_native.py checks creation, idempotency, conflict detection and best-effort rollback. **Mock success is not evidence of real Figma compatibility, successful typography, visual fidelity or a verified customer canvas**; an authorized real Figma run with screenshot and read-back is still the acceptance criterion. Official references: https://developers.figma.com/docs/plugins/api/properties/figma-createframe/ and https://developers.figma.com/docs/plugins/api/properties/figma-loadfontasync/.

