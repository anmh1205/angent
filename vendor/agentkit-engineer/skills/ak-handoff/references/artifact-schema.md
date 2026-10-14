# Handoff artifact schema — portable fallback

The artifact is a human/agent-readable view of ANGENT Continuity and verified current evidence.

## Mission

What outcome is being pursued and what is currently in scope.

## Constraints / authority

Only constraints, non-goals, project rules, and authority boundaries that materially affect continuation.

## Current frontier

Preserve when relevant:
- verified completed units;
- unfinished branches;
- branch state: RUNNABLE / WAITING_EXTERNAL / BLOCKED;
- dependencies/shared-state assumptions;
- saved operation handle and next informative observation condition;
- stale/recheck units after changed evidence/dependencies.

Do not reduce a multi-branch frontier to one “last unfinished action” if doing so would make the successor serialize independent work or replay a wait.

## Decisions

Consequential decisions that affect future work, with only the compact externalizable decision basis needed to reconstruct validity:
- decisive evidence/source pointers;
- governing constraints;
- selected decision;
- reconsideration/refresh trigger.

Do not persist private chain-of-thought.

## Rejected approaches / traps

Include only when a successor would otherwise plausibly repeat a known failed/unsafe path.

State the observable reason/evidence, not hidden reasoning.

## Artifacts and source versions

Paths, URLs, branch/commit, issue/page IDs, provider versions, plan/baseline pointers, or artifact digests required to recover context.

## Verification

Tests/checks/provider reads that already establish state, including their relevant validity boundary.

## Blockers and uncertainty

Unresolved dependencies, contested/stale assumptions, or unavailable capabilities.

## Pending / ambiguous effects

Any PREPARED / ATTEMPTED_UNKNOWN / outcome-unknown external operation that must be reconciled before replay.

## Next safe work

Prefer a small set of currently RUNNABLE work or the exact condition that must become true before a waiting branch can be observed again.

## Metadata

Optional metadata:
- work ID/revision;
- generated-at;
- source session/harness;
- source branch/commit;
- generator: `angent-fallback/ak-handoff`.

The artifact never outranks newest user instruction, applicable `AGENTS.md`, canonical Continuity state, or live provider/source evidence.
