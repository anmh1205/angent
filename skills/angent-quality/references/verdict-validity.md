# Verdict validity

Quality evaluates the work, but Quality itself can be wrong.

Treat PASS, FAIL, or BLOCKED as an evidence-backed judgment whose validity depends on four things:

1. **criteria validity** — the criteria represent the requested success/failure condition;
2. **evidence validity** — observations support those criteria at the required precision and scope;
3. **evaluator validity** — the evaluator can apply the criteria without a material blind spot or circular dependency;
4. **measurement validity** — model/provider version, harness, environment, resources, configuration, inputs, and other conditions do not confound the conclusion.

This is a semantic model, not a new evaluator framework.

## Criteria basis

Derive criteria from the current Contract, active obligations, accepted baseline/protected properties, domain evidence, and reader/endpoint requirements that actually matter.

Do not silently replace user success with an available metric. A metric can be measured precisely and still be the wrong criterion.

## Task and fixture validity

Before treating repeated failure as evidence about ANGENT, check that the task/fixture can actually be satisfied under its stated Contract, available capabilities and measurement environment.

A calibration task is suspect when:
- the grader enforces a hidden requirement not present in the task/Contract;
- two required criteria cannot both be satisfied;
- the environment removes a capability the task assumes exists;
- success depends on an unstated path/identity/version;
- a “correct” reference or expected state cannot itself satisfy the graders.

For consequential or confusing cases, a known-valid reference behavior/solution or expert/manual pass can establish that the fixture and graders are capable of recognizing success. This is strong evidence, not a mandatory ceremony for every simple check.

If a fixture is unsatisfiable or materially ambiguous, classify the verdict as evaluator/criterion defect or BLOCKED/UNRESOLVED rather than repairing the agent toward the broken grader.

## Evidence basis

Prefer evidence that directly establishes the requested property.

Distinguish direct/authoritative observation, source-stated fact, derived inference, and evaluator judgment. A downstream judgment does not become stronger than the evidence and assumptions it depends on merely because several graders repeat it.

## Independence and shared lineage

Several checks are not independent if they depend on the same upstream fact, reference answer, model output, dataset, environment assumption, or failure mode.

Examples:
- three sources copying one vendor announcement remain one weakly independent lineage;
- a generated answer and a grader using that same generated answer as its reference are circular;
- two model graders with the same rubric/model family may add replication while sharing important blind spots;
- provider read-back and a separately derived semantic comparison can establish different complementary properties.

Do not count correlated checks as independent confirmation.

## Isolation and contamination

Evaluation evidence can be invalid even when the grader itself is sound if the trial inherits state that changes the result.

When a behavioral calibration or repeated trial is used to support reliability/regression claims, preserve enough initial-state information to know whether prior runs, cached artifacts, conversation/session memory, modified repositories/workspaces, provider objects, resource exhaustion, or other shared state could have influenced the outcome.

Prefer a clean or deliberately reconstructed initial state when feasible.

If shared state is intentionally part of the behavior being evaluated, declare it as part of the measurement context rather than resetting it away.

Do not count several trials as independent evidence when they share a contaminating state/failure source that can materially couple their outcomes.

## Failure attribution

When an evaluation disagrees with the candidate or expected behavior, distinguish:

- **SUBJECT_DEFECT** — evidence supports a defect in the solution/artifact/behavior;
- **EVALUATOR_DEFECT** — the grader/criterion is wrong or cannot measure the property;
- **ENVIRONMENT_CONFOUND** — environment/provider/infrastructure changed or corrupted what was measured;
- **MIXED** — more than one cause materially contributes;
- **UNRESOLVED** — evidence cannot yet distinguish them.

Use BLOCKED for UNRESOLVED attribution when choosing the wrong owner would cause material rework or false acceptance.

## Stochastic behavior

One successful trial usually establishes possibility more strongly than reliability.

One failure may expose a real failure mode, but its rate and generality remain unknown unless evidence supports them.

When claiming repeatability, robustness, or regression absence for stochastic/open-ended behavior, use representative repeated evidence when consequence warrants it. There is no universal fixed number of trials.

## Baseline validity

An accepted baseline is conditional evidence, not permanent truth.

Record or recover the conditions that can affect its meaning when they matter:
- model/provider/version;
- tool/harness behavior;
- environment/resources/configuration;
- rubric/criterion;
- source/artifact version;
- task/input distribution.

If a condition changes, mark only dependent conclusions stale/recheck. Do not invalidate unrelated accepted properties.

## Verdict semantics

**PASS** — evidence supports the required property within the stated validity boundary, and no unresolved evaluator/environment issue could plausibly reverse the verdict at the current consequence level.

**FAIL** — evidence supports a subject defect strongly enough to route repair to the responsible owner.

**BLOCKED** — evidence is insufficient, evaluator validity is inadequate, attribution is unresolved, or measurement conditions prevent a justified PASS/FAIL.

Avoid synthetic confidence percentages unless the underlying measurement justifies them. Prefer explicit support, boundary, confounders, and reconsideration conditions.
