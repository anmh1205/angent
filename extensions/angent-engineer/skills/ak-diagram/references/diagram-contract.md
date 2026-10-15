# Diagram artifact contract

A diagram succeeds when it makes a specified relation inspectable and the requested artifact can be verified.

## Preserve

- node/entity identity;
- direction or sequence where meaningful;
- grouping/ownership boundaries;
- state transitions or causal/dependency edges;
- labels needed to interpret the relation;
- source-to-render consistency.

## Capability boundary

The fallback does not assume AgentKit's bundled compiler/assets exist.

Check the active harness for the needed route:
- Mermaid renderer;
- HTML/SVG authoring;
- browser rendering;
- screenshot/image inspection;
- video capture;
- local dependency execution.

If a requested format depends on unavailable machinery, preserve the source representation and say exactly which rendered form is unverified rather than fabricating parity.

## Verification

When possible:
1. validate source syntax/schema;
2. render the actual artifact;
3. inspect visible output;
4. verify interactive/search/trace behavior when that behavior is part of the request.

A valid source file alone does not prove render fidelity.
