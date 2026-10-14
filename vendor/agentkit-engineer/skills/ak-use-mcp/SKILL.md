---
name: ak-use-mcp
description: Discover and execute MCP tools through runtime-native capabilities or deterministic direct client tooling while preserving exact schemas, configuration provenance and effect safety.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# MCP Tool Discovery & Execution — Portable Fallback

Use the narrowest MCP path that can satisfy the task.

## Load progressively

- `references/discovery-effects.md` — catalog/effect/retry semantics.
- `references/configuration.md` — project MCP configuration and credential boundaries.
- `references/protocol.md` — tool/prompt/resource and transport semantics.

## Path selection

### Runtime-native MCP — preferred

Use when the active harness already exposes the required MCP server/tool.

1. Discover the actual connected server/tool surface.
2. Inspect the exact tool schema.
3. Select the smallest tool for the task.
4. Validate arguments, target and effect authority.
5. Invoke and preserve structured provider identifiers/state.
6. Reconcile consequential writes through authoritative provider state.

Do not assume tool names are identical across ChatGPT, Codex, Claude Code or another host.

### Deterministic direct client — fallback when supported

Use when a project-declared MCP server is not registered in the active runtime and a local deterministic client path exists or can be safely constructed.

Requirements:
- inspect the project MCP configuration rather than copying it into global config;
- preserve environment-variable indirection instead of embedding credentials;
- discover/list tools before calling an unknown schema;
- persist a tool catalog only when it helps a repeatable/CI workflow;
- bound connection lifecycle, timeout and cleanup;
- do not install packages or launch local servers without the required process/network/file authority.

The upstream package ships a Node MCP client and tool-catalog implementation. The ANGENT fallback preserves that workflow contract but does not claim the same bundled scripts exist.

## Catalog freshness

MCP tool catalogs are runtime/config state.

Re-discover when server config, runtime registration, provider version or capability visibility may have changed.

A cached tool name/schema is not sufficient evidence for a current mutation.

## Boundaries

`ak-mcp-builder` creates MCP servers; it is not a substitute for consuming an existing server.

If browser/profile state is required, use the browser/profile capability that actually owns that state.

Retired runtime-specific paths are not recreated merely for parity.

Never copy MCP credentials/secrets into prompts, generated catalog artifacts or another runtime's global configuration.
