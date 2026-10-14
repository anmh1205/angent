# Stitch capability and workflow decision

Native stable 2.19.0 Stitch differentiates `quota`, `generate`, `edit` and `export`; the original package includes SDK/MCP setup, quota, pipeline and design-to-code references.

**Provider gate:** inspect available authenticated Stitch SDK/MCP methods, target project identity, existing screen ID, current quota/pricing and operation permissions. An environment variable name is not proof a valid account is connected. Never expose `STITCH_API_KEY` or install unreviewed source scripts merely to query quota.

**Artifact gate:** generation returns a provider design/screen; exporting HTML/Tailwind/DESIGN.md creates distinct outputs. Validate responsive layout, tokens, missing interaction/error/empty states and asset rights before frontend implementation.

**Fallback:** host-native frontend-design or a vector/mockup tool can satisfy conceptual design but not native Stitch project, redesign, quota or export semantics. Report which of these capabilities were really executed.
