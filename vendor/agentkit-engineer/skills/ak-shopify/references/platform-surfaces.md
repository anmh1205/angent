# Shopify platform surfaces

## App / Admin integration

Use current Shopify APIs appropriate to where code runs.

New app development should use current GraphQL Admin APIs for store administration; REST Admin is legacy. citeturn108303search9turn108303search11

Preserve:
- exact API version;
- access scopes;
- pagination/query cost;
- app/session authentication;
- webhook/event integration;
- billing when part of the app.

## Extensions

Shopify renders extension code inside specific product/admin/checkout/customer/POS surfaces.

Use only APIs/components allowed by the selected extension target.

Do not assume an Admin extension and Checkout extension share the same authentication/data-fetching contract.

## Themes

Theme source and publication state are separate concerns.

Prefer development/unpublished theme targets for iteration.

Inspect current Shopify permissions and API/CLI restrictions before creating, modifying or publishing themes; current platform permissions can constrain write operations. citeturn108303search8

## Webhooks

Use events/webhooks instead of polling when the platform supports the required event.

Webhook subscriptions are app-scoped and versioned; validate authenticity and process deliveries idempotently. citeturn108303search7turn108303search12
