# TanStack package boundaries

## Router / Start

Own route definitions, params/search state, loaders/beforeLoad, navigation/pending/error boundaries and Start's server/build/runtime layer.

Distinguish server functions used by the application from public server routes/endpoints.

Preserve generated route-tree ownership.

## Form

Own typed field/form state, validation timing, async validation, submission and server validation.

The UI components remain application-owned/headless.

## AI

Own the installed TanStack AI streaming/chat/tool/output contract.

Provider credentials remain server-side unless a documented BYOK/client mode is explicitly selected.

## Not owned by this packaged Skill

TanStack Query, Table, Virtual and other TanStack libraries are not silently pulled into this Skill merely because they share the TanStack brand.

When present in the project, follow their current documentation/project conventions or an appropriate separate capability.

## Version drift

The 2.19.0 package snapshot contains APIs/maturity labels that can age quickly.

Current installed package + official docs outrank memorized examples.
