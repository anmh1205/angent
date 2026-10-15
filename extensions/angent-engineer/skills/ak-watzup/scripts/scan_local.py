#!/usr/bin/env python3
"""Read-only local Git/worktree/plan status; no checkout, fetch, merge or writes.

Independent portable subset of AgentKit Watzup; does not run upstream scanner.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

TASK = re.compile(r"^\s*[-*]\s+\[([ xX])\]\s", re.MULTILINE)


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          check=check, timeout=15)


def output(root: Path, *args: str, check: bool = True) -> str:
    result = git(root, *args, check=check)
    return result.stdout.decode("utf-8", "replace").strip()


def parse_worktrees(raw: str) -> list[dict[str, str | bool]]:
    result: list[dict[str, str | bool]] = []
    current: dict[str, str | bool] = {}
    for line in (raw + "\n\n").splitlines():
        if not line:
            if current:
                result.append(current)
                current = {}
            continue
        key, _, value = line.partition(" ")
        if key == "worktree":
            current["path"] = value
        elif key == "HEAD":
            current["head"] = value
        elif key == "branch":
            current["branch"] = value.removeprefix("refs/heads/")
        elif key in {"detached", "bare"}:
            current[key] = True
        elif key == "prunable":
            current["prunable"] = value or True
    return result


def relevant_plan(path: str) -> bool:
    rel = PurePosixPath(path)
    if rel.suffix.lower() != ".md":
        return False
    if rel.name.lower() == "roadmap.md":
        return True
    return rel.parts[:1] == ("plans",) or rel.parts[:2] == ("docs", "plans")


def scan(root: Path, max_plans: int = 40, max_refs: int = 200) -> dict:
    root = root.resolve(strict=True)
    top = output(root, "rev-parse", "--show-toplevel")
    if root != Path(top).resolve():
        raise ValueError("select the exact local Git worktree root")
    branch = output(root, "symbolic-ref", "--quiet", "--short", "HEAD", check=False)
    head = output(root, "rev-parse", "--verify", "HEAD", check=False) or None
    porcelain = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=normal")
    changes = [x for x in porcelain.stdout.split(b"\0") if x]
    worktrees = parse_worktrees(output(root, "worktree", "list", "--porcelain"))
    local_refs = output(root, "for-each-ref", "--format=%(refname:short)", "refs/heads")
    remote_refs = output(root, "for-each-ref", "--format=%(refname:short)", "refs/remotes")
    local_refs = [x for x in local_refs.splitlines() if x]
    remote_refs = [x for x in remote_refs.splitlines() if x and not x.endswith("/HEAD")]
    tracked = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard")
    candidates = sorted(set(x.decode("utf-8", "replace") for x in
                            tracked.stdout.split(b"\0") if x and
                            relevant_plan(x.decode("utf-8", "replace"))))
    plans: list[dict] = []
    gaps: list[str] = ["remote refs are cached and may be stale; no network fetch performed",
                        "only current worktree cleanliness is checked; other worktrees not opened",
                        "plan checkbox counts do not prove task completion"]
    for rel in candidates[:max_plans]:
        path = root / rel
        try:
            resolved = path.resolve(strict=True)
            if path.is_symlink() or not resolved.is_relative_to(root) or not path.is_file():
                gaps.append(f"skipped nonlocal plan: {rel}")
                continue
            if path.stat().st_size > 200_000:
                gaps.append(f"skipped oversized plan: {rel}")
                continue
            body = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            gaps.append(f"unreadable plan: {rel}")
            continue
        checks = TASK.findall(body)
        done = sum(x.lower() == "x" for x in checks)
        plans.append({"path": rel, "checked": done, "unchecked": len(checks) - done,
                      "total": len(checks)})
    if len(candidates) > max_plans:
        gaps.append(f"only {max_plans} of {len(candidates)} plan candidates scanned")
    if len(local_refs) > max_refs or len(remote_refs) > max_refs:
        gaps.append(f"branch listing capped at {max_refs} per ref category")
    todo: list[dict[str, str]] = []
    if changes:
        todo.append({"reason": "current worktree has uncommitted/untracked changes",
                     "recommendation": "inspect and preserve existing changes before switching branches"})
    if not branch:
        todo.append({"reason": "current HEAD is detached",
                     "recommendation": "identify intended branch before any future commit"})
    pending = [x for x in plans if x["unchecked"] > 0]
    if pending:
        todo.append({"reason": f"{len(pending)} readable plan(s) have unchecked items",
                     "recommendation": "check the actual acceptance evidence before resuming an item"})
    return {
        "repository_root": str(root),
        "current": {"branch": branch or None, "head": head,
                    "detached": not bool(branch), "dirty": bool(changes),
                    "porcelain_records": len(changes)},
        "worktrees": worktrees,
        "refs": {"local": local_refs[:max_refs], "remote_cached": remote_refs[:max_refs]},
        "plans": plans, "next_steps": todo, "limitations": gaps,
        "source": "local_git_read_only", "complete_runtime_parity": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--max-plans", type=int, default=40)
    parser.add_argument("--max-refs", type=int, default=200)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.max_plans < 1 or args.max_refs < 1:
        parser.error("limits must be positive")
    try:
        result = scan(args.root, args.max_plans, args.max_refs)
    except (OSError, subprocess.SubprocessError, ValueError) as exc:
        print(f"watzup fallback: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        now = result["current"]
        print(f"Git: {now['branch'] or '(detached)'} @ {now['head'] or '(unborn)'}")
        print(f"Working tree: {'dirty' if now['dirty'] else 'clean'}")
        print(f"Worktrees: {len(result['worktrees'])}; plans: {len(result['plans'])}")
        for step in result["next_steps"]:
            print(f"- {step['recommendation']} ({step['reason']})")
        print("Remote branches are cached; other worktree state not inspected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
