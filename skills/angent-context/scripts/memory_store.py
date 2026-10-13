#!/usr/bin/env python3
"""Small revisioned store for ANGENT user/project memory.

The model/Context owner decides whether a candidate confirms, refines,
supersedes or conflicts with existing memory. This script only provides
scoped persistence, atomic writes and compare-and-swap conflict detection.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
import time
from typing import Any


SCHEMA_VERSION = 1
LOCK_STALE_SECONDS = 120.0


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_store(scope: str, project_root: Path) -> Path:
    if scope == "project":
        return project_root / ".angent" / "runtime" / "memory" / "project.json"
    home = Path(os.environ.get("ANGENT_HOME", str(Path.home() / ".angent")))
    return home / "memory" / "user.json"


def empty_store(scope: str) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "scope": scope,
        "revision": 0,
        "updated_at": None,
        "entries": {},
    }


def read_store(path: Path, scope: str) -> dict[str, Any]:
    if not path.exists():
        return empty_store(scope)
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA_VERSION:
        raise RuntimeError("unsupported memory store schema")
    if data.get("scope") != scope:
        raise RuntimeError("memory store scope mismatch")
    if not isinstance(data.get("entries"), dict):
        raise RuntimeError("invalid memory entries")
    return data


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
    finally:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass


@contextmanager
def store_lock(path: Path, timeout: float = 3.0):
    lock = path.with_name(path.name + ".lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
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
                raise RuntimeError("memory store is locked by another writer")
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


def content_from_args(args: argparse.Namespace) -> str:
    if args.content is not None:
        return args.content
    return Path(args.content_file).read_text(encoding="utf-8")


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description="ANGENT scoped memory store")
    parser.add_argument("--scope", choices=("user", "project"), required=True)
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--store", help="Override store path; primarily for adapters/tests.")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("read")

    get_p = sub.add_parser("get")
    get_p.add_argument("--topic", required=True)

    put_p = sub.add_parser("put")
    put_p.add_argument("--topic", required=True)
    source = put_p.add_mutually_exclusive_group(required=True)
    source.add_argument("--content")
    source.add_argument("--content-file")
    put_p.add_argument("--status", choices=("active", "contested", "superseded"), default="active")
    put_p.add_argument("--provenance", action="append", default=[])
    put_p.add_argument("--expected-revision", type=int, required=True)

    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    path = Path(args.store).expanduser().resolve() if args.store else default_store(args.scope, root)

    if args.command == "read":
        data = read_store(path, args.scope)
        emit({"store": str(path), **data})
        return 0

    if args.command == "get":
        data = read_store(path, args.scope)
        entry = data["entries"].get(args.topic)
        emit({
            "store": str(path),
            "scope": args.scope,
            "revision": data["revision"],
            "topic": args.topic,
            "found": entry is not None,
            "entry": entry,
        })
        return 0 if entry is not None else 4

    if args.command == "put":
        with store_lock(path):
            data = read_store(path, args.scope)
            current_revision = int(data["revision"])
            if current_revision != args.expected_revision:
                emit({
                    "error": "revision_conflict",
                    "expected_revision": args.expected_revision,
                    "current_revision": current_revision,
                    "store": str(path),
                })
                return 3

            previous = data["entries"].get(args.topic)
            next_revision = current_revision + 1
            entry = {
                "topic": args.topic,
                "content": content_from_args(args),
                "status": args.status,
                "provenance": list(args.provenance),
                "updated_at": now_iso(),
                "created_at": previous.get("created_at") if previous else now_iso(),
                "entry_revision": (int(previous.get("entry_revision", 0)) + 1) if previous else 1,
            }
            data["entries"][args.topic] = entry
            data["revision"] = next_revision
            data["updated_at"] = now_iso()
            atomic_write(path, data)

        emit({
            "ok": True,
            "store": str(path),
            "scope": args.scope,
            "revision": next_revision,
            "entry": entry,
        })
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
