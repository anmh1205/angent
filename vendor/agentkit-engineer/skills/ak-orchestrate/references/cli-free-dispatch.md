# AK orchestration actions mapped to ANGENT without a CLI

The 2.19.0 `ak orchestrate` includes `probe`, `prepare`, `start`, `advance`, `events`, `output`, `status`, `accept`, `resume`, `stop`, `diagnose` and `plan-status`. These are **different behaviors**, not universal file or background-job commands. A host must actually support each effect.

| Native intent | Portable implementation or truthful boundary |
|---|---|
| probe | discover installed worker/process, connected agent delegation and permissions; distinguish inventory from launch readiness |
| prepare | validate job graph dependencies, ownership, expected artifacts, runtime identity and permitted effects. Persist via authorized artifact/Continuity when resume matters |
| start | dispatch only through a **real** host worker/job API; if none, use sequential `Cook`/owner Skill instead of creating imaginary run ID |
| advance | select dependency-ready runnable units and update observed outcomes; do not treat an unchanged pending job as progress |
| status / plan-status | reconcile actual job/provider state and dependency evidence with Continuity; no synthetic RUNNING or DONE |
| output / events | retrieve actual bounded logs/artifacts/events only when the host exposes them; otherwise say unavailable |
| accept | evaluate received artifact/effect evidence against the stated acceptance criteria, not the worker's self-report |
| resume | read Continuity frontier and real operation handles, reconcile ambiguous effects before retry; never replay a write blindly |
| stop | cancel/terminate only via actual provider process control, current authorization and verified operation identity; cancellation request is not completion |
| diagnose | inspect bounded logs/trace, capability/cwd/auth and affected dependencies; never spill secrets into a generic diagnostic dump |

For no-delegation harnesses, the **job-graph reasoning** still applies to sequential work when helpful, but no process supervision, parallelism, durable process handles, event streaming or team semantics are claimed. A process handle that no longer exists cannot be recovered by fabricating an ID. Every side effect requires an independent authority check at invocation time.

## Integration invariants

- Contract scopes allowed work; Execution performs effects; Reasoning owns dependency scheduling; Continuity preserves resume-safe operation identity; Quality checks settled outputs.
- Actual `ak run` dispatch uses a configured adapter with stdout/stderr/NDJSON and timeouts. A portable Skill invocation need only meet the *task outcome*; it must **not** counterfeit the adapter process or event wire format.
- Preserve the exact selected runtime when the user specifies one. Do not silently swap `codex` for the main chat agent to claim a Handover succeeded.
- For external side effects or tools that may be long-running, save PREPARED intent before mutation if a durable store is available, reconcile provider result, and mark uncertain outcomes as ambiguous rather than automatically retry.
