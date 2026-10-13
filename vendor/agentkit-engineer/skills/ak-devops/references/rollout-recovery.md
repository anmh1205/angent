# Rollout and recovery

Plan:
- rollout strategy;
- readiness/health criteria;
- traffic transition;
- migration ordering;
- rollback/forward-fix path.

During rollout observe:
- error rate;
- latency;
- health/readiness;
- crash/restart behavior;
- provider/controller status.

If rollback is unsafe because data/schema already changed, say so explicitly and use forward-fix semantics.
