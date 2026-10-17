# First Hub/Core upgrade: frozen behavioral inputs

`cases.json` embeds sanitized synthetic initial contexts, allowed observations,
constraints and endpoint oracles. These are candidate tasks, **not model runs**.
They remove missing-input ambiguity from the broad Core/Authoring catalogues;
they do not replace that wider corpus or prove all specialists competent.

For each trial, use a fresh session with the same model settings, host/tool
surface and complete case input. Load the actual baseline/candidate source or
installed plugin with identifiable provenance. Supply only `input` to the agent;
keep `criteria` and `oracle` with the reviewer. A simulated host result is a
fixture observation, never evidence of a live provider or rendered destination.
When history or resume is the subject, preserve exactly the shared state declared
by that case. Do not let another trial's output become input.

Save complete observable answers/actions and checks outside Git. Record source,
model, host/settings, case-file digest, output identity, evidence boundary and
reviewer. Use the existing comparator:

```sh
python3 scripts/evaluate_authoring.py --cases evals/upgrade/cases.json
python3 scripts/evaluate_authoring.py --cases evals/upgrade/cases.json --runs /path/to/reviewed-runs.json
```

For `input_ref`, identify the exact frozen input plus any authorized fixture
observations, not a prompt title. Compare positive, negative and transfer cases;
report residual failures alongside gains. Independent or partly blinded review
is needed for consequential prose judgments. No run file ships here, so the
expected current result is `NOT_YET_VERIFIED`. This agent session is not an
isolated matched baseline/candidate trial.

Before broad release, expand actual runs to early/middle/late curriculum units,
unseen subjects, all distinct specialist families, compaction/worker paths and
real editable/rendered destinations. Source and deterministic helper tests cannot
close those gates.
