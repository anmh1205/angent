#!/usr/bin/env python3
"""Collision-safe local Markdown journal actions for ak-journal Skill.

Optional deterministic helper, not an AgentKit CLI compatibility layer.
"""
from __future__ import annotations

import argparse
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import re
import sys

SAFE_ENTRY = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+(?:-\d+)?\.md$")
DATE_PART = re.compile(r"^date:\s*(\d{4}-\d{2}-\d{2})$", re.MULTILINE)
TITLE_PART = re.compile(r"^title:\s*(.+)$", re.MULTILINE)


def journal_root(project_root: Path) -> Path:
    project = project_root.resolve(strict=True)
    if not project.is_dir():
        raise ValueError("project root must be a directory")
    folder = project / "plans" / "journals"
    if folder.is_symlink() or not folder.resolve().is_relative_to(project):
        raise ValueError("journal directory escapes the authorized project")
    return folder


def safe_title(title: str) -> str:
    if not title or len(title) > 200 or any(x in title for x in ("\n", "\r", "\x00")):
        raise ValueError("title must be 1..200 characters on one line")
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:64].strip("-")
    if not slug:
        raise ValueError("title has no usable filename characters")
    return slug


def validate_date(value: str) -> str:
    if date.fromisoformat(value).isoformat() != value:
        raise ValueError("date must use YYYY-MM-DD")
    return value


def create(root: Path, title: str, summary: str, day: str, body: str) -> dict:
    directory = journal_root(root)
    slug = safe_title(title)
    validate_date(day)
    if len(summary) > 600 or "\n" in summary or "\r" in summary:
        raise ValueError("summary is too long or multiline")
    directory.mkdir(parents=True, exist_ok=True)
    # Refuse a directory link that was introduced after the initial scope check.
    if directory.is_symlink() or not directory.resolve().is_relative_to(root.resolve()):
        raise ValueError("journal directory changed while writing")
    payload = (
        "---\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        f"date: {day}\n"
        f"summary: {json.dumps(summary, ensure_ascii=False)}\n"
        "---\n\n"
        + body.rstrip("\n") + "\n"
    )
    for ordinal in range(1, 1001):
        suffix = "" if ordinal == 1 else f"-{ordinal}"
        path = directory / f"{day}-{slug}{suffix}.md"
        try:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError:
            continue
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
        return {"created": True, "path": str(path), "name": path.name,
                "date": day, "title": title, "collision_index": ordinal}
    raise ValueError("journal name collisions exceeded maximum")


def read_entry(directory: Path, filename: str) -> tuple[Path, str]:
    if not SAFE_ENTRY.fullmatch(filename):
        raise ValueError("invalid journal entry name")
    path = directory / filename
    if path.is_symlink() or not path.resolve(strict=True).is_relative_to(directory.resolve()):
        raise ValueError("journal entry escapes directory")
    return path, path.read_text(encoding="utf-8")


def check_entry(name: str, body: str) -> list[str]:
    problems: list[str] = []
    if not body.startswith("---\n") or "\n---\n" not in body[4:]:
        return ["missing_or_unclosed_frontmatter"]
    header = body[4:].split("\n---\n", 1)[0]
    tm = TITLE_PART.search(header)
    dm = DATE_PART.search(header)
    if not tm:
        problems.append("missing_title")
    else:
        try:
            val = json.loads(tm.group(1))
            safe_title(val)
        except (ValueError, TypeError, json.JSONDecodeError):
            problems.append("invalid_title")
    if not dm:
        problems.append("missing_date")
    else:
        try:
            validate_date(dm.group(1))
        except ValueError:
            problems.append("invalid_date")
        if not name.startswith(dm.group(1) + "-"):
            problems.append("filename_date_mismatch")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    sub = parser.add_subparsers(dest="action", required=True)
    new = sub.add_parser("create")
    new.add_argument("--title", required=True)
    new.add_argument("--summary", default="")
    new.add_argument("--date", default=None, help="YYYY-MM-DD; default UTC today")
    new.add_argument("--stdin", action="store_true", help="Read journal body from stdin")
    sub.add_parser("list")
    show = sub.add_parser("show")
    show.add_argument("--name", required=True)
    check = sub.add_parser("validate")
    check.add_argument("--name", required=True)
    args = parser.parse_args(argv)
    try:
        root = journal_root(args.project_root)
        if args.action == "create":
            day = args.date or datetime.now(timezone.utc).date().isoformat()
            body = sys.stdin.read() if args.stdin else ""
            result = create(args.project_root, args.title, args.summary, day, body)
        elif args.action == "list":
            result = {"entries": sorted(
                [x.name for x in root.glob("*.md")
                 if SAFE_ENTRY.fullmatch(x.name) and not x.is_symlink()],
                reverse=True
            ) if root.is_dir() else [], "source": "project_local_journals"}
        else:
            path, body = read_entry(root, args.name)
            if args.action == "show":
                result = {"name": path.name, "content": body}
            else:
                problems = check_entry(path.name, body)
                result = {"name": path.name, "valid": not problems, "errors": problems}
                if problems:
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
