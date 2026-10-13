# Webhooks and reconciliation

## Webhook

- verify signature/authenticity;
- parse versioned schema;
- deduplicate by event/provider identity;
- make processing idempotent;
- handle out-of-order delivery;
- return provider-required acknowledgement only after the required local durability boundary.

## Reconciliation

When request/response is lost or payment state is unclear:
- query provider by stable identifier;
- compare provider state with local order;
- repair only after evidence;
- record the reconciliation action.

Timeout is not proof a charge failed.
