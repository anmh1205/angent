---
name: ak-payment-integration
description: Integrate SePay/VietQR, Polar, Stripe or another selected payment provider using explicit business/provider state machines, idempotency, authenticated webhooks, reconciliation and lifecycle verification.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Payment Integration — Portable Fallback

Use for checkout, bank/QR payments, subscriptions, webhooks, refunds and multi-provider order/payment state.

## Load progressively

- `references/provider-routing.md` — provider roles and freshness boundary.
- `references/payment-state.md` — internal/provider state model.
- `references/webhooks-reconciliation.md` — asynchronous events and ambiguity.
- `references/subscriptions-refunds.md` — recurring billing, refunds and cancellation.

## Core model

The application, payment provider and fulfillment/entitlement system can have different state machines.

Client redirect/UI success is not authoritative payment confirmation.

Persist stable provider identifiers and the internal transition evidence needed to reconcile ambiguity.

## Provider selection

Do not select a provider from a generic popularity ranking.

Use current business requirements such as:
- market/currency/payment rail;
- checkout versus bank/QR transfer;
- subscription/usage/Merchant-of-Record needs;
- marketplace/connect requirements;
- settlement/accounting/tax responsibilities;
- current provider availability/pricing/legal/platform constraints.

The pinned package includes SePay, Polar and Stripe knowledge. Exact APIs, auth methods, limits, products, pricing and SDK calls are volatile: consult the current provider documentation before implementation.

## Workflow

1. Resolve provider, environment/account, API/SDK version and allowed external effects.
2. Define internal order/payment/subscription/refund states and invariants.
3. Define amount/currency units explicitly; never infer major/minor-unit semantics.
4. Create internal order/intent state before handing control to an external checkout when reconciliation depends on it.
5. Use provider-supported idempotency/deduplication identifiers where applicable.
6. Keep privileged credentials/API calls server-side.
7. Verify webhook authenticity using the provider's current mechanism.
8. Make event processing idempotent and tolerant of duplicates/delay/out-of-order delivery.
9. Acknowledge webhooks only after the local durability boundary required by the business invariant.
10. Reconcile ambiguous request/response, webhook or redirect outcomes against provider state using stable identifiers.
11. Test failure, duplicate, timeout, delayed-event, cancellation/refund and subscription transitions relevant to the product.
12. Verify accounting/fulfillment/entitlement invariants, not merely provider API success.

## Multi-provider orders

Keep one internal business model with explicit provider-specific metadata rather than leaking provider status strings throughout the application.

For cross-currency reporting, preserve:
- original amount/currency;
- conversion rate/source/time used for reporting;
- rounding/unit convention;
- whether the normalized value is accounting truth or analytics approximation.

Do not hard-code a fallback FX rate for financial settlement correctness.

## Effects and safety

Sandbox/test mode is preferred for development.

Creating live checkout sessions, subscriptions, refunds, provider webhooks/configuration, bank/VA resources, or real charges are external effects requiring current environment/account/authority.

Never store raw card credentials unless the architecture, provider contract and compliance boundary explicitly require it.

## Completion

A successful provider call, HTTP redirect, webhook receipt or local status flag is not enough by itself.

Completion evidence is the requested business state, reconciled against the provider and internal ledger at the required boundary.
