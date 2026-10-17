"""Compile all six real OSS diagram kinds from independent semantic fixtures."""
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
FIGMA=ROOT/"extensions/angent-figma"
sys.path.insert(0,str(FIGMA/"scripts"))
from to_reqwise_payload import compile_model

class FullOSSContractTests(unittest.TestCase):
    def test_all_six_oss_kinds_and_no_live_write(self):
        for kind in ("activity","sequence","state","erd","userflow","sitemap"):
            with self.subTest(kind=kind):
                path=FIGMA/"examples"/f"rental-fleet-{kind}.json"
                model=json.loads(path.read_text(encoding="utf-8"))
                output=compile_model(model)
                self.assertEqual(output["arguments"]["type"],kind)
                self.assertTrue(output["arguments"]["spec"]["options"]["dryRun"])
                self.assertEqual(output["arguments"]["spec"]["options"]["verify"],True)
                self.assertFalse(output["writes_performed"])
                self.assertTrue(output["requires_live_mcp"])
                spec=output["arguments"]["spec"]
                field={"activity":"nodes","sequence":"messages","state":"states",
                       "erd":"entities","userflow":"nodes","sitemap":"pages"}[kind]
                self.assertTrue(spec[field])
    def test_no_fake_pro_kind(self):
        with self.assertRaises(ValueError):
            compile_model({"type":"bpmn","nodes":[{"id":"start","label":"Start"}],"edges":[]})
if __name__=="__main__":
    unittest.main()
