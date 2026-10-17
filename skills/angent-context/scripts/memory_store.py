#!/usr/bin/env python3
"""Small revisioned store for ANGENT memory and promoted Learning mechanisms.

The model/Context owner decides whether a candidate confirms, refines,
supersedes or conflicts with existing memory. This script only provides
scoped persistence, atomic writes and compare-and-swap conflict detection.
"""

from __future__ import annotations

import argparse
import errno
from contextlib import contextmanager
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
import time
from typing import Any


SCHEMA_VERSION = 1


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_store(scope: str, project_root: Path) -> Path:
    home = Path(os.environ.get("ANGENT_HOME", str(Path.home() / ".angent")))
    if scope == "project":
        return project_root / ".angent" / "runtime" / "memory" / "project.json"
    if scope == "learning-project":
        return project_root / ".angent" / "runtime" / "learning" / "mechanisms.json"
    if scope == "learning-user":
        return home / "learning" / "mechanisms.json"
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
    if not isinstance(data, dict) or data.get("schema_version") != SCHEMA_VERSION:
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
def store_lock(path: Path, timeout: float = 3.0):
    """An OS-owned lock, automatically released after process exit or crash.

    The lock file is intentionally never removed: unlinking an open lock file
    permits a second process to lock a different inode at the same path.
    """
    lock = path.with_name(path.name + ".writer.lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(lock, os.O_RDWR | os.O_CREAT, 0o600)
    acquired = False
    deadline = time.monotonic() + timeout
    try:
        while not acquired:
            try:
                if os.name == "nt":
                    import msvcrt
                    # Windows byte-range locks require a byte to lock.
                    if os.fstat(fd).st_size == 0:
                        os.write(fd, b"\0")
                    os.lseek(fd, 0, os.SEEK_SET)
                    msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                acquired = True
            except OSError as exc:
                if (exc.errno not in (errno.EAGAIN, errno.EACCES, errno.EWOULDBLOCK)
                        and getattr(exc, "winerror", None) not in (32, 33)):
                    raise
                if time.monotonic() >= deadline:
                    raise RuntimeError("memory store is locked by another writer") from exc
                time.sleep(0.05)
        yield
    finally:
        try:
            if acquired:
                if os.name == "nt":
                    import msvcrt
                    os.lseek(fd, 0, os.SEEK_SET)
                    msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def content_from_args(args: argparse.Namespace) -> str:
    if args.content is not None:
        return args.content
    return Path(args.content_file).read_text(encoding="utf-8")


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description="ANGENT scoped memory store")
    parser.add_argument("--scope", choices=("user", "project", "learning-user", "learning-project"), required=True)
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--store", help="Override store path; primarily for adapters or manual tooling.")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("read")

    list_p = sub.add_parser("list")
    list_p.add_argument("--prefix")
    list_p.add_argument("--status", choices=("active", "contested", "superseded", "reopened", "retired"))
    list_p.add_argument("--limit", type=int, default=50, help="Maximum metadata entries (1-200).")
    list_p.add_argument("--after", help="Exclusive topic cursor from a previous list response.")

    get_p = sub.add_parser("get")
    get_p.add_argument("--topic", required=True)

    put_p = sub.add_parser("put")
    put_p.add_argument("--topic", required=True)
    source = put_p.add_mutually_exclusive_group(required=True)
    source.add_argument("--content")
    source.add_argument("--content-file")
    put_p.add_argument("--status", choices=("active", "contested", "superseded", "reopened", "retired"), default="active")
    put_p.add_argument("--provenance", action="append", default=[])
    put_p.add_argument("--expected-revision", type=int, required=True)

    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    path = Path(args.store).expanduser().resolve() if args.store else default_store(args.scope, root)

    if args.command == "read":
        data = read_store(path, args.scope)
        emit({"store": str(path), **data})
        return 0

    if args.command == "list":
        if not 1 <= args.limit <= 200:
            parser.error("--limit must be between 1 and 200")
        data = read_store(path, args.scope)
        entries = []
        for topic, entry in sorted(data["entries"].items()):
            if args.prefix is not None and not topic.startswith(args.prefix):
                continue
            if args.status is not None and entry.get("status") != args.status:
                continue
            if args.after is not None and topic <= args.after:
                continue
            entries.append({"topic": topic, **{key: entry.get(key) for key in
                            ("status", "provenance", "updated_at", "created_at", "entry_revision")}})
            if len(entries) > args.limit:
                break
        emit({
            "store": str(path),
            "scope": args.scope,
            "revision": data["revision"],
            "entries": entries[:args.limit],
            "next_after": entries[args.limit - 1]["topic"] if len(entries) > args.limit else None,
        })
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
        if not args.scope.startswith("learning-") and args.status in {"reopened", "retired"}:
            emit({"error": "learning_status_requires_learning_scope", "scope": args.scope})
            return 2

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
