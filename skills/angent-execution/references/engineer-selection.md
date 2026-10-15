# Engineer source selection — one ANGENT plugin

ANGENT publishes **one** installable plugin with both Core and the portable 103-Skill Engineer catalog. Engineer remains a separate **source-maintenance module** at `extensions/angent-engineer/`. The deterministic package builder `scripts/package_unified.py` projects those Skills into the same top-level `skills/` root as Core, preserves original Engineer source/support files for relative references, and omits the nested installable plugin manifests.

There is one user-facing plugin identity, `angent`, one plugin version and one package. The internal `extensions/angent-engineer/source-manifest.json` in the distribution is only catalog metadata for read-only selector validation; it is not a second plugin.

## Native-first capability selection

The two **capability providers** remain:
1. officially usable AgentKit Engineer in the active harness;
2. portable Engineer Skills bundled with ANGENT.

Determine native usability from **current harness discovery/invocation evidence**, never from `ak` binary presence, a cache, a version number or old memory. Let `native_usable = yes | no | unknown`.

- **yes:** select native Engineer for the engineering task and do not mix in fallback workflows.
- **no or unknown:** use the corresponding `ak-*` Skills already bundled in ANGENT.
- **missing or invalid fallback:** do not pretend support exists; the selector reports BLOCKED when fallback is required.

This is **routing**, not an install/uninstall operation. One plugin remains installed in every case. The read-only `extensions/angent-engineer/scripts/select_engineer.py` still checks the exact 103 Skills, 16 role identities, ledger and catalog fingerprint in source and in the assembled plugin. Its report is structural evidence, not proof every provider or skill works in each harness.

## Static discovery limitation

Agent Plugins v1 discovers the top-level `skills/` tree statically. It cannot conditionally hide the fallback catalog when a separate native AgentKit installation is also visible. Thus **packaging unity does not mean runtime catalog exclusivity**. Root/Execution must choose one provider per task and reject hybrid workflows; any host that offers conditional skill filtering may additionally hide the unselected catalog. Never claim the single ZIP guarantees collision-free co-installation with native Engineer on every client.

The bundled `ak-*` identities avoid replacing ANGENT Core Skills. A deliberate comparison may inspect both sources, but production task execution must not mix their helper assumptions and generations.

## Role and harness boundary

The 16 files in `extensions/angent-engineer/agents/` are portable role contracts, not 16 automatically spawned agents. A harness may project them into supported native agents, one-shot delegation or sequential reasoning. No generic broker or separate AgentKit CLI requirement is introduced.

Source installation from a raw repository checkout is **not** equivalent to installing the assembled plugin: the canonical consumer artifact is `dist/angent-unified.zip`. To test installed behavior, inspect that artifact and the active host's actual discovery state.
