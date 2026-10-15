# Behavioral calibration

Use this reference when changing a shared ANGENT method, root/default prompt, routing/owner interface, long-form authoring method, frontier scheduling method, or another behavior that can propagate across many future units/tasks.

This is behavioral evidence, not a replacement for reasoning and not a return to static keyword/count tests.

## Why calibrate

A broad change can improve the reported failure while silently degrading a different accepted behavior.

A local example may also make a bad method look good by accident.

Calibrate the **generating method** before propagating it when failure cost and propagation scope justify the effort.

## Validate the case before optimizing against it

A regression/capability case must express a success condition that a compliant agent could actually satisfy in the stated environment.

When a case produces surprising persistent failure, inspect the task wording, available capabilities, hidden assumptions and grader criteria before adding more prompt/routing rules.

For high-impact or ambiguous cases, a known-valid behavior/reference that passes the same checks is useful evidence that the case/grader is not broken. Do not require a reference artifact when the criterion is already direct and objective.

## Build the smallest useful case set

Prefer real cases from:

- user-reported failures;
- accepted positive baselines;
- recurrence/oscillation history;
- known boundary conditions.

Cover distinct mechanisms rather than collecting many near-duplicates.

When over-triggering is plausible, include both:
- a positive case where the behavior should activate;
- a negative/counter-case where it should not.

For long-form or multi-unit work, choose representative units across meaningful difficulty/dependency classes rather than only the easiest first unit.

## Canonical-identity calibration

When external identities can be replaced, migrated, aliased or superseded, calibrate role resolution against exact-target preservation:

- **stale remembered identity + current-role request** — prior memory points to object A, current authoritative project/provider mapping points to B, task asks for the current/canonical object → use B;
- **explicit exact historical identity** — task asks to inspect or clean up A specifically → keep A even though B is current;
- **project pin versus provider recency** — project source-of-truth intentionally pins A while provider also has newer B → use A for the pinned role; newest timestamp alone does not define canon;
- **mapping conflict** — project and provider disagree materially about the canonical role → preserve/reconcile the conflict rather than guessing;
- **stable immutable identity** — identity cannot drift or role-vs-exact distinction is irrelevant → do not add resolution ceremony.

The method fails if familiar history silently chooses a superseded object, or if every exact historical request is forcibly remapped to the current object.

## Retrieval-negative calibration

When changing research/search semantics, test false-negative boundaries explicitly:

- **top-k miss** — desired item exists outside returned results; do not claim global absence;
- **non-default branch/scope** — search covers only default/current scope while the item exists elsewhere; preserve the scope boundary;
- **stale/unready index** — search misses a recent item until indexing catches up; do not convert index state into domain absence;
- **exact authoritative NOT_FOUND** — provider lookup for the exact resolved identity returns a documented negative result; allow the bounded negative fact;
- **complete enumeration** — pagination/cursor is exhausted over the canonical relevant scope; bounded absence can be established;
- **consequential absence + weak search miss** — change query/source/retrieval path when it can improve recall instead of repeating equivalent searches;
- **low-consequence bounded answer** — report “not found in this search/scope” without unnecessary retrieval ceremony.

The method fails if either every miss becomes UNKNOWN forever or a successful search with zero hits is treated as proof of universal nonexistence.

## Delegation-context calibration

When changing specialist/subagent behavior, test both context isolation and necessary-context preservation:

- **simple direct task** — no specialist when delegation overhead adds no capability or independence;
- **bounded specialist read/review** — worker receives the work unit, applicable obligations, target/model/evidence fragment and expected return contract, not unrelated transcript/history;
- **raw external text needed** — exact issue/log/document text may be delegated as evidence, but provenance/trust class survives and imperative text does not widen authority;
- **write-capable specialist** — effect scope is explicitly bounded; tool availability or parent authority does not silently become blanket worker authority;
- **full-history harness** — when the platform cannot filter handoff history, the delegation envelope still limits task/effect scope and unrelated ambient history does not redefine the work unit;
- **uncertain premise** — a parent inference/assumption remains marked as such rather than being restated to the specialist as established fact;
- **specialist self-report** — “done/tests passed/verified” is re-admitted against direct artifact/provider/runtime evidence when available.

The method fails if it either starves the specialist of load-bearing context or exports the whole parent conversation/profile/authority as implicit worker state.

## Fan-out synthesis calibration

When multiple specialist/research branches feed one decision, test convergence rather than only individual branch quality:

