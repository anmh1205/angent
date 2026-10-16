# Correctness gates for diagrams and visual artifacts

**Provenance:** Adapted from MIT Dev BA Kit / rules/diagram-principles.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. There is no universal ANGENT diagram validator for every language.

## Four independent levels of correctness

1. **Source fidelity:** every actor, rule, state, table and protocol label comes from accepted source evidence or is identified as a proposal.
2. **Model semantics:** validate identity, ownership, directed edges, branch guards, reachability, cardinality, state rules or time-ordered messages as appropriate to the diagram type.
3. **Format/render:** actual D2 CLI, BPMN XML/XSD, Mermaid renderer, local PlantUML or connected Figma tool must succeed before claiming a rendered/editable artifact.
4. **Visual and operational quality:** open the image/canvas, inspect clipped labels and edges, contrast, readable text and relationship direction; read back editable node structure where a Figma operation was requested.

A format parser cannot establish level 1 or 2. A successful SVG export alone cannot establish Figma editability. Never call an image a genuine device/cloud diagram if its nodes came from a hypothetical example.

## What the portable kit actually runs

- build_d2.py: validated activity/swimlanes, ERD SQL tables and bounded logical architecture; optional D2 CLI renders SVG.
- build_bpmn.py: one acyclic non-executable process with exclusive gateways and lanes; optional independent OMG XSD integration verifies supported XML.
- build_wireframe.py: static or mock-interactive HTML screens, not a generic UML renderer.
- to_reqwise_payload.py: checks candidate models for six Reqwise OSS types but performs **zero live Figma writes**.

Mermaid and PlantUML content may be produced as source, but no universal renderer is bundled. If not actually rendered, report source and limitations instead of an imagined screenshot.

## Domain checks

Activity: single trigger, guarded alternatives, responsible actors and valid terminal paths. ERD: concrete entity IDs/keys, foreign endpoints, optionality and business cardinality. Sequence: lifeline identity, message order and failure/timeout behavior. State: stable entity and events, forbidden transitions and conflicting guards. BPMN: supported event/gateway semantics and real XML validity.

## Security and reproducibility

Prefer offline rendering for confidential business rules, customer identities and schemas. Do not silently call public rendering websites or download remote icons. Preserve source model revision and renderer version; for supported examples run integration checks, then compare images with the actual source.

A failed prerequisite is an explicit blocker for that output mode, not permission to substitute an unrelated diagram while calling it equivalent.
