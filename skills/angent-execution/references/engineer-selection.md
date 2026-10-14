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
    ├── skills/                         # 102 fallback Skills
    └── agents/                         # 16 portable role definitions
```

Client installation/enablement is outside the portable Agent Plugins v1 manifest. A runtime adapter or installer selects which Engineer source to expose.

For ChatGPT/Codex, the same fallback root also carries `.codex-plugin/plugin.json` pointing to the same `skills/` directory. This is a packaging projection only; there is still one fallback Skill source tree.

## Native usability

Do not infer native usability from:

- an `ak` binary alone;
- `~/.agentkit` cache content;
- one historical install receipt;
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

If the fallback plugin is missing/invalid, selection is blocked rather than pretending a capability exists.

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

## Agent roles

Agent Plugins v1 standardizes Skills and MCP servers, not an Agent component.

The 16 fallback Agent files are therefore a portable **role library**:

- a harness with native subagents may project a role into its own agent format;
- Team/Orchestrate may pass the role instruction to a one-shot worker;
- a harness without delegation may apply the role sequentially in the main agent.

Do not duplicate role reasoning into separate Claude/Codex/Cursor sources.

## No hybrid default

Do not expose both full native Engineer and full fallback Skill catalogs at the same time.

That can mix generations, helper assumptions and cross-references into a workflow that neither source owns.

A deliberate debug/comparison session may inspect both, but must not become the production default.
