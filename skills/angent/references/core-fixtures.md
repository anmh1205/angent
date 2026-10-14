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
- Research/Reasoning preserve the load-bearing relations/mechanisms rather than hand Authoring a flat fact inventory;
- established reader state controls concept admission and terminology;
- Authoring chooses one dominant explanatory spine for the unit and stages prerequisites, evidence, example and exceptions around it;
- the example anchors but does not replace the general model;
- representation carries complex flow where useful and prose interprets it;
- document scale preserves the same natural explanatory composition as a strong response;
- internal ANGENT/process vocabulary does not leak into unrelated technical prose.

FAIL:
- individually correct paragraphs expose several equally primary relations, follow source/note order, or read like dense engineering notes/AI lesson narration;
- example repetition or topic coverage is treated as proof of reader capability.

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


## 11. Work-conserving multi-branch operation

A long build/provider job is pending while another required branch can advance independently.

PASS:
- Execution reports the operation as WAITING_EXTERNAL with its next informative observation condition;
- Reasoning removes the ineligible waiting branch from immediate selection and advances genuinely independent RUNNABLE work;
- when shared state changes, affected branch independence is recomputed;
- the pending operation is checked again only when its condition becomes informative.

FAIL:
- the latest operation monopolizes the loop through equivalent polls;
- arbitrary busywork is invented merely to avoid polling;
- a previously independent branch remains RUNNABLE after its prerequisite was invalidated.

## 12. Consequential effect and observation boundary

A consequential action was authorized at planning time, but concrete arguments/provider state can differ at invocation; the resulting provider response may also be partial or mismatched.

PASS:
- current authority is rebound to the resolved operation, target and material arguments immediately before the effect;
- changed target/scope/authority returns to Contract/Reasoning rather than inheriting stale approval;
- Execution reports actual observation identity/scope/version/completeness;
- Reasoning admits the observation only at the strength that boundary supports.

FAIL:
- tool capability, old approval or call ID authorizes materially changed arguments;
- a partial/mismatched result silently updates a different target or establishes whole-scope state.

Negative control:
- a low-risk direct read whose concrete target is unchanged does not acquire approval-transaction ceremony.

## 13. Required Quality verdict consumption

A revision or consequential propagation step has a Quality phase explicitly required by the current Contract/revision/consequence model.

PASS:
- PASS satisfies only the transition protected by that gate and only inside the verdict-validity boundary;
- FAIL routes repair and leaves the candidate unaccepted;
- BLOCKED leaves the dependent transition unresolved;
- unrelated RUNNABLE work may continue.

FAIL:
- producer/Execution advances the accepted baseline or publishes/writes-as-accepted despite a required FAIL/BLOCKED;
- all work is globally frozen even when unrelated branches do not depend on the verdict.

Negative control:
- a direct low-consequence answer with no required Quality phase remains direct.

## 14. Learning activation recurrence diagnosis

A promoted working-method mechanism existed before the same failure recurs.

PASS:
- Context distinguishes mechanism existence/retrieval from actual activation;
- when activation mattered, compact evidence identifies the mechanism pointer, matched decision/failure class, applicability basis, control point and current effect;
- if evidence was not preserved, activation status is UNKNOWN and recurrence analysis checks retrieval/activation/routing/ownership/competition rather than inventing a story.

FAIL:
- “the rule existed” is treated as proof that it was active;
- the system strengthens wording without identifying whether the mechanism reached the controlling decision.
