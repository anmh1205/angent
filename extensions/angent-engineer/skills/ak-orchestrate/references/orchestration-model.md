# Orchestration model

## Job

Each job needs:
- outcome;
- input/artifact pointers;
- scope/owned files;
- prerequisites;
- allowed effects;
- capability requirements;
- acceptance evidence;
- stop/replan condition.

## Isolation

Use separate worktrees/sandboxes when concurrent writes would collide.

Isolation prevents file collisions, not logical/API conflicts.

## Capture

Every job returns:
- artifact/evidence pointer;
- changed state/version;
- unresolved uncertainty;
- completion/blocker status.

Do not rely on worker transcript retention.

## Arbiter

Use an independent reviewer when multiple implementations/analyses need adjudication.

Arbiter compares evidence and contract; it does not majority-vote worker opinions.
