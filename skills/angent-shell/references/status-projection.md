# ANGENT status-sign projection

The status sign is a compact user-facing view of **already-established task state**. Its purpose is situational awareness: the user should be able to see what ANGENT is doing and whether important state changed without reading tool logs or internal reasoning.

## Canonical fields

Use only fields that materially help the current interaction.

### Identity

- `owners` — ANGENT owners actually active for the current work.
- `mode` — optional interaction/effort mode only when it clarifies behavior, such as audit, repair, execute, author, or resume.
- `work` — a short stable work/frontier label for substantial tasks.

### Live state

Prefer one of:
- `ACTIVE` — useful work is currently runnable/in progress;
- `WAITING_EXTERNAL` — the relevant branch is waiting and no claim is made that it is runnable;
- `BLOCKED` — a real dependency/authority/capability/decision prevents safe progress;
- `VERIFYING` — candidate/effect exists but endpoint acceptance is still being checked;
- `VERIFIED` — the stated endpoint/milestone is established by the relevant evidence boundary.

Do not invent a separate status vocabulary when a domain/provider already has an authoritative state that the user needs to see.

### Frontier

When multi-branch state matters, summarize only the decision-relevant frontier:
- currently active/runnable work;
- meaningful WAITING_EXTERNAL branch and its trigger when useful;
- real blocker;
- newly completed/verified branch.

Avoid unexplained counters or scheduler-looking telemetry. Prefer `waiting=build#123; active=audit` over opaque `R2/W1/B0` unless the compact notation was already agreed with the user.

### Verification

`verified=` names one or two newly established milestones that explain why the state changed.

Examples:
- `verified=PR #17 merged + hygiene PASS`
- `verified=provider read-back matches target`

Do not list every completed action.

### Synchronization

Use only when there are multiple versioned surfaces whose alignment affects correctness.

Suggested semantic states:
- `SYNCED` — canonical source/package/runtime identities were directly reconciled;
- `DRIFT` — a material mismatch is directly observed;
- `SYNC_UNKNOWN` — alignment matters but current evidence cannot establish it.

When shown, include the minimum disambiguating identities, for example:
`sync=SYNCED main@601efaa ↔ plugin 1.0.5`

Never infer sync because version strings look equal; reconcile the relevant source/runtime contents or release identity when that distinction matters.

### Next action

`next=` is the next substantive frontier step already selected by Reasoning. It is not a promise of background execution.

## Recommended forms

### Start of substantial work

`[Used ANGENT] [angent + angent-context + angent-reasoning + angent-execution + angent-continuity]`

`[ANGENT Status] ACTIVE | work=engineer-refresh | sync=SYNCED main@94aa67e ↔ plugin 1.0.5 | next=catalog migration`

### Branch waiting while independent work proceeds

`[ANGENT Status] ACTIVE | waiting=build#3855 | active=Engineer audit | next=dependency migration`

### Real blocker

`[ANGENT Status] BLOCKED | work=release | blocker=production credential unavailable | decision=user authority required`

### Verified end

`[ANGENT Status] VERIFIED | endpoint=Engineer fallback refreshed | canonical=main@<sha> | runtime=plugin <version>`

These are forms, not rigid templates. Omit fields that do not change the user's understanding.

## Update discipline

Emit a new PROGRESS sign when a material semantic transition occurs, not after a fixed time or number of tool calls.

Useful transitions include:
- ACTIVE → WAITING_EXTERNAL / BLOCKED / VERIFYING / VERIFIED;
- a waiting branch becomes eligible or completes;
- another branch becomes runnable because a dependency changed;
- a canonical/runtime DRIFT becomes SYNCED;
- Quality FAIL/BLOCKED/PASS changes the transition it protects;
- a checkpoint/baseline advances in a way that changes safe resume behavior.

A long silent stretch may justify one compact state marker even without a new milestone, but it must report the same truth without pretending progress occurred.

## Provenance and confidence

The status line may compress information, but it must preserve evidence strength:
- source/provider observation can be shown as observed/verified only within its actual boundary;
- inferred next work remains a plan/selection, not a completed fact;
- worker/specialist narration is not equivalent to endpoint evidence;
- checkpoint state can summarize prior verified work but cannot override newer live source/provider state.

## Relationship to other owners

- Contract defines authority and requested endpoint.
- Context reconstructs current/collaboration/version state.
- Reasoning owns frontier selection and active/blocked semantics.
- Execution observes effects/providers and reports wait/observation state.
- Continuity persists resume-critical frontier/checkpoint state.
- Quality supplies required acceptance verdicts.
- Shell only renders a compact projection of those states.

This separation keeps the sign informative without turning it into another control plane.
