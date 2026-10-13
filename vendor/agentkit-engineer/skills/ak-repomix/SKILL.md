---
name: ak-repomix
description: Produce compact AI-oriented repository snapshots using Repomix when installed, with deliberate include/exclude boundaries and secret awareness.
metadata: {port: angent-fallback, mode: degraded}
---

# Repomix — Portable Fallback

If Repomix is installed/usable, use it for deliberate repository packaging.

Choose:
- output format;
- include paths;
- excludes for generated/vendor/binary/secret data;
- whether comments/line numbers/security checks are needed.

Do not pack an entire large repository by default.

If Repomix is unavailable, degrade to targeted repository reading/search or generate a small explicit snapshot from needed files.

Never include secret files merely to maximize context.
