# Query performance

Use real plans/measurements.

Inspect:
- predicate selectivity;
- join order/strategy;
- sort/aggregate;
- row estimates vs actual;
- index usage;
- repeated queries/N+1;
- lock/wait time;
- network/result size.

An index has write/storage/maintenance cost.

Do not add indexes based only on column names; tie them to observed query shapes.
