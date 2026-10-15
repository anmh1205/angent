#!/usr/bin/env python3
"""CLI-free, project-scoped plan file operations for the ak-plan Skill.

Deterministic file scaffold/inspection only; plan design and acceptance belong to the Skill.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys

SAFE_ID = re.compile(r"^[a-z0-9][a-z0-9-]{0,127}$")
PHASE = re.compile(r"^phase-(\d{2,})-[a-z0-9-]+\.md$")
CHECKBOX = re.compile(r"^\s*[-*]\s+\[([ xX])\]\s", re.MULTILINE)


def slugify(title: str) -> str:
    if not title or len(title) > 200 or any(c in title for c in ("\n", "\r", "\x00")):
        raise ValueError("title must be a single line of 1..200 characters")
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:64].strip("-")
    if not slug:
        raise ValueError("title cannot create a safe slug")
    return slug


def root_folder(project_root: Path) -> Path:
    root = project_root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("project root is not a directory")
    target = root / "plans"
    if target.is_symlink() or not target.resolve().is_relative_to(root):
        raise ValueError("plans folder escapes project")
    return target


def plan_folder(project_root: Path, plan_id: str) -> Path:
    if not SAFE_ID.fullmatch(plan_id):
        raise ValueError("invalid plan identifier")
    parent = root_folder(project_root)
    path = parent / plan_id
    if path.is_symlink() or not path.resolve().is_relative_to(parent.resolve()):
        raise ValueError("plan directory escapes project")
    return path


def frontmatter(title: str) -> str:
    return "---\ntitle: " + json.dumps(title, ensure_ascii=False) + "\n---\n\n"


def create(project_root: Path, title: str) -> dict:
    slug = slugify(title)
    parent = root_folder(project_root)
    parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dt%H%M%S")
    path = None
    for i in range(1, 1001):
        plan_id = timestamp + "-" + slug + (f"-{i}" if i > 1 else "")
        candidate = plan_folder(project_root, plan_id)
        try:
            candidate.mkdir(mode=0o700, exist_ok=False)
        except FileExistsError:
            continue
        path = candidate
        break
    if path is None:
        raise ValueError("plan name collisions exhausted")

    outline = frontmatter(title) + (
        "## Outcome\n\n"
        "Specify the accepted outcome; this scaffold is not an approved plan.\n\n"
        "## Scope and constraints\n\n"
        "Describe what is in/out, governing instructions and risks.\n\n"
        "## Phases and dependencies\n\n"
        "- Phase 01: start (not accepted or completed)\n\n"
        "## Acceptance evidence\n\n"
        "Record exact tests, observations and unresolved decisions.\n"
    )
    phase = frontmatter("Start") + (
        "## Prerequisites\n\n"
        "Describe the dependency and authorized ownership.\n\n"
        "## Intended change\n\n"
        "Describe the work.\n\n"
        "## Verification\n\n"
        "- [ ] Define and run the acceptance check.\n"
    )
    (path / "plan.md").write_text(outline, encoding="utf-8")
    (path / "phase-01-start.md").write_text(phase, encoding="utf-8")
    return {"created": True, "plan_id": path.name,
            "plan_file": str(path / "plan.md"), "phase_count": 1,
            "accepted": False}


def inventory(folder: Path) -> tuple[list[dict], list[str]]:
    problems: list[str] = []
    plan_file = folder / "plan.md"
    if not plan_file.is_file() or plan_file.is_symlink():
        problems.append("missing_plan_md")
    else:
        content = plan_file.read_text(encoding="utf-8")
        if not content.startswith("---\n") or "\n---\n" not in content[4:]:
            problems.append("invalid_plan_frontmatter")
        elif not re.search(r"^title:\s*\S+", content.split("\n---\n", 1)[0], re.MULTILINE):
            problems.append("missing_plan_title")
    files = sorted(folder.glob("phase-*.md"))
    phases: list[dict] = []
    numbers: set[int] = set()
    for file in files:
        if file.is_symlink():
            problems.append("phase_symlink")
            continue
        match = PHASE.fullmatch(file.name)
        if not match:
            problems.append(f"invalid_phase_filename:{file.name}")
            continue
        number = int(match.group(1))
        if number in numbers:
            problems.append(f"duplicate_phase_number:{number}")
        numbers.add(number)
        text = file.read_text(encoding="utf-8")
        checks = CHECKBOX.findall(text)
        done = sum(x.lower() == "x" for x in checks)
        phases.append({"file": file.name, "number": number, "checked": done,
                       "unchecked": len(checks) - done,
                       "verification": "not_established_from_checkboxes"})
    if not phases:
        problems.append("no_phase_files")
    return phases, problems


def inspect(project_root: Path, plan_id: str) -> dict:
    folder = plan_folder(project_root, plan_id)
    if not folder.is_dir():
        raise FileNotFoundError("plan not found")
    phases, problems = inventory(folder)
    return {"plan_id": plan_id, "valid_structure": not problems,
            "errors": problems, "phases": phases, "phase_count": len(phases),
            "checked_total": sum(x["checked"] for x in phases),
            "unchecked_total": sum(x["unchecked"] for x in phases),
            "acceptance": "requires_independent_evidence"}


def add_phase(project_root: Path, plan_id: str, title: str) -> dict:
    folder = plan_folder(project_root, plan_id)
    if not folder.is_dir():
        raise FileNotFoundError("plan not found")
    slug = slugify(title)
    phases, problems = inventory(folder)
    if problems:
        raise ValueError(f"invalid existing plan: {', '.join(problems)}")
    next_number = max(x["number"] for x in phases) + 1
    path = folder / f"phase-{next_number:02d}-{slug}.md"
    text = frontmatter(title) + (
        "## Prerequisites and owned interfaces\n\n"
        "## Implementation\n\n"
        "## Acceptance evidence\n\n"
        "- [ ] Define verification.\n"
    )
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return {"added": True, "plan_id": plan_id, "phase": path.name,
            "accepted": False}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    sub = parser.add_subparsers(dest="action", required=True)
    new = sub.add_parser("create")
    new.add_argument("--title", required=True)
    sub.add_parser("list")
    for command in ("status", "validate"):
        q = sub.add_parser(command)
        q.add_argument("--plan-id", required=True)
    add = sub.add_parser("add-phase")
    add.add_argument("--plan-id", required=True)
    add.add_argument("--title", required=True)
    args = parser.parse_args(argv)
    try:
        folder = root_folder(args.project_root)
        if args.action == "create":
            result = create(args.project_root, args.title)
        elif args.action == "list":
            plans = []
            if folder.is_dir():
                for d in sorted(folder.iterdir()):
                    if d.is_dir() and not d.is_symlink() and SAFE_ID.fullmatch(d.name):
                        if (d / "plan.md").is_file() and not (d / "plan.md").is_symlink():
                            plans.append(d.name)
            result = {"plans": plans, "source": "project_local_plan_files"}
        elif args.action == "add-phase":
            result = add_phase(args.project_root, args.plan_id, args.title)
        else:
            result = inspect(args.project_root, args.plan_id)
            if args.action == "validate" and not result["valid_structure"]:
                print(json.dumps(result, ensure_ascii=False, indent=2))
                return 3
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": type(exc).__name__, "detail": str(exc)},
                         ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
