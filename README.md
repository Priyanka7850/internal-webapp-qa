# QA Automation Framework - UI & API Testing

## Tech Stack
- **UI Testing**: Selenium, Pytest
- **API Testing**: Requests, Pytest
- **CI/CD**: GitHub Actions
- **Reports**: Allure, HTML

## Overview
This **QA Automation Framework** provides robust support for automated **UI** and **API** testing for **E-Commerce** websites. Designed for scalability and efficiency, the framework integrates seamlessly with **GitHub Actions** for **continuous testing** and **deployment**. Additionally, it generates comprehensive **Allure** and **HTML** test reports for detailed insights into test execution.

## Setup and Installation

### 1. Prerequisites
Ensure the following are installed before getting started:
- **Python 3.9+**
- **Google Chrome** (latest stable version) and **ChromeDriver** matching your installed Chrome version.

### 2. Clone the Repository
Clone this repository and navigate into the project directory:
```bash
git clone https://github.com/yourusername/qa-automation-framework.git
cd qa-automation-framework

### 3. Install Dependencies
Install the required Python dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt

Running the Tests
UI Tests
To execute the UI test suite, navigate to the ui_tests folder and run:

bash
Copy
Edit
pytest test_homepage.py
API Tests
To execute the API test suite, navigate to the api_tests folder and run:

bash
Copy
Edit
pytest test_get_orders.py
Run All Tests
To run both UI and API tests in one go, simply run:

bash
Copy
Edit
pytest
CI/CD Integration
This project is integrated with GitHub Actions to automate the testing process. The workflow configuration is defined in .github/workflows/ci.yml, ensuring that tests are run automatically on each commit or pull request.

Test Reports
HTML Report: After test execution, you can find the HTML report at reports/html/.

Allure Report: For a detailed and interactive report, run the following command:

bash
Copy
Edit
allure serve reports/allure-results
This will generate an interactive Allure report showing the detailed results of each test run.

Conclusion
This QA Automation Framework provides a comprehensive, scalable, and efficient solution for automated UI and API testing. With integrated CI/CD pipelines and detailed test reports, the framework ensures reliable, continuous testing and helps maintain high software quality.

By utilizing this framework, teams can easily execute tests, monitor results, and improve application stability and performance.

