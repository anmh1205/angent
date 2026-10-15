# MCP contract design

For each tool specify:
- purpose;
- inputs and validation;
- effect class/idempotency;
- authorization expectation;
- output structure;
- error structure;
- timeout/retry semantics.

Resources are good for retrievable state/document views.

Tools are good for bounded operations.

Keep server business logic thin when an existing service/library already owns the capability.
