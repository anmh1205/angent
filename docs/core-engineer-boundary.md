# ANGENT Core and Engineer Skill boundaries

Reasoning establishes the mental model, technical mechanism and decision;
Authoring communicates it to the reader. Research supplies missing evidence
when needed; Format preserves the explanation in requested destinations.
Ordinary explanation is a built-in ANGENT responsibility, not an additional
Engineer specialist Skill invocation.

| Source Skill | ANGENT public discovery | Distinct use |
|---|---|---|
| `ak-explain` | No | Preserved only for maintained AgentKit Engineer parity; Core already owns its explanation/HTML outcome |
| `ak-ask` | Yes | Explicit architecture advisory with alternatives, YAGNI and decision gates |
| `ak-bro` | Yes | Restate the immediately preceding assistant reply, without changing certainty or authority |
| `ak-sumup` | Yes | Bounded post-implementation/delivery recap supported by artifacts and tests |

Choose specialist Skills for an additional outcome, not because a generic
question happens to match their names. An explicit request for the native
AgentKit command may be fulfilled by actual usable native AgentKit; Core's
normal explanation must not be reported as an `ak-explain` invocation.

## Source versus runtime inventory

The Engineer source remains complete: 103 Skills and 16 role contracts. The
central suppression rule in `scripts/package_unified.py` keeps `ak-explain`
source-only. The source/support tree remains present for compatibility.
OpenAI exposes one Root with other Core and registered specialist methods
under internal references. Gemini Web imports one Root and a reference
library. Broad CLI profiles expose Core plus published Engineer and Frontend
methods in their host-specific directories. Generated Hub registry/cards and
`bindings.json` describe the actual artifact; source counts are not callable
Skill counts or evidence of activation.

If updating an already installed personal ChatGPT plugin, remove the old
`skills/ak-explain/` paths explicitly: Plugin Creator preserves omitted
files unless `delete_paths` lists them. Compare the complete installed
provider Skill inventory after updating, not just the ZIP.
