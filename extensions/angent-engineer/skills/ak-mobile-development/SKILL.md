---
name: ak-mobile-development
description: Design, implement and verify iOS/Android apps in React Native, Flutter, Swift/SwiftUI or Kotlin/Compose with explicit platform selection, lifecycle, offline sync, permissions, performance and store-release boundaries.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Mobile Development — Portable Fallback

Use when the target is an iOS/Android application.

Read `references/lifecycle-offline.md` and `references/platform-selection.md`.

## Select the stack from constraints

Supported workflow families:
- React Native;
- Flutter;
- native iOS with Swift/SwiftUI/UIKit as required;
- native Android with Kotlin/Compose/Views as required.

Choose from:
- existing code/team skill;
- native API/device integration depth;
- platform fidelity;
- shared-code requirements;
- startup/render/graphics constraints;
- package/plugin maturity;
- release/support requirements.

Do not use package-era GitHub stars/adoption percentages or universal “X% native performance” claims as architecture evidence.

## Contract

Resolve:
- target OS/device classes and minimum supported versions;
- framework/toolchain versions;
- navigation/state/data architecture already used;
- permissions and sensitive-data storage;
- network/cache/offline ownership;
- background/notification/deep-link requirements;
- accessibility/localization/adaptive layout;
- performance symptom/budget when material;
- emulator/simulator versus real-device verification;
- signing/store/release authority.

## Workflow

1. Inspect current project/toolchain and platform constraints.
2. Preserve platform lifecycle: cold/warm start, foreground/background, process termination and state restoration where relevant.
3. Model permissions as states including denial, limited access and later settings changes.
4. Keep secrets/tokens in platform-appropriate secure storage and privileged server operations off the client.
5. Design network/cache/offline behavior with explicit source-of-truth, freshness, conflict and retry semantics.
6. Handle background work, push notifications and deep links according to current OS/platform restrictions.
7. Build adaptive accessible UI that respects platform interaction conventions without forcing every app into a stock visual style.
8. Measure startup/render/network/memory/battery issues before optimizing.
9. Test logic/integration plus representative emulator/simulator and real-device behavior proportional to the claim.
10. Treat signing, certificates/profiles/keystores, store metadata, upload, staged rollout and production release as separate effects.

## Offline

Offline-first is a product/data-consistency choice, not simply “cache everything”.

Define:
- local/remote ownership;
- stale data behavior;
- queued writes;
- retry/backoff;
- conflict resolution;
- deletion/tombstone semantics;
- background/foreground sync triggers;
- user-visible sync/error state.

Flutter's current architecture guidance likewise treats offline behavior as a design choice with multiple sync strategies rather than one mandatory pattern. citeturn852002search10

## Performance and platform facts

Do not retain package-era universal targets for launch time, memory, battery, FPS or framework superiority as current truth.

Use project/product budgets and measure on representative devices. Consult current React Native, Flutter, Apple and Android guidance for version-specific behavior.

## Completion

A simulator build is not proof of production device behavior.

State exactly which platform/device class, lifecycle/offline path and release boundary were verified.
