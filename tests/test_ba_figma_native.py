"""Native Figma output is valid, source-aligned and safe under a mock Plugin API."""
from pathlib import Path
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_figma_native import files

class NativeFigmaGeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=json.loads((ROOT/"extensions/angent-ba/examples/authentication-screen-model.json").read_text(encoding="utf8"))

    def test_source_inventory_retained_in_native_candidate(self):
        generated=files(self.model)
        self.assertEqual(set(generated),{"figma-native-plan.json","figma-native-plugin.js"})
        report=json.loads(generated["figma-native-plan.json"])
        self.assertFalse(report["writes_performed"])
        self.assertEqual(report["runtime_status"],"not-run")
        js=generated["figma-native-plugin.js"]
        for keyword in ("figma.createFrame()","figma.createText()","figma.loadFontAsync","figma.getNodeByIdAsync"):
            self.assertIn(keyword,js)
        for screen in self.model["screens"]:
            self.assertIn(screen["title"],js)
        self.assertNotIn("figma.create(item.tree)",js)
        self.assertNotIn("setPluginData",js)
        self.assertNotIn("loadAllPagesAsync",js)

    def test_injection_is_data_and_password_values_are_excluded(self):
        altered=copy.deepcopy(self.model)
        altered["screens"][0]["controls"][0]["label"]='\\");globalThis.sideEffect=true;//'
        altered["screens"][0]["controls"][1]["test_value"]="SENSITIVE_PASSWORD_SECRET"
        generated=files(altered)
        self.assertNotIn("SENSITIVE_PASSWORD_SECRET",generated["figma-native-plugin.js"])
        self.assertNotIn("SENSITIVE_PASSWORD_SECRET",generated["figma-native-plan.json"])
        self.assertIn(r'globalThis.sideEffect=true',generated["figma-native-plugin.js"])
        self.assertIn(r'\\\"',generated["figma-native-plugin.js"])

    def test_requirement_ids_and_invalid_screen_fail_closed(self):
        modified=copy.deepcopy(self.model)
        modified["screens"][0]["controls"][0]["requirements"]=["FR-AUTH-001"]
        files(modified,evidence_ids={"FR-AUTH-001","FR-AUTH-002","BR-AUTH-001"})
        with self.assertRaisesRegex(ValueError,"Unresolved BA evidence"):
            files(modified,evidence_ids={"FR-OTHER","FR-AUTH-002","BR-AUTH-001"})
        invalid=copy.deepcopy(self.model)
        invalid["screens"][0]["controls"][0]["id"]=invalid["screens"][0]["controls"][1]["id"]
        with self.assertRaisesRegex(ValueError,"Invalid BA screen"):
            files(invalid)

    @unittest.skipUnless(shutil.which("node"),"Node.js is required for JavaScript Plugin API mock")
    def test_native_script_runs_with_idempotency_conflict_and_rollback(self):
        generated=files(self.model)
        with tempfile.TemporaryDirectory() as tmp:
            src=Path(tmp)/"figma-native-plugin.js"
            src.write_text(generated["figma-native-plugin.js"],encoding="utf8")
            result=subprocess.run([shutil.which("node"),str(ROOT/"tests/integration/check_figma_native_mock.js"),str(src)],
                                  capture_output=True,text=True,errors="replace",timeout=30)
            self.assertEqual(result.returncode,0,result.stderr[-3000:])
            obj=json.loads(result.stdout.strip().splitlines()[-1])
            self.assertTrue(obj["ok"],obj)
            self.assertEqual(obj["unchanged_on_retry"],3)
            self.assertTrue(obj["partial_creation_rolled_back"])
            self.assertEqual(obj["live_figma_writes"],0)

if __name__=="__main__":
    unittest.main()
