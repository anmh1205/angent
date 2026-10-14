# AgentKit Engineer integration

ANGENT uses **native-first / portable-fallback** engineering capability.

## Two independent plugin roots

~~~text
<repo>/
├── plugin.json
├── skills/                       # ANGENT cognitive owners
└── vendor/agentkit-engineer/
    ├── plugin.json               # portable Agent Plugins manifest
    ├── .codex-plugin/plugin.json # ChatGPT/Codex companion manifest
    ├── skills/                   # 103 public portable Engineer Skills
    ├── agents/                   # 16 portable role definitions
    ├── internal/                 # non-discoverable fallback support
    ├── retired-routes/           # compatibility navigation only
    └── scripts/select_engineer.py
~~~

Keeping the fallback as a separate plugin prevents its full Skill catalog from colliding with native AgentKit Engineer.

## Native path

If official AgentKit Engineer is usable in the active environment, use native.

Do not vendor or mirror native AgentKit source in this repository. Install/manage native AgentKit from `agentkit.best` and its current stable documentation.

Native usability means the **active harness can actually discover/invoke Engineer now**. An `ak` binary, cache, historical receipt or runtime-specific path is supporting evidence only.

## Fallback path

When native Engineer is absent, unusable, or its usability cannot be established, activate this plugin root.

Current stable-port coverage:

- **103/103 public Skills**
- **16/16 portable Agent roles**

The exact identity baseline and provenance are in `UPSTREAM_BASELINE.md`; per-Skill port modes are in `PORTING_MANIFEST.md`.

Retired upstream identities are navigation aliases only under `retired-routes/`. Internal fallback conventions are under `internal/`. Neither is discoverable as a public Skill.

## Selection and integrity

`scripts/select_engineer.py` is read-only.

The active harness supplies whether native Engineer is usable. The selector may add read-only `ak --version` / doctor evidence, then chooses one source:

1. native usability proven → `native`;
2. no/unknown native usability → `fallback`;
3. fallback package identity/manifest invalid → `blocked`.

Fallback readiness requires the **exact** 103-Skill and 16-role identity sets. Count equality alone is insufficient.

The selector never mutates AgentKit and never enables both libraries.

## Portable runtime behavior

Preserve the useful workflow semantics, not AgentKit runtime implementation mechanics.

Examples:

- plan state → files-first artifact + ANGENT Continuity;
- session handoff → Continuity frontier;
- team/subagent lifecycle → harness-native delegation when available; hard-stop/degrade when lifecycle semantics are load-bearing and unavailable;
- browser/render workflows → actual browser/render capability of the active harness;
- hooks → proactive Continuity behavior, with hooks only as an optimization.

Do not claim parity when replacing a runtime mechanism removes a load-bearing capability.

## Agent roles

Agent Plugins v1 standardizes Skills, not portable Agent components.

The 16 role files can be projected into native subagents/workers where supported, or applied sequentially when that preserves the workflow. Do not pretend sequential execution is parallel.

## Portable Skill identity

Native AgentKit commonly presents identities like `ak:plan`. The fallback uses Agent Skills-compatible directory/name identities such as `ak-plan`.

The mapping is semantic. It does not make the fallback a byte-for-byte upstream mirror.

## Version boundary

All ANGENT-owned package manifests remain semantic version **1.0.0** until the user explicitly changes the project version. Provider release IDs, commit SHAs and artifact digests are deployment evidence, not semantic versions.
