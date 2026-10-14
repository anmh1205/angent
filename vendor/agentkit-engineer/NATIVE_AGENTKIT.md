# Native AgentKit Engineer

Use the **official AgentKit distribution** for the native path. ANGENT does not bundle or mirror native AgentKit Engineer source.

## Official sources

Start from:

- AgentKit: https://agentkit.best
- Stable docs: https://docs.agentkit.best/en/stable
- Installation: https://docs.agentkit.best/en/stable/getting-started/installation
- Engineer Kit: https://docs.agentkit.best/en/stable/kits/engineer
- Engineer Skills: https://docs.agentkit.best/en/stable/kits/engineer/skills
- Engineer Agents: https://docs.agentkit.best/en/stable/kits/engineer/agents

As retrieved on 2026-10-14, the stable resolved Engineer package documents **103 public Skills and 16 Agents**.

That count is provenance, not runtime proof. Native availability still depends on the active target/scope and current installation.

## Target and scope

AgentKit `--global` means **user scope for a selected runtime target**.

It is not one universal “global target”.

Native Engineer may be projected to supported runtimes according to the current AgentKit release.

ANGENT therefore does not detect native Engineer by checking only one runtime home.

## ANGENT native-use rule

ANGENT prefers native Engineer only when it is **usable in the active environment**.

The active harness/session should establish that it can actually discover/invoke native Engineer.

Supporting diagnostics may include:

- `ak --version`;
- `ak doctor --offline --json` or `ak doctor --json`;
- runtime-native Skill/Agent inventory.

Binary presence, an old cache, a historical install receipt, or documentation saying a Skill exists is insufficient on its own.

If native usability cannot be established, use the ANGENT fallback plugin instead of reconstructing native AgentKit from cache.

## Read-only selector

`scripts/select_engineer.py` implements the source-selection contract.

It does not install, login, repair, refresh or mutate AgentKit.

The harness supplies whether native Engineer is usable; the script adds read-only AgentKit health evidence and returns either:

- `native`;
- `fallback`;
- `blocked` when the fallback package/catalog itself is invalid.

## No upstream source copy

Do not copy AgentKit's native Skill/Agent tree into ANGENT for the native path.

The official AgentKit installation owns native upstream content and updates.

ANGENT maintains its own semantically adapted fallback only for environments where native Engineer is unavailable or unusable.
