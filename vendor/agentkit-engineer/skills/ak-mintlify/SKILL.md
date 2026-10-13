---
name: ak-mintlify
description: Build and maintain Mintlify documentation sites using the project's installed/current Mintlify schema, MDX components, navigation and API docs configuration.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Mintlify — Portable Fallback

Use only for projects using Mintlify.

## Workflow

1. Inspect current docs config and installed/current Mintlify docs.
2. Preserve existing navigation/branding unless redesign is requested.
3. Author MDX with supported components.
4. Integrate OpenAPI/AsyncAPI from canonical specs where used.
5. Maintain redirects/links.
6. Validate local build/preview.
7. Verify deployment output when publishing is authorized.

Avoid copying configuration from another Mintlify version without checking the current schema.
