---
name: ak-use-mcp
description: Discover and use MCP capabilities through the active runtime or deterministic client tooling while preserving provider contracts, provenance and effect safety.
metadata: {port: angent-fallback, mode: adapted}
---

# Use MCP — Portable Fallback

Read `references/discovery-effects.md`.

## Workflow

1. Discover currently connected/available MCP servers/tools.
2. Inspect exact tool schema.
3. Select the smallest capability for the task.
4. Check authorization/effect class before mutation.
5. Invoke with validated arguments.
6. Preserve structured result and provider identifiers.
7. Reconcile consequential writes through authoritative state.
8. Re-discover when catalog/config may have changed.

Do not invent MCP tools from memory.
