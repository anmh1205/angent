# ANGENT Figma — diagram and canvas methods

**Scope:** 12 methods, six substantial adaptations of the MIT [Reqwise Figma MCP](https://github.com/hoangpm96/reqwise-figma-mcp) skills and six independently authored methods for use case, BPMN, journey, persona, design system and demo. Attribution and original MIT license: THIRD_PARTY_NOTICES.md.

## Runtime truth

The six free Reqwise kinds (activity, userflow, state, sequence, erd, sitemap) can be prepared as portable semantic models, validated structurally and compiled to the public MIT figma_diagram request shape by scripts/to_reqwise_payload.py. That script defaults to dryRun and NEVER contacts Figma. The result is a request proposal, not evidence of a live canvas mutation.

For actual Figma operations, follow mcp/SETUP.md; inspect figma_status for live connection, file/page/session and version, then send authorized calls and verify by Figma read-back and layout audit. Without these tools, provide model/diagram source only.

Pro-only capabilities are not in Reqwise's public MIT runtime. Their six ANGENT methods specify semantics, quality gates and authorized tooling options. They **do not** currently constitute a proprietary-equivalent Pro server, screen generator, component library, BPMN DI engine or video recorder. Do not report them as such. Art direction belongs to angent-frontend; UX and code specialization may come from Engineer; Root retains decisions and permission checks.

See RESEARCH_AND_PARITY.md for the actual capability limits and verified source.
