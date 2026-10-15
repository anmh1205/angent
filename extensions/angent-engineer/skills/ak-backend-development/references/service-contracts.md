# Backend service contracts

For an API/event define:
- input schema;
- authentication requirement;
- authorization scope;
- idempotency;
- state read/write ownership;
- output schema;
- error model;
- version/compatibility expectation.

Keep transport DTOs separate from persistence/domain objects when that separation protects the contract.

For async events, define delivery/ordering/duplicate semantics.
