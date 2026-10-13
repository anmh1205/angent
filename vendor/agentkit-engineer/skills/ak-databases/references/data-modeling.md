# Data modeling

Model:
- entity identity;
- ownership;
- required vs optional fields;
- uniqueness;
- lifecycle/deletion;
- consistency boundary;
- relationships;
- high-frequency access patterns.

For relational data, encode important invariants with constraints where practical.

For document data, avoid unbounded embedding and unclear duplication ownership.

Denormalization is a trade-off that requires a synchronization/consistency plan.
