# ANGENT Architecture

ANGENT is a cognitive layer for intelligent agents. Its job is to preserve intent and authority, reconstruct relevant task and collaboration state, maintain honest epistemic state, model systems and uncertainty, interpret corrections at the right abstraction level, schedule work across independent frontier branches, seek evidence, reason, decide, repair existing work without regression, act, verify, communicate and learn.

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
- correction interpretation, repair model and protected properties;
- active-frontier branch state and wait conditions;
- task-relevant progress/stall signals;
- relevant reader/artifact pointers;
- observations and invalidated dependencies.

The workspace is conceptual. It is not a service, state database, event-sourcing system, workflow runtime, queue, scheduler service or new owner.

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

Continuity persists resume-critical state/decision basis/frontier branch state.
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

Operational failure and domain evidence are distinct. Tool lookup/schema errors, access denial, timeout, transport failure, and ambiguous side effects can establish facts about the execution path without establishing the intended target proposition. A negative domain fact requires an authoritative observation whose identity, scope and documented semantics actually entail it.

Existing-state mutation has a separate freshness boundary. A candidate derived from canonical version V remains trustworthy only while the live state that its delta depends on is compatible with V. Provider-native expected-version/CAS mechanics are preferred when available; otherwise ANGENT refreshes enough state to rebase/reconcile the semantic delta. This is not a transaction subsystem.

Canonical identity has a different boundary: provider identity is a locator, while project canon is a role binding. Context resolves a semantic role such as current/production/private to the authoritative live object before dependent work; explicit exact/historical targets remain exact. Provider recency alone does not define project canon.

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

## Correction semantics

A correction has two layers that must not be collapsed:

~~~text
observed example / explicit wording
              ↓
failed property / candidate mechanism
              ↓
actual abstraction level + causal scope
              ↓
repair owner and delta
~~~

The user may point to one sentence while criticizing the authoring method, one tool action while criticizing execution policy, or one project result while criticizing a recurring collaboration pattern.

Therefore:

- the named example is evidence, not automatically the complete repair scope;
- recurrence and method-level language trigger retrieval of relevant prior complaints, positive baselines and promoted mechanisms;
- Reasoning determines whether the failure is local, repeated, method-level, owner/interface/state-model level or collaboration-level before editing;
- repeated failure despite an existing rule is evidence that retrieval, activation, routing, ownership or abstraction may be wrong;
- systemic repair changes the generating mechanism at its causal scope without widening into unrelated work.

This is not a feedback classifier service. It is a reasoning invariant.

## Work-conserving frontier scheduling

Long-running operations create dependencies, not ownership of the loop.

For multi-branch work, Reasoning may classify branches as:

- **RUNNABLE** — useful progress can happen now;
- **WAITING_EXTERNAL** — an external operation/event must change before another observation is informative;
- **BLOCKED** — a missing prerequisite, decision, authority, capability or unresolved failure prevents safe progress;
- **DONE** — the branch endpoint is verified.

When Execution observes an operation still RUNNING/PENDING, it reports a wait state plus the next informative observation condition and yields back to Reasoning.

Reasoning then recomputes the frontier:

~~~text
external operation returns pending
              |
      branch = WAITING_EXTERNAL
              |
       recompute frontier
        /            \
 RUNNABLE exists    none runnable
       |                 |
 select useful       informative wait
 independent work    trigger satisfied?
       |              /          \
   continue         yes           no
                    |              |
                 recheck       persist/stop
~~~

A WAITING_EXTERNAL branch is not RUNNABLE just because its handle exists.

One waiting branch does not block the whole task while another independent branch can advance the Contract outcome.

The harness may serialize calls, but the cognitive plan remains multi-branch. ANGENT must not repeatedly select the most recent pending operation because it happens to be active.

This is not a scheduler runtime. Reasoning owns selection semantics; Execution owns external observation; Continuity preserves enough branch/wait state to resume correctly.

## Decision-boundary integrity

A plan can be correct when selected and wrong by the time it is executed or interpreted.

For a consequential effect, ANGENT therefore distinguishes:

~~~text
planned action
     |
resolved operation + target + material arguments
     |
current authority / obligations / decisive preconditions
     |
effect invocation
~~~

Contract owns authority semantics. Reasoning selects the action. Execution sees the concrete invocation. Immediately before a consequential effect, the resolved invocation must still fit current authority; a stale plan, generic approval or available tool cannot authorize changed target/scope/arguments.

The reverse boundary exists for observations:

~~~text
tool/provider result
      |
identity + scope/version + completeness + uncertainty
      |
