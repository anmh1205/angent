# Synthetic Fleet Requirements — Demonstration Data Only

This is an **invented test fixture**, not a record of a real IVTS deployment, stakeholder interview, production acceptance, or a person approving requirements. No claim in this file is evidence about live fleet authorization.

**BR-IVTS-01 — Proposed business rule:** For this hypothetical fleet, only an account owning the vehicle may see its private status. Shared and delegated permissions are deliberately not modeled here.

**FR-IVTS-01 — Proposed status reading:** When an authenticated account requests status for its own vehicle, the example backend returns a vehicle identifier and visible status. When it requests a vehicle not owned by that account, the example backend responds with access denied and does not expose vehicle details.

**FR-IVTS-02 — Proposed connectivity presentation:** The example status screen displays the latest connectivity state of a vehicle (e.g. connecting, connected, disconnected) and identifies changes over time. These example lifecycle states are *not* asserted as production ECU/GPS data semantics; actual state names and transition triggers require a real device/cloud contract.

**AC-IVTS-01 — Proposed denial criterion:** Given a request by an unrelated account, when status is read, the response does not disclose status details and a forbidden response is observable.

**TC-IVTS-01 — Draft example test:** Exercise access denial using a controlled loopback mock. This mock is not an authorization penetration test against live fleet devices.

These examples exist only to verify ID traceability across BA, D2, Bruno and six Reqwise OSS-compatible model shapes. No approval state is implied. Source identity validation means only that a declared file and ID exist, not that all statements in a diagram accurately implement its business semantics.
