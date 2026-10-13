---
name: angent-format
description: Render established ANGENT content faithfully for the destination, preserving semantic relationships and verifying the final visible result.
---

# ANGENT Format — Destination Fidelity

Format owns destination mechanics, not solution logic or prose authorship.

## Load reference

- references/render-fidelity.md — preserve semantic structure through destination constraints and verify actual render.

## Inputs

Receive:
- canonical content from Authoring;
- representation intent;
- citation/link requirements;
- destination constraints.

If a destination limitation requires changing meaning, return the problem to Authoring rather than silently rewriting.

## Preserve semantics

Do not:
- flatten causal/dependency structure into bullets merely for scanability;
- turn a true comparison table into prose for stylistic uniformity;
- replace required physical/UI evidence with a generic diagram;
- change code/equation semantics to fit formatting.

## Destination mechanics

Handle hierarchy, blocks, code/equations, citations, links, figures, tables, page breaks and destination-specific spacing/layout.

Strip transport-only metadata and raw internal citation tokens.

## Verify visible output

API success is not render success.

When possible inspect/read back the actual destination:
- rendered Mermaid rather than source presence;
- table/page hierarchy;
- code/equation fidelity;
- links/citations;
- missing/duplicated blocks;
- layout artifacts.

Return render failures to Format; return meaning/content failures to Authoring.
