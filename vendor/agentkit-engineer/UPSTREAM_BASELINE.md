# AgentKit Engineer stable package baseline

## Authoritative recheck (2026-10-15)

On the authenticated AgentKit 2.19.0 CLI with an active Engineer license, an explicit remote registry export completed:

```sh
ak kit init engineer --target portable --channel stable --version 2.19.0 --out <isolated-temp-dir> --json --no-interactive
```

The returned `kit.init` result had `success: true`, `skillsSelected: 103`, `skillsAvailable: 103` and `filesWritten: 1758`. Direct inspection of the exported `agentkit-portable/skills/*/SKILL.md` files confirmed **103 public Skill identities**, and `.agentkit/agents/*.md` confirmed **16 Agent sidecars**. A recursive count of all nested `SKILL.md` files is not the public catalog count (it includes nested guidance).

The canonical SHA-256 of the lexicographically sorted identity arrays (`agent_roles`, `skills`, compact JSON with sorted keys) was independently computed from the exported tree:

```
439bc625174a6e9e780f8f464b0129ccf9bfcb4ba5b63d7fa3734d0e05541ddc
```

That digest matches the 103/16 catalog baseline recorded by the previous stable catalog PR. This direct package observation supersedes the older 102-directory export snapshot. A successful authenticated export establishes identity/catalog provenance, not byte-identical runtime or model performance.

## Migration of retired and internal identities

Six former workflow names are retired from public Skill discovery: `ak-security-scan`, `ak-use-mcp`, `ak-handover`, `ak-html-video`, `ak-sequential-thinking`, `ak-web-design-guidelines`. The portable replacement routes are documented in `retired-routes/README.md`; previous Git history retains their earlier guidance.

The former `ak-common` entry is an internal convention, now in `internal/common.md`, not a public invocation identity.

Eight current public identities are included: `ak-bro`, `ak-diagram`, `ak-enhance-ux-ax`, `ak-explain`, `ak-page-builder`, `ak-sowat`, `ak-sumup`, and `ak-webmcp`.

## Porting and verification boundary

ANGENT's fallback preserves relevant workflow outcomes and the cognitive/authorization gates, not AgentKit CLI internals, authentication state, hooks, proprietary services or background runtimes. Agent sidecars are roles, not live team processes. Skills depending on browsers, provider services, live teams, rendering or remote datasets remain adapted/degraded or explicitly blocked where necessary.

The earlier 102-Skill support-path and source-line comparison belongs to the historical `AUDIT_REPORT.md` evidence and cannot prove parity for this revised catalog. Use the current `PORTING_MANIFEST.md` for per-identity source-level status, the selector for exact identity checks, and independent activated-harness acceptance for behavioral claims.

Official documentation: https://docs.agentkit.best/en/stable/kits/engineer
