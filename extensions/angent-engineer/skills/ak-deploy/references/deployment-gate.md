# Deployment gate

Verify:
- immutable/reproducible artifact identity when the project requires it;
- environment selection;
- config/secret presence without exposing values;
- migration compatibility;
- health/readiness;
- critical smoke path;
- provider-reported release state;
- rollback/forward-fix option.

For production, preserve stronger evidence than for preview/staging.

A successful upload is not a healthy deployment.
