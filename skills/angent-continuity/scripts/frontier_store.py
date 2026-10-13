#!/usr/bin/env python3
"""Revisioned local persistence for ANGENT Continuity frontiers.

Each save writes an immutable revision first, then refreshes current.json.
Recovery and discovery both scan coherent immutable revisions so a stale
current.json cannot hide newer durable work after an interruption.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import time
from typing import Any


SCHEMA_VERSION = 1
LOCK_STALE_SECONDS = 120.0
VALID_LIFECYCLES = {
    "ACTIVE",
    "PAUSED",
    "BLOCKED",
    "COMPLETED",
    "SUPERSEDED",
    "ABANDONED",
}
VALID_REPAIR_STATES = {"NONE", "REPAIRING", "UNSTABLE"}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def work_dir_name(work_key: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", work_key).strip("-")[:64] or "work"
    digest = hashlib.sha256(work_key.encode("utf-8")).hexdigest()[:10]
    return f"{slug}-{digest}"


def default_root(project_root: Path) -> Path:
    return project_root / ".angent" / "runtime" / "continuity"


def atomic_write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
        try:
            os.chmod(path, 0o600)
        except OSError:
            pass
    finally:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass


@contextmanager
def work_lock(work_dir: Path, timeout: float = 3.0):
    lock = work_dir / ".lock"
    work_dir.mkdir(parents=True, exist_ok=True)
    deadline = time.monotonic() + timeout
    while True:
        try:
            lock.mkdir()
            try:
                (lock / "owner.json").write_text(
                    json.dumps({"pid": os.getpid(), "created_at": now_iso()}),
                    encoding="utf-8",
                )
            except OSError:
                pass
            break
        except FileExistsError:
            try:
                age = time.time() - lock.stat().st_mtime
                if age > LOCK_STALE_SECONDS:
                    for child in lock.iterdir():
                        child.unlink(missing_ok=True)
                    lock.rmdir()
                    continue
            except OSError:
                pass
            if time.monotonic() >= deadline:
                raise RuntimeError("continuity work item is locked by another writer")
            time.sleep(0.05)
    try:
        yield
    finally:
        try:
            for child in lock.iterdir():
                child.unlink(missing_ok=True)
            lock.rmdir()
        except OSError:
            pass


def revision_files(work_dir: Path) -> list[Path]:
    revisions = work_dir / "revisions"
    if not revisions.is_dir():
        return []
    return sorted(revisions.glob("*.json"))


def read_revision(path: Path) -> dict[str, Any] | None:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if record.get("schema_version") != SCHEMA_VERSION:
        return None
    if not isinstance(record.get("work_key"), str) or not record["work_key"]:
        return None
    revision = record.get("revision")
    if not isinstance(revision, int) or revision < 1:
        return None
    if not isinstance(record.get("frontier"), dict):
        return None
    return record


def load_latest(work_dir: Path, work_key: str) -> dict[str, Any] | None:
    latest = None
    for path in revision_files(work_dir):
        record = read_revision(path)
        if record is None or record["work_key"] != work_key:
            continue
        if latest is None or record["revision"] > latest["revision"]:
            latest = record
    return latest


def load_latest_discoverable(work_dir: Path) -> dict[str, Any] | None:
    by_key: dict[str, dict[str, Any]] = {}
    for path in revision_files(work_dir):
        record = read_revision(path)
        if record is None:
            continue
        key = record["work_key"]
        previous = by_key.get(key)
        if previous is None or record["revision"] > previous["revision"]:
            by_key[key] = record

    if len(by_key) != 1:
        return None
    return next(iter(by_key.values()))


def frontier_from_args(args: argparse.Namespace) -> Any:
    if args.frontier_json is not None:
        value = json.loads(args.frontier_json)
    else:
        value = json.loads(Path(args.frontier_file).read_text(encoding="utf-8"))
    if isinstance(value, dict):
        value.setdefault("lifecycle", "ACTIVE")
    return value


def validate_frontier(frontier: Any) -> str | None:
    if not isinstance(frontier, dict):
        return "frontier_must_be_json_object"

    lifecycle = frontier.get("lifecycle")
    if lifecycle is not None and lifecycle not in VALID_LIFECYCLES:
        return "invalid_lifecycle"

    repair_state = frontier.get("repair_state")
    if repair_state is not None and repair_state not in VALID_REPAIR_STATES:
        return "invalid_repair_state"

    for field in ("active_obligations", "verified_completed", "stale_or_recheck"):
        if field in frontier and not isinstance(frontier[field], list):
            return f"{field}_must_be_list"

    return None


def emit(payload: Any) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description="ANGENT Continuity frontier store")
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--root", help="Override continuity root.")

    sub = parser.add_subparsers(dest="command", required=True)

    load_p = sub.add_parser("load")
    load_p.add_argument("--work-key", required=True)

    save_p = sub.add_parser("save")
    save_p.add_argument("--work-key", required=True)
    source = save_p.add_mutually_exclusive_group(required=True)
    source.add_argument("--frontier-json")
    source.add_argument("--frontier-file")
    save_p.add_argument("--expected-revision", type=int, required=True)

    sub.add_parser("list")

    args = parser.parse_args()
    project_root = Path(args.project_root).resolve()
    root = Path(args.root).expanduser().resolve() if args.root else default_root(project_root)

    if args.command == "list":
        items = []
        if root.is_dir():
            for directory in sorted(p for p in root.iterdir() if p.is_dir()):
                latest = load_latest_discoverable(directory)
                if latest is None:
                    continue
                items.append({
                    "work_key": latest["work_key"],
                    "revision": latest["revision"],
                    "updated_at": latest.get("updated_at"),
                    "frontier": latest["frontier"],
                })
        emit({"root": str(root), "items": items})
        return 0

    work_dir = root / work_dir_name(args.work_key)

    if args.command == "load":
        latest = load_latest(work_dir, args.work_key)
        if latest is None:
            emit({"found": False, "work_key": args.work_key, "revision": 0})
            return 4
        emit({"found": True, **latest})
        return 0

    if args.command == "save":
        frontier = frontier_from_args(args)
        validation_error = validate_frontier(frontier)
        if validation_error is not None:
            emit({"error": validation_error})
            return 2

        with work_lock(work_dir):
            latest = load_latest(work_dir, args.work_key)
            current_revision = latest["revision"] if latest else 0
            if current_revision != args.expected_revision:
                emit({
                    "error": "revision_conflict",
                    "work_key": args.work_key,
                    "expected_revision": args.expected_revision,
                    "current_revision": current_revision,
                })
                return 3

            next_revision = current_revision + 1
            record = {
                "schema_version": SCHEMA_VERSION,
                "work_key": args.work_key,
                "revision": next_revision,
                "updated_at": now_iso(),
                "frontier": frontier,
            }
            revision_path = work_dir / "revisions" / f"{next_revision:08d}.json"
            if revision_path.exists():
                emit({"error": "revision_path_already_exists", "path": str(revision_path)})
                return 3
            atomic_write(revision_path, record)

            current = {
                "schema_version": SCHEMA_VERSION,
                "work_key": args.work_key,
                "revision": next_revision,
                "updated_at": record["updated_at"],
                "revision_path": str(revision_path),
            }
            atomic_write(work_dir / "current.json", current)

        emit({"ok": True, **record})
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
