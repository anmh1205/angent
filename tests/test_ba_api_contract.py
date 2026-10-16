"""Compare Bruno tests to real OpenAPI 3.1 contract structure before creating a collection."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
BA=ROOT/"extensions/angent-ba"
sys.path.insert(0,str(BA/"scripts"))
from audit_api_contract import audit_contract
from build_bruno import compile_collection

class APIContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=json.loads((BA/"examples/synthetic-fleet-api-tests.json").read_text(encoding="utf8"))
        cls.spec=json.loads((BA/"examples/synthetic-fleet-openapi.json").read_text(encoding="utf8"))

    def test_real_synthetic_contract_matches_four_bruno_cases(self):
        result=audit_contract(self.spec,self.model)
        self.assertTrue(result["ok"],result)
        self.assertEqual(result["requests_checked"],4)
        self.assertEqual(result["contract_version"],"3.1.0")
        self.assertEqual(result["execution_status"],"not-run")
        self.assertTrue(self.spec["x-angent-mock-only"])
        generated=compile_collection(self.model,api_contract=self.spec)
        self.assertEqual(len([k for k in generated if k.endswith(".bru") and k.startswith("requests/")]),4)

    def test_wrong_status_and_field_are_caught(self):
        a=copy.deepcopy(self.model);a["requests"][0]["expected_status"]=202
        self.assertFalse(audit_contract(self.spec,a)["ok"])
        a=copy.deepcopy(self.model);a["requests"][1]["expected_json"]["unknown"]="secret"
        self.assertTrue(any("not declared" in e for e in audit_contract(self.spec,a)["errors"]))
        a=copy.deepcopy(self.model);a["requests"][1]["expected_json"]["error"]="BAD_VALUE"
        self.assertTrue(any("type, const or enum" in e for e in audit_contract(self.spec,a)["errors"]))

    def test_wrong_operation_and_post_body_are_caught(self):
        a=copy.deepcopy(self.model);a["requests"][0]["path"]="/vehicles/{{vehicleId}}/wrong"
        self.assertFalse(audit_contract(self.spec,a)["ok"])
        a=copy.deepcopy(self.model);a["requests"][3].pop("body_json")
        self.assertTrue(any("required JSON requestBody" in e for e in audit_contract(self.spec,a)["errors"]))
        a=copy.deepcopy(self.model);a["requests"][3]["body_json"]["unexpected"]=1
        self.assertTrue(any("undeclared body" in e for e in audit_contract(self.spec,a)["errors"]))

    def test_restricted_schema_does_not_fake_reference_support(self):
        a=copy.deepcopy(self.spec)
        a["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]={"$ref":"#/components/schemas/Vehicle"}
        self.assertFalse(audit_contract(a,self.model)["ok"])
        a=copy.deepcopy(self.spec)
        a["openapi"]="3.0.3"
        self.assertFalse(audit_contract(a,self.model)["ok"])

    def test_resolves_local_response_body_and_property_references(self):
        spec=copy.deepcopy(self.spec)
        components=spec.setdefault("components",{})
        schemas=components.setdefault("schemas",{})
        schemas["Vehicle"]={"type":"object","properties":{
            "vehicleId":{"type":"string"},"state":{"$ref":"#/components/schemas/VehicleState"}}}
        schemas["VehicleState"]={"type":"string","enum":["online","offline"]}
        response=spec["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]
        response["content"]["application/json"]["schema"]={"$ref":"#/components/schemas/Vehicle"}
        reqbody=spec["paths"]["/vehicles/{vehicleId}/diagnostics/ack"]["post"]["requestBody"]
        schemas["DTC"]={"type":"string"}
        schemas["AckBody"]={"type":"object","properties":{
            "code":{"$ref":"#/components/schemas/DTC"},"operator":{"type":"string"}},
            "required":["code","operator"],"additionalProperties":False}
        reqbody["content"]["application/json"]["schema"]={"$ref":"#/components/schemas/AckBody"}
        self.assertTrue(audit_contract(spec,self.model)["ok"],audit_contract(spec,self.model))
        generated=compile_collection(self.model,api_contract=spec)
        self.assertIn("requests/TC-FLEET-004.bru",generated)

    def test_rejects_remote_recursive_and_composed_refs(self):
        a=copy.deepcopy(self.spec)
        response=a["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]
        response["content"]["application/json"]["schema"]={"$ref":"https://example.com/schema.json"}
        self.assertTrue(any("Only local" in x for x in audit_contract(a,self.model)["errors"]))
        a=copy.deepcopy(self.spec)
        a["components"]={"schemas":{"Recursive":{"$ref":"#/components/schemas/Recursive"}}}
        a["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]={"$ref":"#/components/schemas/Recursive"}
        self.assertTrue(any("Recursive" in x for x in audit_contract(a,self.model)["errors"]))
        a=copy.deepcopy(self.spec)
        a["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]={"oneOf":[]}
        self.assertTrue(any("composition" in x for x in audit_contract(a,self.model)["errors"]))

    def test_auth_contract_mismatch_blocks_generation(self):
        a=copy.deepcopy(self.spec)
        a["paths"]["/vehicles/{vehicleId}/status"]["get"]["security"]=[{"bearerAuth":[]}]
        result=audit_contract(a,self.model)
        self.assertFalse(result["ok"])
        self.assertTrue(any("requires auth" in e for e in result["errors"]))
        with self.assertRaises(ValueError):
            compile_collection(self.model,api_contract=a)

if __name__=="__main__":
    unittest.main()
