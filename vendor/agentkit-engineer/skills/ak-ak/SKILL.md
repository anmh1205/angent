---
name: ak-ak
description: Operate or diagnose the official AgentKit CLI when it is installed; otherwise provide the official installation path instead of emulating AgentKit lifecycle commands.
metadata: {port: angent-fallback, mode: degraded}
---

# AgentKit CLI — Native Integration Helper

This Skill intentionally does **not** reimplement the AgentKit control plane.

## When `ak` is available

Use the official CLI for AgentKit lifecycle work such as setup, kit install/update, doctor, login, plan/journal tooling and recovery.

Before mutation:
- inspect current scope/project/global state;
- prefer JSON/read-only inspection when available;
- understand whether the command changes project or user/global installation;
- preserve authorization and rollback/recovery expectations.

## When `ak` is not available

Do not fake AgentKit lifecycle behavior.

Use the official sources:
- https://agentkit.best
- https://docs.agentkit.best/en/stable
- https://docs.agentkit.best/en/stable/getting-started/installation

If the user only needs ANGENT engineering capability, continue with the portable fallback library instead of forcing AgentKit installation.

## Boundary

This Skill is the deliberate degraded case in the full-port target: it preserves the native-control capability by delegating to the official product rather than cloning its lifecycle runtime.
