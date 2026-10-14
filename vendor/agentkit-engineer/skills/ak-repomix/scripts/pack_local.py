#!/usr/bin/env python3
"""Package a bounded local Git repository; no network or remote uploads.

Independent ANGENT fallback subset; NOT the original Repomix implementation.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fnmatch import fnmatchcase
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

SENSITIVE_NAME = re.compile(
    r"(^|/)(?:\.env(?:\..*)?|\.npmrc|\.pypirc|\.netrc|"
    r"id_(?:rsa|ed25519|ecdsa)(?:\.pub)?|credentials(?:\.[^/]*)?|"
    r"secrets?(?:\.[^/]*)?|.*\.(?:pem|p12|pfx|key))$",
    re.IGNORECASE,
)
SENSITIVE_TEXT = re.compile(
    r"(?im)^\s*(?:export\s+)?[a-z0-9_]*(?:SECRET|TOKEN|PASSWORD|PRIVATE_KEY|API_KEY)"
    r"[a-z0-9_]*\s*[:=]\s*['\"]?[a-z0-9+/=_\-]{12,}|"
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
    r"\bghp_[A-Za-z0-9]{30,}\b",
    re.IGNORECASE,
)
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip",
              ".tar", ".gz", ".7z", ".exe", ".so", ".dll", ".mp4", ".mp3", ".wav"}


@dataclass(frozen=True)
class Item:
    path: str
    content: str
    size: int


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          check=check, timeout=20)


def matches(path: str, patterns: list[str]) -> bool:
    name = path.rsplit("/", 1)[-1]
    return any(fnmatchcase(path, glob) or fnmatchcase(name, glob) for glob in patterns)


def collect(root: Path, include: list[str], exclude: list[str],
            max_files: int, max_file_bytes: int, max_total_bytes: int,
            output: Path | None) -> tuple[list[Item], list[dict[str, str]], str]:
    root = root.resolve(strict=True)
    top = git(root, "rev-parse", "--show-toplevel").stdout.decode("utf-8").strip()
    if root != Path(top).resolve():
        raise ValueError("root must be the exact Git worktree root")
    found = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard")
    candidates = sorted(set(x.decode("utf-8", "replace") for x in
                            found.stdout.split(b"\0") if x))
    rev = git(root, "rev-parse", "--verify", "HEAD", check=False)
    revision = rev.stdout.decode("utf-8").strip() if rev.returncode == 0 else "UNBORN"
    items: list[Item] = []
    skipped: list[dict[str, str]] = []
    total = 0
    for rel in candidates:
        if include and not matches(rel, include):
            continue
        if matches(rel, exclude):
            continue
        path = root / rel
        reason = None
        try:
            resolved = path.resolve(strict=True)
            if path.is_symlink() or not resolved.is_relative_to(root) or not path.is_file():
                reason = "not_regular_or_symlink"
            elif output is not None and resolved == output:
                reason = "output_self_reference"
            elif SENSITIVE_NAME.search(rel):
                reason = "sensitive_filename"
            elif path.suffix.lower() in BINARY_EXT:
                reason = "binary_extension"
            elif path.stat().st_size > max_file_bytes:
                reason = "file_size_limit"
            else:
                data = path.read_bytes()
                if b"\0" in data:
                    reason = "binary_content"
                else:
                    try:
                        content = data.decode("utf-8")
                    except UnicodeDecodeError:
                        reason = "non_utf8"
                    else:
                        if SENSITIVE_TEXT.search(content):
                            reason = "possible_secret"
                        elif len(items) >= max_files:
                            reason = "file_count_limit"
                        elif total + len(data) > max_total_bytes:
                            reason = "total_size_limit"
                        else:
                            items.append(Item(rel, content, len(data)))
                            total += len(data)
        except OSError:
            reason = "file_unreadable_or_changed"
        if reason:
            skipped.append({"path": rel, "reason": reason})
    return items, skipped, revision


def render(items: list[Item], skipped: list[dict[str, str]],
           revision: str, fmt: str) -> str:
    meta = {
        "revision": revision, "files_included": len(items),
        "bytes_included": sum(x.size for x in items),
        "complete": not skipped, "skipped": skipped,
        "scope": "local_git_only", "security": "heuristic_not_a_secret_scan",
    }
    if fmt == "json":
        return json.dumps({"metadata": meta, "files": [
            {"path": x.path, "content": x.content} for x in items
        ]}, ensure_ascii=False, indent=2) + "\n"
    if fmt == "xml":
        root = ET.Element("repository", revision=revision, complete=str(not skipped).lower())
        ET.SubElement(root, "metadata").text = json.dumps(meta, ensure_ascii=False)
        for item in items:
            ET.SubElement(root, "file", path=item.path).text = item.content
        return ET.tostring(root, encoding="unicode") + "\n"
    tick = chr(96)
    result = ["# Local repository context", "", tick * 3 + "json",
              json.dumps(meta, ensure_ascii=False, indent=2), tick * 3, ""]
    for item in items:
        longest = max((len(match.group()) for match in
                       re.finditer(tick + "+", item.content)), default=0)
        fence = tick * max(3, longest + 1)
        result.extend(["## " + item.path, "", fence, item.content, fence, ""])
    return "\n".join(result)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--format", choices=("markdown", "json", "xml"), default="markdown")
    p.add_argument("--include", action="append", default=[])
    p.add_argument("--exclude", action="append", default=[])
    p.add_argument("--max-files", type=int, default=200)
    p.add_argument("--max-file-bytes", type=int, default=200_000)
    p.add_argument("--max-total-bytes", type=int, default=1_000_000)
    dest = p.add_mutually_exclusive_group(required=True)
    dest.add_argument("--output", type=Path, help="Create a new file, never overwrite")
    dest.add_argument("--stdout", action="store_true", help="Explicitly print source contents")
    dest.add_argument("--dry-run", action="store_true", help="Print paths only, no file contents")
    args = p.parse_args(argv)
    if min(args.max_files, args.max_file_bytes, args.max_total_bytes) < 1:
        p.error("limits must be positive")
    try:
        output = args.output.resolve() if args.output else None
        items, skipped, revision = collect(args.root, args.include, args.exclude,
                                           args.max_files, args.max_file_bytes,
                                           args.max_total_bytes, output)
        if args.dry_run:
            print(json.dumps({"revision": revision, "included": [i.path for i in items],
                              "skipped": skipped, "complete": not skipped,
                              "no_contents_output": True}, ensure_ascii=False, indent=2))
        else:
            content = render(items, skipped, revision, args.format)
            if args.stdout:
                sys.stdout.write(content)
            else:
                with args.output.open("x", encoding="utf-8", newline="\n") as fp:
                    fp.write(content)
            if skipped:
                print(f"PARTIAL: {len(skipped)} files omitted; inspect metadata.",
                      file=sys.stderr)
        return 0
    except (OSError, subprocess.SubprocessError, ValueError) as exc:
        print(f"repomix fallback: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
