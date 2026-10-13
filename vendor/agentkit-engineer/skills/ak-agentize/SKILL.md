---
name: ak-agentize
description: Turn an existing codebase capability into an agent-friendly CLI and/or MCP surface with stable contracts, credentials, docs, tests and packaging.
metadata: {port: angent-fallback, mode: adapted}
---

# Agentize — Portable Fallback

Use when a library, service or feature should become reusable by agents instead of being driven only through a human UI or ad-hoc scripts.

Read `references/surface-design.md` for transport and contract choices.

## Workflow

1. Identify the capability boundary and current source-of-truth implementation.
2. Define a small command/tool surface around stable operations.
3. Separate pure/read operations from side-effecting operations.
4. Design machine-readable output and errors.
5. Resolve credentials from existing secure mechanisms; never bake secrets into generated tools.
6. Add tests for argument validation, effect semantics and failure paths.
7. Package/document the surface so another agent can discover and use it without project-specific tribal knowledge.
8. Add MCP only when tool discovery/session transport materially helps; a CLI is often the simpler base.

## Output

Return the exposed operations, transport, credential model, package/install path, tests, docs and remaining limitations.

Do not invent a second business-logic implementation inside the tool wrapper.
