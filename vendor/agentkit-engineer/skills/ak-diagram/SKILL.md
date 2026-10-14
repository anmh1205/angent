---
name: ak-diagram
description: Compile or render inspectable system diagrams from typed structure, Mermaid, editorial data, or prepared HTML using deterministic local/harness capabilities when available.
metadata: {port: angent-fallback, mode: adapted}
---

# Diagram — Portable Fallback

Read `references/diagram-contract.md` for artifact, capability and verification boundaries.
Use for architecture, workflow, sequence, dataflow, lifecycle, or editorial diagrams whose relationships need to be inspected rather than merely described.

Prefer `ak-mermaidjs-v11` when reviewable Mermaid source is the actual deliverable, `ak-excalidraw` for editable canvas work, and `ak-graphify` for large-graph exploration.

## Input tiers

Choose the strongest representation the active harness can preserve:

1. typed structured data / JSON IR for explicit nodes, edges, states, and semantic roles;
2. Mermaid source for reviewable graph/sequence/state syntax;
3. structured editorial template data;
4. prepared HTML when the user already owns the visual implementation.

Do not invent a compiler/runtime that is unavailable.

## Workflow

1. Identify the relation the diagram must make inspectable.
2. Validate input identities, edge semantics, labels, and intended output.
3. Discover actual local/harness render capability before choosing SVG/HTML/PNG/video.
4. Keep geometry/rendering deterministic where the active toolchain permits it.
5. Generate the requested artifact without CDN/network dependencies unless explicitly allowed.
6. Inspect the visible result for clipped labels, ambiguous edges, broken assets, unreadable density, and incorrect relation encoding.
7. Record actual output paths and important renderer/tool-version boundaries when reproducibility matters.

## Static versus motion

Treat HTML, PNG/SVG extraction, and video capture as different artifacts with different verification requirements.

Do not claim standalone SVG fidelity merely because an SVG can be extracted from a rendered page; page CSS/fonts/assets may remain part of the visual contract.

Dependency installation, browser launch, file overwrite, network access, and video tooling are effects that require the normal project/authority boundary.

A complete result names what was actually rendered and what could not be verified.
