#!/usr/bin/env python3
"""Check a scoped BA evidence graph; structural coverage is not semantic truth."""
from __future__ import annotations
import argparse
import json
from collections import defaultdict, deque
from pathlib import Path
import re
from typing import Any

ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9-]+$")


def audit(data: Any, require_tests: bool = False,
          source_root: Path | None = None) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict):
        return {"ok": False, "errors": ["Root must be a JSON object"], "warnings": [], "coverage": {}}
    artifacts, sources = data.get("artifacts"), data.get("sources")
    if not isinstance(artifacts, list) or not isinstance(sources, list):
        return {"ok": False, "errors": ["Expected artifacts and sources arrays"], "warnings": [], "coverage": {}}
    nodes: dict[str, dict] = {}
    source_ids: set[str] = set()
    for pos, src in enumerate(sources):
        if not isinstance(src, dict) or not isinstance(src.get("id"), str) or not isinstance(src.get("uri"), str) or not src["uri"].strip():
            errors.append(f"sources[{pos}]: expected id and nonempty uri")
            continue
        if src["id"] in source_ids:
            errors.append(f"sources[{pos}]: duplicate source ID {src['id']}")
        source_ids.add(src["id"])
        if source_root is not None:
            uri = src["uri"]
            if "://" in uri or uri.startswith("#"):
                warnings.append(f"sources[{pos}]: external or in-document reference needs provider verification: {uri}")
            else:
                root = source_root.resolve()
                candidate = (root / uri).resolve()
                if not candidate.is_relative_to(root):
                    errors.append(f"sources[{pos}]: local evidence path escapes allowed root")
                elif not candidate.is_file():
                    errors.append(f"sources[{pos}]: source evidence file missing: {uri}")
    for pos, obj in enumerate(artifacts):
        if not isinstance(obj, dict):
            errors.append(f"artifacts[{pos}]: expected object")
            continue
        key = obj.get("id")
        if not isinstance(key, str) or not ID_RE.fullmatch(key):
            errors.append(f"artifacts[{pos}]: invalid stable ID")
            continue
        if key in nodes:
            errors.append(f"artifacts[{pos}]: duplicate artifact ID {key}")
            continue
        nodes[key] = obj
        for field in ("kind", "title"):
            if not isinstance(obj.get(field), str) or not obj[field].strip():
                errors.append(f"{key}: missing {field}")
        for field in ("depends_on", "source_refs"):
            val = obj.get(field)
            if not isinstance(val, list) or not all(isinstance(x, str) and x for x in val):
                errors.append(f"{key}: {field} must be a string list")
            elif len(set(val)) != len(val):
                errors.append(f"{key}: duplicate {field}")
    outgoing: dict[str, set[str]] = {}
    reverse: dict[str, set[str]] = defaultdict(set)
    for key, obj in nodes.items():
        deps = obj.get("depends_on", [])
        outgoing[key] = set(deps) if isinstance(deps, list) and all(isinstance(x, str) for x in deps) else set()
        for target in sorted(outgoing[key]):
            if target not in nodes:
                errors.append(f"{key}: missing dependency {target}")
            else:
                reverse[target].add(key)
        refs = obj.get("source_refs", [])
        if isinstance(refs, list):
            for ref in refs:
                if isinstance(ref, str) and ref not in source_ids:
                    errors.append(f"{key}: missing source {ref}")
        if not refs:
            warnings.append(f"{key}: no evidence sources")
    state: dict[str, int] = {}
    stack: list[str] = []
    def visit(key: str) -> None:
        if state.get(key) == 2:
            return
        if state.get(key) == 1:
            i = stack.index(key)
            errors.append("dependency cycle: " + " -> ".join(stack[i:] + [key]))
            return
        state[key] = 1
        stack.append(key)
        for nxt in sorted(outgoing.get(key, [])):
            if nxt in nodes and state.get(nxt) != 2:
                visit(nxt)
        stack.pop()
        state[key] = 2
    for key in sorted(nodes):
        if state.get(key) != 2:
            visit(key)
    requirements = sorted(k for k, obj in nodes.items() if str(obj.get("kind", "")).upper() == "FR")
    tested: list[str] = []
    for fr in requirements:
        queue = deque([fr])
        seen = {fr}
        found = False
        while queue:
            key = queue.popleft()
            if key != fr and str(nodes[key].get("kind", "")).upper() in ("TEST", "TC"):
                found = True
                break
            for dep in sorted(reverse.get(key, set())):
                # Story and use-case memberships often encompass more FRs than
                # one specific test covers. Only explicit FR/error/AC/checklist
                # references can justify a structurally traceable test chain.
                kind = str(nodes[dep].get('kind', '')).upper()
                if kind not in ('ERROR','E','AC','ACCEPTANCE','CHECKLIST','CHK','TEST','TC'):
                    continue
                if dep not in seen:
                    seen.add(dep)
                    queue.append(dep)
        if found:
            tested.append(fr)
        else:
            message = f"{fr}: no traceable test artifact"
            (errors if require_tests else warnings).append(message)
    coverage = {"functional_requirements": len(requirements), "traced_to_test": len(tested),
                "uncovered": sorted(set(requirements) - set(tested))}
    return {"ok": not errors, "errors": sorted(set(errors)), "warnings": sorted(set(warnings)),
            "coverage": coverage, "artifact_count": len(nodes), "source_count": len(source_ids)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--require-tests", action="store_true")
    parser.add_argument("--source-root",type=Path,help="Optional base for checking local source file existence; external URIs only warn")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}))
        return 2
    result = audit(data, require_tests=args.require_tests,source_root=args.source_root)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
