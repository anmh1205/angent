---
name: ak-chrome-profile
description: Use an authorized real Chrome profile when the active browser runtime supports it; otherwise fall back to an isolated session without extracting credentials.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Chrome Profile — Portable Fallback

Read `references/profile-safety.md`.

## Preferred behavior

If the harness can attach to an authorized real Chrome profile:
1. enumerate/select by observable profile/tab identity;
2. attach through supported browser/DevTools integration;
3. reuse existing authenticated state only for the authorized task;
4. verify the target page/account before consequential action.

## Fallback

When profile attachment is unavailable:
- use isolated browser;
- ask the user to authenticate normally when appropriate;
- or mark authenticated-profile capability unavailable.

Do not copy browser profile files or export cookies/tokens as a workaround.
