# ANGENT Engineer extension

ANGENT-owned engineering **source module**, with portable fallback semantics adapted from the AgentKit Engineer stable catalog. This directory is not a second user-facing plugin installation, an upstream AgentKit repository or a raw source mirror.

ANGENT uses **native-first / portable-fallback** engineering capability.

## One plugin, separate source module

The released ANGENT plugin is assembled by `scripts/package_unified.py` from Core's `skills/` and this module's `skills/`.

```text
angent (Git repository)
├── plugin.json                         # one public plugin identity
├── skills/                             # 12 Core Skills in source
├── extensions/angent-engineer/
│   ├── skills/                         # 103 maintained Engineer Skills
│   ├── agents/                         # 16 role contracts
│   ├── scripts/                        # selector and structural checks
│   └── plugin.json                     # legacy source/verification metadata
└── scripts/package_unified.py          # builds one installable ZIP
```

The installable ZIP contains **115 discoverable Skills under one root**, the 16 role contracts, the existing Engineer support tree and **only ANGENT's root installable manifests**. Nested Engineer plugin metadata becomes `source-manifest.json` for selector compatibility and is not installable. Original source copies are retained within the package to keep relative references and scripts intact; they are not another discovery root.

Native AgentKit remains preferred **per task**, not via automatic unloading of packaged Skills. Agent Plugins v1 lacks conditional static discovery; the host may show both native and fallback catalogs, so selection must avoid combining them.

## Native path

If official AgentKit Engineer is usable in the active environment, use native. **Installing the `ak` binary is not a prerequisite for normal fallback engineering work:** Plans, Journal, Skill routing, status boards and orchestration reasoning are independently routed to Skills and available host file/agent capabilities.

Do not vendor or mirror native AgentKit source in this repository.

Official sources:

- https://agentkit.best
- https://docs.agentkit.best/en/stable
- https://docs.agentkit.best/en/stable/getting-started/installation
- https://docs.agentkit.best/en/stable/kits/engineer
- https://docs.agentkit.best/en/stable/kits/engineer/skills
- https://docs.agentkit.best/en/stable/kits/engineer/agents

Native usability means the **current harness can actually discover/invoke Engineer**. An `ak` binary, old cache or one runtime-specific filesystem path is not sufficient proof.

AgentKit `--global` means user scope for the selected runtime target; it is not a universal runtime-independent target.

## Fallback path

If native AgentKit Engineer is absent, unusable or not proven usable, route to the `ak-*` Skills **already included** in the installed ANGENT plugin. Do not install this source module as a second plugin.

Coverage:

- **103/103 stable 2.19.0 public Skill identities present**
- **16/16 Agent role identities present**
- **current per-Skill semantic status and explicit runtime degradations are tracked only in [PORTING_MANIFEST.md](PORTING_MANIFEST.md); do not duplicate mutable progress counts here**

Identity presence is not accepted as capability parity. See `PORTING_MANIFEST.md` for the live semantic-review ledger, `AUDIT_REPORT.md` for dated verification evidence and remaining runtime gates, and `UPSTREAM_BASELINE.md` for pinned upstream evidence.

The fallback is an independent ANGENT implementation, not an upstream mirror. [Outcome routing](skills/ak-agentkit/references/outcome-routing.md) describes how agent capabilities are selected by the actual engineering problem, not by reproducing CLI commands. Native product administration remains under `ak-ak`.

The six retired workflow names are documented under `retired-routes/`, and internal `ak-common` support lives outside public discovery in `internal/`. Neither is an installable public Skill. Source-level completeness is not full runtime equivalence.

## Agent-led engineering

Engineer Skills transmit **the way an agent should think and work**: how to inspect and question evidence, select a method, plan dependencies, act with bounded authority, detect contradictions and verify real outcomes. The portable contract is not a map of `ak` subcommands to replacement scripts. Normal planning, journaling, testing and coordination do not require the AgentKit binary.

Apply the [outcome routing](skills/ak-agentkit/references/outcome-routing.md), [plan stewardship](skills/ak-plan/references/plan-stewardship.md), [journal judgment](skills/ak-journal/references/journal-judgement.md) and [coordination judgment](skills/ak-orchestrate/references/coordination-judgement.md). A Skill should teach the reasoning and decision criteria; tools are invoked only when the task actually needs an effect.

## Optional deterministic helpers

The following helpers remain subordinate to Skill-based judgment, for repeatable local inspections that genuinely benefit from code:

- `skills/ak-repomix/scripts/pack_local.py` — bounded local Git source export, with sensitive-file safeguards and completeness reporting.
- `skills/ak-watzup/scripts/scan_local.py` — read-only Git/worktree and project-plan status observations.
- `skills/ak-gkg/scripts/search_python_ast.py` — Python AST symbol definitions and candidate references.

They require Git, Python and an accessible local worktree. The previously introduced `ak-plan` and `ak-journal` file-lifecycle CLI substitutes were removed as unnecessary: these are first and foremost **agent reasoning methods** applied using existing project file/document tools. External AgentKit account/licensing/kit/service effects still require the real product.

## Selection

`scripts/select_engineer.py` is a small read-only selector.

The active harness/adapter supplies whether native Engineer is usable. The helper may add `ak --version` / doctor health evidence, then returns one source:

1. native usability proven → `native`;
2. no/unknown native usability → `fallback`;
3. fallback package invalid → `blocked`.

It never mutates AgentKit and never enables both libraries.

## Agent roles

Agent Plugins v1 does not define a portable Agent component.

The files under `agents/` are therefore role semantics for adapters/workflows:

- project into a harness-native agent/subagent when supported;
- pass to one-shot workers when supported;
- apply sequentially when delegation is unavailable.

Do not create separate Claude/Codex/Cursor reasoning forks.

## Pinned upstream baseline

The current fallback catalog is the authenticated **AgentKit Engineer stable 2.19.0** package re-exported on 2026-10-15 (103 public Skills, 16 roles). The stable docs Skill guide is used for routing/capability context, but not as packaged-inventory authority.

Raw upstream source/export content is not stored here. Audit evidence and source boundaries are recorded in `UPSTREAM_BASELINE.md`.

## Porting principle

Preserve the useful workflow outcome, critical gates, reusable domain/support knowledge and safety boundaries—not AgentKit implementation mechanics.

Examples:

- AgentKit plan state → files-first plan artifact + Continuity;
- session handoff → Continuity frontier;
- team/subagent runtime → harness-native delegation or sequential fallback;
- hooks → proactive Continuity capture, with hooks only as an optimization;
- browser helper → the browser/computer-use/test capability actually available.

## Repository boundary

Do not add a raw `upstream/` source mirror here.

This directory contains ANGENT's maintained fallback Skill source, portable role library and native-use documentation.


## ChatGPT / Codex packaging

Install the **single** `angent-unified.zip` artifact. The root `plugin.json` and `.codex-plugin/plugin.json` describe one plugin with one discoverable `skills/` tree. Engineer files here are maintained source and non-discoverable support, not a second package.

The portable native-first behavior is guidance and runtime routing, **not** a claim that static Skill discovery can be switched off from inside a plugin manifest.

## Portable Skill identity

Native AgentKit may present an Engineer Skill with an upstream identity such as `ak:plan`.

The portable fallback must conform to the Agent Skills specification, where the Skill `name` matches its directory and uses lowercase alphanumerics plus hyphens. Fallback identities are therefore `ak-plan`, `ak-debug`, `ak-test`, and so on.

This changes only the portable package identity. Capability mapping remains one-to-one with the corresponding native Engineer workflow.
