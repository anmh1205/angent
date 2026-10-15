# Reasoning about coordinated engineering work

Orchestration is a choice about **dependencies, ownership and evidence**. It is not inherently a daemon or a sequence of `ak orchestrate` commands. Native command names can suggest operations, but they do not establish useful parallelism or any worker capability.

## Decide whether work should be split

First understand the accepted outcome. Split work only where independent context, distinct specialist expertise, parallel execution or an independent challenge materially improves the result. If two work units edit the same state or one cannot start before the other's decision, model that dependency explicitly; a shared live repo does not become isolated merely because two agent prompts differ.

For each work unit, identify what it needs, what it owns, what it may change, what evidence it must return and what blocks acceptance. Avoid verbose general job manifests for work a single agent can own.

## Route based on the actual harness

A Skill can guide this decomposition even if no agent spawn API exists: one agent can execute the runnable units sequentially and reconcile their outputs. With a real delegate or process runtime, verify authentication/capability, workspace isolation, durable result and cancellation before dispatching effects. A role description is not a live teammate. Real Team requires creation, shared state/messaging, join and cleanup.

## Reason about progress, interruption and integration

A ready phase has satisfied dependencies. A submitted job is not a completed job; a worker's answer is not automatically proof of the expected artifact. Use observed provider handles and outcomes to maintain the actual frontier. Record long-running identities only when they really exist; a saved plan is not a running process.

When an operation's result is ambiguous, inspect authoritative state before retry, particularly for repository writes, deployments or destructive effects. Progress on independent work can continue while a real dependency is waiting. Integrate outputs with awareness of shared interfaces, incompatible assumptions and combined test needs. Preserve disagreement until evidence settles it.

## Calibration cases

- **Independent modules:** parallel coding may be suitable if contracts and file ownership do not overlap.
- **One blocking schema decision:** settle it first; two independent implementations based on conflicting assumptions are wasted work.
- **No worker API:** perform the dependency sequence in the main agent, do not invent worker IDs or streams.
- **Cancelled launch with uncertain effects:** reconcile actual files/provider state; don't resubmit blindly.
