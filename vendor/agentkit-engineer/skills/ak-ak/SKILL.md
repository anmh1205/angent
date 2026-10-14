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

## Stable 2.19.0 native control-plane operations
For real `ak` invocations, distinguish read-only inspection, local/project write, user-global write, external network effect and destructive recovery. Resolve kit, target runtime, installation mode and scope before mutation. Inspect `ak --version`, exact `ak <cmd> --help` and `--json` envelopes; reuse until the CLI/target changes. Some diagnostics/semantic shadow evaluators execute tests or transmit data and incur costs despite no project file edit.

Kit lifecycle, skills/agents, plans, journals, config, secrets, login, orchestration, recovery and updates have different write semantics. Never assume all status-like commands are read-only or all dry runs have no effects. Use an isolated AgentKit home for destructive tests; preserve unknown files and previous versions, reconcile partial writes, do not combine `--force` and `--fresh`, and never enable background updates or remote evaluations without user authority. With native `ak` unavailable, do not synthesize a control plane.
