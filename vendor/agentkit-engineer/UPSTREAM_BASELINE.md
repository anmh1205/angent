# AgentKit Engineer stable baseline

This file records the upstream **semantic/catalog baseline** used by ANGENT's portable Engineer fallback. It is not a vendored upstream source mirror.

## Retrieval

- channel: `stable`
- retrieved: `2026-10-14`
- resolved public Skills: `103`
- resolved Agents: `16`
- catalog identity SHA-256: `fbe4be0fa01ff696fdc783d8e398a4fb157b7c31d831d6eb792dea55ca627a9e`

The digest is over the sorted resolved public Skill identities and Agent role identities recorded by the fallback selector. It proves which identity set this migration targets; it is **not** an upstream package-byte digest.

## Primary sources

- https://agentkit.best
- https://docs.agentkit.best/en/stable/kits/engineer
- https://docs.agentkit.best/en/stable/kits/engineer/skills
- https://docs.agentkit.best/en/stable/kits/engineer/agents
- individual stable Skill guides for workflow semantics and runtime boundaries

The stable Engineer overview reports 103 resolved Skill identities and 16 Agents.

## Retired identities

Stable documentation keeps navigation pages for these names but states they are no longer packaged public Skills:

- `ak-security-scan`
- `ak-use-mcp`
- `ak-handover`
- `ak-html-video`
- `ak-sequential-thinking`
- `ak-web-design-guidelines`

Fallback compatibility mapping lives in `retired-routes/README.md`, outside the discovery root.

## Internal support

`ak-common` is ANGENT fallback support, not an upstream/public workflow. Its conventions live under `internal/common.md` and are excluded from public Skill counting.

## Porting rule

Preserve workflow outcome, gates, evidence semantics and capability boundaries.

Do not mirror AgentKit runtime implementation, Hooks, statusline, installer state or helper internals merely to make the fallback look structurally identical.

When a current workflow depends on a capability the active harness cannot reproduce, mark the route adapted/degraded or block the unavailable operation instead of claiming false parity.
