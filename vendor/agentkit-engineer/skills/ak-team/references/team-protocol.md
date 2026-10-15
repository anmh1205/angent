# Team protocol

## Capability contract

A Team run requires live:
- teammate creation;
- shared work/state;
- direct coordination/messaging;
- wait/join;
- shutdown;
- cleanup.

If the runtime lacks one of these, do not emulate Team with ordinary subagents and claim parity. Route to Orchestrate or sequential work instead.

## Teammate contract

For each teammate define:
- role;
- exact question/work unit;
- owned scope/files/state;
- inputs/evidence pointers;
- allowed effects;
- dependencies;
- acceptance evidence;
- return format.

Avoid overlapping writers and hidden shared-state dependencies.

## Shared work

The lead keeps:
- dependency graph;
- ownership;
- blocked/runnable/completed state;
- decisions that affect multiple teammates.

Teammates receive only the context needed for their owned work, not the entire user/project profile.

## Join and integration

At join:
- inspect artifacts/evidence rather than trusting completion narration;
- deduplicate repeated findings;
- detect shared assumptions;
- preserve contradictions;
- integrate compatible work;
- route strategic disagreement to Reasoning;
- run combined verification where integration can create new failure modes.

Do not majority-vote.

## Shutdown

After required work is integrated or intentionally abandoned:
- stop/shutdown live teammate sessions;
- preserve only durable evidence/frontier needed for resume;
- clean up temporary team state.

A Team workflow that leaves live workers/state orphaned is incomplete.
