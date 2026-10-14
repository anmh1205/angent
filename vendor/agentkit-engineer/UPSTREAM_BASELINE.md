# AgentKit Engineer upstream baseline

## Canonical package baseline

ANGENT's portable fallback is currently audited against **AgentKit Engineer stable 2.19.0**.

Evidence observed on 2026-10-14:

- AgentKit CLI: `ak 2.19.0`, authenticated, stable channel.
- Signed `ak changelog --channel stable --target engineer --json` reports Engineer `2.19.0` as the latest stable release, published 2026-09-28.
- A fresh remote-registry portable export of Engineer stable resolves **102 Skills**.
- The same export preserves **16 Agent** definitions under `.agentkit/agents/` as sidecar reference content.
- Exact Skill-directory comparison against the ANGENT fallback is **102 ↔ 102**, with no upstream-only or fallback-only identities.

The earlier docs-derived expectation of 103 public Skills is therefore not used as package truth.

## Documentation versus package inventory

The stable “choose an Engineer Skill” documentation is a routing/usage guide and explicitly should not be treated as the packaged-identity inventory.

Documentation may describe replacement routes or newer capability concepts before/without changing the currently published package directory set. ANGENT therefore uses:

1. signed release/catalog metadata for current release identity;
2. a freshly resolved stable package artifact for packaged Skill/Agent inventory;
3. stable documentation for public workflow meaning, migration guidance and capability context.

A docs/package discrepancy is preserved as a discrepancy rather than “fixed” by guessing.

## Portable-export boundary

AgentKit's portable export explicitly describes itself as best-effort/non-production.

It treats `skills/` and exported `AGENTS.md` as first-class portable content, while Agent/hook/command material under `.agentkit/` is preserved-only/inert reference content.

ANGENT uses that export as **audit evidence and source material**, not as a verified runtime adapter and not as permission to commit a raw upstream mirror.

## Parity objective

Portable parity is evaluated by:

- primary workflow outcome;
- materially distinct modes/options;
- critical decision, safety and validation gates;
- reusable domain/support knowledge needed for the workflow to work;
- assumptions and runtime-specific dependencies;
- an explicit portable replacement for runtime-specific mechanics;
- real limitations when equivalent behavior is impossible.

Identity presence, text similarity, source-file count and directory count are evidence for audit triage. None is a parity verdict by itself.

## Current evidence of semantic drift

At the start of the 2.19.0 semantic refresh:

- upstream portable Skill support files: approximately **1428**;
- ANGENT fallback Skill support files: approximately **236**;
- identical relative support paths: **112**;
- upstream SKILL.md lines: approximately **20,150**;
- fallback SKILL.md lines: approximately **3,632**;
- upstream direct support references: approximately **545**;
- fallback direct support references: approximately **136**.

The fallback is intentionally independently adapted and may legitimately be much smaller. The disparity is nevertheless large enough that the old blanket “102/102 implemented” claim cannot serve as semantic acceptance evidence.

## Update rule

When the signed stable package changes, pin the new release evidence first, then re-run identity and semantic review. Do not migrate identities from documentation alone and do not carry old parity verdicts across an upstream release without checking their validity boundary.