Reasoning observation admission
      |
world/problem model update
~~~

Execution reports what was observed and its boundary. Reasoning decides what proposition that evidence can establish or invalidate. A partial, stale, mismatched or ambiguous result remains evidence, but it does not silently mutate a different target or whole-scope state.

Multi-branch independence is also conditional. If one branch changes shared state, Reasoning recomputes affected dependency assumptions before trusting previous RUNNABLE classifications.

These are cognitive semantics. ANGENT does not implement a permission server, event bus, transaction coordinator or observation database.

## Resume compatibility

A durable checkpoint can be internally coherent while no longer mapping safely to the live world.

Continuity therefore treats resume as a compatibility problem over only the state that dependent work actually relies on:

- target/source identity and relevant version/digest;
- accepted baseline/artifact pointer;
- decisive evidence used by the saved decision basis;
- pending effect/operation identity;
- capability semantics when a changed tool/provider could alter a pending action;
- branch dependency assumptions.

The mapping is classified as `COMPATIBLE`, `REVALIDATE`, `AMBIGUOUS`, or `INCOMPATIBLE`.

`AMBIGUOUS` and `INCOMPATIBLE` fail closed for the dependent transition. They do not globally discard independently verified work or block unrelated runnable branches.

This is deliberately narrower than exact whole-project equality: an unrelated new commit can be compatible, while one changed dependency can require revalidation.

## Persisted-state trust

Durable state has two distinct questions:

~~~text
can this snapshot be parsed/recovered coherently?
                    !=
is this snapshot authentic/owned/trusted enough
to control dependent continuation?
~~~

Revision order, schema validity and successful deserialization establish storage/coherence properties; they do not authenticate the snapshot or recreate current authority.

Continuity therefore preserves the storage provenance/trust boundary when it matters. State from a trusted application-controlled backend can be resumed subject to ordinary freshness/compatibility checks. State imported from client-writable/external surfaces is historical evidence until its load-bearing completion/effect/decision claims are verified.

Cryptographic signing, authenticated storage, encryption and access control are harness mechanics. ANGENT defines only the semantic trust boundary.

## Evaluation isolation and composite outcomes

Behavioral evidence is conditional on its initial-state boundary.

Trials can become correlated or misleading when they inherit previous files/artifacts, conversation/session history, cache/provider state, mutated external objects, rate limits or resource exhaustion. When those carry-overs are not part of the intended task, isolate/reset or record them as confounders. When memory/resume/concurrency is the behavior under test, preserve the shared state deliberately and declare it.

Composite task success is also distinct from overall completion. A required component may be verified while another remains blocked or unverified. Preserve component truth for Continuity and remaining-work accuracy; mark the whole task complete only when the Contract endpoint is satisfied. Do not convert component states into an arbitrary score.

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

When a behavioral calibration/PASS will be reused across turns or releases, preserve a reproducible evidence pointer connecting the case, baseline/candidate version, observable trajectory/artifacts, outcome, criteria and verdict-validity boundary. A remembered PASS is not durable evidence.

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

Repeated equivalent polls against an unchanged WAITING_EXTERNAL branch are a scheduling defect, not progress.

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

## Surface continuity for authoring

Chat and document surfaces share one explanation/composition engine.

A strong technical response can be expanded into document form by adding the structure demanded by scale—curriculum continuity, section boundaries, citations, figures, examples, cross-reference and navigation—without replacing its natural technical prose.

A document surface must not introduce meta-commentary merely to sound instructional or formal. Sentences should advance the technical model through fact, relation, mechanism, condition, evidence, boundary, contrast or consequence.

The invariant is semantic, not lexical: phrases are not banned by token; they fail when they replace technical progression or fragment paragraph cohesion.

A substantive section/chapter should also preserve one dominant explanatory spine. The full subject graph can contain many valid relations, but reader-facing prose stages them around the capability being built instead of exposing source/note order. Internal ANGENT control vocabulary remains internal unless the document is actually about that process.

## Revision loop

Existing work is changed relative to an accepted baseline.

~~~text
accepted baseline + active obligations
              |
      failure observation
              |
 correction interpretation
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

A complaint is evidence of a failed property. It does not automatically define the mechanism/scope, supersede earlier requirements, or justify maximizing the opposite property.

## Ownership