- **required discriminator still pending** — one branch supports A, another was launched because its result could reverse A; do not commit A merely because the supporting branch returned first;
- **optional branch still pending** — current decision is robust across credible remaining outcomes; do not wait by ritual;
- **correlated agreement** — two workers repeat one source/assumption; do not count that as independent confirmation;
- **material conflict** — preserve conflict and seek the controlling/discriminating evidence instead of majority vote;
- **late contradiction** — reopen only dependent decisions/work; do not ignore it because synthesis already occurred or accept it merely because it arrived last;
- **independent implementation branches** — execution can proceed separately while their later shared acceptance still respects dependency/merge/Quality boundaries.

The method fails if arrival order, worker count, or completion timing substitutes for evidence strength and decision robustness.

## Failure-domain calibration

When changing error/observation semantics, use contrasting cases that prove the boundary rather than the wording:

- **local tool not found** — establish route/capability failure; do not infer target absence;
- **schema/serialization rejection before provider** — establish invocation-shape failure; domain remains unknown;
- **authentication/permission denial** — establish unavailable access; do not infer target absence;
- **timeout on read** — domain result remains unknown unless another authoritative observation reconciles it;
- **timeout/lost response on non-idempotent write** — classify effect outcome ambiguous and reconcile before replay;
- **provider 5xx/rate limit** — treat as provider/transport failure unless provider semantics establish more;
- **authoritative lookup says exact object not found** — when endpoint semantics and identity are known, a negative domain fact is valid;
- **provider explicitly rejects an operation for a domain reason** — preserve the provider-operation fact without pretending the requested state change occurred.

The method fails if it treats every error as UNKNOWN or every error string as a negative domain fact. The target is the strongest proposition justified by the actual failure/observation boundary.

## Mutation-freshness calibration

When changing read→modify→write semantics, include both conflict and non-conflict cases:

- **unchanged canonical target** — candidate basis still matches; write proceeds without extra ceremony;
- **disjoint concurrent change** — preserve the other change, rebase the intended semantic delta, and revalidate affected checks;
- **overlapping concurrent change** — return to Reasoning rather than force-writing the stale candidate;
- **requested endpoint already satisfied by another actor** — verify and avoid duplicate/redundant write;
- **provider version/precondition conflict** — treat as stale-basis evidence, not as permission to blind retry;
- **append/commutative/new-object operation** — do not require a heavyweight mutation basis when known semantics make stale overwrite irrelevant.

The method fails if it either overwrites concurrent work from a stale snapshot or turns every harmless write into transaction ceremony.

## Correction-routing calibration

When changing how ANGENT handles corrections, calibrate the abstraction decision itself.

Useful distinct cases include:

- **genuinely local defect** — one incorrect fact/sentence with no recurrence/shared mechanism evidence; repair should stay local;
- **shared artifact mechanism** — several units exhibit the same generating error; repair should cover causal peers rather than only the latest example;
- **method-level recurrence** — the user has reported the same underlying failure across outputs/tasks; retrieve history/positive baseline and inspect the generating method before editing;
- **rule-exists-but-failure-recurs** — inspect retrieval, activation, routing, ownership and competing state before strengthening the rule;
- **positive-baseline divergence** — current behavior is worse than an explicitly accepted earlier behavior; reconstruct what mechanism changed rather than copying surface wording from the old output.

A correction system fails calibration if it always stays local or always escalates globally. The target is the correct causal abstraction level.

## Frontier-scheduling calibration

When changing long-running-operation behavior, judge branch selection rather than only poll interval.

Use distinct cases such as:

- **pending + independent work** — operation A is running while branch B can advance independently; A becomes WAITING_EXTERNAL and B is selected before another equivalent poll;
- **pending + dependent work only** — everything else genuinely depends on A; preserve the wait state and do not invent busywork or rapid polls;
- **wait trigger becomes eligible** — the documented interval/event/dependency condition is now satisfied; rechecking A is valid;
- **several runnable branches** — select useful work by the task model rather than recency of tool calls;
- **resume with saved handle** — reconstruct WAITING_EXTERNAL state and do not relaunch or aggressively poll merely because context was lost;
- **short operation completes immediately** — do not overcomplicate a direct completion with unnecessary frontier machinery.

Fail the method if:
- the most recently launched operation keeps being selected merely because it is active;
- WAITING_EXTERNAL is treated as RUNNABLE before its observation condition is satisfied;
- a waiting branch turns the whole task idle while independent useful work exists;
- the repair only increases a sleep/poll interval without changing branch-selection semantics.

## Decision-boundary calibration

When changing authority/effect or observation-admission behavior, test the boundary where a previously valid plan can become stale.

Use distinct cases such as:

