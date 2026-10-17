#!/usr/bin/env python3
"""Read-only lexical candidate lookup over packaged method cards.

No activation, tool probes, permissions, execution or persisted task state.
For semantic mismatches, reformulate or inspect catalog.md across all domains.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[^\W_]+", text.casefold(), re.UNICODE))


def discover(root: Path, query: str, *, explicit: bool = False,
             domain: str | None = None, limit: int = 6, exclude=()) -> dict:
    if not 1 <= limit <= 20:
        raise ValueError("limit must be between 1 and 20")
    terms = tokens(query)
    matches = []
    bindings = json.loads((root / "bindings.json").read_text(encoding="utf-8"))["methods"]
    inspected = 0
    for path in sorted((root / "methods").glob("*.json")):
        card = json.loads(path.read_text(encoding="utf-8"))
        inspected += 1
        if card["entry"] in exclude or (card["invocation"] == "explicit" and not explicit):
            continue
        identity = tokens(" ".join([card["entry"], *card["capabilities"], *card["aliases"]]))
        meaning = tokens(" ".join([card["summary"], *card["outputs"]]))
        overlap = terms & (identity | meaning)
        if not overlap:
            continue
        score = 3 * len(terms & identity) + len(terms & meaning)
        # A domain is a soft prior, never an inventory filter or proof of fit.
        score += int(domain is not None and domain in card["domains"])
        matches.append({"score": score, "matched_terms": sorted(overlap),
                        "resource": bindings[card["entry"]], **card})
    matches.sort(key=lambda x: (-x["score"], x["id"]))
    return {"query": query, "search": "lexical-all-domains", "cards_inspected": inspected,
            "total_matches": len(matches), "candidates": matches[:limit],
            "activation": "not-performed", "availability": "not-checked",
            "next_on_miss": "Reformulate by outcome/output or inspect catalog.md; a miss does not prove absence."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--query")
    action.add_argument("--method", help="Exact method entry; inspect only, never invoke.")
    parser.add_argument("--domain", help="Soft ranking preference, never a hard filter.")
    parser.add_argument("--explicit", action="store_true", help="Include explicitly requested workflows among candidates.")
    parser.add_argument("--exclude", action="append", default=[], help="Exclude a known denied/inapplicable entry.")
    parser.add_argument("--limit", type=int, default=6)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    if args.method is not None:
        if not re.fullmatch(r"[a-z][a-z0-9-]*", args.method):
            parser.error("invalid method identity")
        path = root / "methods" / (args.method + ".json")
        if args.method in args.exclude or not path.is_file():
            result = {"found": False, "entry": args.method, "scope": "this packaged inventory"}
        else:
            result = json.loads(path.read_text(encoding="utf-8"))
            result["resource"] = json.loads((root / "bindings.json").read_text(encoding="utf-8"))["methods"][args.method]
        result["activation"] = "not-performed"
    else:
        if not 1 <= args.limit <= 20:
            parser.error("--limit must be between 1 and 20")
        result = discover(root, args.query, explicit=args.explicit, domain=args.domain,
                          limit=args.limit, exclude=args.exclude)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
