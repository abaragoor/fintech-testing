import os

class Config:
    ENV = os.getenv("ENV", "dev")

    ENV_URLS = {
        "dev": "http://localhost:3000",
        "staging": "https://floqast-api.staging",
        "prod": "https://floqast-api.prod"
    }

    BASE_URL = ENV_URLS.get(ENV)
    REPORT_DIR = "reports"
