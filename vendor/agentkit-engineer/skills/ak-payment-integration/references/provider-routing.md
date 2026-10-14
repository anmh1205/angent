# Payment provider routing and freshness

The pinned 2.19.0 package includes guidance for SePay, Polar and Stripe.

Use it as workflow/domain context, not as a permanent copy of each provider's live API.

## SePay / VietQR

Typical fit:
- Vietnamese bank-transfer/VND flows;
- transaction/webhook-based payment confirmation;
- payment codes/virtual-account or VietQR-style order identification.

Current SePay documentation is authoritative for:
- webhook authentication options and acknowledgement contract;
- API limits/retry headers;
- current transaction/VA fields and endpoints.

Do not hard-code package-era timeout/rate-limit values into new integrations without checking current docs.

## Polar

Typical fit:
- SaaS/digital-product checkout and subscription lifecycle;
- Merchant-of-Record style responsibility when the current Polar product/account supports it;
- product/benefit/entitlement workflows.

Read current Polar docs for exact SDK APIs, product/price model, webhook events, tax/MoR behavior and subscription semantics before coding.

## Stripe

Typical fit:
- checkout/payment intents and broader payment infrastructure;
- Billing/subscription lifecycle;
- Connect/marketplace flows when required.

Read current Stripe docs for the exact integration path, API version, SDK, webhook signature flow, idempotency behavior and payment-method requirements.

## Provider-neutral invariant

Provider-specific transport/status does not own the application's business truth.

Map external events into explicit internal transitions and preserve identifiers for reconciliation.
