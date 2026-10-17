# Shopify platform surfaces

## App / Admin integration

Use current Shopify APIs appropriate to where code runs.

Use GraphQL Admin for new store-administration work; [Shopify API guidance](https://shopify.dev/docs/apps/build/apis) identifies REST Admin as legacy.

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

Inspect current permissions before theme writes. For example, [themeFilesUpsert](https://shopify.dev/docs/api/admin-graphql/latest/mutations/themeFilesUpsert) documents the scopes and eligibility required by that operation; do not generalize one operation's access to every theme effect.

## Webhooks

Use events/webhooks instead of polling when the platform supports the required event.

Subscriptions have configuration and API-version boundaries described by [Shopify Webhooks](https://shopify.dev/docs/api/webhooks/latest). [Verify deliveries](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries) explains authentication and duplicate handling; keep processing idempotent.
