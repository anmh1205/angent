# Changelog

## 1.0.0 — Unreleased candidate

The candidate is under active core hardening and is not release-ready.

### Core hardening

- Added explicit constraint evolution so newer corrections do not silently erase still-active requirements.
- Added active-obligation preservation in Context.
- Added baseline-preserving repair semantics, protected properties, dependency invalidation and oscillation escalation in Reasoning.
- Added semantic artifact state for long-form and iterative Authoring.
- Reworked Quality around solution, comparative-candidate and endpoint concerns, including overcorrection/regression detection.
- Added trust boundaries between retrieved external content and task authority.
- Strengthened broad-audit coverage semantics for pagination, truncation and stale/recheck units.
- Added Continuity lifecycle, accepted-baseline pointers and recovery/discovery coherence.
- Added Learning activation and recurrence semantics.
- Clarified that Format defines destination representation while Execution owns external writes.
- Removed the root `tests/` suite that mainly asserted static structure, keywords and counts.
- Reduced the GitHub workflow to diff hygiene only; it is not behavioral acceptance evidence.

### Engineer

Engineer integration remains native-first / fallback-second.

Fallback inventory/parity is intentionally deferred until after the core-hardening phase. Historical completeness counts are not considered current upstream-parity evidence.

### Release boundary

Previous statements that implementation/acceptance were complete are superseded by this hardening work.

Do not publish, tag or describe 1.0.0 as released or implementation-complete until:

1. the core-hardening branch is reconciled into the intended canonical source;
2. the core architecture is read back for internal consistency;
3. the deferred Engineer inventory/parity phase is resolved;
4. the intended release surface/version strategy is explicitly approved.
