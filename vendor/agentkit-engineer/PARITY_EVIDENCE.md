# Engineer fallback parity evidence — 2026-10-14

This record supports ANGENT's **workflow-semantic/public-contract coverage** claim for the portable Engineer fallback.

It does not claim exact AgentKit source, package, Hook, Agent runtime, process-supervisor, or registry-export parity.

## Source evidence

Two upstream surfaces were observed and are intentionally kept separate.

### Stable documentation

Stable docs describe:

- 103 public Engineer Skill identities;
- 16 Agent roles;
- six retired route names outside the current public workflow set.

Identity target digest:

`439bc625174a6e9e780f8f464b0129ccf9bfcb4ba5b63d7fa3734d0e05541ddc`

### Stable registry portable export

Current stable CLI `ak 2.19.0` was verified as current through `ak self-update --check --channel stable --json`.

A remote portable export observed:

- 102 Skill identities;
- 16 preserved Agent sidecar roles;
- legacy identities including `ak-common` and six retired routes;
- identity digest `42b5e9c0b21fdad38ea8278202f730350e85557b6e03a97c1e27256f922dcb35`.

The export explicitly marks the portable target as best-effort/non-production.

Therefore the fallback is **not** described as exact current-registry package parity.

## Candidate migration

The fallback public discovery tree is reconciled to the documented stable public workflow contract:

- add 8 documented current identities:
  - `ak-bro`
  - `ak-diagram`
  - `ak-enhance-ux-ax`
  - `ak-explain`
  - `ak-page-builder`
  - `ak-sowat`
  - `ak-sumup`
  - `ak-webmcp`
- remove 6 retired route identities from public Skill discovery;
- move `ak-common` conventions outside the public Skill root;
- preserve 16 portable Agent role definitions.

Retired route guidance remains documentation, not runnable Skill identity.

## Readiness semantics

Fallback readiness means:

1. fallback manifest is structurally valid;
2. `STABLE_CATALOG.json` is internally coherent and its documented-contract digest matches the expected 103/16 identity set;
3. discovered fallback public Skill identities exactly equal that target;
4. discovered fallback Agent roles exactly equal the 16-role target;
5. no retired or internal identity leaks into public discovery.

A count match alone is insufficient. Same-count identity substitution must fail readiness.

## Semantic calibration focus

High-risk/current workflows receive behavior review beyond catalog presence:

- native-first selection: CLI/cache/docs presence is not native runtime usability;
- Team: requires the live team lifecycle; ordinary subagents/sequential roles are not silently relabeled as Team;
- Orchestrate: preserves dependency-aware routing/evidence and states interruption/parallelism limitations honestly;
- Bootstrap/Cook: mode semantics do not create unrelated authority;
- Test/Code Review: review/test evidence stays independent enough for the claim and unsupported parallel/ultra behavior fails closed;
- Security: scan/threat/fix boundaries preserve authorization, redaction, and verification;
- Find Skills: local installed discovery and external package installation remain distinct;
- new Skills preserve the workflow boundaries documented by AgentKit while mapping unavailable runtime helpers to harness-native capabilities or explicit limitations.

## Acceptance evidence

Populate/refresh this section from the exact candidate commit before acceptance:

- exact Skill/Agent set check;
- frontmatter name ↔ directory identity check;
- retired/internal discovery leak check;
- selector native/fallback/blocked behavior;
- negative same-count identity substitution check;
- Python syntax and manifest parse;
- committed diff hygiene;
- representative semantic read-back for new/high-risk workflows.

Do not turn this file into remembered PASS authority: acceptance evidence is valid only for the source commit and conditions it records.
