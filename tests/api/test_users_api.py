import pytest
from utils.api_client import ApiClient
from data.test_data_factory import create_user_data

client = ApiClient()

@pytest.fixture(scope="module")
def created_user():
    """Fixture to create and yield a user ID for CRUD tests"""
    payload = create_user_data()
    resp = client.post("/api/users", payload)
    assert resp.status_code in (200, 201)
    data = resp.json()
    user_id = data.get("id") or data.get("userId", "123")
    yield user_id

# ------------------ CRUD TESTS ------------------

def test_create_user_success():
    """C: Create user successfully"""
    payload = create_user_data()
    resp = client.post("/api/users", payload)
    assert resp.status_code in (200, 201)
    data = resp.json()
    assert data["email"] == payload["email"]
    assert "id" in data or "userId" in data

def test_get_user_success(created_user):
    """R: Read user details"""
    resp = client.get(f"/api/users/{created_user}")
    assert resp.status_code == 200
    assert "email" in resp.json()

def test_update_user_account_type(created_user):
    """U: Update user's account type"""
    update_payload = {"accountType": "standard"}
    resp = client.post(f"/api/users/{created_user}/update", update_payload)
    assert resp.status_code in (200, 204)

def test_delete_user(created_user):
    """D: Delete user record"""
    resp = client.post(f"/api/users/{created_user}/delete", {})
    assert resp.status_code in (200, 204)

# ------------------ ERROR SCENARIO TESTS ------------------

def test_create_user_missing_email():
    """Error: Missing required field"""
    payload = {"name": "Test User"}  # no email field
    resp = client.post("/api/users", payload)
    assert resp.status_code in (400, 422)
    data = resp.json()
    assert "error" in data or "message" in data

def test_get_user_invalid_id():
    """Error: Invalid user ID"""
    resp = client.get("/api/users/!@#")
    assert resp.status_code in (400, 404)

def test_create_user_duplicate_email():
    """Error: Duplicate user email"""
    user = create_user_data()
    client.post("/api/users", user)  # first creation
    resp = client.post("/api/users", user)  # duplicate
    assert resp.status_code in (400, 409)

# ------------------ DATA VALIDATION TESTS ------------------

def test_create_user_invalid_email_format():
    """Validation: Invalid email format"""
    payload = {"name": "Test", "email": "not-an-email", "accountType": "premium"}
    resp = client.post("/api/users", payload)
    assert resp.status_code in (400, 422)

def test_create_user_invalid_account_type():
    """Validation: Invalid account type"""
    payload = {"name": "John", "email": "john@example.com", "accountType": "unknown-type"}
    resp = client.post("/api/users", payload)
    assert resp.status_code in (400, 422)

# ------------------ AUTHENTICATION / AUTHORIZATION TESTS ------------------

def test_get_user_unauthorized(monkeypatch):
    """Auth: Missing or invalid token should be rejected"""
    # mock API client call with invalid header
    unauthorized_headers = {"Authorization": "Bearer invalid_token"}
    resp = client.get("/api/users/123", headers=unauthorized_headers)
    assert resp.status_code in (401, 403)

def test_create_user_without_auth():
    """Auth: No token -> unauthorized"""
    resp = client.post("/api/users", create_user_data(), headers={})
    assert resp.status_code in (401, 403)
