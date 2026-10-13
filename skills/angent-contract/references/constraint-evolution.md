# Constraint evolution — preserve meaning across corrections

User instructions accumulate unless the user actually replaces them.

For every material new instruction or correction, classify its relation to the active task model:

- **ADD** — introduces a new constraint or requirement without changing earlier ones;
- **REFINE** — narrows or clarifies an existing requirement while preserving its intent;
- **SUPERSEDE** — explicitly replaces an earlier requirement;
- **SCOPED_EXCEPTION** — changes behavior only for a named scope, unit, phase or case;
- **CONFLICT** — cannot be satisfied together with another still-active requirement.

Do not infer SUPERSEDE merely because an instruction is newer.

A complaint describes an observed failure. It does not automatically authorize maximizing the opposite property.

Examples:

- "Nội dung còn mỏng" adds a depth requirement; it does not remove the existing requirement to avoid repetition.
- "Cần thêm Mermaid ở chỗ khó hình dung" refines representation choice; it does not require a diagram in every section.
- "Từ chương 7 giả định người đọc chưa biết phần này" is a scoped reader-state correction; it does not reset unrelated concepts already established earlier.
- "Bỏ quy tắc X, dùng Y thay thế" explicitly supersedes X.

## Active obligation set

Maintain the currently binding obligations that downstream work must preserve:

- hard constraints;
- accepted project/architecture decisions;
- explicit exclusions;
- accepted quality floors;
- unresolved promises;
- scoped exceptions;
- current authority boundaries.

Each obligation should retain its provenance and scope.

When a new instruction arrives:

1. classify its relation;
2. update only the obligations it actually changes;
3. preserve unaffected obligations;
4. propagate changed obligations to decisions/artifacts that depended on them;
5. expose a true conflict only when no valid interpretation preserves both.

Recency resolves explicit replacement. It is not a general-purpose merge algorithm.


## Obligation lifecycle

The active obligation set must not grow forever.

An obligation can be:

- **ACTIVE** — still constrains current work;
- **SATISFIED** — its required state has been achieved and no continuing constraint remains;
- **SUPERSEDED** — explicitly replaced by newer authority;
- **EXPIRED** — its scope/phase ended;
- **OUT_OF_SCOPE** — no longer applies after an authorized scope change.

Only ACTIVE obligations are carried as mandatory context.

A scoped exception expires with its scope unless explicitly extended. A promise becomes SATISFIED when its promised state is delivered. Do not keep completed procedural instructions active merely because they were once explicit.
