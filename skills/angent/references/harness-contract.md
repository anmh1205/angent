# Harness contract

ANGENT's cognitive semantics should survive differences between ChatGPT, Codex, Claude Code, Cursor, other local agents, and future harnesses.

The adapter boundary is intentionally small. A harness adapter exposes **facts and mechanisms the harness actually has**; it does not become a second cognitive architecture or a generic capability broker.

## Canonical inputs

Every project-capable harness should expose the applicable `AGENTS.md` hierarchy as the canonical project instruction surface.

Harness-specific instruction files may exist only as compatibility projections. They must not become independent authorities that drift from `AGENTS.md`.

## Capability inventory

At the start of work that depends on a non-trivial capability, discover current availability instead of assuming it from the client name.

Relevant capability classes include:

- repository/files/terminal;
- web/research;
- browser/computer use;
- connected providers/plugins;
- subagent/team execution;
- Agent Plugins / Skill loading;
- native AgentKit Engineer visibility;
- durable local/cloud storage;
- provider read-back after external effects.

The inventory can be implicit when a capability is directly exposed by the host. ANGENT does not require one universal capability registry.

## Engineer source

The adapter reports:

`native_engineer_usable = yes | no | unknown`

Use `yes` only when the active harness can actually discover/invoke native AgentKit Engineer.

- `yes` → use native Engineer;
- `no` or `unknown` → activate/project the ANGENT Engineer fallback;
- do not expose both complete catalogs by default.

The selection semantics live with Execution. The adapter only supplies current runtime evidence and performs package activation through the client's supported mechanism.

## Skill/plugin loading

When the harness supports Agent Plugins or another Skill standard, load ANGENT and the selected Engineer source through that mechanism.

When it does not, an adapter may project the same Skill files into its native Skill/prompt surface.

Projection must preserve the canonical Skill text and owner boundaries. Do not create a separate Claude/Codex/Cursor reasoning fork.

## Agent roles and delegation

The Engineer fallback contains portable role definitions, not a universal Agent runtime.

An adapter may map a role to:

1. a native persistent agent/team member;
2. a one-shot subagent/worker;
3. sequential role execution in the current agent.

It should expose whether delegation is available and what write/isolation boundary it provides.

Do not pretend sequential execution is parallel or a worktree is an OS sandbox.

## Context and memory

The adapter provides access to:

- current interaction/instruction;
- applicable project instructions;
- user/project memory backend when available;
- historical/session search when available.

For local harnesses, ANGENT's file-backed memory store is a portable default.

A host-native memory system may replace that backend if it preserves scope, provenance, update/supersession, retrieval and conflict semantics.

Memory never grants authority.

## Continuity

The adapter must give Continuity a durable location appropriate to the environment.

For local harnesses, use the revisioned file backend by default.

For a hosted/chat harness, use the strongest durable backend available to that product/workspace.

Regardless of backend, preserve:

- stable work identity;
- revision/coherence;
- active frontier;
- ambiguous-effect state;
- artifact/source pointers;
- next safe action.

A transient transcript or hidden model context alone is not a Continuity backend.

## External effects and read-back

After consequential GitHub/Jira/Notion/deployment/email/etc. effects, use the provider/tool that can establish actual current state.

The adapter supplies the provider mechanism. Execution and Continuity own retry/reconciliation semantics.

Do not infer provider success from local memory, a previous response, or an exit code when authoritative read-back exists.

## Degradation

When the harness lacks a capability:

- choose a semantically adequate alternate route when one exists;
- degrade parallel work to sequential work when safe;
- preserve the limitation explicitly when the outcome cannot be fully established;
- do not invent unsupported tool results or background execution.

## What the adapter does not own

The adapter does not own:

- task scope or authority;
- problem/system model;
- strategic decisions;
- evidence interpretation;
- authoring quality;
- learning policy.

Those remain ANGENT owner responsibilities.

The purpose of the harness contract is to make ANGENT portable **without duplicating its mind per client**.
