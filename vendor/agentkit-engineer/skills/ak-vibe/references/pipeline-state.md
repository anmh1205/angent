# Vibe pipeline state

Track the pipeline as durable semantic state:

- requested outcome;
- current stage;
- accepted plan/artifact pointers;
- branch/worktree/PR identifiers;
- completed verification;
- blocking findings;
- unresolved decisions;
- exact next runnable stage;
- authorized endpoint.

## Failure continuation

A failure does not reset the whole pipeline.

Examples:
- test failure → Debug/Fix → rerun affected tests → continue to review;
- review finding → Cook/Fix → targeted verification → re-review;
- CI failure → diagnose/fix → push/update → observe CI again;
- merge conflict/base drift → reconcile branch → rerun materially affected checks.

Continue until the authorized endpoint is verified or a genuine blocker/decision/authority boundary is reached.

## Endpoint examples

Possible endpoints include:
- implementation verified locally;
- PR created and ready;
- PR reviewed and checks green;
- merged;
- post-merge CI green.

Release/deployment is separate unless the task explicitly includes it.
