# Agent-facing surface design

Prefer contracts that are deterministic, inspectable and scriptable.

## CLI

Good when:
- operations map naturally to commands;
- stdout/stderr and exit codes are enough;
- the tool should work in any harness with shell access.

Use machine-readable JSON mode for non-trivial outputs.

## MCP

Good when:
- runtime-native tool discovery matters;
- persistent transport/session state is useful;
- resources/prompts/tools benefit from structured exposure.

Do not add MCP only for branding.

## Operation design

Each operation should make clear:
- inputs;
- effect class;
- authorization/credential expectation;
- output schema;
- error cases;
- idempotency/retry semantics.

Keep business logic in the underlying application/library and make the agent surface a thin adapter.
