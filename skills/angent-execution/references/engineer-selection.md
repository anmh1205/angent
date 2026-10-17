# Engineer selection and resource resolution

ANGENT has one installable plugin identity. Engineer is maintained under
`extensions/angent-engineer/`; its nested manifest becomes source metadata in
the package. The native product and bundled port are alternative providers.
Hub routing owns selection policy; this reference explains Engineer-specific
observations and the resource boundary.

## Select a method, then establish its provider

Native is usable only when the current harness can discover/invoke the needed
method and its load-bearing runtime facilities. A binary, cached catalogue,
doctor result or success with a different method cannot establish that fact.
The read-only selector reports kit health and a harness-supplied usability
observation; its structural result cannot certify every method.

Use one provider for the bounded work. If it fails mid-operation, reconcile any
uncertain effects before switching. Re-evaluate method/output equivalence: a
portable recommendation is not a deployed change, and sequential work is not
Team's persistent-session lifecycle. Keep native and fallback workflow
assumptions separate even when their task labels match.

## Resolve from the installed artifact

Find the Hub belonging to the active ANGENT origin. Its `bindings.json` maps
method entries and qualified role identities to resource paths **relative to
that Hub directory**. Search bounded metadata with `discover.py` when Python
and filesystem access exist; otherwise inspect `catalog.md`, then the selected
`methods/<entry>.json` card and binding. The global catalogue remains available
when a domain guess misses. Inspect source before using an `inspect-required`
contract; an empty requirement list in such a card means unknown, not no needs.

OpenAI exposes one Root and internal methods; Gemini Web has one imported Root;
broad CLI profiles project Skills into the destination host's directory. A raw
source checkout is a maintenance layout, not proof of the installed layout.
Do not use internal references to bypass a host/user-denied skill or action.

## Roles and activation

The 16 role files are supporting contracts. Reading one creates no worker,
memory backend, messaging channel or process. Project a role only through an
actually available, authorized host mechanism; ordinary single-agent reasoning
needs no role instance. Native/fallback routing does not hide unrelated static
catalogues or guarantee Root activation. Provider discovery and actual execution
need separate observations.
