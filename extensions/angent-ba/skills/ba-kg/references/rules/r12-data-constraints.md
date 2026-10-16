# R12: Entity, identifier and relationship invariants

## Operational contract

Ground each entity and identifier in the source dictionary/schema. Record data owner, key uniqueness, cardinality, nullability, lifecycle, retention, tenant boundary and delete semantics when material.

## Checks before accepting an artifact

Reconcile ERD edges with actual foreign keys if discussing deployed code. A SQL-table visual is conceptual unless it was derived from and checked against migrations or live schema metadata.

## Failure response

Check optional and one-to-one relationships explicitly: a nullable foreign key, unique constraint and many-to-many join model carry different business meaning.

## Grounded example

A 1:N from account to vehicle is not valid just because vehicles have owner_id; shared rental ownership or transfer history may require a temporal assignment table.

**Evidence boundary:** specialist advice does not establish completed provider writes or approve business requirements. The actual source and observed result remain decisive; ANGENT Root and Quality retain oversight.
