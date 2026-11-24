# Restful Booker API Automation Framework

A Python-based API automation framework built using **Pytest, Requests and Allure** to automate and validate REST API operations.

## Project Overview

This project automates the RESTful Booker public API and covers positive and negative API test scenarios.

## Tech Stack

- Python
- Pytest
- Requests
- PyYAML
- Allure Reports
- Pytest HTML Reports

## Project Structure

```text
RestfulBooker-API-Automation/
├── api/
│   ├── base_api.py
│   └── booking_api.py
├── config/
│   └── config.yaml
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_booking.py
├── test_data/
│   └── booking_data.json
├── utils/
│   └── logger.py
├── reports/
├── pytest.ini
├── requirements.txt
└── .gitignore
```

## Features

- Reusable API request methods (GET, POST, PUT, PATCH and DELETE)
- Authentication using token-based authorization
- Positive and negative test scenarios
- Pytest fixtures for reusable setup
- Parameterized test cases
- External test data using JSON
- Centralized configuration using YAML
- Logging of API requests and responses
- Allure test reporting
- HTML test reporting

## Installation

Clone the repository:

```bash
git clone https://github.com/Joel-Abrm/RestfulBooker-API-Automation.git
```

Navigate to the project:

```bash
cd RestfulBooker-API-Automation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Execute Tests

Run all tests:

```bash
python -m pytest
```

Generate an HTML report:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Generate Allure results:

```bash
python -m pytest --alluredir=reports/allure-results
```

Generate and open the Allure report (Allure CLI and Java required):

```bash
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

## API Under Test

RESTful Booker API:

https://restful-booker.herokuapp.com

API Documentation:

https://restful-booker.herokuapp.com/apidoc/index.html

## Author

**Joel Abraham**

GitHub: https://github.com/Joel-Abrm