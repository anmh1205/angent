# Release verification

After deployment inspect:
- provider deployment/revision status;
- expected artifact/version;
- health/readiness;
- critical user/API smoke path;
- migration state;
- logs/errors for the rollout window.

For production, verify the exact endpoint users reach.

If staging and production share a build promotion model, verify the same immutable artifact was promoted when that is a project requirement.

Do not call a deployment complete while provider state is still converging unless the Contract allows asynchronous handoff.
