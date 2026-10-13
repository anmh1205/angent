# Changelog

## 17.0.0 — ANGENT cognitive-core redesign

- Rebranded the canonical system from Cogent to **ANGENT**, with the repository `anmh1205/angent` as source of truth.
- Added first-class **ANGENT Reasoning** ownership for problem modeling, systems thinking, hypotheses, causal inference, decisions, dependency-aware planning and replanning.
- Upgraded Contract from a request envelope to an explicit task boundary and success-semantics owner.
- Reframed Context as authoritative state reconstruction instead of history retrieval.
- Reframed Research around evidence targeting and information gain for active uncertainties.
- Reframed Chat Work as **Execution**: act on an explicit plan, observe, reconcile and return evidence to Reasoning.
- Expanded Quality to judge solution integrity before communication integrity.
- Consolidated Feedback + Distill into **Learning**, preserving the distinction between observation, causal model and promoted mechanism.
- Renamed Checkpoint to **Continuity** while preserving durable PREPARED/COMMITTED/ATTEMPTED_UNKNOWN semantics.
- Retained the integrated Authoring architecture introduced in Cogent 15 rather than re-splitting planning, prose and Vietnamese realization.
