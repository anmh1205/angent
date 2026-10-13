# MCP discovery and effects

Treat tool catalogs as runtime state.

For each selected tool know:
- server/provider;
- input schema;
- output/error schema;
- side-effect class;
- idempotency/retry behavior if known;
- authentication boundary.

A tool name alone is not enough to infer safety.

For ambiguous writes, query provider state before retrying.
