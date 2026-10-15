# SauceDemo UI Test Automation

A QA portfolio project for testing the SauceDemo e-commerce application (https://www.saucedemo.com/) using Python, Playwright, and Pytest.
The project covers login and the purchase journey from product selection to order confirmation. It includes both direct test scripts and a Page Object Model (POM) implementation, demonstrating how page interactions can be organized into reusable classes.

## Branches
| Branch | Contents |
| --- | --- |
| `main` | Initial login and checkout test scripts. |
| [`page-object-model`](https://github.com/cyl2chan/playwright-saucedemo/tree/page-object-model) | Expanded page objects, CSV-driven tests, Docker configuration, and GitHub Actions workflow. |

## Technology Stack
- **Python** — test implementation.
- **Playwright** — browser automation and UI assertions.
- **Pytest / pytest-playwright** — test execution, parametrization, and browser fixtures.
- **CSV files** — external login and product test data.
- **pytest-html** — self-contained HTML test reports.
- **Docker** — containerized test execution using the official Playwright Python image.
- **GitHub Actions** — automated execution and report uploads.

## Test Coverage
| Area | Implemented scenario and checks |
| --- | --- |
| Login | Submit credentials from CSV data and verify navigation to the inventory page. |
| Product selection | Select each product listed in the inventory CSV and add it to the cart. |
| Cart | Check that the cart displays the selected product name. |
| Checkout | Enter customer details, continue to the overview, and finish the order. |
| Order confirmation | Verify that “Thank you for your order!” is visible. |

The POM checkout test runs separately for each product in the CSV.

## Test Design
Page classes contain locators and actions for login, products, cart, customer information, checkout overview, and order confirmation. Test files combine those actions into user journeys.
pytest.mark.parametrize supplies login credentials and product names from CSV files, allowing additional cases to be added without duplicating the test flow. The tests use the page fixture supplied by pytest-playwright.

## Project Structure
```
pages/                        Page classes and UI interactions
tests/
  test_login_POM.py            CSV-driven login tests
  test_checkout_POM.py         CSV-driven checkout tests
  test_login_single.py         Direct login test script
  test_checkout_single.py      Direct checkout test script
test_data/
  login_data.csv              Login credentials
  inventory_data.csv          Product names
.github/workflows/tests.yml    CI workflow
requirements.txt              Python dependencies
pytest.ini                    Pytest configuration
dockerfile                    Playwright container definition
reports/                      HTML report output
```

## Local Setup
Prerequisites: Git, Python with venv support, and internet access to SauceDemo. The configured browser is Chromium.
```bash
  git clone https://github.com/cyl2chan/playwright-saucedemo.git
  cd playwright-saucedemo
  git switch page-object-model
```

Activate the virtual environment:

**Windows PowerShell**
```bash
  .\.venv\Scripts\Activate.ps1
```
**Linux**
```bash
  source .venv/bin/activate
```

Install dependencies and Chromium:
```bash
  python -m pip install -r requirements.txt
  python -m playwright install chromium
```

## Run the POM Tests
Run more than one tests togather:
```bash
  python -m pytest tests/test_login_POM.py tests/test_checkout_POM.py
```

Run one test at a time:
```bash
  python -m pytest tests/test_login_POM.py
  python -m pytest tests/test_checkout_POM.py --headed
```

Capture traces and screenshots for failed tests:
```bash
  python -m pytest tests/test_login_POM.py tests/test_checkout_POM.py --tracing=retain-on-failure --screenshot=only-on-failure
```

The configured HTML report is written to reports/report.html.

## Docker
For Docker, first build the image:
```bash
  docker build -f dockerfile -t playwright-tests .
```
Then run the container:
```bash
  docker run --rm playwright-tests
```
The report is generated inside the container. To get it out:
```bash
  docker run --rm -v $(pwd)/reports:/app/reports playwright-tests
```
Example of workflow with docker:
https://github.com/cyl2chan/playwright-saucedemo/actions/runs/37501034816/job/112397782399

## Caching
Code for caching in tests.yml is commented out.

Example of workflow using caching: https://github.com/cyl2chan/playwright-saucedemo/actions/runs/37020379822/job/110881634084 

## Continuous Integration
Workflow on the POM branch is configured for pushes to main and pull requests targeting main. 
It also does the following:
  - builds a Docker image, 
  - runs tests in a container,
  - uploads **test artifacts** under Github Actions when test fail (eg.https://github.com/cyl2chan/playwright-saucedemo/actions/runs/37020964420/job/110883618436), and 
  - report.html under folder reports/ as the test-report artifact.

## Purpose
Built as a hands-on QA automation portfolio to demonstrate browser testing, reusable page objects, data-driven scenarios, test reporting, and CI configuration against a public practice application.


