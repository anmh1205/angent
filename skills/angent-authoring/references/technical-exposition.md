# Technical exposition

Technical writing succeeds when the reader can reconstruct the mechanism, not when every relevant fact has been mentioned.

## Start from the technical relation

Before writing a section, identify the relation doing the teaching:

- object and ownership;
- state transition;
- cause → mechanism → effect;
- request/data/control flow;
- layer/interface crossing;
- dependency and constraint;
- contrast between nearby concepts;
- observation → diagnosis;
- configuration → runtime consequence.

The visible prose should make that relation inspectable.

Do not open with generic importance statements when the mechanism can be stated directly.

The full subject model may contain many valid relations. A section should expose one dominant explanatory spine and subordinate source details, side cases and implementation notes to the reader capability being built.

## Concepts need both definition and operation

A concept is not established merely because its name is defined.

For an important technical concept, give the reader enough to answer the relevant subset of:

- what object/abstraction is it?
- who owns or creates it?
- what state/information does it carry?
- when does it participate?
- what does it connect to?
- what observable consequence follows?
- how would I recognize/debug/use it?

The exact subset depends on the chapter.

## Cross-layer explanations

When explaining a path through several layers, keep one stable object/event/value moving through them.

Example pattern:

```text
user operation
→ API/syscall
→ subsystem object
→ driver/protocol operation
→ observable device/result
```

At each boundary explain:
- what representation changes;
- who owns the next step;
- what invariant/assumption is required.

Do not jump from an API name to a hardware/runtime result with the mechanism hidden in one sentence.

## Example ↔ general model

Examples and the general model must support each other.

A good sequence can be:

1. establish the concept/model needed to interpret the example;
2. follow a concrete example through that model;
3. generalize what the example demonstrates;
4. state where the example stops being representative.

Avoid two common failures:
- abstract definitions with no inspectable case;
- one long example that replaces the general concept entirely.

## Code and commands

A code block should expose something exact that prose would make vague.

After code, interpret:
- what part is load-bearing;
- how data/control moves;
- why the shown API/config matters;
- what output or failure to expect.

Do not narrate every syntax token.

For commands, distinguish:
- command;
- observation it produces;
- conclusion the observation supports.

Source paths, API names, logs and exact implementation details are evidence for an explanation; they should not become the section's organizing principle unless the reader's actual task is source/runtime navigation.

## Diagrams

Use a diagram when spatial/flow/state structure would otherwise have to be reconstructed mentally.

Every arrow must mean a real relation.

A diagram needs an interpretation in prose. It should not be inserted because the section “looks text-heavy”.

Mermaid is appropriate for software/data/control/state relations. Use authentic schematics, screenshots, waveforms, photos or source figures when those carry the real evidence better.

## Mechanism before advice

When teaching, explain why before turning the section into recommendations.

“Do X” is not a substitute for understanding:
- what X changes;
- what state it acts on;
- why the alternative fails;
- what evidence verifies the result.

## Closure

A section should close the question it opened at the promised depth.

Do not finish with vague commentary such as “đây là điểm rất quan trọng” or “từ đây có thể thấy sức mạnh của hệ thống”.

Finish with the technical consequence, capability or inference the reader can now use.
