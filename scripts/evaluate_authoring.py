#!/usr/bin/env python3
"""Validate authoring cases and compare reviewed real model outputs.

This script does NOT run a language model or infer prose quality from keywords.
Without comparable reviewed baseline/candidate outputs, quality is NOT VERIFIED.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "evals" / "authoring" / "cases.json"
VERDICTS = {"PASS", "FAIL", "UNKNOWN"}


class EvaluationError(ValueError):
    pass


def load_cases(path: Path) -> dict[str, dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not isinstance(data.get("cases"), list):
        raise EvaluationError("invalid case catalog schema")
    cases: dict[str, dict[str, Any]] = {}
    for case in data["cases"]:
        cid = case.get("id")
        criteria = case.get("criteria")
        if not isinstance(cid, str) or not cid or cid in cases:
            raise EvaluationError("missing/duplicate case id")
        if not isinstance(criteria, dict) or len(criteria) < 2:
            raise EvaluationError(f"{cid}: expected at least two criteria")
        if not all(isinstance(k, str) and k and isinstance(v, str) and v.strip() for k, v in criteria.items()):
            raise EvaluationError(f"{cid}: invalid criterion")
        if not all(isinstance(case.get(k), str) and case[k].strip() for k in ("genre", "prompt")):
            raise EvaluationError(f"{cid}: invalid genre or prompt")
        if type(case.get("negative_control")) is not bool:
            raise EvaluationError(f"{cid}: negative_control must be boolean")
        cases[cid] = case
    if not cases or not any(c["negative_control"] for c in cases.values()):
        raise EvaluationError("catalog requires cases and negative controls")
    return cases


def reviewed_trial(case: dict[str, Any], name: str, result: Any) -> dict[str, str]:
    if not isinstance(result, dict):
        raise EvaluationError(f"{case['id']}: missing {name} trial")
    for field in ("identity", "model", "host", "input_ref", "output_ref"):
        if not isinstance(result.get(field), str) or not result[field].strip():
            raise EvaluationError(f"{case['id']}: {name} missing {field}")
    ratings = result.get("ratings")
    if not isinstance(ratings, dict) or set(ratings) != set(case["criteria"]):
        raise EvaluationError(f"{case['id']}: {name} rating keys do not match criteria")
    out: dict[str, str] = {}
    for key, rating in ratings.items():
        if not isinstance(rating, dict) or rating.get("verdict") not in VERDICTS:
            raise EvaluationError(f"{case['id']}: invalid {name} verdict for {key}")
        if not isinstance(rating.get("evidence"), str) or not rating["evidence"].strip():
            raise EvaluationError(f"{case['id']}: {name} {key} lacks review evidence")
        out[key] = rating["verdict"]
    return out


def compare(cases: dict[str, dict[str, Any]], data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema_version") != 1 or not isinstance(data.get("trials"), list):
        raise EvaluationError("invalid trial schema")
    results: list[dict[str, str]] = []
    seen: set[str] = set()
    for trial in data["trials"]:
        cid = trial.get("case_id")
        if cid not in cases or cid in seen:
            raise EvaluationError(f"unknown/duplicate case id: {cid}")
        seen.add(cid)
        case = cases[cid]
        baseline = trial.get("baseline")
        candidate = trial.get("candidate")
        before = reviewed_trial(case, "baseline", baseline)
        after = reviewed_trial(case, "candidate", candidate)
        identity = tuple(baseline[k] == candidate[k] for k in ("model", "host", "input_ref"))
        if not all(identity) or baseline["identity"] == candidate["identity"]:
            outcome = "INCOMPARABLE"
        elif "UNKNOWN" in before.values() or "UNKNOWN" in after.values():
            outcome = "UNVERIFIED"
        else:
            regression = any(before[k] == "PASS" and after[k] == "FAIL" for k in before)
            improvement = any(before[k] == "FAIL" and after[k] == "PASS" for k in before)
            if regression and improvement:
                outcome = "MIXED"
            elif regression:
                outcome = "REGRESSION"
            elif improvement:
                outcome = "IMPROVEMENT"
            elif "FAIL" in after.values():
                outcome = "UNRESOLVED_DEFECT"
            else:
                outcome = "NO_CHANGE"
        results.append({"case_id": cid, "outcome": outcome})
    observed = {r["outcome"] for r in results}
    if not results or len(seen) < len(cases) or any(x in observed for x in ("INCOMPARABLE", "UNVERIFIED")):
        verdict = "NOT_YET_VERIFIED"
    elif "REGRESSION" in observed or "MIXED" in observed:
        verdict = "REGRESSION_OR_MIXED"
    elif "UNRESOLVED_DEFECT" in observed:
        verdict = "UNRESOLVED_DEFECT"
    elif "IMPROVEMENT" in observed:
        verdict = "OBSERVED_IMPROVEMENT_WITH_REVIEW"
    else:
        verdict = "NO_OBSERVED_GAIN"
    return {
        "catalog_cases": len(cases),
        "reviewed_cases": len(results),
        "verdict": verdict,
        "evidence_level": "external_reviewed_outputs" if results else "catalog_only",
        "cases": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--runs", type=Path, help="JSON of observed baseline/candidate outputs and reviewed verdicts")
    args = parser.parse_args()
    try:
        cases = load_cases(args.cases)
        data = json.loads(args.runs.read_text(encoding="utf-8")) if args.runs else {"schema_version": 1, "trials": []}
        print(json.dumps(compare(cases, data), ensure_ascii=False, indent=2))
    except (EvaluationError, OSError, ValueError, TypeError) as exc:
        print(json.dumps({"error": str(exc), "verdict": "INVALID_EVIDENCE"}))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
