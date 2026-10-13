# Technical diagram language

Choose the diagram type from the question:

- architecture — components, trust/deployment boundaries and dependencies;
- data flow — sources, transformations, stores and sinks;
- flowchart — control/process choices;
- sequence — time-ordered interaction between actors;
- state machine — states and valid transitions;
- ER — entities, keys and relationships;
- network/topology — nodes, links and network boundaries;
- agent/memory — agent roles, context/memory stores, tool and feedback flow;
- concept map — conceptual relationships where execution order is not implied.

## Visual vocabulary

Keep shape meaning stable inside one diagram.

Use:
- containers for real ownership/boundary;
- directed arrows only when direction has meaning;
- labels on edges when the relation would otherwise be ambiguous;
- different line treatment for optional/async/control relationships only when useful.

Do not overload color as the only carrier of meaning.

## Layout

Prefer one primary reading direction.

Group by ownership/layer before optimizing aesthetics.

Minimize edge crossings and long backtracking arrows.

Split a diagram when several unrelated concerns would make one canvas unreadable.
