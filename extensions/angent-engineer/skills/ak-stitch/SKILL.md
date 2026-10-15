---
name: ak-stitch
description: Use real Google Stitch project/quota and design export workflows where authorized, or clearly degrade to a source-grounded frontend-design replacement.
license: MIT
metadata: {port: angent-fallback, mode: degraded}
---

# Google Stitch — Portable Fallback

Stable Engineer 2.19.0 Stitch uses **Google Stitch SDK/API and optional MCP** for AI-generated UI, project selection, redesign, quota checks and export to HTML/Tailwind and `DESIGN.md`. The native API client, account/quota and export scripts are not implicit in this fallback. The pinned source's credit numbers and provider CLI syntax are time-sensitive; inspect current service/account rather than promising historical free-tier limits.

Read `references/import-normalization.md` and `references/stitch-runtime.md`.

## Native actions and project identity

- **quota:** confirm authenticated provider and live account quota/credits before cost-incurring work.
- **generate:** derive the prompt from real audience, required components, design system and screen states; select an explicit Stitch project and avoid mixing assets from unrelated tasks.
- **edit:** redesign an existing selected screen/variant using actual project/screen identifiers rather than creating unrelated new work.
- **export:** retrieve existing provider output and inspect **actual** HTML/Tailwind/components and `DESIGN.md` tokens, assets and responsiveness.

The pinned source resolves project identity by explicit `--project`, named project, environment default, repository context and fallback. Always favor a user-selected or accepted project; **never assume the default project is safe** for private or concurrent work. Auth from `STITCH_API_KEY` or an authenticated connector must remain secret. Installing the SDK, generating provider assets and requesting public links require authorization.

## Design-to-code integration

1. Preflight provider/model and quota; scope prompt and screens.
2. Generate **only when the backend is really connected**; inspect image/screen output, constraints, missing states and text/brand fidelity.
3. Request meaningful variants only if the user is exploring approaches.
4. Export as actual source/design contract, with real file paths and asset provenance.
5. Normalize imported tokens/components, error/loading/empty states, keyboard and screen-reader behavior into the project's approved design system. An exported HTML file is a prototype, not production-quality authorization/data architecture.
6. Implement through the real frontend design/development owner and test responsive/UI behavior. Do not claim production implementation from Stitch generation alone.

When native Stitch isn't callable, use a host-supported mockup/design workflow **and label it as a substitute**; no fictitious quota, provider project, export or API action.

**Capability:** VERIFIED_DEGRADED without the native Stitch SDK/credential/provider and actual export artifacts.
