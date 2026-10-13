# Core capability fixtures — behavior ANGENT must preserve

These are calibration cases for the cognitive architecture, not templates to copy into answers.

## 1. Means versus objective

A user requires reuse of a high-quality UI template because the existing product feels inconsistent.

PASS:
- Contract preserves explicit reuse as a constraint;
- Reasoning models the real success state as fidelity/usability, not component-count reuse;
- audit covers user journeys and states, not only visible components.

FAIL:
- "reuse template" is reduced to importing components while the resulting flow remains poor.

## 2. Cross-layer system diagnosis

A connected embedded device produces incorrect speech recognition.

PASS:
- Reasoning separates audio capture, preprocessing, encoding/transport, server/model and output interpretation;
- hypotheses have discriminating observations;
- Research/Execution gather evidence at the earliest boundary that can separate alternatives.

FAIL:
- jump directly to the most familiar layer or list generic causes.

## 3. Conflicting sources

Official documentation and current implementation disagree.

PASS:
- Research labels source roles and version boundaries;
- Reasoning distinguishes required/normative behavior from observed implementation;
- uncertainty stays explicit if the task cannot resolve the conflict.

FAIL:
- average the two statements into a compromise.

## 4. Reversible architecture decision

Two technical options meet hard constraints but one has uncertain long-term cost.

PASS:
- decision considers reversibility, switching cost and information value;
- a small probe may precede commitment when it can resolve decisive uncertainty.

FAIL:
- generic pros/cons matrix with no recommendation mechanism.

## 5. Replanning after observation

An implementation step succeeds syntactically but runtime behavior contradicts the assumed interface.

PASS:
- Execution returns the observation delta;
- Reasoning updates the system model and invalidates dependent plan nodes;
- unrelated verified work remains intact.

FAIL:
- continue stale steps because they were in the original plan.

## 6. Whole-scope audit

The user asks for a full book/application/system audit.

PASS:
- Contract/Reasoning establish the scope dimensions and inventory;
- samples can guide depth but cannot certify unseen scope;
- Quality distinguishes sampled evidence from full coverage.

FAIL:
- deeply inspect one recent complaint and label the whole target acceptable.

## 7. Long-form technical explanation

A chapter teaches a mechanism with several new concepts and a concrete project example.

PASS:
- established reader state controls terminology;
- the example anchors but does not replace definitions/relationships;
- representation carries complex flow where useful;
- prose interprets code/figures.

FAIL:
- example name repetition is treated as proof of understanding.

## 8. Direct-answer negative control

The user asks for a narrow stable API semantic fact.

PASS:
- Root uses Direct mode;
- answer remains concise;
- no visible task model, hypothesis tree or planning ceremony.

FAIL:
- cognitive machinery becomes user-facing overhead.

## 9. Learning from success

A repeated strategy reduces uncertainty efficiently across unrelated tasks.

PASS:
- Learning separates strategy contribution from coincidence;
- mechanism is promoted only with a plausible causal link and boundary.

FAIL:
- every successful sequence becomes a global workflow rule.

## 10. Ambiguous external effect

A provider write may have succeeded but the response is lost.

PASS:
- Continuity leaves PREPARED/ATTEMPTED_UNKNOWN;
- Execution queries provider state before replay;
- Reasoning resumes from reconciled reality.

FAIL:
- blindly repeat the write or assume it failed.
