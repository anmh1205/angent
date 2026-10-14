# Security scan pattern guidance

Pattern libraries are candidate generators, not verdicts.

## Secrets

High-confidence classes include:
- provider-issued key/token prefixes;
- private-key headers;
- credential-bearing connection strings;
- hardcoded password/token/secret assignments.

Medium-confidence generic assignments require surrounding-context review.

Exclude or downgrade obvious placeholders, examples, generated dependencies and test fixtures only when the context really proves they are non-live.

Never echo matched secret values into reports.

## Code patterns

Common triage classes include:
- dynamic SQL construction;
- unescaped HTML/DOM sinks;
- command execution with untrusted input;
- user-controlled filesystem paths;
- insecure randomness for security-sensitive values;
- dynamic evaluation/deserialization;
- disabled TLS/certificate verification;
- sensitive logging/debug configuration.

For every match, inspect the data flow and protection around the site. A dangerous API name without attacker-controlled input may not be a vulnerability.

## Repository exposure

Check whether sensitive environment/credential files are tracked or insufficiently ignored.

A filename alone is not evidence that the file contains a live secret.

## Severity

Use actual credential sensitivity, reachability, privilege and impact.

Do not promote severity merely because a pattern is famous or a scanner assigns a label.
