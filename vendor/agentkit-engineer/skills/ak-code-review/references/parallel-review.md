# Parallel and multi-reviewer strategies

Parallel review is useful only when independence changes coverage, elapsed time, or confidence.

## Partitioned parallel review

Good partitions include:
- backend vs frontend;
- independent packages/services;
- security-specific pass plus correctness pass when both are substantial;
- migration/data path vs application behavior.

Each reviewer receives:
- exact scope;
- relevant requirements/AGENTS.md;
- specific risk/question;
- no-write rule;
- expected evidence/finding format.

Join findings before fixes. Deduplicate shared root causes and preserve conflicts.

If the requested strategy is merely partitioned review and safe delegation is unavailable, sequential independent passes may be an honest degradation when elapsed-time parallelism is not load-bearing.

## Ultra / fixed independent candidate pool

A strategy such as `--ultra` uses a stronger evidence contract: several independent read-only candidate reviews over the same evidence packet followed by a verification/deduplication finalizer.

When the current installed stable workflow specifies a fixed independent candidate pool or parallel wave, preserve that requirement.

If the runtime cannot produce the required usable independent candidates after the allowed retry behavior, fail closed for that strategy.

Do not silently:
- run one reviewer and call it ultra;
- reuse one review several times;
- replace required parallel independent candidates with sequential self-review;
- combine ultra with another mode that owns the same multi-reviewer strategy when the stable workflow marks them incompatible.

## Independence

Different reviewer labels do not guarantee independent evidence.

Record shared source packets, model/runtime family, rubric and assumptions when those correlations can materially affect the verdict.

Final synthesis verifies/deduplicates evidence; it does not majority-vote candidate opinions.
