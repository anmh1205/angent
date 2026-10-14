# Engineer selection contract

ANGENT has two Engineer sources:

1. official native AgentKit Engineer;
2. the portable fallback plugin under `vendor/agentkit-engineer/`.

The selector chooses **one source per active session/workspace**.

## Why selection cannot live only in plugin.json

Agent Plugins v1 discovers Skills only from the fixed `skills/` directory of one plugin root. The portable manifest cannot declare a second Skill root or conditionally enable a nested directory.

Therefore ANGENT core and Engineer fallback are separate plugin roots in the same repository:

```text
angent/
├── plugin.json                         # ANGENT cognitive plugin
├── skills/                             # ANGENT owners
└── vendor/agentkit-engineer/
    ├── plugin.json                     # portable Engineer fallback plugin
    ├── STABLE_CATALOG.json             # documented stable public workflow target
    ├── skills/                         # 103 public fallback Skills
    ├── internal/                       # non-public support semantics
    └── agents/                         # 16 portable role definitions
```

Client installation/enablement is outside the portable Agent Plugins v1 manifest. A runtime adapter or installer selects which Engineer source to expose.

For ChatGPT/Codex, the same fallback root also carries `.codex-plugin/plugin.json` pointing to the same `skills/` directory. This is a packaging projection only; there is still one fallback Skill source tree.

## Native usability

Do not infer native usability from:

- an `ak` binary alone;
- `~/.agentkit` cache content;
- one historical install receipt;
- documentation saying a Skill exists;
- a Claude/Codex/Cursor-specific path;
- memory of a prior session.

AgentKit global installation is **user scope for a selected runtime target**, not one universal global target.

The decisive evidence is whether the **active harness can actually discover/invoke native Engineer now**.

A harness adapter should report:

```text
native_usable = yes | no | unknown
```

Use `yes` only after the current runtime inventory/session proves Engineer is callable.

## Read-only AgentKit diagnostics

`vendor/agentkit-engineer/scripts/select_engineer.py` may also inspect:

- `ak --version`;
- `ak doctor --offline --json` by default;
- full `ak doctor --json` only when requested.

These diagnostics describe AgentKit health. They do not by themselves prove Skill visibility in the current harness.

The selector never calls setup, install, repair, refresh, login or other mutating AgentKit commands.

## Decision

```text
native_usable = yes
        ↓
     NATIVE

native_usable = no / unknown
        ↓
    FALLBACK
```

Unknown fails closed to fallback so ANGENT never exposes native and fallback together based on a guess.

If fallback is selected, `scripts/select_engineer.py` validates the ANGENT fallback against its documented-stable public workflow target:

- fallback plugin manifest;
- `STABLE_CATALOG.json`;
- exact public Skill identity set;
- exact portable Agent role set.

Missing or extra identities block fallback readiness. Counts alone are insufficient.

A ready fallback means the local ANGENT package exactly matches its recorded semantic identity target. It does **not** mean the current AgentKit registry export is byte-for-byte or identity-for-identity identical. Upstream docs/registry drift is carried in `STABLE_CATALOG.json` / `UPSTREAM_BASELINE.md` and does not alter the native-first rule.

If the fallback package/catalog is invalid, selection is blocked rather than pretending a capability exists.

## Fallback activation

The selector returns the fallback plugin root.

A standards-compatible Agent Plugins client may install/enable that plugin root through its own plugin lifecycle.

A harness without Agent Plugins support may project the fallback Skills/roles through its adapter.

This projection is mechanical packaging/runtime work. It must not rewrite the Skill semantics into a harness-specific fork.

## Version identity during preview and acceptance

A cross-harness acceptance run is not a version event.

Every ANGENT-owned package used for canonical, private, preview, staging, or acceptance purposes keeps semantic version **1.0.0** until the user explicitly changes the project version.

Provider-specific release IDs, upload revisions, artifact digests, commit SHAs, or preview identities may change and should be used to distinguish deployments/builds. They must not be translated into any other semantic version automatically.

If a client/tool cannot update the canonical private plugin without mutating the manifest version, do not accept that mutation as ANGENT version policy. Use a disposable preview identity, staging mechanism, or another harness while preserving manifest version `1.0.0`.

The preview must be built from the exact source being accepted.

Do not claim ChatGPT/Codex acceptance from an older installed baseline package merely because that package is callable.

After acceptance, the disposable preview is evidence only; it does not become release authority.

## Agent roles and workflow guarantees

Agent Plugins v1 standardizes Skills and MCP servers, not a portable Agent component.

The 16 fallback Agent files are therefore a portable **role library**. A workflow may project a role into a harness-native agent/worker only when that workflow's contract allows the available lifecycle.

This is not a blanket rule that every multi-agent workflow can degrade to sequential role execution.

Examples:

- a bounded researcher/reviewer role can often be applied through one-shot delegation or sequential isolation;
- `ak-orchestrate` may explicitly degrade a job graph when its contract and evidence remain honest;
- `ak-team` requires a live team lifecycle and must not silently label ordinary subagents/sequential work as Team when creation/shared-state/messaging/wait/shutdown/cleanup are unavailable.

Do not duplicate role reasoning into separate Claude/Codex/Cursor sources.

## No hybrid default

Do not expose both full native Engineer and full fallback Skill catalogs at the same time.

That can mix generations, helper assumptions and cross-references into a workflow that neither source owns.

A deliberate debug/comparison session may inspect both, but must not become the production default.
