"""Synthetic fleet access policy *illustration*, not the user's IVTS implementation."""

def may_read_vehicle_status(request_account: str, registered_owner: str) -> bool:
    """Reject access when current account does not own this particular vehicle."""
    return bool(request_account) and request_account == registered_owner


def public_status(request_account: str, registered_owner: str, status: dict) -> dict:
    """Illustrative business-layer guard; no authentication or HTTP runtime."""
    if not may_read_vehicle_status(request_account, registered_owner):
        return {"error": "ACCESS_DENIED"}
    return {"status": status}
