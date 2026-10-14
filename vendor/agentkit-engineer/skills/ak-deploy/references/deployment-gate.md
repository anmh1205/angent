# Deployment gate

Before the concrete deployment invocation, verify:

- exact provider/account/organization/project/service;
- exact environment/region/domain when material;
- immutable/reproducible artifact identity when the project requires it;
- config/secret presence without exposing values;
- migration compatibility;
- required build/test/review state;
- expected traffic/cost/outward-facing effect;
- health/readiness and critical smoke plan;
- rollback/forward-fix option;
- **current authority bound to the resolved target, artifact and material command/action arguments**.

If any material target/argument changes after this check, revalidate authority before executing.

For production, preserve stronger evidence than for preview/staging.

A successful upload is not a healthy deployment.
