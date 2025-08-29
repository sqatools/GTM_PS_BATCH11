# OrangeHRM Automation Test Suite

This comprehensive automation test suite covers the OrangeHRM application with 20+ test cases across Admin, Leave, and Maintenance modules.

## 🎯 Test Coverage

### Admin Module (25 Test Cases)
- **User Management**: Users navigation
- **Job Management**: Job Titles, Pay Grades, Employment Status, Job Categories, Work Shifts
- **Organization**: General Information, Locations, Structure
- **Qualifications**: Skills, Education, Licenses, Languages, Memberships
- **Nationalities**: Nationalities management
- **Corporate Branding**: Branding configuration
- **Configuration**: Email, Subscriptions, Localization, Modules, Social Media Auth, OAuth Client

### Leave Module (15 Test Cases)
- **Leave List**: Leave list navigation and search
- **Apply Leave**: Leave application form
- **My Leave**: Personal leave records
- **Entitlements**: Add, Employee, and Personal entitlements
- **Reports**: Leave entitlements and usage reports
- **Configure**: Leave Types, Period, Work Week, Holidays

### Maintenance Module (6 Test Cases)
- **Purge Records**: Employee and Candidate records
- **Access Records**: System access logs
- **Password Protection**: Maintenance access control

### Additional Test Categories (15 Test Cases)
- **Common Functionality**: Dashboard, User dropdown, Logout
- **Integration**: Cross-module navigation workflows
- **Negative Testing**: Invalid inputs and error scenarios
- **Performance**: Navigation and page load timing
- **Accessibility**: Page headers and navigation elements
- **Security**: Logout and access control
- **Data Validation**: Page consistency and state persistence

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Chrome/Firefox browser
- Internet connection for OrangeHRM demo site

### Installation

1. **Clone the repository and navigate to the framework directory:**
   ```bash
   cd Deepesh/AutomationFramework
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify the login data configuration:**
   - Check `page_objects/login_hrm/login_data.json` contains:
     ```json
     {
       "url": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
       "username": "Admin",
       "password": "admin123"
     }
     ```

## 🧪 Running Tests

### Run All Tests
```bash
pytest
```

### Run Tests by Module
```bash
# Admin module tests only
pytest -m admin

# Leave module tests only
pytest -m leave

# Maintenance module tests only
pytest -m maintenance
```

### Run Tests by Category
```bash
# Smoke tests only
pytest -m smoke

# Integration tests only
pytest -m integration

# Performance tests only
pytest -m performance

# Security tests only
pytest -m security
```

### Run Specific Test Files
```bash
# Run comprehensive test suite
pytest tests/login_hrm/test_comprehensive_hrm.py

# Run original login test
pytest tests/login_hrm/test_login_hrm.py
```

### Run Tests with Parallel Execution
```bash
# Run tests in parallel (4 workers)
pytest -n 4

# Run tests with auto-detection of CPU cores
pytest -n auto
```

### Run Tests with HTML Report
```bash
# Generate HTML report
pytest --html=reports/report.html --self-contained-html

# Generate HTML report with metadata
pytest --html=reports/report.html --self-contained-html --metadata Title "OrangeHRM Test Report"
```

### Run Tests with Coverage
```bash
# Run tests with coverage report
pytest --cov=. --cov-report=html --cov-report=term-missing

# Generate coverage report in HTML format
pytest --cov=. --cov-report=html
```

## 📊 Test Execution Examples

### Quick Smoke Test Run
```bash
pytest -m smoke -v --tb=short
```

### Admin Module Regression Test
```bash
pytest -m admin -v --tb=short --html=reports/admin_report.html
```

### Performance and Security Test Suite
```bash
pytest -m "performance or security" -v --tb=short
```

### Critical Path Testing
```bash
pytest -m "smoke or critical" -v --tb=short
```

## 🏷️ Test Markers

The test suite uses pytest markers for organization:

- `@pytest.mark.smoke`: Critical path tests
- `@pytest.mark.admin`: Admin module tests
- `@pytest.mark.leave`: Leave module tests
- `@pytest.mark.maintenance`: Maintenance module tests
- `@pytest.mark.common`: Common functionality tests
- `@pytest.mark.integration`: Cross-module workflow tests
- `@pytest.mark.negative`: Negative test scenarios
- `@pytest.mark.performance`: Performance and timing tests
- `@pytest.mark.accessibility`: Accessibility and UI tests
- `@pytest.mark.security`: Security and access control tests
- `@pytest.mark.validation`: Data validation tests

## 📁 Project Structure

```
Deepesh/AutomationFramework/
├── page_objects/
│   ├── login_hrm/
│   │   ├── login_page_class.py
│   │   ├── login_page_locators.py
│   │   └── login_data.json
│   └── hrm_admin_page/
│       ├── admin_page_class.py
│       └── admin_page_locator.py
├── tests/
│   └── login_hrm/
│       ├── test_login_hrm.py
│       └── test_comprehensive_hrm.py
├── utilities/
│   └── util_tools.py
├── base/
│   └── selenium_base.py
├── pytest.ini
├── requirements.txt
└── README_Automation.md
```

## 🔧 Configuration

### pytest.ini
- Configures test discovery and execution
- Defines custom markers
- Sets up HTML reporting
- Configures test metadata

### requirements.txt
- Lists all Python dependencies
- Specifies version requirements
- Includes testing, reporting, and utility packages

## 📈 Test Reports

### HTML Reports
- Generated in `reports/` directory
- Self-contained HTML files
- Include test metadata and execution details
- Can be shared and viewed in any browser

### Coverage Reports
- Code coverage analysis
- HTML and terminal output
- Identifies untested code paths

## 🚨 Troubleshooting

### Common Issues

1. **WebDriver Issues:**
   - Ensure Chrome/Firefox is installed
   - Check webdriver-manager is properly configured
   - Verify browser compatibility

2. **Element Locator Issues:**
   - OrangeHRM demo site may have UI changes
   - Update locators in `admin_page_locator.py` if needed
   - Check for dynamic content loading

3. **Test Execution Issues:**
   - Verify all dependencies are installed
   - Check Python version compatibility
   - Ensure proper file paths and imports

### Debug Mode
```bash
# Run tests with detailed output
pytest -v -s --tb=long

# Run single test with debug output
pytest tests/login_hrm/test_comprehensive_hrm.py::TestComprehensiveHRM::test_admin_module_navigation -v -s
```

## 🎯 Best Practices

1. **Test Organization:**
   - Use descriptive test names
   - Group related tests with markers
   - Maintain clear test documentation

2. **Page Object Model:**
   - Separate locators from test logic
   - Use reusable page methods
   - Maintain clean separation of concerns

3. **Test Data Management:**
   - Use external data files
   - Implement proper test isolation
   - Clean up test data after execution

4. **Reporting and Monitoring:**
   - Generate comprehensive test reports
   - Monitor test execution time
   - Track test coverage metrics

## 📞 Support

For questions or issues with the automation framework:
- Check the test logs and reports
- Verify configuration files
- Review element locators for UI changes
- Ensure OrangeHRM demo site is accessible

## 🔄 Continuous Integration

This test suite can be integrated with:
- Jenkins
- GitHub Actions
- GitLab CI/CD
- Azure DevOps
- Any CI/CD platform supporting Python and pytest

## 📝 License

This automation framework is part of the GTM PS Batch 11 training program and is intended for educational and demonstration purposes.
