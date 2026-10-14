# Needs, value and change analysis

This is an optional deep reference for ANGENT Reasoning when the user's work concerns an ambiguous need, a consequential proposed solution, competing stakeholder interests, systemic failure or a change with nonlocal effects. It adapts general business-analysis ideas to any domain. It is not a separate BA agent, an automatic sequence, a required document set or a persistent requirements database. A small direct request stays direct.

## Model the need without usurping the user's decision

Business analysis distinguishes **need** (a problem/opportunity), **change** (a transformation), **solution** (a way to address the need), **stakeholder** (someone affected or invested), **value** (worth in that person's context) and **context** (the circumstances that shape all of these). These are interacting perspectives rather than stages or fields that must all be populated. A different context can make the same solution valuable, costly or unacceptable.

In a consequential case, Reasoning may ask:
- What current condition is established, and what is merely a complaint, prediction or interpretation? Who experiences its effects?
- What would be different if the work succeeds, and for whom? Is the desired outcome directly observable or only indirectly measured?
- What constraints, baselines, risks and decision rights make some attractive options unauthorized or unacceptable?
- Is the named artifact/tool/process a **binding deliverable** or a **candidate means**? Infer this from actual instructions, never from a generic preference for optimization.
- Which contextual change could invalidate the chosen option even when its immediate output passes tests?

Answer only decision-relevant questions. Do not invent business objectives, personas, stakeholders, value functions or baselines. Contract owns what is binding; Reasoning cannot override explicit methods because its analysis found a different optimum.

## Elicit or derive a reliable current state

The observed situation, stakeholder reports, documented rules and inferred causes are different evidence classes. To understand a service bottleneck, inspect time at each handoff rather than equating an individual's proposed fix with the bottleneck. To understand a degraded educational document, trace which prerequisite relation the reader cannot reconstruct rather than treating a request for more pages as proof of the deficit.

Research obtains the needed observations or domain mechanisms. Use available artifacts, actual use traces, interviews or stakeholder feedback **only when those sources exist and are authorized**. Do not describe simulated interviews or data as real. If the decisive unknown is how a system behaves, choose the smallest discriminatory observation. Ask the user when an authority/priority trade-off cannot be inferred safely; otherwise advance work on supported premises, with uncertainty explicit.

Distinguish symptoms from causes. A weak outcome may arise from a missing capability, a misaligned process, a poor interface, conflicting incentives, unreliable measurements or an incorrect specification. An attractive technology choice does not establish that technology is the causal intervention. Test causes against expected observations and negative cases before designing a fix.

## Move from current state to desired value

The useful gap is the change in **capability or outcome**, not automatically the difference between two document inventories. Current state may be a workflow, product behavior, reader comprehension, team practice or visual artifact. Desired state describes what must become possible or improve. For material changes, separate:
- baseline evidence of present performance or properties;
- desired ability, outcome or invariant;
- affected stakeholder interests and their relative decision authority;
- hard constraints and transition or switching costs;
- measurable or inspectable evidence that could establish the intended improvement.

Avoid artificial numeric KPIs. Some outcomes need observational or qualitative acceptance; others need a defined measurement method, comparison window, confound controls and baseline. A polished artifact may meet acceptance criteria without the claimed downstream business benefit being demonstrated.

Stakeholder preferences can conflict. Preserve who made each claim, what supports it, who has authority to choose and what trade-off would expose. Do not average incompatible stakeholder objectives into an invented number or silently substitute the loudest person's preference for the user's contract.

## Compare solutions before committing

Generate distinct options only when the choice is real. At minimum consider a do-nothing or retain-baseline option when opportunity cost and reversibility matter; include a nontechnical/process alternative when the root cause could be organizational. Compare candidate options on shared outcome axes: need coverage, benefits/avoided harms, constraints, operational costs, uncertainty, transition burden, residual risks and reversibility.

Select an option only if its expected effect is supported. An intervention should imply a causal mechanism: which change affects which state, through what relation, and which observation would show the mechanism worked. Prefer a reversible experiment when it can resolve a decision-reversing unknown more cheaply than a large commitment. If the user specified a fixed deliverable, fulfil it; separate any alternative as a recommendation that requires authorization.

A diagram is useful when it exposes a relation that prose would otherwise conceal. Use a process/swimlane model for handoffs and responsibility; state transitions for lifecycle behavior; a concept/dependency graph for prerequisites or impact; a decision table for conditional policy; a matrix for comparable alternatives. BPMN 2.0 or another importable notation requires valid domain semantics and destination verification, not a renamed generic flowchart. No mandatory diagrams, templates or diagram quota.

## Carry meaning through requirements and changes

Requirements are representations of needs; designs represent candidate solutions. Do not collapse the two. For complex work, distinguish purpose/desired outcome, stakeholder obligations, required capabilities and quality, transition constraints, and acceptance evidence. In a personal or creative task, these distinctions can remain implicit.

Traceability is a small **semantic dependency map**, not a requirement to assign IDs to every sentence. Preserve a relationship only when it can answer a live question such as:
- Why does this decision or artifact exist, and what claim/requirement supports it?
- If a constraint or upstream decision changes, which dependent behavior, document, test or stakeholder outcome may become invalid?
- Which requested outcomes have no supporting work or acceptance evidence?
- Which accepted baseline remains protected despite the change?

For a change request, determine which premise changed, inspect the dependency closure, distinguish direct from indirect effects, and revise only affected decisions/artifacts. Preserve unrelated accepted properties and evidence. If a change crosses the existing authorization boundary, return the actual decision to Contract/the user instead of applying the most convenient fix.

The agent does not need a graph database or new state schema to do this. Use existing task context, artifact references and Continuity decision-basis pointers when the relationships matter for correctness or resume. Never store entire private reasoning traces as traceability.

## Validate deliverables and outcomes separately

A solution has at least three possible assertions with different evidence:
1. **Execution completed:** the authorized action/commit/write occurred at the intended target.
2. **Deliverable conforms:** its content, behavior or quality satisfies the relevant accepted requirements.
3. **Need/value improved:** the affected people/system actually experienced the desired benefit or avoided harm.

These assertions may coincide for a tiny task, but must not be conflated for consequential change. A tested dashboard is not necessarily useful to a manager; a published guide has not yet proved shorter service times. Quality evaluates claims at their actual evidence boundary. If adoption or operational benefit is unobservable until later, label it expected or unknown, without erasing verified delivery or inventing measured improvement.

## Application boundaries

- **Operational process:** observe where delay occurs, consider policy/hand-off changes before attributing delay to missing software, compare results using the actual operational baseline.
- **Education or research:** define what a reader should subsequently explain or infer; track concept prerequisites and reasoning links, not topic count or word count.
- **Design/creative revision:** carry approved identity and visual constraints, judge changes against the actual rendering, do not rebrand under a narrow edit request.
- **Repository or product engineering:** reconstruct the live existing architecture and consumers before proposing renamed APIs or new modules; trace migration and regression consequences.
- **Simple fact lookup:** answer the fact. No stakeholder register, gap analysis, mock interview or change program.

## Attribution and limits

This is an independent adaptation of general business analysis practice, not a reproduction of proprietary BA-Kit templates or private instructions. Primary conceptual sources:
- IIBA, The Business Analysis Standard, defining business analysis and the six BACCM concepts: https://www.iiba.org/knowledgehub/the-business-analysis-standard/2-understanding-business-analysis/2-1-defining-business-analysis/
- IIBA, BACCM as a thinking and organizing model: https://www.iiba.org/knowledgehub/the-business-analysis-standard/2-understanding-business-analysis/2-3-using-the-baccm/
- IIBA, needs and solutions versus representations as requirements and designs: https://www.iiba.org/professional-development/knowledge-centre/articles/needs-and-solutions/

These sources establish conceptual distinctions, not empirical proof that any particular ANGENT prompt improves real-world outcomes. Calibrate transfer on domain-specific failure, successful baseline and counter-cases before asserting a general quality gain.
