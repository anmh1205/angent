# Mobile platform selection and volatile-fact boundary

## Framework choice

Compare only criteria that matter to the product:

- existing code and team expertise;
- platform-specific API depth;
- shared-code requirement;
- UI/animation/graphics needs;
- package/plugin/native-module maturity;
- tooling/build/release constraints;
- long-term support and upgrade surface.

Do not use repository star counts, broad survey percentages or unsourced performance ratios as decisive evidence.

## Current-source boundary

React Native, Flutter, Swift/SwiftUI and Android/Compose change rapidly.

For version-specific architecture, lifecycle, build tooling, background execution, permissions or release requirements, read the current official documentation for the installed/target version.

## Native behavior

Cross-platform frameworks do not erase:
- iOS/Android permission models;
- background execution restrictions;
- safe-area/system UI behavior;
- secure storage;
- notification/deep-link configuration;
- signing/store release.

When a feature depends on those platform contracts, test the actual platform path.

## Verification

Use simulator/emulator for fast coverage, but use representative real-device evidence when the claim concerns performance, sensors, background behavior, notifications, memory pressure, battery, camera/Bluetooth/location or store release.
