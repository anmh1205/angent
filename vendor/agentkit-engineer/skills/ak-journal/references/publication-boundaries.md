# Journal publishing boundary

Upstream stable 2.19.0 includes Zernio CLI scripts and optional media generation, config cascades, per-channel bodies, thread splitting, media upload, rate-limit handling and successful-post state. These runtime resources are **not bundled** in this portable fallback.

Before publication resolve the real provider, account/channel identity, user authorization, intended visibility, content/media constraints and credential access. Prepare per-channel copy, inspect a preview/dry-run if supported and verify current CLI/provider version. Never commit secrets or run an unpinned remote executable with publishing credentials.

Preserve success URLs and per-journal/per-channel operation identities. A timeout is ATTEMPTED_UNKNOWN; inspect provider history before retry. Do not double-post successful channels. A failed media channel must not silently drop essential content. Honor rate limits and report partial successes.

If a host lacks actual provider tooling, provide local journals and drafts only; report no external posting occurred.