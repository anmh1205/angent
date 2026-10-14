# Team protocol

## Live lifecycle preflight

Before calling a workflow Team, verify the active harness can provide the load-bearing lifecycle:
- create teammates/sessions;
- maintain shared work/task state;
- send direct coordination messages;
- observe wait/status;
- shut down teammates;
- clean up team state;
- preserve required write/isolation boundaries.

If a required capability is absent, hard-stop Team and offer a separately named route. Do not silently replace it with ordinary subagents or sequential role-play.

## Teammate contract

For each teammate define:
- role;
- exact question/work unit;
- owned scope/files;
- inputs;
- allowed effects;
- acceptance evidence;
- return format.

Avoid overlapping writers.

Prefer artifact/evidence pointers over transcript exchange.

## Coordination

Treat idle/waiting as a lifecycle state, not completion.

Do not poll a teammate repeatedly when another independent team workstream remains runnable.

Shared team messages are coordination evidence, not automatic strategic decisions.

## Join

At join:
- require prerequisite teammates/work units to have actually settled;
- deduplicate repeated findings;
- detect shared assumptions;
- preserve contradictions;
- integrate compatible work;
- verify combined state independently;
- route strategic disagreement to ANGENT Reasoning.

Do not majority vote.

## Shutdown and cleanup

Shut down and clean up through the verified live lifecycle.

Report cleanup failures as unresolved runtime state. Do not guess internal team directories or claim cleanup without observation.
