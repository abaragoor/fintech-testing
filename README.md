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
├── tests/
│   ├── api/
│   │   ├── test_users_api.py
│   │   ├── test_transactions_api.py
│   │
│   ├── ui/
│   │   ├── test_user_registration_ui.py
│   │   └── test_transaction_ui.py
│
├── pages/
│   ├── base_page.py
│   ├── user_registration_page.py
│   └── transaction_page.py
│
├── data/
│   ├── test_data_factory.py
│   ├── user_data.json
│   └── transaction_data.json
│
├── utils/
│   ├── api_client.py
│   ├── config.py
│   ├── logger.py
│   └── report_manager.py
│
├── playwright.config.py
├── requirements.txt
└── README.md

#How to use this Framework
Unzip and enter the folder:
unzip automation-framework.zip -d automation-framework
cd automation-framework
Create and activate a virtualenv, then install deps:
python -m venv .venv && source .venv/bin/activate (macOS/Linux)
or .\\.venv\\Scripts\\activate (Windows)
pip install -r requirements.txt
Install Playwright browsers:
playwright install

#Setting the ENV to "dev" or "staging" or "production" server before executing the commands.

#Run tests:
pytest — runs all tests
pytest tests/api — API tests only
pytest tests/ui --headed — UI tests (open browser)

#Generate Reports
pytest --html=reports/report.html --self-contained-html