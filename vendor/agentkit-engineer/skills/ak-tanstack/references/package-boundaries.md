# TanStack package boundaries

## Router / Start

Own routing, loaders/server functions and route error boundaries.

## Query

Own server-state caching, query keys, invalidation/refetch and mutation lifecycle.

## Form

Own field/form state and typed validation/submission.

## AI

Own streaming/chat/tool transport behavior.

Keep concerns separated: Query is not local UI state management, and Router loading is not automatically a replacement for all server-state caching.
