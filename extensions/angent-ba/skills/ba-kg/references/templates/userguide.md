# userguide: Write user-facing operational guidance grounded in shipped behavior

**Scope or capability:** `<project-id>`  
**Artifact ID and revision:** `<stable-id / known revision>`  
**Approval state:** proposed / in-review / approved (verify before marking)  
**Evidence source:** `<provider path, link, commit, line when actually read>`

## Necessary content

### 1. Approved artifact baseline

Record project-specific evidence, observations, decisions and remaining unknowns concerning approved artifact baseline. Link every material conclusion to the currently accepted requirement or verified provider data.

### 2. Remote identity and last observed revision

Record project-specific evidence, observations, decisions and remaining unknowns concerning remote identity and last observed revision. Link every material conclusion to the currently accepted requirement or verified provider data.

### 3. Planned changes and owner permissions

Record project-specific evidence, observations, decisions and remaining unknowns concerning planned changes and owner permissions. Link every material conclusion to the currently accepted requirement or verified provider data.

### 4. Conflict avoidance and rollback

Record project-specific evidence, observations, decisions and remaining unknowns concerning conflict avoidance and rollback. Link every material conclusion to the currently accepted requirement or verified provider data.

### 5. Provider read-back and remaining exceptions

Record project-specific evidence, observations, decisions and remaining unknowns concerning provider read-back and remaining exceptions. Link every material conclusion to the currently accepted requirement or verified provider data.

## Specialist outcome

**Write user-facing operational guidance grounded in shipped behavior.** Produce the actual requested output appropriate to this capability, distinguish design from current behavior, and preserve agreed constraints.

| Reference | Observation/decision | Source and revision | Confidence/approval | Downstream dependency | Verification |
|---|---|---|---|---|---|
| `<id>` | `<evidence-backed claim>` | `<source>` | proposed | `<id>` | `<observable check>` |

## Review

Check traceability, completeness, actors and permission boundaries, error paths, contradiction with other artifacts, and acceptance based on real evidence. Missing tool execution must be reported, never simulated. Related: [operating model](../operating-model.md) and [review rules](../rules-index.md).
