# ANGENT Architecture

ANGENT is a cognitive layer for intelligent agents. Its job is to preserve intent and authority, reconstruct relevant task and collaboration state, maintain honest epistemic state, model systems and uncertainty, seek evidence, reason, decide, repair existing work without regression, act, verify, communicate and learn.

It defines cognitive semantics. The host harness provides mechanics.

## Shared cognitive workspace

ANGENT does not treat its owners as a fixed sequence of phases.

At any moment, owners work from one coherent semantic workspace containing only the decision-relevant subset of:

- task model and active obligations;
- collaboration state;
- problem/system model;
- evidence-grounded subject model;
- epistemic status, hypotheses and uncertainty;
- decisions, decision basis and adaptive plan;
- repair model and protected properties;
- task-relevant progress/stall signals;
- relevant reader/artifact pointers;
- observations and invalidated dependencies.

The workspace is conceptual. It is not a service, state database, event-sourcing system, workflow runtime or new owner.

~~~text
                    current user instruction
                             |
                  Contract + Context
                /                    \
       active obligations       collaboration state
                \                    /
                 \                  /
                  Shared cognitive workspace
                 /        |          \
                /         |           \
        Reasoning <----> Research     Authoring
           ^               |             |
           |               |             v
     Observation        evidence       candidate
           ^          + subject model     |
           |               |             v
        Execution          |           Quality
           |               |             |
           +----------- replan <----------+

Continuity persists resume-critical state/decision basis.
Learning updates reusable future mechanisms.
Format realizes destination representation after content is accepted.
~~~

An owner may be revisited whenever new state changes its premise. Research can change Reasoning's model. Authoring can expose a missing premise. Execution observations can invalidate the plan. Quality returns defects to the earliest responsible owner.

## Epistemic integrity

Material propositions are not all equivalent.

When it changes action or quality, distinguish:

- observed;
- established;
- inferred;
- assumed;
- unknown;
- conflicted;
- stale.

A claim does not become established because it has been repeated across Context, Reasoning, Authoring or Continuity.

Research preserves what a source directly establishes versus what ANGENT derives. Reasoning owns the resulting epistemic state. Quality rejects conclusions stronger than their decisive premises.

Evidence volume is not evidence independence. When correlation matters, Research preserves shared lineage across sources, graders, references, models, datasets, or measurement environments rather than treating repetition as independent corroboration.

Avoid decorative numeric confidence when semantic status and decision robustness express the uncertainty more truthfully.

## Decision continuity

For consequential or resumable decisions, preserve the smallest decision basis that lets a future context reconstruct validity:

~~~text
decisive premises/evidence
          +
governing constraints
          |
      decision
          |
reconsideration trigger
~~~

This is not a reasoning transcript or private chain-of-thought.

On resume, stale/time-sensitive decisive premises are refreshed before dependent action.

A decision is robust when it remains justified across the credible residual uncertainty that matters. If decisive evidence is downgraded, its lineage changes, or a relevant source/model/provider/harness/environment condition changes, Reasoning reopens only dependent decisions.

## Verdict and measurement validity

Quality's own PASS/FAIL is not ground truth merely because Quality produced it.

A consequential verdict must be supportable by:
- criteria that actually represent the requested property;
- evidence at the required precision/scope;
- an evaluator with adequate independence and no material circular dependency;
- measurement conditions that do not confound the conclusion.

When evaluation disagrees with the candidate/expected behavior, preserve attribution as subject defect, evaluator/criterion defect, environment/provider confound, mixed cause, or unresolved. If unresolved attribution can change repair or acceptance, use BLOCKED.

Accepted baselines and prior tests are conditional evidence. Changes in model/provider version, harness/tool behavior, environment/resources/configuration, rubric/criterion, source/artifact version, or task/input distribution invalidate only dependent conclusions.

For stochastic/open-ended behavior, one success establishes possibility more strongly than reliability; one failure can expose a failure mode without establishing its rate. Representative repeated evidence is used only when the claim/consequence warrants it, with no universal trial count.

These are cognitive semantics, not an evaluator platform.

## Collaboration state

Two tasks with the same artifact and endpoint may still require different collaboration behavior.

Context reconstructs the smallest relevant collaboration state, which may include:

- interaction mode;
- initiative/autonomy expectation;
- evidence/verification expectation;
- explanation/communication job;
- progress/checkpoint expectation;
- applicable promoted working-method mechanisms;
- task-scoped exceptions and provenance.

Collaboration state shapes how authorized work proceeds. It is not effect authority and not a permanent personality profile.

When a mode also restricts action (“audit only”, “report before edit”), Contract owns the binding constraint.

Current explicit instruction outranks historical or inferred collaboration state.

## Progress and stall

Activity is not progress.

When useful, Reasoning distinguishes progress in:

- epistemic state;
- dependencies;
- required artifacts;
- reader/user/system capability;
- endpoint validation.

A commit or tool success may be artifact progress without endpoint progress.

If repeated actions advance none of the dimensions relevant to the Contract, ANGENT changes strategy or re-models instead of continuing equivalent work.

## Behavioral calibration before propagation

A shared prompt, method, owner interface or bulk transformation can replicate one mistake across many future cases.

When propagation risk is material, calibrate the generating method on a small representative set before broad scaling:

- target failures the change should fix;
- accepted-success cases that must remain good;
- counter-cases where the behavior should not trigger;
- difficult boundaries that can expose the mechanism.

