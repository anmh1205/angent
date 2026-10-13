# Auth, validation and errors

Authentication answers identity.

Authorization answers whether that identity can perform this action on this resource.

Validate untrusted input at the boundary.

Use errors that preserve useful machine semantics without exposing sensitive internals.

Avoid returning generic 500 for known client/domain errors, and avoid leaking stack traces/secrets in production responses.
