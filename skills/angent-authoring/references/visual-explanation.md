# Visual explanation — choose and verify a representation

A visual is part of the explanation, not a decoration or a quota. First identify the exact relation or observation the reader must understand. Select the representation that makes that relation directly inspectable. A figure with true facts can still mislead when its arrows, scale, groupings or timing imply the wrong relationship.

## Match the representation to the question

- **Flowchart**: causal/control branches, decisions and stages. Label whether arrows mean control, data, dependency or material transformation; do not silently mix them.
- **Sequence diagram**: messages and ordered interactions between named participants. Distinguish calls, returns, asynchronous messages and the initiator of each event.
- **State diagram**: legal states, transition conditions and outcomes. State ownership and guards when they affect correctness; do not confuse state with a process step.
- **Entity-relationship / class / block diagram**: structural entities and typed relationships. Use only when those relationships are the subject, not to display a glossary.
- **Timeline / Gantt / git graph**: events, schedule dependencies or branching history; date and dependency facts must be supported.
- **XY chart / Sankey / quadrant**: numeric series, proportional flow or explicit two-axis classification. Values, units, dimensions, baselines and aggregation must be evidenced; use a plotting library if Mermaid cannot faithfully express them.
- **Mindmap / journey**: meaningful hierarchy or an experience path. Do not replace actual causal explanation with a tree of labels.
- **Venn / Ishikawa**: membership overlap or a causal-factor hypothesis map where the destination supports the relevant Mermaid version; newer or beta syntax is optional, never a deployment assumption.
- **Real photo, screenshot, pinout, schematic, timing capture**: physical identity, exact interface, pixel-level UI state, electrical wiring or observed signals. These are evidence; abstract Mermaid cannot replace them.
- **Annotated image, SVG illustration, quantitative plot, worked trace, comparison matrix**: use these when spatial labeling, geometry, quantities or exact intermediate values are the essential information and Mermaid is a worse fit.

Use prose for a relation that fits naturally in two sentences. Mixed representations are often strongest: the diagram exposes arrangement or sequence, while text explains what the reader should infer; code or a trace establishes one exact boundary.

## Mermaid production discipline

1. Define the question and the semantics of each node, arrow, label, lane, guard and direction before drawing.
2. Choose the simplest diagram type that preserves those semantics. In particular, a process flow is not a message trace, and a dependency arrow is not a data-flow arrow.
3. Use concise stable identifiers, readable labels and only the necessary participants or branches. Break large diagrams at a real conceptual boundary; never use an unreadably compressed wall of nodes.
4. Verify syntax against the target renderer and version, not a web example from a newer Mermaid release. Avoid experimental types where the destination cannot render them; do not silently fall back to raw fenced code.
5. Render and inspect the actual figure when tools permit. Check arrow endpoints, ordering, labels, conditional paths, clipping, contrast and mobile legibility. A parsable source file does not prove successful rendering.
6. Explain the decisive relationship in nearby prose. A caption identifies the figure and its scope; it does not substitute for interpreting it.

Examples (each arrow or transition has one interpretable meaning):

    flowchart LR
      U[User-space process] -->|system call| K[Kernel entry]
      K -->|driver request| D[Device driver]

    sequenceDiagram
      participant A as Application
      participant K as Kernel
      A->>K: read(fd, buf, n)
      K-->>A: count or error

    stateDiagram-v2
      [*] --> Idle
      Idle --> Active: start accepted
      Active --> Idle: stop completed

These examples demonstrate different jobs, not interchangeable diagram templates. Verify actual syscall paths, messages, state labels and event order against the task's platform and version before reusing any example.

Mermaid references:
- https://mermaid.ai/open-source/intro/
- https://mermaid.ai/open-source/syntax/flowchart.html
- https://mermaid.ai/open-source/syntax/sequenceDiagram.html
- https://mermaid.ai/blog/posts/mermaid-v11-13-0-two-new-diagram-types-and-our-most-polished-release-yet

## Figure acceptance

For every consequential figure, check:
- factual source and relevant version/device/model;
- whether every relation/axis/scale/transition is justified;
- whether the desired insight is visible without guessing hidden conventions;
- renderer/platform compatibility, rendered legibility and destination fidelity;
- source attribution and reuse permission when imagery comes from elsewhere.

A missing or unsuitable image is a research gap, not permission to invent evidence. A strong diagram is also unnecessary when it conveys no additional information beyond the prose.
