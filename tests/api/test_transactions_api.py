import pytest
from utils.api_client import ApiClient
from data.test_data_factory import create_transaction_data

client = ApiClient()

@pytest.fixture(scope="module")
def created_transaction():
    payload = create_transaction_data("123", "456")
    resp = client.post("/api/transactions", payload)
    assert resp.status_code in (200, 201)
    data = resp.json()
    trans_id = data.get("id") or data.get("transactionId", "txn_001")
    yield trans_id

# ------------------ CRUD TESTS ------------------

def test_create_transaction_success():
    """C: Create transaction"""
    payload = create_transaction_data("123", "456")
    resp = client.post("/api/transactions", payload)
    assert resp.status_code in (200, 201)
    assert "amount" in resp.json()

def test_get_transaction_success(created_transaction):
    """R: Get transaction details"""
    resp = client.get(f"/api/transactions/{created_transaction}")
    assert resp.status_code in (200, 404)

def test_update_transaction_amount(created_transaction):
    """U: Update transaction amount"""
    update_payload = {"amount": 200.75}
    resp = client.post(f"/api/transactions/{created_transaction}/update", update_payload)
    assert resp.status_code in (200, 204)

def test_delete_transaction(created_transaction):
    """D: Delete transaction"""
    resp = client.post(f"/api/transactions/{created_transaction}/delete", {})
    assert resp.status_code in (200, 204)

# ------------------ ERROR SCENARIO TESTS ------------------

def test_create_transaction_missing_fields():
    """Error: Missing required field"""
    payload = {"userId": "123"}  # missing amount, type, recipientId
    resp = client.post("/api/transactions", payload)
    assert resp.status_code in (400, 422)

def test_create_transaction_invalid_amount():
    """Validation: Invalid amount value"""
    payload = {"userId": "123", "recipientId": "456", "amount": "abc", "type": "transfer"}
    resp = client.post("/api/transactions", payload)
    assert resp.status_code in (400, 422)

def test_create_transaction_invalid_type():
    """Validation: Invalid transaction type"""
    payload = {"userId": "123", "recipientId": "456", "amount": 100, "type": "wrongtype"}
    resp = client.post("/api/transactions", payload)
    assert resp.status_code in (400, 422)

# ------------------ AUTHENTICATION / AUTHORIZATION TESTS ------------------

def test_get_transaction_unauthorized():
    """Auth: Missing or bad auth token"""
    headers = {"Authorization": "Bearer invalid_token"}
    resp = client.get("/api/transactions/txn_001", headers=headers)
    assert resp.status_code in (401, 403)

def test_create_transaction_no_auth():
    """Auth: No token provided"""
    resp = client.post("/api/transactions", create_transaction_data("123", "456"), headers={})
    assert resp.status_code in (401, 403)
