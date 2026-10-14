# Active-work frontier

Continuity is proactive because interruption timing is not predictable.

## Create active work when

The task has meaningful state that would be costly, ambiguous, or unsafe to reconstruct: repository migration, broad audit, project execution, long research, multi-chapter writing, multi-stage mutation, or a long-running operation whose handle/result matters later.

Do not create durable work state for trivial one-turn questions.

## Frontier contents

Keep:
- requested outcome;
- active scope/phase;
- constraints/invariants;
- verified completed units;
- current unfinished unit;
- consequential decisions;
- compact decision basis or pointer when later work depends on why a decision was valid;
- accepted baseline/artifact pointers when later work depends on them;
- collaboration-state pointer/subset when losing it would change resume behavior;
- active long-running operations when needed: provider/tool, operation identity/handle, last observed state, dependent work, and next informative check condition;
- artifact/source pointers and versions;
- unresolved dependencies;
- pending/ambiguous effects;
- next safe action.

Do not persist raw hidden reasoning. A decision basis contains only reconstructable premises/evidence pointers, constraints, decision and reconsideration trigger needed for future correctness.

## Meaningful boundaries

Advance a revision when a work unit completes, a consequential decision changes later work, a decisive premise/evidence version materially changes, an artifact/source version materially changes, a blocker changes, scope/invariant changes, a collaboration mode materially changes ongoing work, a long-running operation materially changes state, an external effect is reconciled, or a handoff/compaction/phase boundary occurs.

An unchanged pending/running status is not by itself a meaningful frontier revision.

Do not persist after every read/tool call unless risk requires it.

## Separation

The frontier is task state.

It is not AGENTS.md, a permanent user profile, project memory, promoted Learning, or a transcript.

Collaboration state is reconstructed by Context. Continuity carries only the compact subset/pointer needed for safe resume.

Execution owns the decision of when polling a running operation is informative.
