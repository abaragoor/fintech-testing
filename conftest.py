# conftest.py
import os
import pytest

# Ensure screenshots directory exists
SCREENSHOT_DIR = os.path.join("reports", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take a screenshot automatically on UI test failure."""
    outcome = yield
    result = outcome.get_result()

    # Only capture if the test failed and the 'page' fixture is available
    if result.failed and "page" in item.fixturenames:
        page = item.funcargs["page"]
        test_name = item.name.replace("/", "_").replace("::", "_")
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"{test_name}.png")

        try:
            page.screenshot(path=screenshot_path)
            print(f"\n🖼️  Saved screenshot for failed test: {screenshot_path}")
        except Exception as e:
            print(f"⚠️  Could not save screenshot: {e}")
