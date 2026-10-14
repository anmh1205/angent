---
name: ak-mintlify
description: Author or maintain a Mintlify docs site with version-verified docs.json, MDX, navigation, API references, AI assets and local validation/deployment checks.
license: MIT
metadata: {port: angent-fallback, mode: degraded}
---

# Mintlify — Portable Fallback

Use **only** for an existing/desired Mintlify documentation site. Stable Engineer 2.19.0 includes six substantial platform-specific reference guides (docs.json, MDX components, navigation, API components, deployment/CI and AI integrations). This portable text retains their decision/workflow contracts but **does not bundle** those six full manuals or an installed Mintlify CLI. Consult the actual installed CLI and current official documentation for exact version-specific fields/commands.

## Discovery and content plan

1. Inspect actual project config: Mintlify `docs.json` or a legacy `mint.json`, package/CLI version, repo docs root, navigation, theme, branding, deployment host, redirects and versioning.
2. Preserve existing navigation, branding, domains and authored MDX by default. Model readers, canonical section ownership, API/code contracts and language/version variants before adding pages.
3. Validate `docs.json` against **the installed release**, including theme, colors, navigation groups/tabs, product/version/locale scopes and supported integration settings. Legacy migration is a separate authorized change, not a formatting tweak.
4. Author MDX with appropriate page frontmatter and **supported** Mintlify/React components. Ensure code tabs, callouts, steps, interactive content, accessibility and mobile/print behavior serve the actual topic rather than increasing visual density.
5. For API references, link or generate from canonical OpenAPI/AsyncAPI schemas where supported, preserving specification version, auth, errors and examples. Do not manually duplicate source-of-truth API endpoints in prose.
6. For AI-facing assets such as `llms.txt`, `skill.md` and MCP surfaces, only expose approved documentation; verify actual feature support and public/private data boundaries.
7. Review path/redirect changes, navigation reachability and CI/deployment effects before editing. Use exact native validation tools if installed: stable examples include `mint validate`, `mint broken-links`, `mint a11y`, `mint openapi-check` and `mint dev`; current CLI help owns actual command availability.
8. Read back changed files and run applicable build/preview/validation. Deployment or updating docs hosting requires user authority; report checks not run instead of certifying the site from valid MDX source alone.

## Reference and scope boundary

The pinned skill covered theme families, MDX API/interactive components, product/version/i18n navigation, deployment targets, SEO/redirects, AI assets and analytics. External behavior can change; never paste a remembered configuration without current release verification. Where the native CLI or reference manuals are inaccessible, mark missing validation/details as degraded.

Return affected paths, source-of-truth decisions, validation and preview results, version assumptions and publishing state. Do not claim `mint dev` or a deployment was executed unless observed.
