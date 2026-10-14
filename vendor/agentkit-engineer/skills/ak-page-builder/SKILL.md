---
name: ak-page-builder
description: Build, extend, or operate a project-specific reusable page-composition system using the project's existing stack, components, storage, preview, and publication boundaries.
metadata: {port: angent-fallback, mode: adapted}
---

# Page Builder — Portable Fallback

Use only when the project needs a reusable **page-building system**. A one-off page change belongs to the normal frontend workflow.

Read `references/page-builder-contract.md`.

## Modes

### `setup <project>`

1. inspect the current stack, routing, design system, content/storage model and existing blocks;
2. define page/block schemas and binding boundaries;
3. implement editor/composition behavior using project-native components;
4. keep draft, preview and publication states distinct;
5. create/update the project-specific operator Skill through `ak-skill-creator` when the builder is intended to be operated by an agent; keep it scoped to the project's real builder API/commands rather than generic page mutation;
6. expose any additional agent/operator interface only where the project actually needs it;
7. verify at least one representative real block/page across target viewports and state transitions, including the operator Skill when it is part of the contract.

### `update <request>`

Change the existing builder without redesigning its contract unnecessarily.

Preserve existing content compatibility and migration requirements.

### `operate <request>`

Use an existing verified builder/operator surface to create or modify page content.

Do not publish unless the request authorizes publication.

## Capability boundary

Use the project's own framework/storage/runtime.

If live browser, preview, CMS, database, or deployment capability is unavailable, implement only the parts that can be verified and report the remaining boundary.

A generated scaffold or operator Skill file is not proof that editing, preview, persistence, agent operation, or publication works.
