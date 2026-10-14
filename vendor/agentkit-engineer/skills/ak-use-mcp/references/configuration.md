# MCP configuration boundary

Treat project MCP configuration as sensitive executable configuration.

Typical server entries contain:
- command/executable;
- arguments;
- optional environment-variable mapping;
- transport/endpoints depending on the host.

## Discovery

Prefer runtime-native registered servers first.

For a direct-client fallback, inspect the project-specific MCP config supported by that runtime/project. Do not assume one universal config location outside the pinned workflow.

Validate:
- configuration parses;
- server identity is the intended one;
- executable/transport exists;
- arguments are explicit;
- environment references resolve without exposing secret values.

## Credentials

Keep credential values in the environment/secret store.

Do not:
- inline them into generated config;
- persist them in a tool catalog;
- move them from a project-scoped config into global runtime configuration without explicit intent;
- print them during diagnostics.

## Installation/process effects

Starting an stdio server can execute a local process; remote transports can send data over the network.

Package installation, first-time runtime download and server launch are effects that require the corresponding authority.
