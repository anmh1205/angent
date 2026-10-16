# state: Define lifecycle invariants for a business object

**Scope or capability:** `<project-id>`  
**Artifact ID and revision:** `<stable-id / known revision>`  
**Approval state:** proposed / in-review / approved (verify before marking)  
**Evidence source:** `<provider path, link, commit, line when actually read>`

## Necessary content

### 1. Actors, nodes and edges

Record project-specific evidence, observations, decisions and remaining unknowns concerning actors, nodes and edges. Link every material conclusion to the currently accepted requirement or verified provider data.

### 2. Model assumptions and business semantics

Record project-specific evidence, observations, decisions and remaining unknowns concerning model assumptions and business semantics. Link every material conclusion to the currently accepted requirement or verified provider data.

### 3. Guards, cardinality and direction

Record project-specific evidence, observations, decisions and remaining unknowns concerning guards, cardinality and direction. Link every material conclusion to the currently accepted requirement or verified provider data.

### 4. Negative or terminal paths

Record project-specific evidence, observations, decisions and remaining unknowns concerning negative or terminal paths. Link every material conclusion to the currently accepted requirement or verified provider data.

### 5. Rendering tool and visual verification

Record project-specific evidence, observations, decisions and remaining unknowns concerning rendering tool and visual verification. Link every material conclusion to the currently accepted requirement or verified provider data.

## Specialist outcome

**Define lifecycle invariants for a business object.** Produce the actual requested output appropriate to this capability, distinguish design from current behavior, and preserve agreed constraints.

| Reference | Observation/decision | Source and revision | Confidence/approval | Downstream dependency | Verification |
|---|---|---|---|---|---|
| `<id>` | `<evidence-backed claim>` | `<source>` | proposed | `<id>` | `<observable check>` |

## Review

Check traceability, completeness, actors and permission boundaries, error paths, contradiction with other artifacts, and acceptance based on real evidence. Missing tool execution must be reported, never simulated. Related: [operating model](../operating-model.md) and [review rules](../rules-index.md).
