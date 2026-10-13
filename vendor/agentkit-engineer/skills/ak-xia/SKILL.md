---
name: ak-xia
description: Study a feature in another repository, compare it with the current project, and port the behavior idiomatically into the local stack without blindly copying implementation.
metadata: {port: angent-fallback, mode: adapted}
---

# XIA — Portable Feature Porting

Use when the user wants “the feature from repo X” or asks to compare/adapt another implementation.

Read `references/feature-porting.md`.

## Workflow

1. Define the behavior/outcome to port.
2. Inspect the source implementation and its dependencies.
3. Inspect the destination architecture and AGENTS.md.
4. Separate essential semantics from source-specific framework/runtime choices.
5. Design the destination-native equivalent.
6. Implement the smallest coherent slice.
7. Test behavior against the source/reference expectation where possible.
8. Document intentional differences.

Do not copy code merely because it is convenient; respect license/provenance and destination conventions.
