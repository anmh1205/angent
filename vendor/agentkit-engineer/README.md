# AgentKit Engineer integration

ANGENT uses **native-first / portable-fallback** engineering capability.

## Two independent plugin roots

ANGENT core and Engineer fallback are intentionally separate package roots:

```text
<repo>/
├── plugin.json
├── skills/                         # ANGENT cognitive owners
└── vendor/agentkit-engineer/
    ├── plugin.json                 # portable Agent Plugins manifest
    ├── .codex-plugin/plugin.json   # ChatGPT/Codex companion manifest
    ├── STABLE_CATALOG.json         # documented-stable workflow target + registry observation
    ├── PORTING_MANIFEST.md         # human-readable port status
    ├── COMPATIBILITY.md            # retired-route migration guidance
    ├── internal/                   # non-public support semantics
    ├── skills/                     # 103 current stable public fallback Skills
    ├── agents/                     # 16 portable role definitions
    └── scripts/select_engineer.py
```

Agent Plugins v1 uses a fixed `skills/` discovery root and does not provide a portable conditional second Skill root. Keeping the fallback as its own plugin prevents fallback Skills from always colliding with native AgentKit Engineer.

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

Documented stable public workflow target, retrieved 2026-10-14:

- **103/103 public Skill identities**
- **16/16 portable Agent roles**

A same-day remote portable export from current stable CLI 2.19.0 returned 102 legacy Skill identities and 16 preserved Agent sidecars. This upstream docs/registry-export drift is recorded in `UPSTREAM_BASELINE.md` and `STABLE_CATALOG.json`.

The fallback is an independent ANGENT implementation targeting documented workflow semantics. It is not an upstream mirror and does not claim exact registry package parity.

`STABLE_CATALOG.json` is the machine-readable fallback identity target plus upstream drift observation. `UPSTREAM_BASELINE.md` records the two upstream surfaces. `PORTING_MANIFEST.md` explains portability mode and coverage.

Retired upstream routes are not kept as public Skills merely for compatibility; use `COMPATIBILITY.md`.

Internal common conventions are outside the public Skill discovery tree.

## Selection

`scripts/select_engineer.py` is a small read-only selector.

The active harness/adapter supplies whether native Engineer is usable. The helper may add `ak --version` / doctor health evidence, then returns one source:

1. native usability proven → `native`;
2. no/unknown native usability → `fallback`;
3. fallback package invalid or catalog identity mismatch → `blocked`.

Fallback readiness compares the exact Skill/Agent identity sets against `STABLE_CATALOG.json`; a matching count alone is not sufficient.

The selector never installs or mutates AgentKit and never enables both libraries.

## Agent roles

Agent Plugins v1 does not define a portable Agent component.

The files under `agents/` are role semantics for adapters/workflows:

- project into a harness-native Agent/team role when supported;
- pass to one-shot workers when supported;
- apply sequentially only when the selected workflow permits that degradation.

Do not create separate Claude/Codex/Cursor reasoning forks.

Some upstream workflows intentionally require a live lifecycle. For example, `ak-team` must block rather than silently pretending ordinary subagents are a live team when creation/shared-work/messaging/wait/shutdown/cleanup capabilities are absent.

## Porting principle

Preserve the useful workflow outcome, gates and failure semantics—not AgentKit implementation mechanics.

Examples:

- AgentKit plan state → files-first plan artifact + Continuity;
- session handoff → Continuity frontier;
- runtime-specific delegation → harness-native delegation only when the workflow permits it;
- hooks → proactive Continuity capture, with hooks only as an optimization;
- browser helper → the browser/computer-use/test capability actually available;
- public catalog identity → documented stable public workflow identity;
- retired route → compatibility mapping outside public Skill discovery.

## Repository boundary

Do not add a raw `upstream/` source mirror here.

This directory contains ANGENT's fallback plugin, portable role library, stable catalog provenance, and native-use documentation.

## ChatGPT / Codex packaging

ChatGPT and Codex use the package manifest at `.codex-plugin/plugin.json`.

The fallback companion points that manifest at the same `./skills/` tree used by the portable package. No Skill content is duplicated.

Installing/enabling this companion is a client-level action. It should be enabled only when native AgentKit Engineer is not the selected source.

## Portable Skill identity

Native AgentKit presents Engineer Skills with identities such as `ak:plan`.

The portable fallback conforms to Agent Skills naming under directory IDs such as `ak-plan`, `ak-debug`, and `ak-page-builder`. Capability mapping remains one-to-one with the corresponding current stable workflow identity.