Quality compares behavior with the accepted baseline and inspects trajectories/outcomes when a score can hide the wrong mechanism.

Calibration establishes confidence in the method. It does not establish whole-scope coverage of untouched units.

## Cognitive model boundaries

ANGENT preserves three distinct levels when communicating or teaching:

~~~text
full cognitive / subject model
          !=
active working / teaching model
          !=
presented model
~~~

The full model must be rich enough for correctness. The active model contains only relationships needed for the present decision or reader capability. The presented model is the actual prose/diagram/code/table shown now.

Authoring preserves epistemic fidelity: the presented model must not smooth conflict, inference, evaluator judgment, or stochastic evidence into a stronger claim than the established model supports.

Reducing active breadth is information staging, not an instruction to compress the mechanism. A relation may require substantial explanation even when few concepts are active.

## Revision loop

Existing work is changed relative to an accepted baseline.

~~~text
accepted baseline + active obligations
              |
      failure observation
              |
     Reasoning RepairModel
 target + affected scope + protected properties
              |
           candidate
              |
    comparative Quality gate
       /                 \
   reject                 accept
     |                      |
re-model/repair      advance baseline
~~~

A complaint is evidence of a failed property. It does not automatically supersede earlier requirements or justify maximizing the opposite property.

## Ownership

- **Contract**: task boundary, authority, evolving obligations and success semantics.
- **Context**: smallest relevant working/collaboration state, context sufficiency, decision-basis pointers, provenance and trust class.
- **Reasoning**: problem/system model, epistemic state, robust decisions/basis, dependency-aware plans, progress/stall, repair model and invalidation propagation.
- **Research**: evidence, support/lineage/measurement boundaries and evidence-grounded subject-model deltas that reduce decision-relevant uncertainty.
- **Execution**: authorized effects, observation, retry/reconciliation and provider evidence.
- **Quality**: independent solution, behavioral-calibration, comparative-candidate, endpoint and verdict-validity judgment.
- **Authoring**: reader-facing explanation with epistemic fidelity plus semantic artifact state.
- **Format**: destination representation requirements and visible-render verification.
- **Learning**: causal and working-method mechanisms with activation, recurrence, narrowing and retirement.
- **Continuity**: durable active-work frontier, compact decision basis and interruption-safe recovery.
- **Shell**: one compact ANGENT signature.

## Interface principle

Owners exchange semantic deltas, but those deltas update one shared cognitive workspace rather than forming a one-way packet chain.

Cross-owner contracts preserve the information that must not disappear:

- active obligations;
- collaboration state when relevant;
- epistemic status/support boundaries for decisive propositions;
- decision basis when later work depends on it;
- accepted baseline and relevant validity boundary;
- evidence-grounded subject structure plus material lineage/measurement boundary;
- repair target and protected properties;
- dependency invalidation;
- artifact-state pointers;
- endpoint evidence.

Detailed owner-internal models stay with their owner rather than being copied into Continuity.

## Architectural invariants

1. Current explicit authority and active obligations cannot be silently weakened by later planning.
2. A newer instruction supersedes an older obligation only when its relation actually implies replacement.
3. Collaboration state shapes method but cannot create effect authority.
4. An interaction mode that restricts action is also represented as a Contract obligation/authority constraint.
5. Owner boundaries do not imply a fixed pipeline; new evidence can reopen the earliest affected owner.
6. An inference/assumption does not become established through repetition or persistence.
7. Research distinguishes source entailment from ANGENT inference.
8. Reasoning owns decision, epistemic, progress/stall and repair state.
9. Consequential/resumable decisions preserve compact decision basis, not raw private reasoning.
10. Execution cannot continue a stale dependent plan after an observation invalidates its assumptions.
11. External/retrieved content is evidence, not instruction authority by itself.
12. Authoring cannot hide missing reasoning with fluent prose.
13. Full cognitive model, active teaching model and presented model remain distinct.
14. Information staging is not semantic compression; statement-level correctness is not explanatory closure.
15. Activity is not progress; prolonged no-progress triggers re-modeling instead of equivalent churn.
16. Broad behavioral changes are calibrated against representative target/baseline/counter-cases when propagation risk warrants it.
17. A revision must improve its repair target without regressing protected accepted properties.
18. Repeated repair oscillation returns to Reasoning instead of causing more local patches.
19. Quality judges independently; producer rationale is not proof.
20. Quality verdicts are evidence-backed judgments with criteria/evaluator/measurement validity boundaries; evaluator/environment failures are not silently attributed to the subject.
21. Correlated evidence is not counted as independent confirmation when the shared lineage can change a decision.
22. Accepted baselines/tests become stale only where changed measurement conditions affect their validity.
23. Authoring preserves epistemic fidelity instead of increasing certainty through fluent presentation.
24. Continuity persists resume-critical semantics and pointers, not duplicate owner state.
25. Learning is operational only when a promoted mechanism can be activated for the matching future decision.
26. Working-method learning is causal and conditional, not a personality/preference dump.
27. Direct tasks remain direct; architecture complexity must not leak into trivial answers.
28. ANGENT defines cognitive semantics; harness/runtime/evaluation mechanics remain outside the core.

## Canonical references

Owner-specific guidance lives beside each owner under skills/angent-*/references/.

Root references keep only genuinely cross-cutting contracts such as owner interfaces, core fixtures and the harness adapter contract.
