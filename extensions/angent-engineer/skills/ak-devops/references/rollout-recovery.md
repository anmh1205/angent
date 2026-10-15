# Rollout and recovery

Plan:
- rollout strategy;
- readiness/health criteria;
- traffic transition;
- migration/state ordering;
- rollback or forward-fix path;
- stop/abort condition.

During rollout observe:
- provider/controller status;
- readiness/health;
- error rate;
- latency;
- crash/restart behavior;
- traffic and dependency health when material.

A rollout can be partially successful: preserve which resources/replicas/steps changed instead of collapsing the result to success/failure.

If rollback is unsafe because data/schema/state already changed, say so explicitly before relying on it and use forward-fix/compensation semantics.

Cancellation/rollback/deletion are separate effects with their own authority and blast radius.
