# Handoff artifact schema — portable fallback

The artifact is a human/agent-readable view of ANGENT Continuity state.

Recommended sections:

## Mission

What outcome is being pursued and what is currently in scope.

## Constraints / invariants

Only constraints that matter to continuation.

## Current frontier

- verified completed units;
- active unfinished unit;
- remaining dependent work.

## Decisions

Consequential decisions that affect future work, including concise decisive evidence or reconsideration trigger when useful.

## Artifacts and source versions

Paths, URLs, branch/commit, issue/page IDs, or provider versions required to recover context.

## Verification

Tests/checks/reads that have already established state.

## Blockers and uncertainty

Unresolved dependencies, contested assumptions, or unavailable capabilities.

## Pending / ambiguous effects

Any PREPARED or ATTEMPTED_UNKNOWN external operation that must be reconciled before replay.

## Next safe action

The first unfinished action a successor can take after revalidating stale-sensitive state.

## Metadata

Optional metadata may include:
- work ID;
- revision;
- generated-at;
- source session/harness;
- generator: `angent-fallback/ak-handoff`.

The artifact must not be treated as more authoritative than current user instruction, AGENTS.md scope, or live provider state.
