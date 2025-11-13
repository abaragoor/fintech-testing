# fintech-testing
Test Automation Framework for FinTech
Copyright 2025 - Arati Baragoor

#Scenario
#Imagine yourself at a hypothetical fintech company that processes financial transactions through
#a microservices architecture. The system includes:
#● User Service (Node.js/Express + MongoDB)
#● Transaction Service (Node.js/Express + MongoDB)
#● Notification Service (Node.js/Express + Redis)
#● API Gateway (Routes requests to services

#Automation Structure
automation-framework/
│
├── conftest.py                 ← screenshot hook + report integration
├── playwright.config.py        ← environment + browser settings
├── floqast_frontend/
│   ├── server.py
│   └── templates/...
├── data/
│   ├── test_data_factory.py
│   ├── user_data.json
│   └── transaction_data.json
├── pages/
│   ├── base_page.py
│   ├── user_registration_page.py
│   └── transaction_page.py
├── tests/
│   ├── api/...
│   └── ui/...
├── utils/
│   ├── api_client.py
│   ├── logger.py
│   ├── config.py
│   └── report_manager.py
├── reports/
│   └── (generated output)
├── requirements.txt
└── README.md


#How to use this Framework

#1 Unzip and enter the folder:

unzip automation-framework.zip -d automation-framework
cd automation-framework
Create and activate a virtualenv, then install deps:
python -m venv .venv && source .venv/bin/activate (macOS/Linux)
or .\\.venv\\Scripts\\activate (Windows)
pip install -r requirements.txt
Install Playwright browsers:
playwright install

#2 Setting the ENV to "dev" or "staging" or "production" server before executing the test commands in "config.py"

#3 Run tests:
pytest — runs all tests
pytest tests/api — API tests only
pytest tests/ui --headed — UI tests (open browser)

#4 Generate Reports
pytest --html=reports/report.html --self-contained-html

| Category                 | Description                                      | Example                                                         |
| ------------------------ | ------------------------------------------------ | --------------------------------------------------------------- |
| **CRUD**                 | Create, Read, Update, Delete operations          | `test_create_user`, `test_delete_transaction`                   |
| **Error Handling**       | Simulate missing fields, invalid IDs, duplicates | `test_create_user_missing_email`, `test_get_user_invalid_id`    |
| **Data Validation**      | Check server rejects invalid email, type, etc.   | `test_create_user_invalid_email_format`                         |
| **Auth / Authorization** | Ensure endpoints enforce security                | `test_get_user_unauthorized`, `test_create_transaction_no_auth` |
