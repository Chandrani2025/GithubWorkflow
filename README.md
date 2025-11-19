# Selenium BDD (Behave) Framework — AutomationPractice

This project is a robust Selenium + Python test automation framework built with:
- BDD using `behave` (Cucumber-style features)
- Page Object Model (POM)
- Data-driven tests (Scenario Outline + JSON data)
- Allure reporting support
- CI pipelines for GitHub Actions and Azure DevOps

URL under test: `https://rahulshettyacademy.com/AutomationPractice/`

Quick start

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run tests (creates `results/` with artifacts):

```bash
chmod +x scripts/run_behave.sh
./scripts/run_behave.sh
```

3. Run tests and produce Allure results (requires Allure CLI to generate HTML):

```bash
ALLURE=true ./scripts/run_behave.sh
# then (if Allure CLI installed):
./scripts/generate_allure_report.sh
```

CI

- GitHub Actions workflow: `.github/workflows/ci.yml` (installs Allure CLI, runs tests with Allure, uploads artifacts).
- Azure DevOps pipeline: `azure-pipelines.yml` (similar steps).

Report locations

- `results/junit/` — JUnit XML
- `results/cucumber.json` — Cucumber JSON
- `results/allure-results/` — Allure raw results (when `ALLURE=true`)
- `results/allure-report/` — Allure HTML (after running `generate_allure_report.sh`)
- `results/screenshots/` — screenshots saved on scenario failures