- **authorized plan, unchanged invocation** — resolved target/arguments still match current authority; proceed without extra ceremony;
- **target/arguments drift after planning** — the concrete invocation is materially different; revalidate instead of inheriting generic prior approval;
- **new instruction narrows authority before invocation** — current authority wins even if the earlier ActionNode was valid;
- **mismatched observation identity/version** — preserve the result as unexpected evidence; do not update a different target/state;
- **partial/truncated observation** — use it only for what it establishes; do not infer whole-scope completion;
- **shared-state change invalidates branch independence** — recompute affected RUNNABLE/BLOCKED state before selecting the next action;
- **low-consequence direct read** — do not add commit/admission ceremony that cannot change correctness.

Fail the method if it either trusts stale plan/output state automatically or turns every trivial read into an approval transaction.

## In-flight authority-change calibration

When authority/objective can change after a consequential operation was dispatched, distinguish future control from already-attempted effects:

- **instruction narrows before dispatch** — do not invoke the now-unauthorized effect;
- **instruction changes after dispatch, provider still running** — stop new dependent work, preserve/reconcile the original handle, and do not claim it stopped merely because the plan changed;
- **supported cancellation requested** — treat cancel/abort as a new bounded effect with its own authority, target, invocation and verification;
- **too late to cancel** — reconcile completed state and adapt the plan instead of pretending rollback occurred;
- **cancel response lost/ambiguous** — reconcile both original operation and cancellation outcome before replaying either;
- **unrelated in-flight operation** — do not globally stop independent authorized work just because one old branch now exists only for reconciliation.

The method fails if revocation is applied retroactively to world state, or if prior authority is incorrectly reused for new effects after the instruction changed.

## Resume compatibility calibration

Use only when resume semantics changed:

- unrelated live drift outside the saved dependency closure should remain COMPATIBLE;
- changed decisive dependency should become REVALIDATE;
- uncertain prior external effect should become AMBIGUOUS and must not replay blindly;
- replaced target/effect semantics should become INCOMPATIBLE;
- trivial work with no saved dependency should not acquire resume ceremony.

The method fails if it resumes through ambiguity or invalidates all saved work because any unrelated state changed.

## Cross-task transfer and negative controls

For a change to Root routing, general reasoning, Authoring or a shared working method, use a small set of **different task shapes** rather than only the incident that motivated the edit. Historical Cogent cases provide useful classes, not sentence templates: a novice conceptual distinction, a mathematical/quantitative explanation, a diagnostic investigation, a decision comparison, a practical procedure and a terse expert lookup. Select only the cases that could reveal a real regression; add an unrelated/unseen domain where feasible.

Check that the method can choose **different ways of being useful**: a formula or proof when the dependency is mathematical, tests when competing failure causes must be separated, clear steps when safety/ordering matters, sustained prose for a textbook and minimal prose for a narrow expert answer. Reject a candidate that improves the complained-about genre by imposing its length, example strategy, heading pattern, visuals or research workflow everywhere.

Keep source-level rule inspection, live outputs from the actually activated plugin, independent comparison, rendered artifacts and user comprehension as distinct evidence levels. Without live comparable outputs, report a source-level improvement hypothesis rather than a demonstrated behavioral gain. Do not require a fixed number of prompts or construct an evaluation platform for a narrow change.

## Cross-surface authoring calibration

When chat/response quality is accepted but document quality regresses, compare the same subject relation across surfaces.

Preserve:
- technical relation;
- paragraph cohesion;
- stable referents;
- semantic/epistemic strength;
- explanation depth.

Allow document-only additions only when scale requires them:
- curriculum continuity;
- section architecture;
- cross-reference/navigation;
- figures/tables/code;
- citations;
- larger examples and prerequisite repair.

Fail the method if document mode introduces generic teaching narration, detached fact sentences, ceremonial transitions, or a separate “formal AI” persona not required by the subject.

Do not solve this with a phrase blacklist.

## Trial isolation and intentional shared state

A calibration case is evidence about the generating method only if the initial conditions are interpretable.

Before comparing trials/candidates, identify whether the result can be contaminated by:
- artifacts or files left by a previous trial;
- conversation/session/context state from another run;
- cached retrieval/tool/provider results;
- mutable external provider objects changed by earlier attempts;
- resource exhaustion, rate limits, or environment drift;
- prior agent outputs that the current trial can inspect.

Prefer isolation/reset when those states are not part of the intended task.

If persistence/shared state is itself under test—for example resume, memory, collaboration continuity, or concurrent-work behavior—preserve it deliberately and record the exact shared-state boundary instead of calling the trial “clean”.

