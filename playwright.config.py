"""
Playwright Configuration File for pytest-playwright
---------------------------------------------------
Defines browser options, base URLs for environments, and reporting behavior.
This file is auto-detected by pytest-playwright when you run `pytest`.
"""

import os

# Determine environment
ENV = os.getenv("ENV", "dev").lower()

BASE_URLS = {
    "dev": "http://localhost:5000",  # mock frontend
    "staging": "https://mock-ui.staging",
    "prod": "https://mock-ui.prod"
}

BASE_URL = BASE_URLS.get(ENV, BASE_URLS["dev"])

# Playwright test configuration dictionary
# pytest-playwright reads these as fixtures
def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=BASE_URL, help="Base URL for UI tests")
    parser.addoption("--browser", action="store", default="chromium", help="Browser: chromium, firefox, webkit")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode (default off)")
    parser.addoption("--slowmo", action="store", default=50, type=int, help="Delay in ms between actions for visibility")


def pytest_configure(config):
    """Optional global configuration hook."""
    base_url = config.getoption("--base-url")
    print(f"\nRunning Playwright tests on environment: {ENV}")
    print(f"Base URL: {base_url}\n")


# Default fixtures available:
# - `page` : for UI interaction
# - `browser` : for browser instance
# - `context` : for browser context

"""
Example run commands:
    pytest tests/ui --headed
    ENV=staging pytest tests/ui --browser=firefox --headed
    pytest tests/ui --base-url=http://localhost:8080
"""
