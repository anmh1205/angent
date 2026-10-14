"""Behavioral runtime tests for durable state and concurrency.

Exercises real subprocesses and filesystem effects; does not claim to measure
model reasoning or document-writing quality.
"""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
MEMORY = ROOT / "skills" / "angent-context" / "scripts" / "memory_store.py"
FRONTIER = ROOT / "skills" / "angent-continuity" / "scripts" / "frontier_store.py"


def module_from(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def invoke(path, *args):
    proc = subprocess.run([sys.executable, str(path), *map(str, args)],
                          capture_output=True, text=True, timeout=8)
    if not proc.stdout:
        return proc.returncode, {}
    return proc.returncode, json.loads(proc.stdout)


class RuntimeStateTests(unittest.TestCase):
    def test_live_writer_cannot_be_stolen_due_to_old_mtime(self):
        for src, fun, lock_file in [
            (MEMORY, "store_lock", lambda p: p.with_name(p.name + ".writer.lock")),
            (FRONTIER, "work_lock", lambda p: p / ".writer.lock"),
        ]:
            with self.subTest(script=src.name):
                module = module_from(src, src.stem + fun)
                with tempfile.TemporaryDirectory() as d:
                    target = Path(d) / "task"
                    with getattr(module, fun)(target, timeout=2):
                        lock = lock_file(target)
                        old = time.time() - 1000
                        os.utime(lock, (old, old))
                        child = subprocess.run(
                            [sys.executable, "-c",
                             "import importlib.util,sys;"
                             "from pathlib import Path;"
                             "s=importlib.util.spec_from_file_location('x',sys.argv[1]);"
                             "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
                             f"c=getattr(m,'{fun}');"
                             "c(Path(sys.argv[2]),timeout=0.2).__enter__()",
                             str(src), str(target)],
                            capture_output=True, text=True, timeout=5)
                        self.assertNotEqual(child.returncode, 0, child.stdout)
                        self.assertIn("locked by another writer", child.stderr)
                    # Once the owner releases, the next writer must succeed.
                    with getattr(module, fun)(target, timeout=1):
                        pass

    def test_lock_released_after_abrupt_process_exit(self):
        for src, fun in [(MEMORY, "store_lock"), (FRONTIER, "work_lock")]:
            with self.subTest(script=src.name):
                module = module_from(src, src.stem + fun + "2")
                with tempfile.TemporaryDirectory() as d:
                    target = Path(d) / "task"
                    child = subprocess.run(
                        [sys.executable, "-c",
                         "import importlib.util,os,sys;"
                         "from pathlib import Path;"
                         "s=importlib.util.spec_from_file_location('x',sys.argv[1]);"
                         "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
                         f"c=getattr(m,'{fun}');"
                         "c(Path(sys.argv[2]),timeout=1).__enter__();os._exit(0)",
                         str(src), str(target)],
                        capture_output=True, text=True, timeout=5)
                    self.assertEqual(child.returncode, 0, child.stderr)
                    with getattr(module, fun)(target, timeout=1):
                        pass

    def test_memory_revision_compare_and_swap(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d) / "memory.json"
            command = ["--scope", "project", "--store", str(store)]
            code, data = invoke(MEMORY, *command, "put", "--topic", "lesson",
                                "--content", "mechanism", "--expected-revision", "0")
            self.assertEqual(code, 0, data)
            self.assertEqual(data["revision"], 1)
            code, stale = invoke(MEMORY, *command, "put", "--topic", "lesson",
                                 "--content", "stale overwrite", "--expected-revision", "0")
            self.assertEqual(code, 3)
            self.assertEqual(stale["error"], "revision_conflict")
            code, current = invoke(MEMORY, *command, "get", "--topic", "lesson")
            self.assertEqual(code, 0)
            self.assertEqual(current["entry"]["content"], "mechanism")

    def test_frontier_fast_path_and_crash_recovery(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d) / "frontiers"
            args = ["--root", str(root)]
            for revision in (0, 1, 2):
                code, data = invoke(FRONTIER, *args, "save", "--work-key", "project/task",
                                    "--frontier-json", json.dumps({"verified_completed": [revision]}),
                                    "--expected-revision", str(revision))
                self.assertEqual(code, 0, data)
            module = module_from(FRONTIER, "frontier_caching")
            work = root / module.work_dir_name("project/task")
            self.assertEqual(module.cached_latest(work, "project/task")["revision"], 3)
            # Simulate power loss between the revision write and current.json refresh.
            pointer = json.loads((work / "current.json").read_text(encoding="utf-8"))
            pointer["revision"] = 1
            (work / "current.json").write_text(json.dumps(pointer), encoding="utf-8")
            self.assertIsNone(module.cached_latest(work, "project/task"))
            code, data = invoke(FRONTIER, *args, "load", "--work-key", "project/task")
            self.assertEqual(code, 0, data)
            self.assertEqual(data["revision"], 3)
            code, listing = invoke(FRONTIER, *args, "list")
            self.assertEqual(code, 0)
            self.assertEqual(listing["items"][0]["revision"], 3)
            (work / "current.json").write_text("{bad json", encoding="utf-8")
            code, data = invoke(FRONTIER, *args, "load", "--work-key", "project/task")
            self.assertEqual(code, 0, data)
            self.assertEqual(data["revision"], 3)
            # Saving from recovered state must not overwrite an earlier revision.
            code, data = invoke(FRONTIER, *args, "save", "--work-key", "project/task",
                                "--frontier-json", '{"lifecycle":"COMPLETED"}',
                                "--expected-revision", "3")
            self.assertEqual(code, 0, data)
            self.assertEqual(data["revision"], 4)
            self.assertEqual(module.cached_latest(work, "project/task")["revision"], 4)

    def test_concurrent_writers_cannot_both_commit_revision_one(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d) / "frontiers"
            cmd = [sys.executable, str(FRONTIER), "--root", str(root), "save",
                   "--work-key", "shared", "--frontier-json", '{"lifecycle":"ACTIVE"}',
                   "--expected-revision", "0"]
            procs = [subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                      text=True) for _ in range(2)]
            results = [(p.returncode, p.stdout) if p.poll() is not None
                       else (None, None) for p in procs]
            results = [p.communicate(timeout=8) for p in procs]
            codes = sorted(p.returncode for p in procs)
            self.assertEqual(codes, [0, 3], results)


if __name__ == "__main__":
    unittest.main()
