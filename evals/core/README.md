# Core behavioral case extension

These cases complement the authoring/report cases and the existing root calibration fixtures. They target live-core reliability: cognitive quality on short qualified prompts, context freshness, retrieval bounds, root-cause evidence, task frontier scheduling, provider outcome verification, Learning transfer and native-versus-fallback routing.

The same neutral comparator can validate reviewed baseline/candidate observations:

    python3 scripts/evaluate_authoring.py --cases evals/core/cases.json
    python3 scripts/evaluate_authoring.py --cases evals/core/cases.json --runs /path/to/core-review.json

Without observed outputs the result must remain NOT_YET_VERIFIED. This catalog is not a new core owner, orchestration runtime or synthetic scoring platform. Run representative positive and negative controls only when the change could affect those capabilities; do not require every skill to activate on each request. Preserve release/model/host/input identity and real output references when reviewing. The fixture prompts do not themselves prove the behavior.