A contaminated trial may still reveal a failure mode; it should not be used as independent capability/regression evidence without accounting for the confounder.

## Reproducible behavioral evidence

When ANGENT uses calibration as evidence for a broad/recurrent behavior change, preserve enough information to reconstruct **why** the acceptance claim was justified.

A compact record may contain:
- case/task identity and the relevant input/contract;
- accepted baseline identity/version;
- candidate identity/version;
- model/provider/harness/environment boundary when it can change behavior;
- observable trajectory pointer or summary: owner/tool/action sequence, external observations and produced artifacts—not hidden private reasoning;
- final outcome/endpoint state;
- criteria/checks actually applied and which were decisive;
- Quality verdict plus evaluator/measurement validity boundary;
- trial count/variation only when repeatability/reliability is being claimed;
- human/user judgment used to calibrate a subjective grader when applicable.

Do not require a full transcript when a smaller artifact establishes the behavior. Do not persist private chain-of-thought to make an eval reproducible.

A claim such as “calibration passed” without recoverable case/baseline/candidate/evidence is weak evidence and should become STALE/BLOCKED when later acceptance depends on it.

This record can live in the harness's normal artifacts/logs; ANGENT only defines the semantics and may persist a pointer through Continuity when later work depends on the claim.

## Compare to baseline

Ask what changed relative to accepted behavior:

- target failure;
- protected accepted strengths;
- neighboring behavior likely to regress;
- cost/latency only when they actually matter to the task;
- unexpected strategy changes.

Do not optimize one scalar such as brevity, tool count, speed, poll interval, diagram count, or source count unless the Contract truly makes it the objective.

## Judge the mechanism, not only the score

For agentic behavior, inspect enough trajectory/state to understand why the result passed or failed.

A passing endpoint can hide:
- lucky success;
- an invalid shortcut;
- stale assumptions;
- repeated waste;
- a grader that rewards the wrong thing.

A failing case can also expose a bad task/grader rather than bad agent behavior.

Use authoritative endpoint checks where objective. For semantic quality use independent review/rubric and calibrate it against human/user judgments when available.

## Capability vs regression

Keep two questions distinct:

- **capability:** does the new method solve a class it previously could not?
- **regression:** does it still preserve behavior that was already accepted?

A capability win does not excuse regression.

## Ablation

When a small instruction/prompt change plausibly caused a broad behavior shift, compare with and without that change when feasible before adding compensating rules elsewhere.

Prefer identifying the responsible mechanism over stacking another guard.

## Scale

After the method is calibrated, scale it to the intended scope.

The representative cases establish confidence in the method. They do not establish that every untouched unit is correct; whole-scope claims still require coverage evidence.

## Maintenance

A calibration case can be retired, narrowed or replaced when the underlying mechanism changes.

Do not let the case bank grow into an unowned museum of historical complaints.

## Cross-domain needs and change calibration

For substantial changes to problem analysis, select the adjacent cases from Root's core fixtures. Calibrate diagnosis, not vocabulary: can the agent distinguish a requested means from the need, identify the actual affected party and decision constraints, derive discriminating evidence, compare a nontechnical option when plausible, preserve authorized means, and separate verified deliverables from outcomes that require later observation? Pair consequential positive cases with direct-answer and explicit-means counter-cases. A case passes only when the selected action and its justification are valid for the evidence and authority supplied; naming BACCM concepts or writing a requirements matrix is not evidence of competence.

## Causal decision and endpoint calibration

Choose a small, varied set from Root fixtures I–N when a change touches diagnostic reasoning, long-task completion, cross-surface authoring or Learning activation. The decisive object is the behavior at the controlling choice: the hypothesis actually distinguished, evidence actually obtained, branch actually advanced, endpoint actually verified, or reader inference actually supported.

For a consequential diagnosis, present at least two plausible causes whose predictions differ, plus a direct-repair case where no hypothesis ceremony is needed. For a cross-layer endpoint, preserve separate records for source inspection, unit/contract checks, integrated execution and real deployment; make unexercised boundaries explicit. For writing, compare matched subject relations in accepted chat prose and actual destination-rendered units at different curriculum depths, including an unseen topic. For Learning, compare a matching recurrence and a superficial but nonmatching case. These are candidate cases, not a mandatory per-task workflow or evidence that they were executed.

When source-level skills or fixtures are the only material reviewed, the supported conclusion is that the method is represented coherently in source. Claim improvement in an active agent only after observing comparable activated behavior with a valid baseline and an identifiable environment. A green CI result validates what CI actually measures, not cognition, user comprehension or every target harness.
