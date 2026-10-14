# AgentKit Engineer integration

ANGENT uses **native-first / portable-fallback** engineering capability.

## Two independent plugin roots

ANGENT core and Engineer fallback are intentionally separate package roots:

```text
<repo>/
├── plugin.json
├── skills/                     # ANGENT cognitive owners
└── vendor/agentkit-engineer/
    ├── plugin.json             # portable Agent Plugins manifest
    ├── .codex-plugin/plugin.json # ChatGPT/Codex companion manifest
    ├── skills/                 # 102 portable Engineer Skill identities
    ├── agents/                 # 16 portable role definitions
    └── scripts/select_engineer.py
```

Agent Plugins v1 uses a fixed `skills/` discovery root and does not provide a portable conditional second Skill root. Keeping the fallback as its own plugin prevents the 102 fallback Skills from always colliding with native AgentKit Engineer.

## Native path

If official AgentKit Engineer is usable in the active environment, use native.

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

If native AgentKit Engineer is absent, unusable or not proven usable, activate the plugin rooted at this directory.

Coverage:

- **102/102 stable 2.19.0 Skill identities present**
- **16/16 Agent role identities present**
- **current per-Skill semantic status and explicit runtime degradations are tracked only in [PORTING_MANIFEST.md](PORTING_MANIFEST.md); do not duplicate mutable progress counts here**

Identity presence is not accepted as capability parity. See `PORTING_MANIFEST.md` for the live semantic-review ledger, `AUDIT_REPORT.md` for dated verification evidence and remaining runtime gates, and `UPSTREAM_BASELINE.md` for pinned upstream evidence.

The fallback is an independent ANGENT implementation, not an upstream mirror.

## Executable offline fallback subsets

Some DEGRADED Skills still provide a **tested runnable local subset**, not just instructions:

- `skills/ak-repomix/scripts/pack_local.py`: bounded Git context export; use `--dry-run` before explicitly emitting source or creating an output.
- `skills/ak-watzup/scripts/scan_local.py`: read-only local Git/worktree/plan inventory; use `--json` for structured status.

Both need Git, Python 3.12-compatible runtime and an accessible local worktree. They never enable the full upstream native CLI. The [audit report](AUDIT_REPORT.md) records exactly what CI has tested.

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

The current fallback audit baseline is the signed **AgentKit Engineer stable 2.19.0** package resolved through the official registry. The stable docs Skill guide is used for routing/capability context, but not as packaged-inventory authority.

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

This directory contains ANGENT's fallback plugin, portable role library and native-use documentation.


## ChatGPT / Codex packaging

ChatGPT and Codex use the package manifest at `.codex-plugin/plugin.json`.

The fallback companion points that manifest at the same `./skills/` tree used by the portable package. No Skill content is duplicated.

Installing/enabling this companion is a client-level action. It should be enabled only when native AgentKit Engineer is not the selected source.


## Portable Skill identity

Native AgentKit may present an Engineer Skill with an upstream identity such as `ak:plan`.

The portable fallback must conform to the Agent Skills specification, where the Skill `name` matches its directory and uses lowercase alphanumerics plus hyphens. Fallback identities are therefore `ak-plan`, `ak-debug`, `ak-test`, and so on.

This changes only the portable package identity. Capability mapping remains one-to-one with the corresponding native Engineer workflow.
