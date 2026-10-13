# Kubernetes and cloud

Before changing live infrastructure identify:
- cluster/account/project/region;
- namespace/environment;
- resource owner;
- current rollout/state;
- quotas/limits;
- secret/config dependencies.

For Kubernetes inspect desired manifest and live state separately.

For cloud resources preserve resource identifiers and deletion/replace semantics.

Do not treat `apply` success as application readiness.
