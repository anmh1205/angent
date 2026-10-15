# Kubernetes and cloud

Before changing live infrastructure identify:
- account/project/subscription and region;
- cluster and namespace/environment;
- resource identity and owner/controller;
- current desired configuration and live state;
- quotas/limits;
- secret/config dependencies;
- create/update/replace/delete semantics;
- traffic and data/state dependencies.

For Kubernetes inspect desired manifest and live/controller state separately.

For GitOps, edit the source of truth and let the reconciler own the apply path unless the task explicitly authorizes a different operational route.

For cloud resources preserve canonical resource identifiers. A seemingly small field change can force replacement.

Do not treat `apply` success as application readiness and do not delete/recreate a resource merely to converge state without reviewing data, identity and downstream dependencies.
