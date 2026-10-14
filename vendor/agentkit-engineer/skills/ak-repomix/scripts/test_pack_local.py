"""Safety and format regression fixtures for the local repository packer."""
from pathlib import Path
import hashlib
import xml.etree.ElementTree as ET
import json
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("pack_local.py")


class PackerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / "README.md").write_text("Read me\n", encoding="utf-8")
        (self.root / "src.py").write_text("print('hello')\n", encoding="utf-8")
        (self.root / ".env").write_text("API_KEY=verysecretvalue123\n", encoding="utf-8")
        (self.root / "ignored.txt").write_text("not visible\n", encoding="utf-8")
        (self.root / ".gitignore").write_text("ignored.txt\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)

    def tearDown(self):
        self.tmp.cleanup()

    def invoke(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), *args],
                              capture_output=True, text=True)

    def test_json_secret_ignore_and_source(self):
        out = self.invoke("--format", "json", "--stdout")
        self.assertEqual(out.returncode, 0, out.stderr)
        value = json.loads(out.stdout)
        paths = {x["path"] for x in value["files"]}
        self.assertIn("README.md", paths)
        self.assertIn("src.py", paths)
        self.assertNotIn(".env", paths)
        self.assertNotIn("ignored.txt", paths)
        self.assertFalse(value["metadata"]["complete"])
        self.assertNotIn("verysecretvalue123", out.stdout)

    def test_provenance_tracks_uncommitted_source_and_sha(self):
        result = json.loads(self.invoke('--format', 'json', '--stdout').stdout)
        self.assertTrue(result['metadata']['git_worktree_dirty'])
        self.assertEqual(result['metadata']['revision'], 'UNBORN')
        source = next(x for x in result['files'] if x['path'] == 'src.py')
        self.assertEqual(source['sha256'], hashlib.sha256(source['content'].encode('utf-8')).hexdigest())

    def test_xml_excludes_invalid_control_character(self):
        p = self.root / 'invalid.xml'
        p.write_bytes(b'<good>hello\x01world</good>')
        subprocess.run(['git', '-C', str(self.root), 'add', 'invalid.xml'], check=True)
        out = self.invoke('--format', 'xml', '--stdout')
        self.assertEqual(out.returncode, 0, out.stderr)
        tree = ET.fromstring(out.stdout)
        self.assertNotIn('invalid.xml', [node.attrib['path'] for node in tree.findall('file')])
        self.assertIn('control_character', out.stdout)

    def test_markdown_header_escapes_html_filename(self):
        p = self.root / 'evil<img onerror=alert(1)>.md'
        p.write_text('safe\n', encoding='utf-8')
        subprocess.run(['git', '-C', str(self.root), 'add', p.name], check=True)
        out = self.invoke('--format', 'markdown', '--stdout', '--include', 'evil*')
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn('## "evil&lt;img', out.stdout)
        self.assertNotIn('## evil<img', out.stdout)

    def test_dry_run_excludes_contents(self):
        out = self.invoke("--dry-run")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertTrue(json.loads(out.stdout)["no_contents_output"])
        self.assertNotIn("print('hello')", out.stdout)

    def test_existing_output_never_overwritten(self):
        output = self.root / "pack.json"
        first = self.invoke("--format", "json", "--output", str(output))
        self.assertEqual(first.returncode, 0, first.stderr)
        second = self.invoke("--format", "json", "--output", str(output))
        self.assertEqual(second.returncode, 2)
        self.assertIn('"files"', output.read_text(encoding="utf-8"))

    def test_secret_in_source_omitted(self):
        (self.root / "tracked.txt").write_text(
            "API_TOKEN=abcdefghijklmnopqrstuvwxyz0123456789\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", "tracked.txt"], check=True)
        out = self.invoke("--format", "json", "--stdout")
        self.assertEqual(out.returncode, 0, out.stderr)
        val = json.loads(out.stdout)
        self.assertTrue(any(x["path"] == "tracked.txt" and x["reason"] == "possible_secret"
                            for x in val["metadata"]["skipped"]))
        self.assertNotIn("abcdefghijklmnopqrstuvwxyz0123456789", out.stdout)

    def test_total_budget_is_reported_not_truncated(self):
        out = self.invoke("--format", "json", "--stdout", "--max-total-bytes", "1")
        self.assertEqual(out.returncode, 0, out.stderr)
        val = json.loads(out.stdout)
        self.assertFalse(val["metadata"]["complete"])
        self.assertEqual(val["metadata"]["files_included"], 0)

    def test_symlink_outside_is_omitted(self):
        link = self.root / "escape.md"
        try:
            link.symlink_to(Path(__file__))
        except OSError:
            self.skipTest("symlinks unsupported")
        subprocess.run(["git", "-C", str(self.root), "add", "escape.md"], check=True)
        out = self.invoke("--format", "json", "--stdout")
        self.assertEqual(out.returncode, 0, out.stderr)
        val = json.loads(out.stdout)
        self.assertTrue(any(x["path"] == "escape.md" for x in val["metadata"]["skipped"]))

    def test_markdown_fence_longer_than_source_fence(self):
        tick = chr(96)
        (self.root / "fenced.md").write_text(tick * 4 + "py\ncode\n" +
                                            tick * 4 + "\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", "fenced.md"], check=True)
        out = self.invoke("--format", "markdown", "--stdout", "--include", "fenced.md")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn(tick * 5, out.stdout)


if __name__ == "__main__":
    unittest.main()
