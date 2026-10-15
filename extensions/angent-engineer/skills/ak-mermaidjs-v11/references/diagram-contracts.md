# Mermaid v11 diagram semantics and syntax

These examples are portable **source patterns**, not proof that every target renderer implements every v11 feature. Confirm the installed renderer for experimental/advanced types.

## Core diagrams

### Decision flow

~~~mermaid
flowchart TD
  request[Receive request] --> authenticated{Authenticated?}
  authenticated -->|No| reject[Reject request]
  authenticated -->|Yes| authorized{Authorized?}
  authorized -->|No| reject
  authorized -->|Yes| handler[Run handler]
  handler --> response[Return result]
~~~

Flow edges must state who decides a condition. Avoid inventing arrows merely to connect all boxes. Use TB/TD, BT, LR or RL according to reading flow. Subgraphs represent real groupings, not decorative borders.

### Sequence and async boundaries

~~~mermaid
sequenceDiagram
  participant Client
  participant API
  participant Store
  Client->>API: POST /resource
  API->>Store: write record
  alt Commit accepted
    Store-->>API: committed ID
    API-->>Client: 201 + ID
  else Commit failed
    Store-->>API: error
    API-->>Client: failure response
  end
~~~

Use participants and arrow types accurately; model error/retry/timeout paths when they affect the outcome. Parallel blocks or activation bars are appropriate only when supported by actual concurrency or call lifetime.

### State transitions

~~~mermaid
stateDiagram-v2
  [*] --> Idle
  Idle --> Active: start
  Active --> Failed: operation_error
  Active --> Complete: success
  Failed --> Idle: reset
  Complete --> [*]
~~~

State labels represent actual persistent or logical states; event labels represent transitions. Do not use a process flow to hide missing states or guards.

### Entity relationship and type structure

~~~mermaid
erDiagram
  CUSTOMER ||--o{ ORDER : places
  ORDER ||--|{ LINE_ITEM : contains
~~~

Check optionality and one-to-many semantics against schema constraints, not just names. Class diagrams instead express inheritance, composition and static dependency; avoid mixing runtime message flow with static class arrows.

## Other selection contracts

| Diagram | Answers | Special checks |
|---|---|---|
| gantt | When tasks occur and depend on others | Explicit date format, milestones, sequencing |
| timeline | Which events happened when | Confirmed dates and event ordering |
| journey | Which actor experiences which stage | Source-grounded score/actor assignments |
| gitGraph | Which branches and merges exist | Real commit topology, not a fictional example |
| mindmap | What concept hierarchy exists | Hierarchy vs causal link distinction |
| requirementDiagram | Which requirement is satisfied | Real requirement IDs and traceability |
| C4Context / architecture-beta | What components and connections exist | Supported renderer/version; deployment vs logical view |
| block-beta | How modules/groups connect | Layout and supported syntax |
| xychart-beta / pie | What measured quantity changes | Grounded numerical values, units and scale |
| sankey-beta | What quantity flows between nodes | Conservation or known boundary loss |
| packet-beta | Which fields occupy bit ranges | Exact offsets/field widths |
| radar-beta / treemap-beta | How multiple dimensions compare | Data comparability, feature availability |

Prefer plain tables/charts when rendering support or quantitative accuracy cannot be established. Features such as user click callbacks, theme directives, HTML labels and icons are runtime/security-dependent and should not be injected into portable output by default.

## Version and layout pitfalls

- GitHub/Notion/other Markdown engines can pin older Mermaid releases and may reject new diagram kinds.
- Renderer support and parser grammar may differ between browser, CLI, static-site build and embedded viewer.
- Arrow crossings, long technical labels, clipped notes, dark-theme contrast and extremely dense graphs are **rendered-result** failures, not merely syntax failures.
- Source diagrams often embed untrusted labels; sanitize/escape user-provided text and keep interactive behavior disabled unless the application explicitly owns that trust boundary.
