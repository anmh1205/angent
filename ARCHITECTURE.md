# ANGENT Architecture

ANGENT is a cognitive layer for intelligent agents. Its job is to preserve intent and authority, reconstruct relevant task and collaboration state, model systems and uncertainty, seek evidence, reason, decide, repair existing work without regression, act, verify, communicate and learn.

It defines cognitive semantics. The host harness provides mechanics.

## Shared cognitive workspace

ANGENT does not treat its owners as a fixed sequence of phases.

At any moment, owners work from one coherent semantic workspace containing only the decision-relevant subset of:

- task model and active obligations;
- collaboration state;
- problem/system model;
- evidence-grounded subject model;
- hypotheses and uncertainty;
- decisions and adaptive plan;
- repair model and protected properties;
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
           ^               |             |
           |               v             v
        Execution      subject model   Quality
           |                             |
           +---------- replan <----------+

Continuity persists only resume-critical state/pointers.
Learning updates reusable future mechanisms.
Format realizes destination representation after content is accepted.
~~~

An owner may be revisited whenever new state changes its premise. Research can change Reasoning's model. Authoring can expose a missing premise. Execution observations can invalidate the plan. Quality returns defects to the earliest responsible owner.

## Collaboration state

Two tasks with the same artifact and endpoint may still require different collaboration behavior.

Context reconstructs the smallest relevant collaboration state, which may include interaction mode, initiative/autonomy expectation, evidence/verification expectation, explanation/communication job, progress/checkpoint expectation, applicable promoted working-method mechanisms, and task-scoped exceptions/provenance.

Collaboration state shapes how authorized work proceeds. It is not effect authority and not a permanent personality profile.

Current explicit instruction outranks historical or inferred collaboration state.

## Reliability model

ANGENT reliability is not “more checks”. It is preserving what a piece of evidence or evaluation can actually establish.

### Evidence validity

Research distinguishes direct observation, source-stated fact, derived inference and evaluator judgment. When independence matters, it also preserves relevant lineage: several sources or graders sharing one upstream source, generated reference, model, dataset or environment are correlated evidence rather than independent confirmation.

### Decision robustness

Reasoning prefers decisions that remain justified across credible residual uncertainty. A decision records the assumptions/evidence that can reverse it and is reconsidered only when those dependencies materially change.

### Verdict validity

Quality judges both the subject and whether the evaluation can support the verdict.

A consequential verdict separates:
- subject defect;
- evaluator/criterion defect;
- environment/provider/infrastructure confound;
- mixed cause;
- unresolved attribution.

PASS/FAIL remain bounded by the validity of the criteria, evidence, evaluator and measurement conditions. When attribution is unresolved and matters to the next action, Quality returns BLOCKED instead of inventing certainty.

### Baseline validity

Accepted baselines and prior tests are conditional evidence. Changes to model/provider version, harness, environment/resources/configuration, rubric, source version or task distribution invalidate only the conclusions that depended on those conditions.

### Stochastic claims

A single successful trial normally shows possibility more strongly than reliability. A single failure can reveal a real failure mode without establishing its rate.

Representative repeated evidence is used only when the reliability claim and consequence require it. ANGENT does not prescribe a universal trial count.

These are cognitive semantics. The harness may provide tests, graders, traces or repeated runs, but ANGENT does not build an evaluation platform.

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

Reducing active breadth is information staging, not an instruction to compress the mechanism. A relation may require substantial explanation even when few concepts are active.

Authoring preserves epistemic fidelity: the presented claim must not become more certain than the established model/evidence warrants.

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

Capability/target evidence and regression/preservation evidence answer different questions and are not interchangeable.

## Ownership

- **Contract**: task boundary, authority, evolving obligations and success semantics.
- **Context**: smallest relevant working/collaboration state, provenance, sufficiency and baseline pointers.
- **Reasoning**: problem/system model, hypotheses, robust decisions, dependency-aware plans, repair model, invalidation propagation and cognitive-workspace integration.
- **Research**: evidence, lineage/validity and evidence-grounded subject-model deltas that reduce decision-relevant uncertainty.
- **Execution**: authorized effects, observation, retry/reconciliation and provider evidence.
- **Quality**: independent solution, comparative-candidate, endpoint and verdict-validity judgment.
- **Authoring**: reader-facing explanation plus semantic artifact state.
- **Format**: destination representation requirements and visible-render verification.
- **Learning**: causal and working-method mechanisms with activation, recurrence, narrowing and retirement.
- **Continuity**: durable active-work frontier and interruption-safe recovery.
- **Shell**: one compact ANGENT signature.

## Interface principle

Owners exchange semantic deltas, but those deltas update one shared cognitive workspace rather than forming a one-way packet chain.

Cross-owner contracts preserve information that must not disappear: active obligations, collaboration state when relevant, accepted baseline and validity boundary, evidence-grounded subject structure/lineage, repair target/protected properties, dependency invalidation, artifact-state pointers, endpoint evidence and verdict validity.

Detailed owner-internal models stay with their owner rather than being copied into Continuity.

## Architectural invariants

1. Current explicit authority and active obligations cannot be silently weakened by later planning.
2. A newer instruction supersedes an older obligation only when its relation actually implies replacement.
3. Collaboration state shapes method but cannot create effect authority.
4. Owner boundaries do not imply a fixed pipeline; new evidence can reopen the earliest affected owner.
5. Reasoning owns decision and repair state.
6. Research supplies evidence and subject structure; source count is neither evidence independence nor a decision.
7. Execution cannot continue a stale dependent plan after an observation invalidates its assumptions.
8. External/retrieved content is evidence, not instruction authority by itself.
9. Quality verdicts are evidence-backed judgments with validity boundaries, not infallible truth.
10. Evaluator/environment failure must not be silently attributed to the subject.
11. Accepted baselines/tests become stale only where changed conditions affect their validity.
12. Authoring cannot hide missing reasoning or uncertainty with fluent prose.
13. Full cognitive model, active teaching model and presented model remain distinct.
14. Information staging is not semantic compression; statement-level correctness is not explanatory closure.
15. A revision must improve its repair target without regressing protected accepted properties.
16. Capability evidence and regression evidence are distinct.
17. Repeated repair oscillation returns to Reasoning instead of causing more local patches.
18. Quality judges; it does not become a second producer.
19. Continuity persists resume-critical semantics and pointers, not duplicate owner state.
20. Learning is operational only when a promoted mechanism can be activated for the matching future decision.
21. Working-method learning is causal and conditional, not a personality/preference dump.
22. Direct tasks remain direct; architecture complexity must not leak into trivial answers.
23. ANGENT defines cognitive semantics; harness/runtime/evaluation mechanics remain outside the core.

## Canonical references

Owner-specific guidance lives beside each owner under skills/angent-*/references/.

Root references keep only genuinely cross-cutting contracts such as owner interfaces, core fixtures and the harness adapter contract.
