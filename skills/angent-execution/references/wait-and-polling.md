# Wait and polling semantics

Long-running operations must not monopolize the execution loop merely because a status endpoint is available.

## Start

When an operation returns a running/pending state or a durable handle:

1. capture the handle/operation identity;
2. record the latest observed state;
3. identify the next condition that would make a re-check informative;
4. persist it through Continuity when interruption-safe resume matters;
5. mark only dependent work as waiting.

A running operation is not automatically a global blocker.

## Prefer useful work over polling

Before polling again, inspect the current plan for independent useful work.

Independent work may include:
- read-only inspection unrelated to the pending result;
- research for another unresolved branch;
- preparing a candidate that does not depend on the running result;
- checking another independent source/provider;
- documenting or reconciling state already established.

Do not invent busywork merely to avoid a poll. The alternative work must advance the requested outcome.

## Poll only when informative

A new status check is justified when at least one is true:

- a meaningful time interval has passed relative to the operation;
- the provider emitted an event/state transition;
- another completed work unit now depends on the result;
- the operation's documented next-check condition is satisfied;
- a timeout/lease/deadline is near enough that status changes the next action;
- the user explicitly asks for the current status.

Do not issue repeated equivalent polls merely because the previous response was still pending.

## No-progress detection

If equivalent checks return the same state and no new evidence:

- treat them as one continuing wait state, not multiple completed work units;
- increase the threshold for another check when appropriate;
- continue independent work if available;
- return to Reasoning if the plan has become dominated by waiting or if a different strategy may unblock progress.

Polling frequency is a reasoning/execution decision, not a fixed timer baked into ANGENT.

## If nothing else can run

Preserve the handle and current frontier.

When the host permits visible progress updates, send a brief state marker rather than generating a stream of identical tool calls.

Do not tell the user that ANGENT will continue in the background unless the host actually schedules/runs future work.

## Resume

On resume:

1. recover the saved operation handle/identity;
2. inspect authoritative current state;
3. reconcile whether it completed, failed, disappeared, or is still running;
4. do not relaunch until the prior outcome is known or safe replay is established;
5. continue dependent work only after the needed state is observed.

## Behavioral calibration

A correct behavior case:

> A long build is running while independent source inspection remains.

Expected behavior:
- preserve PID/job/run ID;
- inspect the independent source;
- return to the build later;
- poll only when another check can plausibly add information.

Incorrect behavior:
- repeatedly call status/read-output with no intervening evidence or useful work;
- hold the entire task idle while runnable independent work exists;
- interpret repeated pending responses as progress.
