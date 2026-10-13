---
name: ak-payment-integration
description: Integrate payment providers with explicit order state, idempotency, webhook verification, reconciliation, subscriptions and refund lifecycle semantics.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Payment Integration — Portable Fallback

Use for Stripe, SePay/VietQR, Polar or another selected provider.

## Load progressively

- `references/payment-state.md` — internal/provider state model.
- `references/webhooks-reconciliation.md` — asynchronous events and ambiguity.
- `references/subscriptions-refunds.md` — recurring billing, refunds and cancellation.

## Core rule

The provider and the application have distinct state machines.

Client redirect/UI success is not authoritative payment confirmation.

## Workflow

1. Read current provider API/docs/version.
2. Define internal order/payment/subscription states.
3. Define idempotent creation keys and provider identifiers.
4. Keep secrets and privileged API calls server-side.
5. Verify webhook authenticity.
6. Make event processing idempotent.
7. Reconcile provider state after ambiguous outcomes.
8. Test duplicate, delayed, out-of-order and failed flows.
9. Verify accounting/business invariants.

Do not store raw card credentials unless the architecture is explicitly PCI-compliant and requires it.
