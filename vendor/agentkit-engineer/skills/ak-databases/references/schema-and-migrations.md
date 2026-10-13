# Schema and migration safety

For each migration identify:
- current and target schema/data state;
- application versions that may coexist;
- backfill requirements;
- lock/table rewrite risk;
- rollback/forward-fix strategy;
- validation query;
- deployment ordering.

Prefer expand → migrate/backfill → contract for compatibility-sensitive changes.

Indexes should correspond to real query predicates/order/join patterns and be verified with plans/measurements.
