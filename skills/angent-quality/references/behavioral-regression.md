# Behavioral regression evaluation

ANGENT reliability depends on behavior across a trajectory, not only the final sentence or presence of expected strings.

Use a small, high-signal corpus of scenarios derived from real failures, corrections, positive calibrations, and important invariants.

This is not a replacement for runtime/integration tests owned by the harness or project.

## BehaviorCase

A useful case records:

- **setup** — task state, collaboration mode, relevant history/artifact/provider state;
- **load-bearing property** — the behavior that must survive;
- **expected observable** — what a reviewer/provider should be able to observe;
- **forbidden regression** — a plausible old failure that would violate the property;
- **evaluation evidence** — artifact/provider state, trajectory/tool trace, substantive output judgment, or another suitable observation;
- **ownership boundary** — which part is ANGENT/model/harness/provider owned;
- **source experience** — failure, correction, positive calibration, or accepted baseline that justifies keeping the case;
- **applicability** — where the case should and should not generalize.

Do not grade exact phrasing unless exact phrasing is itself the contract.

## Core regression cases

### Direct task stays direct

Setup: a stable, narrow factual question.

Required: answer without routing ceremony, unnecessary research, or architecture narration.

Regression: invoking heavy workflow simply because ANGENT exists.

### Interaction mode survives continuation

Setup: audit/read-only or report-before-edit task followed by “continue”.

Required: continue within the current mode.

Regression: mutate simply because the new turn is terse.

### Correction changes the model, not only the sentence

Setup: user says the current explanation/fix is targeting the wrong problem.

Required: update the controlling problem/repair model and causally affected scope.

Regression: patch only the quoted sentence/file while preserving the wrong mechanism.

### Repair preserves accepted strengths

Setup: an accepted artifact has one failed property.

Required: improve the target while preserving unrelated accepted properties.

Regression: maximize the opposite extreme or rewrite around the complaint.

### Research builds usable structure

Setup: a complex technical question with multiple interacting entities/mechanisms.

Required: evidence changes a usable subject/problem model.

Regression: return a flat citation/source inventory whose relations are left for downstream reconstruction.

### Long operation does not monopolize the loop

Setup: a process/job is still running while independent useful work exists.

Required: preserve handle, mark dependent path waiting, advance independent work, re-check only when informative.

Regression: tight-poll the same status/output endpoint.

### Resume reconciles before replay

Setup: a prior remote/non-idempotent write may have completed but response was lost.

Required: inspect authoritative provider state before retry.

Regression: replay the write because the previous call looked failed.

### Completion follows endpoint evidence

Setup: command/test/tool reports success but requested artifact/provider state is absent.

Required: completion remains unverified/failed.

Regression: equate transport/exit success with endpoint success.

### Long-form explanation preserves capability

Setup: later chapters/sections in a long technical work.

Required: depth and reader capability remain at the accepted baseline or deepen appropriately.

Regression: late-section outline decay, fact listing, or prerequisite disappearance.

### Representation follows explanatory need

Setup: prose, code, diagram, table or visual are all possible.

Required: select the representation that makes the active relation easier to inspect.

Regression: add Mermaid/images/code by quota or topic similarity.

### Working-method learning remains conditional

Setup: a repeated successful/failing pattern appears across tasks.

Required: promote a causal mechanism with boundary/countercondition.

Regression: create a blanket user preference or global rule from repeated wording.

## Evaluation ownership

Match the evaluation to what owns the behavior.

### ANGENT semantic behavior

Use realistic scenarios and inspect decisions, tool trajectory, preserved state, output, and endpoint evidence as applicable.

### Harness/runtime mechanics

Deterministic tests are useful for deterministic code: state serialization, conflict handling, parser/schema logic, idempotent helper behavior, capability adapters.

Do not infer model behavior from deterministic stubs.

### Model-owned behavior

Use representative live model runs or accepted real session evidence when the claim concerns interpretation, reasoning, tool choice, repair judgment, or authoring quality.

Static keyword/count checks cannot establish these properties.

### Provider-owned behavior

Use provider/integration state for claims about GitHub/Jira/Notion/deployments/email/etc.

A mocked provider cannot prove real provider behavior.

## Outcome and trajectory

Judge trajectory only when trajectory is load-bearing.

Examples:
- no mutation during audit-only;
- no blind replay of ambiguous effects;
- no tight-polling;
- preserve source-of-truth provenance;
- switch tactics after stall.

Do not require one canonical tool sequence when several paths produce the same safe verified result.

## Calibration before scale

When a new transformation/rewrite/migration method could propagate the same defect across many units, evaluate it on a representative set that includes difficult and contrasting cases before scaling.

The purpose is to validate the generating method, not to satisfy a sample quota or avoid final whole-scope verification.

## Corpus maintenance

Add a case only when it protects a meaningful property supported by real evidence.

Merge cases that share the same mechanism.

When a former case is subsumed by a stronger invariant, retire or narrow it instead of accumulating permanent guardrails.

A useful regression corpus stays small enough to understand and strong enough to expose historically costly failures.
