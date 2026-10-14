---
name: ak-page-builder
description: Build, extend, or operate a project-specific reusable page composition system using the project's existing stack, components, storage, preview, and publication boundaries.
metadata: {port: angent-fallback, mode: adapted}
---

# Page Builder — Portable Fallback

Read `references/page-builder-contract.md` for composition, persistence, publication and verification boundaries.
Use when the project needs a reusable page composition system, not for a one-off page edit.

## Modes

- **setup** — discover the existing stack/components/storage and create the builder contract/integration;
- **update** — extend the builder with bounded new block/editor/runtime behavior;
- **operate** — use the existing project-specific builder/operator surface to create or update draft content.

Mode names describe workflow intent; they do not create publication authority.

## Setup

1. Inspect the canonical project and reuse its component/design/data conventions.
2. Define a typed block/page contract: identity, props/content schema, allowed nesting, responsive behavior, validation, serialization, migration/version boundary.
3. Separate editor state, persisted draft state, preview state, and published state.
4. Integrate the smallest editor/composer surface needed.
5. Reuse existing components rather than creating parallel UI libraries.
6. Define preview and publication boundaries explicitly.
7. Expose agent/operator interfaces only for actions that can be verified safely.
8. Produce project documentation and, when useful, a project-specific operator Skill through `ak-skill-creator`.

## Update

Inspect the existing builder contract first. Extend it without invalidating stored pages or silently changing publication semantics.

Add migrations/compatibility handling when schema changes require them.

## Operate

Use the project's own operator contract. Work in draft/preview unless the user explicitly authorized publication.

## Verification

Verify at least one representative real block/page across:
- serialization/round-trip;
- responsive and touch editing where applicable;
- preview fidelity;
- validation/error behavior;
- draft versus publication boundary;
- requested agent/operator interface.

Do not report the builder complete from scaffold or editor rendering alone.
