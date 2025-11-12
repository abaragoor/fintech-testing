def assert_status_code(response, expected_code):
    assert response.status == expected_code, \
        f"Expected status code {expected_code}, but got {response.status}. Response: {response.text()}"

def assert_response_contains(response, key):
    try:
        data = response.json()
        assert key in data, f"Key '{key}' not found in response: {data}"
    except Exception as e:
        raise AssertionError(f"Failed to parse JSON or find key: {e}. Response: {response.text()}")