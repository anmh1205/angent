---
name: ak-mobile-development
description: Build iOS/Android apps using the chosen native or cross-platform stack with explicit lifecycle, offline, permissions and store boundaries.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Mobile Development — Portable Fallback

Read `references/lifecycle-offline.md`.

## Workflow

1. Identify target platforms/framework versions.
2. Model app lifecycle/navigation.
3. Define permissions and sensitive-data storage.
4. Design network/cache/offline behavior.
5. Handle background/notification/deep-link flows when required.
6. Build adaptive accessible UI.
7. Test on relevant device/emulator classes.
8. Profile startup/render/network/battery when material.
9. Treat signing/store release as a separate authorized effect.

Do not hide platform-specific constraints behind a generic abstraction.