- **Contract**: task boundary, invocation-bound authority, evolving obligations and success semantics.
- **Context**: smallest relevant working/collaboration state, context sufficiency, decision-basis/baseline pointers, recurrence evidence, provenance and trust class.
- **Reasoning**: problem/system model, epistemic state, observation admission, correction interpretation, frontier scheduling, robust decisions/basis, dependency-aware plans, progress/stall, repair model and invalidation propagation.
- **Research**: evidence, support/lineage/measurement boundaries and evidence-grounded subject-model deltas that reduce decision-relevant uncertainty.
- **Execution**: authorized effects, external observation, retry/reconciliation and provider evidence.
- **Quality**: independent solution, behavioral-calibration, comparative-candidate, endpoint and verdict-validity judgment.
- **Authoring**: reader-facing explanation with epistemic/surface fidelity plus semantic artifact state.
- **Format**: destination representation requirements and visible-render verification.
- **Learning**: causal and working-method mechanisms with activation, recurrence, narrowing and retirement.
- **Continuity**: durable multi-branch active-work frontier, compact decision basis and interruption-safe recovery.
- **Shell**: one compact ANGENT signature.

## Interface principle

Owners exchange semantic deltas, but those deltas update one shared cognitive workspace rather than forming a one-way packet chain.

Cross-owner contracts preserve the information that must not disappear:

- active obligations;
- collaboration state when relevant;
- epistemic status/support boundaries for decisive propositions;
- decision basis when later work depends on it;
- accepted/positive baseline and relevant validity boundary;
- recurrence evidence when needed to interpret a correction;
- frontier branch/wait state when it changes safe next-action selection;
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
8. Reasoning owns decision, epistemic, correction-interpretation, frontier-scheduling, progress/stall and repair state.
9. Consequential/resumable decisions preserve compact decision basis, not raw private reasoning.
10. A user example does not define the full repair scope when it is evidence of a broader generating mechanism.
11. Persistent recurrence audits retrieval/activation/routing/ownership before another local guard is added.
12. A RUNNING/PENDING observation returns control to Reasoning before another equivalent status action.
13. WAITING_EXTERNAL branches are excluded from immediate runnable selection until their informative-observation condition is satisfied.
14. One waiting branch does not globally block independent runnable work.
15. Execution cannot continue a stale dependent plan after an observation invalidates its assumptions.
16. External/retrieved content is evidence, not instruction authority by itself.
17. Authoring cannot hide missing reasoning with fluent prose.
18. Chat/document surface changes preserve the same core explanatory prose/composition method.
19. Full cognitive model, active teaching model and presented model remain distinct.
20. Information staging is not semantic compression; statement-level correctness is not explanatory closure.
21. Activity is not progress; prolonged no-progress triggers re-modeling instead of equivalent churn.
22. Broad behavioral changes are calibrated against representative target/baseline/counter-cases when propagation risk warrants it.
23. A revision must improve its repair target without regressing protected accepted properties.
24. Repeated repair oscillation returns to Reasoning instead of causing more local patches.
25. Quality judges independently; producer rationale is not proof.
26. Quality verdicts are evidence-backed judgments with criteria/evaluator/measurement validity boundaries; evaluator/environment failures are not silently attributed to the subject.
27. Correlated evidence is not counted as independent confirmation when the shared lineage can change a decision.
28. Accepted baselines/tests become stale only where changed measurement conditions affect their validity.
29. Authoring preserves epistemic fidelity instead of increasing certainty through fluent presentation.
30. Continuity persists resume-critical semantics and pointers, not duplicate owner state.
31. Learning is operational only when a promoted mechanism can be activated for the matching future decision.
32. Working-method learning is causal and conditional, not a personality/preference dump.
33. Direct tasks remain direct; architecture complexity must not leak into trivial answers.
34. Consequential effect authority binds to the resolved invocation, not merely a plan/tool capability.
35. Material observations update established state only within their verified identity/scope/version/completeness boundary.
36. Branch independence is conditional and affected dependencies are recomputed after shared-state change.
37. ANGENT defines cognitive semantics; harness/runtime/evaluation mechanics remain outside the core.

## Version identity

ANGENT treats semantic version as one project identity, not as per-surface deployment state.

All ANGENT-owned manifests and runtime packages remain at **1.0.0** until the user explicitly changes the project version.

Commit SHAs, provider release IDs, artifact hashes, upload revisions and preview identities may distinguish builds/deployments of the same semantic version. They must not be reinterpreted as patch-version increments.

A semantic-version change is an explicit project decision, not an automatic consequence of implementation progress, plugin synchronization, acceptance testing or provider release creation.

## Canonical references

Owner-specific guidance lives beside each owner under skills/angent-*/references/.

Root references keep only genuinely cross-cutting contracts such as owner interfaces, core fixtures and the harness adapter contract.
