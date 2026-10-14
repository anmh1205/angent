# AgentKit Engineer upstream baseline

This file records the upstream evidence used to maintain ANGENT's portable Engineer fallback. It intentionally separates the **documented public workflow contract** from the **registry portable export actually observed**.

ANGENT does not vendor or mirror the native AgentKit source/runtime.

## Documented stable public contract

Retrieved: **2026-10-14**

Official stable documentation used:

- https://docs.agentkit.best/en/stable/kits/engineer
- https://docs.agentkit.best/en/stable/kits/engineer/skills
- https://docs.agentkit.best/en/stable/kits/engineer/agents
- individual stable Skill guides for changed or high-risk workflows

Documented public contract:

- public Skill identities: **103**
- Agent roles: **16**
- identity-set SHA-256: `439bc625174a6e9e780f8f464b0129ccf9bfcb4ba5b63d7fa3734d0e05541ddc`

The digest is computed from canonical UTF-8 JSON with sorted keys and arrays:

```json
{"agent_roles":[...sorted 16 roles...],"skills":[...sorted 103 skill IDs...]}
```

using compact separators and SHA-256.

Stable documentation marks these old routes as retired rather than current public workflows:

- `ak-security-scan`
- `ak-use-mcp`
- `ak-handover`
- `ak-html-video`
- `ak-sequential-thinking`
- `ak-web-design-guidelines`

The documented surface includes the newer public identities:

- `ak-bro`
- `ak-diagram`
- `ak-enhance-ux-ax`
- `ak-explain`
- `ak-page-builder`
- `ak-sowat`
- `ak-sumup`
- `ak-webmcp`

## Observed stable registry portable export

Observed: **2026-10-14**

CLI evidence:

- `ak --version` → `2.19.0`
- `ak self-update --check --channel stable --json` → current = latest = `2.19.0`, update unavailable
- remote stable portable export command:
  `ak kit install engineer --target portable --out C:\Temp\ak-engineer-stable-export --zip --channel stable --yes --no-interactive --json`
- CLI result: `skillsSelected=102`, `skillsAvailable=102`, 16 Agent sidecars preserved
- exported identity-set SHA-256: `42b5e9c0b21fdad38ea8278202f730350e85557b6e03a97c1e27256f922dcb35`

The exported 102 set still contained `ak-common` and the six retired routes above and did not contain the eight newer documented identities.

The portable export itself states that it is a best-effort, unsupported, non-production target and that Agent/Hook sidecars are preserved-only rather than activated.

## Reconciliation policy

These observations are not collapsed into one false claim.

- **Native path:** use the actual AgentKit package/runtime visible in the active harness. ANGENT does not force its fallback catalog onto native AgentKit.
- **Fallback identity target:** follow the documented stable public workflow contract (103 public Skill identities + 16 portable role definitions).
- **Fallback parity claim:** workflow-semantic/public-contract coverage only.
- **Not claimed:** byte parity, source parity, runtime-mechanics parity, or identity equality with the currently observed registry portable export.
- **Drift trigger:** when either docs or the registry export changes, re-run catalog reconciliation before updating the fallback claim.

This boundary lets ANGENT provide the current documented workflows without hiding upstream delivery drift.
