"""Bounded Python AST symbol discovery, false-negative and safety cases."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("search_python_ast.py")


class PythonASTSearchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / "service.py").write_text(
            "class Tracker:\n"
            "    def update(self):\n"
            "        return 3\n"
            "\n"
            "async def refresh():\n"
            "    return 4\n", encoding="utf-8")
        (self.root / "app.py").write_text(
            "from service import Tracker\n"
            "instance = Tracker()\n"
            "result = instance.update()\n", encoding="utf-8")
        (self.root / "ignored.py").write_text("def update(): pass\n", encoding="utf-8")
        (self.root / ".gitignore").write_text("ignored.py\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)

    def tearDown(self):
        self.tmp.cleanup()

    def invoke(self, symbol: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root),
                               "--symbol", symbol, *args], capture_output=True, text=True)

    def test_function_definition_and_attribute_use(self):
        out = self.invoke("update")
        self.assertEqual(out.returncode, 0, out.stderr)
        obj = json.loads(out.stdout)
        self.assertEqual([(x["path"], x["qualified"]) for x in obj["definitions"]],
                         [("service.py", "Tracker.update")])
        self.assertIn(("app.py", "attribute_load"),
                      {(x["path"], x["kind"]) for x in obj["possible_uses"]})
        self.assertEqual(obj["index"]["files_parsed"], 2)
        self.assertFalse(any(x["path"] == "ignored.py" for x in obj["definitions"]))

    def test_class_import_and_symbol_load(self):
        out = self.invoke("Tracker")
        self.assertEqual(out.returncode, 0, out.stderr)
        obj = json.loads(out.stdout)
        self.assertEqual(obj["definitions"][0]["kind"], "class")
        self.assertEqual({x["kind"] for x in obj["possible_uses"]},
                         {"import_binding", "name_load"})

    def test_unparsable_file_is_reported_incomplete(self):
        (self.root / "bad.py").write_text("def syntax(:\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", "bad.py"], check=True)
        out = self.invoke("Tracker")
        self.assertEqual(out.returncode, 0, out.stderr)
        obj = json.loads(out.stdout)
        self.assertFalse(obj["index"]["complete_python_parse"])
        self.assertTrue(any(x["reason"] == "SyntaxError" for x in obj["index"]["skipped"]))

    def test_file_limit_is_not_hidden(self):
        out = self.invoke("Tracker", "--max-files", "1")
        self.assertEqual(out.returncode, 0, out.stderr)
        obj = json.loads(out.stdout)
        self.assertEqual(obj["index"]["files_parsed"], 1)
        self.assertTrue(any(x["reason"] == "file_limit" for x in obj["index"]["skipped"]))

    def test_symlink_outside_root_is_skipped(self):
        path = self.root / "outside.py"
        try:
            path.symlink_to(Path(__file__))
        except OSError:
            self.skipTest("symlinks unsupported")
        subprocess.run(["git", "-C", str(self.root), "add", "outside.py"], check=True)
        out = self.invoke("Tracker")
        self.assertEqual(out.returncode, 0, out.stderr)
        obj = json.loads(out.stdout)
        self.assertTrue(any(x["path"] == "outside.py" for x in obj["index"]["skipped"]))

    def test_invalid_identifier_rejected(self):
        out = self.invoke("__import__('os')")
        self.assertEqual(out.returncode, 2)
        self.assertNotIn("service.py", out.stdout)

    def test_definition_only_mode(self):
        out = self.invoke("Tracker", "--mode", "definitions")
        self.assertEqual(out.returncode, 0, out.stderr)
        obj = json.loads(out.stdout)
        self.assertTrue(obj["definitions"])
        self.assertEqual(obj["possible_uses"], [])


if __name__ == "__main__":
    unittest.main()
