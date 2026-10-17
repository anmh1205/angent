# ANGENT Hub — capability coordination

ANGENT Core remains the only cognitive authority. Hub is a **small routing contract and generated catalogue**, not an independent agent, runtime, message bus or second decision system.

A kit is maintained under `extensions/<id>/`, with its own `extension.json` and optional `adapter/` rules. A build scans manifests and produces `hub/registry.json` in the **package only**, not as committed mutable state. The registry records actually packaged skills, optional roles, capability identifiers and their source. Multiple extensions may provide the same capability; the Core selects by genuine applicability, availability, evidence and the user's authority.

**Kit adapters** interpret external kit methods and their native/fallback constraints. **Host adapters** under `platforms/` expose actual platform mechanisms. Neither is allowed to replace Contract, Reasoning, Execution, Quality, Continuity or Learning. Use `routing.md` for the coordination policy and `extension.schema.json` for the manifest contract.

Do not paste an upstream kit's global system prompt into ANGENT. Imported documents are specialist guidance under ANGENT, and scripts/tools require independent authorization and runtime verification.

## Onboarding

1. Review license, origin, scripts, tool side effects, references and actual specialist value.
2. Place maintained source in one `extensions/<id>/` directory; preserve attribution.
3. Add `extension.json` with declared source counts, optional roles and semantic capabilities pointing to real Skills.
4. Describe only kit-specific differences under `adapter/`. A direct Skill may need no custom adapter code.
5. Run packaging and Hub tests, inspect generated registry and available Skill inventory in every host. Validate behavioral routing and real host activation before release.

**Do not** change `scripts/package_unified.py` merely to register another ordinary Skill-based kit. A novel runtime integration may require a deliberate Host Adapter implementation.

## Method contracts and gradual migration

Manifest v1 remains supported. Manifest v2 adds `methods`: bounded cards with
an entry, intent summary, semantic capabilities, several soft domain labels,
aliases, invocation condition, outputs and load-bearing requirements. Kit
identity owns attribution/update boundaries; a semantic capability may have
multiple methods, even within one kit. A method card is descriptive data,
not an executable tool grant or a replacement for reading the selected method.

The initial v2 migration declares 17 Engineer methods and Frontend's method.
Other published entries stay searchable with `inspect-required` contracts;
their output/invocation/runtime conditions must be read in source before use.
Do not interpret missing metadata as automatic invocation or no requirements.
The port ledger remains the owner of per-source semantic parity/degradation;
the cards describe selection, not runtime certification.

Packaging generates `registry.json`, `catalog.md`, one small JSON card per
published method and `bindings.json`. None is committed as a second registry.
Bindings resolve methods and roles relative to the actual packaged Hub folder,
including internal gateway and broad CLI layouts. With local Python access,
`discover.py --query "architecture advice"` returns a bounded lexical shortlist;
`--method ak-advise` inspects one exact card. Neither executes a method.
Browser-only hosts can read the global catalogue and selected card/binding.
Native tool search does not implicitly index these filesystem resources.
