---
name: ak-ak
description: Resolve requests framed as AgentKit CLI operations into genuine portable Engineer Skills and host mechanisms, retaining native-only administrative boundaries.
metadata: {port: angent-fallback, mode: degraded}
---

# AgentKit CLI — Native Integration Helper

This Skill is the **CLI-to-capability router** for requests expressed in AgentKit terms. Most engineering outcomes should run directly through ANGENT/Engineer Skills and available host tools; do not require or install the `ak` CLI merely to create plans, execute Skills, journal work, test, inspect code or coordinate tasks. Read `references/cli-workflow-crosswalk.md` before routing a CLI-shaped request.

This Skill intentionally does **not** counterfeit the proprietary AgentKit control plane.

## When the request can be fulfilled without AgentKit

Identify the *user outcome* and use the crosswalk to resolve Plan, Journal, Run/Skill dispatch, Scout, Test, Orchestrate, local activity/continuity or provider operations. Preserve native feature-specific semantics (identity, project scope, errors, safety and verification). Do not invoke `ak` for convenience when the same goal can be achieved directly with the selected Skill.

## When `ak` is available

Use the official CLI for AgentKit lifecycle work such as setup, kit install/update, doctor, login, plan/journal tooling and recovery.

Before mutation:
- inspect current scope/project/global state;
- prefer JSON/read-only inspection when available;
- understand whether the command changes project or user/global installation;
- preserve authorization and rollback/recovery expectations.

## When `ak` is not available

Do not fake AgentKit lifecycle behavior.

Only if the user specifically wants to **manage AgentKit itself** and the necessary control plane is absent, use the official sources. Otherwise dispatch the requested engineering task through the appropriate portable Skill without creating an installation prerequisite:
- https://agentkit.best
- https://docs.agentkit.best/en/stable
- https://docs.agentkit.best/en/stable/getting-started/installation

If the user only needs ANGENT engineering capability, continue with the portable fallback library instead of forcing AgentKit installation.

## Boundary

Native AgentKit administration, signed-kit state, accounts, license, dashboard services and installed-binary upgrades remain product-specific and degraded without that product. Ordinary engineering tasks are **adapted** through their owning portable Skills. No universal fake `ak` executable or competing runtime registry is introduced.

## Stable 2.19.0 native control-plane operations
For real `ak` invocations, distinguish read-only inspection, local/project write, user-global write, external network effect and destructive recovery. Resolve kit, target runtime, installation mode and scope before mutation. Inspect `ak --version`, exact `ak <cmd> --help` and `--json` envelopes; reuse until the CLI/target changes. Some diagnostics/semantic shadow evaluators execute tests or transmit data and incur costs despite no project file edit.

Kit lifecycle, skills/agents, plans, journals, config, secrets, login, orchestration, recovery and updates have different write semantics. Never assume all status-like commands are read-only or all dry runs have no effects. Use an isolated AgentKit home for destructive tests; preserve unknown files and previous versions, reconcile partial writes, do not combine `--force` and `--fresh`, and never enable background updates or remote evaluations without user authority. With native `ak` unavailable, do not synthesize a control plane.
