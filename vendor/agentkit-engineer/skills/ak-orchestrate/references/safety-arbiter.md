# Orchestration safety and arbitration

## Safety

For each job make explicit:
- working directory;
- writable files/roots;
- expected external effects;
- destructive/credentialed operations;
- timeout;
- acceptance output.

Worktrees prevent file collisions; they are not OS sandboxes.

Do not place secrets/cookies/private keys in prompts or captured reports.

External destructive/deployment/release effects need the same authorization as if a single agent performed them.

## Arbiter

Use an independent reviewer when:
- high-risk implementation is being accepted;
- parallel workers produce conflicting conclusions;
- integration crosses important interfaces;
- the user requested competing approaches.

The arbiter compares results with the original job contract and evidence.

It must flag:
- unsupported claims;
- missing artifacts/checks;
- contradictions;
- safety gaps;
- failed or timed-out jobs.

Do not majority-vote worker opinions.
