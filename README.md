# Automation Exercise Test Automation Framework

## Overview
An end-to-end UI and API test automation framework built with **Python** and **Pytest** to validate [Automation Exercise](https://automationexercise.com/). The framework uses the **Page Object Model (POM)** design pattern and **Data-Driven Testing (DDT)** to separate test logic, page locators, and external test data for high maintainability and scalability.

## Tech Stack
- **Language:** Python
- **Test Runner:** Pytest
- **UI & API Automation:** Selenium WebDriver / Playwright, Python `requests`
- **Design Pattern:** Page Object Model (POM) & Data-Driven Testing (JSON / CSV / Pytest Parametrize)
- **Reporting:** `pytest-html`

## Project Structure
```text
automation-exercise-framework/
├── pages/               # Page Object classes (Login, Registration, Home, etc.)
├── tests/               # UI, API, and Data-Driven test suites
├── data/                # External test datasets for data-driven scenarios
├── utils/               # Helper functions, config readers, and fixtures
├── reports/             # Generated HTML execution reports
├── requirements.txt     # Project dependencies
└── pytest.ini           # Pytest configuration and markers
