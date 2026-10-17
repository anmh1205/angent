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

    def test_openapi_response_range_and_default_are_valid(self):
        spec=copy.deepcopy(self.spec)
        responses=spec["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]
        responses["2XX"]=responses.pop("200")
        responses["default"]=responses.pop("403")
        responses["5XX"]=responses.pop("503")
        result=audit_contract(spec,self.model)
        self.assertTrue(result["ok"],result)
        self.assertEqual(result["requests_checked"],4)
        self.assertIn("requests/TC-FLEET-002.bru",compile_collection(self.model,api_contract=spec))
        # Explicit status must win over a general range, even when the schema differs.
        responses["403"]={"description":"conflicting specific 403","content":{
            "application/json":{"schema":{"type":"object","properties":{"other":{"type":"string"}}}}}}
        self.assertFalse(audit_contract(spec,self.model)["ok"])

    def test_security_is_or_of_and_requirements_not_a_truthy_list(self):
        original=copy.deepcopy(self.spec)
        op=original["paths"]["/vehicles/{vehicleId}/status"]["get"]
        original["components"]={"securitySchemes":{
            "bearerAuth":{"type":"http","scheme":"bearer"},
            "keyAuth":{"type":"apiKey","in":"header","name":"X-API-Key"}}}
        original["security"]=[{"bearerAuth":[]}]
        original["paths"]["/vehicles/{vehicleId}/diagnostics/ack"]["post"]["security"]=[]
        self.assertFalse(audit_contract(original,self.model)["ok"])
        op["security"]=[{"bearerAuth":[]},{}]
        self.assertTrue(audit_contract(original,self.model)["ok"],audit_contract(original,self.model))
        op["security"]=[{"bearerAuth":[]},{"keyAuth":[]}]
        request=copy.deepcopy(self.model)
        for test in request["requests"][:3]:
            test["auth"]="bearer"
        # The fourth POST explicitly overrides root authentication as anonymous.
        request["requests"][3]["auth"]="none"
        self.assertTrue(audit_contract(original,request)["ok"],audit_contract(original,request))
        op["security"]=[{"bearerAuth":[],"keyAuth":[]}]
        self.assertFalse(audit_contract(original,request)["ok"])
        self.assertTrue(any("bearer-only" in msg for msg in audit_contract(original,request)["errors"]))
        op["security"]=[]
        for test in request["requests"]:
            test["auth"]="none"
        self.assertTrue(audit_contract(original,request)["ok"],audit_contract(original,request))

    def test_nonfinite_python_numbers_cannot_be_valid_json_schema_values(self):
        from audit_api_contract import _match_scalar
        for bad in (float("nan"),float("inf"),float("-inf")):
            with self.subTest(value=repr(bad)):
                self.assertFalse(_match_scalar(bad,{"type":"number"},self.spec))
                spec=copy.deepcopy(self.spec)
                model=copy.deepcopy(self.model)
                op=spec["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]
                op["content"]["application/json"]["schema"]["properties"]["vehicleId"]={"type":"number"}
                model["requests"][0]["expected_json"]["vehicleId"]=bad
                self.assertFalse(audit_contract(spec,model)["ok"])

    def test_json_schema_nullable_and_value_boundaries(self):
        spec=copy.deepcopy(self.spec)
        ok_model=copy.deepcopy(self.model)
        op=spec["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]
        fields=op["content"]["application/json"]["schema"]["properties"]
        fields["state"]={"type":["string","null"],"minLength":3,"maxLength":10}
        self.assertTrue(audit_contract(spec,ok_model)["ok"],audit_contract(spec,ok_model))
        ok_model["requests"][0]["expected_json"]["state"]="ab"
        self.assertFalse(audit_contract(spec,ok_model)["ok"])
        ok_model["requests"][0]["expected_json"]["state"]=None
        self.assertTrue(audit_contract(spec,ok_model)["ok"],audit_contract(spec,ok_model))
        fields["vehicleId"]={"type":"string","pattern":"^[0-9]+$"}
        self.assertFalse(audit_contract(spec,ok_model)["ok"])
        fields.pop("vehicleId")
        fields["vehicleId"]={"type":"string"}
        fields["state"]={"type":"string","enum":["online","offline"]}
        ok_model["requests"][0]["expected_json"]["state"]="online"
        schema=spec["paths"]["/vehicles/{vehicleId}/diagnostics/ack"]["post"]["requestBody"]["content"]["application/json"]["schema"]
        schema["properties"]["operator"]={"type":"string","minLength":20}
        self.assertFalse(audit_contract(spec,ok_model)["ok"])

    def test_rejects_unreflected_2020_12_constraints_instead_of_false_green(self):
        spec=copy.deepcopy(self.spec)
        schema=spec["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]
        schema["minProperties"]=4
        errors=audit_contract(spec,self.model)["errors"]
        self.assertTrue(any("Unsupported object JSON Schema constraints" in e for e in errors),errors)
        spec=copy.deepcopy(self.spec)
        schema=spec["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]
        schema["properties"]["state"]={"$ref":"#/components/schemas/State","maxLength":2}
        spec["components"]={"schemas":{"State":{"type":"string"}}}
        self.assertTrue(any("$ref sibling" in e for e in audit_contract(spec,self.model)["errors"]))
        spec=copy.deepcopy(self.spec)
        schema=spec["paths"]["/vehicles/{vehicleId}/status"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]
        schema["properties"]["state"]={"type":"string","pattern":"^off"}
        self.assertFalse(audit_contract(spec,self.model)["ok"])
        spec=copy.deepcopy(self.spec)
        body=spec["paths"]["/vehicles/{vehicleId}/diagnostics/ack"]["post"]["requestBody"]["content"]["application/json"]["schema"]
        body["dependentRequired"]={"code":["approvedBy"]}
        self.assertFalse(audit_contract(spec,self.model)["ok"])

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
