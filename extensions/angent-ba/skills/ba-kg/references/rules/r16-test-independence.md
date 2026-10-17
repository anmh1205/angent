# R16: Test independence and effective assertions

## Operational contract

Tests must state what failed behavior they would detect and how a regression is observable. A passing unit test that only searches generated code for 'expect' is not runtime proof.

## Checks before accepting an artifact

Separate synthetic mock, local integration, provider sandbox, staging and production evidence. Use a negative mutation or counterexample when practical to demonstrate the assertion bites.

## Failure response

Each case needs source links, input/fixture boundaries, steps, expected status/state side effect, cleanup and observed result. Keep blocked/skipped separate from pass.

## Grounded example

The generated login suite passed seven Chrome cases and correctly failed when an error message was deliberately changed. It still cannot prove actual account security.

**Evidence boundary:** specialist advice does not establish completed provider writes or approve business requirements. The actual source and observed result remain decisive; ANGENT Root and Quality retain oversight.
