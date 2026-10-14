# MCP protocol semantics

MCP uses a client-host-server model over JSON-RPC-style requests.

For portable tool use, preserve the semantic distinctions:

- **tools** — executable operations with argument schemas and possible effects;
- **resources** — data surfaces that may be read according to server capability;
- **prompts** — reusable server-provided prompt templates.

## Lifecycle

A client normally:
1. connects/initializes;
2. learns server capabilities;
3. lists or resolves the required surface;
4. executes/reads with validated arguments;
5. handles protocol/provider errors;
6. closes/cleans up when it owns the connection.

## Transports

Local stdio and remote HTTP-style transports have different process/network/credential boundaries.

Do not infer remote safety from a local MCP abstraction.

## Error handling

Distinguish:
- schema/invalid-argument errors;
- method/tool absence;
- transport/server failure;
- provider/domain failure returned by the tool.

A transport error during a consequential non-idempotent call requires provider reconciliation before blind retry.
