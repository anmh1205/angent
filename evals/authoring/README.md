# ANGENT authoring and report behavioral evaluation

The case catalog contains realistic writing, report, explanation, continuity and skill-routing tasks, with positive cases and negative controls. They are task descriptions, **not outputs from a model** and not evidence of model performance.

Run source/schema and comparator tests:

    python3 -m unittest discover -s tests -p 'test_authoring_eval.py' -v
    python3 scripts/evaluate_authoring.py

Without runs, the tool returns NOT_YET_VERIFIED. This is the expected honest state.

## Reviewing real outputs

Run each selected task with the released baseline and proposed candidate in genuinely comparable model/harness environments and frozen task context. Do not substitute an unactivated source text for a plugin invocation. Save distinct output references (published document or chat transcript links, sanitized where needed). If a destination is Notion/Docs, review the actual rendered output, not only block-write acknowledgement. Record the matched input reference for both executions.

Prepare an external JSON review file:

    {
      "schema_version": 1,
      "trials": [
        {
          "case_id": "chat-short",
          "baseline": {
            "identity": "actual-baseline-release",
            "model": "actual-model",
            "host": "actual-host",
            "input_ref": "same-frozen-input",
            "output_ref": "actual-baseline-output",
            "ratings": {
              "correct": {"verdict": "PASS", "evidence": "concrete passage and why"},
              "economy": {"verdict": "FAIL", "evidence": "specific unnecessary content"}
            }
          },
          "candidate": {
            "identity": "actual-candidate-release",
            "model": "actual-model",
            "host": "actual-host",
            "input_ref": "same-frozen-input",
            "output_ref": "actual-candidate-output",
            "ratings": {
              "correct": {"verdict": "PASS", "evidence": "concrete passage and why"},
              "economy": {"verdict": "PASS", "evidence": "no irrelevant content observed"}
            }
          }
        }
      ]
    }

Then run:

    python3 scripts/evaluate_authoring.py --runs /path/to/reviewed-runs.json

Reviewer verdicts are PASS/FAIL/UNKNOWN for each case criterion. The comparator rejects duplicate case IDs, missing reviews and non-comparable host/model/input. A single favorable case is not a full-catalog win. The tool records review inputs; it does not grade prose or verify evidence strings automatically. For consequential claims, use independent/partly blinded human review, meaningful user understanding tests and negative controls, then publish only conclusions justified by the observed sample.

Keep private transcripts, provider identifiers and task runtime state out of Git. Preserve only reusable sanitized cases and scripts in source.
