# Schema and migration safety

For each migration identify:
- current and target schema/data state;
- exact environment and owner;
- application versions that may coexist;
- backfill requirements and resumability;
- lock/table rewrite or long-running transaction risk;
- destructive/replace semantics;
- forward plan;
- rollback or compensating strategy;
- validation queries and application-level checks;
- post-change observation window when required.

Prefer expand → migrate/backfill → contract for compatibility-sensitive changes.

## Production gate

Before production mutation, establish the recovery boundary appropriate to the change:
- current backup/snapshot or another sufficient recoverable state;
- a restore route that is tested or otherwise credibly established;
- least-privilege credentials;
- maintenance/traffic assumptions;
- explicit authority for the exact environment and operation.

If rollback becomes unsafe after a data transform, say so before execution and use a forward-fix/compensation plan instead of pretending reversibility.

Indexes should correspond to real query predicates/order/join patterns and be verified with plans/measurements.

A migration command returning success does not establish application compatibility or correct backfill results.
