# Optional native Figma integration — Reqwise OSS MIT

ANGENT Figma specialists need **real** provider tools for editable Figma output. This adapter generates the open-source Reqwise `figma_diagram` arguments, but never launches or contacts a native MCP server itself.

## Installation under user control

1. Review the official MIT repository, licensing and version: https://github.com/hoangpm96/reqwise-figma-mcp. The upstream example has `package.json` declaring the `reqwise-figma-mcp` executable and an `install:mcp` script.
2. In an authorized development environment, clone the official repository, run `npm install`, `npm run build`, then `npm run install:mcp` following the official README. This setup is **not** bundled in the ANGENT extension and may vary by host.
3. In Figma Desktop, load the reviewed plugin from `plugin/manifest.json` and keep its UI connected. The local bridge uses a series of localhost ports; avoid exposing it to other networks.
4. In an MCP-capable host, inspect live `figma_status`: connected must be measured true, file/page and session must be correct, and server/plugin build versions should agree. Query `figma_docs` for the exact diagram kind before sending a write.
5. Generate the model payload via `python extensions/angent-figma/scripts/to_reqwise_payload.py input.json`. This defaults to `options.dryRun=true`. Examine findings and do not conflate dry-run with written nodes.
6. Only with explicit write authority, generate a prospective write payload using `--emit-write-payload`, invoke `figma_diagram` through an available provider tool, then `figma_read` the target frame and run layout/semantic checks. When native functions are missing, provide the portable model without claiming a Figma edit.

## Origin and security

The `figma_diagram` input shape for the six OSS diagram types was compared with the public MIT repository's `src/server/validate.ts` and `src/server/tools.ts`. These are independently written ANGENT conversion utilities; no Pro code or commercial templates are embedded. Check upstream version for incompatibilities before every release. Never pass arbitrary remote page scripts into `figma_write`.

Pro-only functions (BPMN, usecase, journey, persona, design system, demo recording) are **method descriptions** and are not implemented by the OSS bridge. For a live Pro capability, require separately authorized tooling that actually exposes it; never misrepresent the OSS tool as supporting them.
