"""Git-pinned BA code witnesses: real commit blobs, exact excerpts and negative cases."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from verify_code_witness import inspect

class CodeWitnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph=json.loads((BA/"examples/rental-fleet-traceability.json").read_text(encoding="utf8"))
        cls.ledger=json.loads((BA/"examples/code-evidence/synthetic-code-witness.json").read_text(encoding="utf8"))
        cls.sha=subprocess.check_output(["git","-C",str(ROOT),"rev-parse","HEAD"],text=True).strip()

    def test_real_pinned_commit_and_honest_scope(self):
        report=inspect(ROOT,self.sha,self.ledger,self.graph)
        self.assertTrue(report["ok"])
        self.assertEqual(report["revision"],self.sha)
        self.assertEqual(report["linked_requirement_ids"],["FR-IVTS-01"])
        self.assertEqual(report["verified_count"],1)
        self.assertEqual(report["witnesses"][0]["lines"],[3,5])
        self.assertEqual(len(report["witnesses"][0]["sha256"]),64)
        self.assertEqual(report["semantic_alignment"],"not-assessed")
        self.assertFalse(report["deployment_verified"])
        self.assertFalse(report["writes_performed"])

    def test_wrong_excerpt_or_hash_rejected(self):
        a=copy.deepcopy(self.ledger)
        a["witnesses"][0]["expected_excerpt"]="return True  # invented"
        with self.assertRaisesRegex(ValueError,"Expected excerpt absent"):
            inspect(ROOT,self.sha,a,self.graph)
        a=copy.deepcopy(self.ledger)
        a["witnesses"][0]["sha256"]="0"*64
        with self.assertRaisesRegex(ValueError,"fingerprint mismatch"):
            inspect(ROOT,self.sha,a,self.graph)

    def test_invalid_commit_or_unsafe_source_path_rejected(self):
        with self.assertRaisesRegex(ValueError,"Git source read failed"):
            inspect(ROOT,"0"*40,self.ledger,self.graph)
        a=copy.deepcopy(self.ledger)
        a["witnesses"][0]["path"]="../unrelated/private.py"
        with self.assertRaisesRegex(ValueError,"Unsafe or invalid"):
            inspect(ROOT,self.sha,a,self.graph)
        a=copy.deepcopy(self.ledger)
        a["witnesses"][0]["path"]="src/missing.py"
        with self.assertRaisesRegex(ValueError,"Git source read failed"):
            inspect(ROOT,self.sha,a,self.graph)

    def test_unknown_requirement_or_doubled_witness_rejected(self):
        a=copy.deepcopy(self.ledger)
        a["witnesses"][0]["requirement_id"]="FR-OTHER-999"
        with self.assertRaisesRegex(ValueError,"Unknown BA"):
            inspect(ROOT,self.sha,a,self.graph)
        a=copy.deepcopy(self.ledger)
        a["witnesses"].append(copy.deepcopy(a["witnesses"][0]))
        with self.assertRaisesRegex(ValueError,"Duplicate code witness"):
            inspect(ROOT,self.sha,a,self.graph)

    def test_line_bounds_are_strict(self):
        a=copy.deepcopy(self.ledger)
        a["witnesses"][0]["line_end"]=99999
        with self.assertRaisesRegex(ValueError,"bounded source line range"):
            inspect(ROOT,self.sha,a,self.graph)
        a=copy.deepcopy(self.ledger)
        a["witnesses"][0]["line_start"]=10
        a["witnesses"][0]["line_end"]=13
        with self.assertRaisesRegex(ValueError,"line range exceeds"):
            inspect(ROOT,self.sha,a,self.graph)

if __name__=="__main__":
    unittest.main()
