---
name: ak-mcp-builder
description: Design, implement and evaluate MCP servers that expose external/service capabilities through small typed tools/resources with safe effect semantics.
metadata: {port: angent-fallback, mode: portable}
---

# MCP Builder — Portable Fallback

Read:
- `references/mcp-contracts.md`;
- `references/evaluation.md`.

## Workflow

1. Define the external capability and trust boundary.
2. Identify target MCP clients/runtimes and the current SDK/protocol version.
3. Choose tools, resources and prompts only where their MCP semantics help.
4. Keep tool schemas small and explicit.
5. Separate read-only from side-effecting tools.
6. Design authentication/credential resolution outside ordinary tool arguments when possible.
7. Make provider errors structured and actionable.
8. Add tests for schemas, provider failures, timeout/retry and effect semantics.
9. Validate against at least one actual target MCP client/runtime.
10. Evaluate whether an agent can discover and use the surface reliably on representative tasks.

Do not build a generic “execute arbitrary command” tool unless the security model explicitly requires and tightly constrains it.

Keep business logic in the underlying service/library when it already has an owner; the MCP server should usually be an adapter rather than a second implementation.
