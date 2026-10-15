---
name: ak-ak
description: Reason safely about the real AgentKit product control plane when the user specifically asks to inspect, configure, install, recover or remove AgentKit-managed state.
metadata: {port: angent-fallback, mode: degraded}
---

# AgentKit product administration

This Skill teaches the **safe operating judgment** for actual AgentKit installations. It is not the default way to run Engineer, and it does not make the `ak` executable a prerequisite for tasks. The ordinary work of planning, journaling, coding, testing, browsing or coordinating belongs to the corresponding Engineer Skill, selected by `ak-agentkit`.

Activate this Skill only when the user's **object of change is AgentKit itself**: its installed kits, CLI version, runtime adapter, licenses, credentials, project registration, backups or managed services. A user asking to "plan" or "run a Skill" is not automatically asking to manage AgentKit.

## Establish the real object of change

Before an AgentKit operation, distinguish:

- **Product state**: installer, user/global registration, kit receipts, AgentKit login/licensing or daemon.
- **Project work**: a roadmap, code review, journal, task board, skill instructions or source files. Route this to its domain Skill.
- **Host capability**: runtime agents, browser, secret manager, package management or scheduling. Use a real supported host capability when the user wants its result.

For product state, determine whether the operation is observation, a project-local write, a user-global write, an external account/network action, or a potentially destructive recovery. Identify the exact installation, target environment, owner and scope. A local `ak` command can affect an adapter's global home; current working directory alone does not establish the target.

## Decide and act safely

Prefer read-only inspection and live version/help over remembered syntax. A configured binary's current `--help` is authoritative for that binary; a version-pinned Skill reference may lag. For material mutations, inspect ownership, uncommitted files, backup/recovery path, pending effects and conflicts first. Do not infer that "doctor", dry-run, or a status-like command has zero external effect without checking its actual implementation.

Execute only when a **real product CLI/provider** is available and the effect is authorized. For risky installation/uninstall/recovery tests use an isolated environment, never a maintainer's actual home. Preserve unknown files. Afterward inspect actual changed product/provider state; command success alone does not establish that the requested runtime can use the installed kit.

If no AgentKit installation/provider exists, explain precisely which **product-admin** capability is missing. Do not fabricate installation status, account/session data or an `ak` shim. If the underlying request was an engineering task, use `ak-agentkit` and the relevant Skill instead.

Official references: https://agentkit.best and https://docs.agentkit.best/en/stable.
