# Wait and polling semantics

Long-running operations must not monopolize the cognitive loop merely because a status endpoint is available.

Execution owns observation of the external operation. Reasoning owns selection of the next branch of work.

## Start

When an operation returns a running/pending state or a durable handle:

1. capture the handle/operation identity;
2. record the latest observed state;
3. identify the next condition that would make another observation informative;
4. return a wait-state observation to Reasoning;
5. persist it through Continuity when interruption-safe resume matters;
6. mark only dependent work as waiting.

A running operation is not automatically a global blocker.

After reporting WAITING_EXTERNAL, Execution should yield control. It must not immediately re-enter the same status call unless Reasoning has made the branch eligible again because its informative-check condition is satisfied.

## Prefer useful work over polling

Reasoning, not Execution in isolation, decides whether independent useful work exists because that requires the whole active frontier.

Independent work may include:
- read-only inspection unrelated to the pending result;
- research for another unresolved branch;
- preparing a candidate that does not depend on the running result;
- checking another independent source/provider;
- documenting or reconciling state already established.

Do not invent busywork merely to avoid a poll. The alternative work must advance the requested outcome.

## Poll only when informative

Execution should perform another status observation only after Reasoning returns to the waiting branch because at least one is true:

- a meaningful time interval has passed relative to the operation;
- the provider emitted an event/state transition;
- another completed work unit now depends on the result;
- the operation's documented next-check condition is satisfied;
- a timeout/deadline is near enough that status changes the next action;
- the user explicitly asks for the current status.

Do not issue repeated equivalent polls merely because the previous response was still pending.

## No-progress detection

If equivalent checks return the same state and no new evidence:

- treat them as one continuing wait state, not multiple completed work units;
- return WAITING_EXTERNAL to Reasoning;
- do not locally compensate by choosing a larger arbitrary poll interval;
- inspect whether the branch was incorrectly left runnable or independent work was missed.

Polling frequency is not a fixed timer baked into ANGENT.

## If nothing else can run

If Reasoning determines that no independent branch is runnable and no informative wait trigger is currently satisfied, preserve the handle/current frontier instead of issuing another equivalent tool call.

When the host permits visible progress updates, send a brief state marker only when useful to the user.

Do not tell the user that ANGENT will continue in the background unless the host actually schedules/runs future work.

## Changed instruction while waiting

If a new user instruction changes the objective or authority while a branch is WAITING_EXTERNAL:
- Reasoning re-evaluates whether any **future dependent work** remains authorized/useful;
- keep the operation handle until authoritative state shows what happened;
- do not interpret “stop” as proof the provider operation stopped;
- when cancellation is available and currently desired/authorized, execute it as a separate bounded effect rather than as a polling shortcut;
- continue unrelated newly authorized work only when its dependencies remain valid.

The branch may remain relevant only for reconciliation even when it is no longer part of the desired forward plan.

## Resume

On resume:

1. recover the saved operation handle/identity and wait condition;
2. inspect authoritative current state when the wait condition is now eligible or live reconciliation is required;
3. reconcile whether it completed, failed, disappeared, or is still running;
4. do not relaunch until the prior outcome is known or safe replay is established;
5. continue dependent work only after the needed state is observed.

## Behavioral calibration

A correct behavior case:

> A long build is running while independent source inspection remains.

Expected behavior:
- preserve PID/job/run ID and next informative observation condition;
- classify build branch WAITING_EXTERNAL;
- return to Reasoning;
- inspect the independent source;
- return to the build only when another check is eligible.

Incorrect behavior:
- repeatedly call status/read-output with no intervening trigger;
- let the most recent long-running operation monopolize next-action selection;
- hold the entire task idle while runnable independent work exists;
- interpret repeated pending responses as progress.
