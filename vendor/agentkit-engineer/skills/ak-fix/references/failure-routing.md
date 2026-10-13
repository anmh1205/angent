# Failure routing

## Direct fix

Appropriate when:
- defect mechanism is obvious and deterministic;
- owner is known;
- change is local and low-risk;
- verification is straightforward.

## Debug first

Required when:
- several causes remain plausible;
- failure is intermittent/environment-specific;
- state crosses layers;
- previous fixes failed;
- the suspected fix does not explain the symptom.

## Reasoning/Plan first

Required when the “fix” is actually an architecture/product behavior decision.

Do not use workflow labels as ceremony; choose the minimum route that protects correctness.
