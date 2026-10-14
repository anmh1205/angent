---
name: ak-find-skills
description: Route to the best installed capability first, or search for an external Skill package and install it only after explicit review and approval.
metadata: {port: angent-fallback, mode: adapted}
---

# Find Skills — Portable Fallback

Use when the needed capability is unclear or may require an external reusable Skill.

## Separate two decisions

1. **Local routing** — choose among capabilities already installed/available.
2. **External discovery** — search a third-party Skill ecosystem when local capability is insufficient and the user actually wants package discovery.

Do not turn a local routing question into an installation.

## Local route

1. Identify the concrete outcome/domain.
2. Inspect current active Skill/plugin/tool inventory.
3. Choose one primary owner; name secondary helpers only for distinct follow-up work.
4. State when a referenced capability is unavailable.

Prefer general assistant capability when the task does not need a reusable package.

## External discovery

When external discovery is requested and the harness can search the relevant registry:
1. use a focused query that excludes secrets/private source;
2. return a small set of candidates with source/owner and inspection link;
3. distinguish search relevance from trust/quality;
4. inspect package instructions/scripts/tools/data boundaries before recommending installation when possible;
5. show the exact package/scope to be installed;
6. wait for explicit approval before the install effect.

Search does not authorize installation. Installation does not authorize later execution against unrelated data.

If no suitable package exists, offer general assistance or `ak-skill-creator` for a recurring workflow.

After installation, verify the actual installed scope/discovery state before claiming the new Skill is usable.
