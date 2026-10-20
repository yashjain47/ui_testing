"""
# Interview Q&A











# QA / SDET 4-5 Years Interview Master Question Bank

## How to use this

For every question, prepare to answer in this order:

**Definition → Practical example → Your implementation → Problems/trade-offs**

At 4-5 years, don't answer like a fresher. Whenever possible, explain **why you chose an approach**.

---

# SECTION 1 — QA FUNDAMENTALS

## 1. What is the difference between Verification and Validation?

**Answer:**

**Verification** checks whether we are building the product correctly.

Examples:

* Requirement review
* Design review
* Code review
* Test-case review

**Validation** checks whether we built the correct product.

Examples:

* Functional testing
* Integration testing
* System testing
* User acceptance testing

Simple way to remember:

> Verification = "Are we building it right?"
>
> Validation = "Are we building the right thing?"

---

## 2. What is the difference between QA, QC and Testing?

**Answer:**

**QA — Quality Assurance**

* Process-oriented
* Prevents defects
* Includes process improvement, standards, reviews, automation strategy, etc.

**QC — Quality Control**

* Product-oriented
* Detects defects in the actual product.

**Testing**

* A QC activity used to identify defects by executing/evaluating the software.

As an SDET, I contribute to both QA and QC because I can improve the testing process through automation and also detect product defects.

---

## 3. What is the difference between severity and priority?

**Answer:**

**Severity** = impact of the defect on the application.

**Priority** = how urgently the defect should be fixed.

Example:

A typo on the company's homepage:

* Severity: Low
* Priority: High

A crash in an internal admin feature used once a year:

* Severity: High
* Priority: potentially lower depending on business impact.

---

## 4. What is the difference between functional and non-functional testing?

**Answer:**

Functional testing verifies **what the application does**.

Examples:

* Login
* Search
* Payment
* CRUD operations

Non-functional testing verifies **how well the application behaves**.

Examples:

* Performance
* Security
* Usability
* Scalability
* Reliability
* Compatibility

Automation frameworks such as Selenium and Playwright are primarily used for functional/UI automation, although they can participate in some non-functional validation.

---

## 5. What is regression testing?

**Answer:**

Regression testing verifies that existing functionality continues working after changes.

For example:

A developer changes the payment module.

I would run:

* Payment tests
* Login
* Cart
* Order creation
* Refund
* Other impacted workflows

The scope depends on the change and risk.

---

## 6. What is retesting?

**Answer:**

Retesting verifies that a **specific previously failed defect has been fixed**.

Example:

Bug:

> Login fails with valid credentials.

Developer fixes it.

I execute the exact failed scenario again.

That's retesting.

Regression testing is broader.

---

## 7. What is smoke testing?

**Answer:**

Smoke testing is a small set of critical tests used to determine whether a build is stable enough for deeper testing.

Typical smoke tests:

* Application launches
* Login works
* Main page loads
* Critical API responds
* Basic transaction works

If smoke testing fails, we generally don't waste time executing the complete regression suite.

---

## 8. What is sanity testing?

**Answer:**

Sanity testing is a focused validation of a particular change or area after a build/change.

For example:

Developer fixes password reset.

I test:

* Password reset request
* Email/link
* New password
* Login using new password

I don't necessarily execute the entire regression suite.

---

## 9. Explain STLC.

**Answer:**

Typical STLC phases:

1. Requirement analysis
2. Test planning
3. Test-case design
4. Test environment setup
5. Test execution
6. Defect reporting/tracking
7. Test closure

At each stage QA contributes different activities.

For example, during requirement analysis I identify:

* Ambiguous requirements
* Missing acceptance criteria
* Testability issues
* Dependencies
* Risks

---

## 10. Explain SDLC.

**Answer:**

Typical SDLC:

1. Requirement gathering
2. Analysis
3. Design
4. Development
5. Testing
6. Deployment
7. Maintenance

Modern Agile teams perform these activities iteratively rather than strictly sequentially.

As an SDET, I should be involved early rather than waiting until development is completed.

---

# SECTION 2 — TEST DESIGN & LOGICAL THINKING

## 11. Explain equivalence partitioning.

**Answer:**

We divide input data into groups where values are expected to behave similarly.

Example:

Age allowed: 18–60.

Partitions:

* `<18` → invalid
* `18–60` → valid
* `>60` → invalid

Instead of testing every possible value, we test representative values from each partition.

---

## 12. Explain boundary value analysis.

**Answer:**

BVA focuses on values around boundaries because defects frequently occur there.

For age 18–60:

Test:

* 17
* 18
* 19
* 59
* 60
* 61

This gives much better coverage than testing random values.

---

## 13. What is decision table testing?

**Answer:**

Decision tables are useful when output depends on multiple conditions.

Example:

Login:

| Username | Password | Account Active | Result           |
| -------- | -------- | -------------- | ---------------- |
| Valid    | Valid    | Yes            | Login            |
| Valid    | Invalid  | Yes            | Error            |
| Invalid  | Valid    | Yes            | Error            |
| Valid    | Valid    | No             | Account disabled |

It helps identify combinations that might otherwise be missed.

---

## 14. What is state transition testing?

**Answer:**

State transition testing validates behavior based on the current state.

Example:

Order:

`Created → Paid → Shipped → Delivered`

Invalid transition:

`Delivered → Payment Pending`

We test both valid and invalid transitions.

---

## 15. How would you test a login page?

**Answer:**

I would divide testing into:

### Functional

* Valid username/password
* Invalid username
* Invalid password
* Empty fields
* Password masking
* Remember me
* Logout
* Account lock

### Boundary

* Minimum/maximum username length
* Maximum password length

### Security

* SQL injection
* XSS
* Brute-force protection
* Session handling

### UI

* Error messages
* Alignment
* Keyboard navigation

### Compatibility

* Browsers
* Mobile/responsive layouts

### Automation

Automate stable, repeatable high-value scenarios.

---

## 16. How would you test a search box?

**Answer:**

I would test:

* Valid keyword
* Empty search
* Partial keyword
* Special characters
* Numbers
* Very long input
* Case sensitivity
* Spaces
* No-result scenario
* Multiple results
* Pagination
* Sorting/filter interaction
* SQL injection
* XSS
* Response time
* API/backend behavior

---

## 17. How would you test an elevator?

**Answer:**

I would identify states and conditions.

Functional:

* Floor selection
* Door opening/closing
* Up/down movement
* Emergency button

Boundary:

* Ground floor
* Highest floor

Negative:

* Press invalid/nonexistent floor
* Door obstruction
* Overweight condition

State transitions:

* Idle → Moving
* Moving → Stopped
* Stopped → Door Opening
* Door Opening → Door Closing

Safety:

* Power failure
* Emergency alarm
* Door sensor

This question tests structured thinking more than domain knowledge.

---

# SECTION 3 — SELENIUM

## 18. What is Selenium WebDriver?

**Answer:**

Selenium WebDriver is a browser automation API used to automate web applications.

It communicates with browsers through browser-specific drivers/protocol implementations.

Typical Python usage:

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
```

---

## 19. What are different locator strategies in Selenium?

**Answer:**

Common locators:

* ID
* Name
* Class name
* Tag name
* Link text
* Partial link text
* CSS selector
* XPath

My preference is generally:

1. Stable unique ID
2. Stable data-testid/data attribute
3. CSS
4. XPath when necessary

I avoid fragile locators based on dynamic CSS classes or changing DOM hierarchy.

---

## 20. CSS selector vs XPath?

**Answer:**

CSS is generally concise and readable.

Example:

```python
driver.find_element(By.CSS_SELECTOR, "#username")
```

XPath:

```python
driver.find_element(By.XPATH, "//input[@id='username']")
```

XPath becomes useful when relationships or text-based navigation are needed.

Example:

```xpath
//label[text()='Username']/following::input[1]
```

I choose based on DOM stability rather than simply preferring one.

---

## 21. What is the difference between implicit and explicit waits?

**Answer:**

**Implicit wait** applies globally when locating elements.

```python
driver.implicitly_wait(10)
```

**Explicit wait** waits for a specific condition.

```python
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)
```

I prefer explicit waits because they are targeted and make synchronization clearer.

---

## 22. Why should we avoid `time.sleep()`?

**Answer:**

`time.sleep()` waits for a fixed amount of time regardless of application state.

Example:

```python
time.sleep(10)
```

Problems:

* Slows tests
* Creates unnecessary waiting
* Can still fail if the application takes longer
* Doesn't represent the actual condition

Better:

```python
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
```

---

## 23. How do you handle dynamic elements in Selenium?

**Answer:**

I avoid locating elements using unstable properties.

For example, instead of:

```xpath
//button[@class='btn-928372']
```

I use a stable attribute:

```xpath
//button[@data-testid='submit']
```

Other techniques:

* Partial attributes
* Relative XPath
* Parent/child relationships
* Explicit waits
* JavaScript only when necessary

---

## 24. How do you handle stale element exceptions?

**Answer:**

`StaleElementReferenceException` happens when the DOM changes and the previously located element is no longer attached to the DOM.

Instead of storing the element for too long, I locate it again.

Example:

```python
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
element.click()
```

For dynamic applications, I may implement controlled retry logic.

---

## 25. How do you handle multiple windows/tabs?

**Answer:**

Use window handles.

```python
original = driver.current_window_handle

driver.find_element(By.ID, "open").click()

for handle in driver.window_handles:
    if handle != original:
        driver.switch_to.window(handle)
        break
```

After validation, I can switch back:

```python
driver.switch_to.window(original)
```

---

## 26. How do you handle iframes?

**Answer:**

Switch into the iframe first.

```python
driver.switch_to.frame("payment-frame")
```

Perform operations.

Then:

```python
driver.switch_to.default_content()
```

For nested frames, I switch through each required frame.

---

## 27. How do you handle alerts in Selenium?

**Answer:**

```python
alert = driver.switch_to.alert

print(alert.text)
alert.accept()
```

For cancel:

```python
alert.dismiss()
```

For prompt:

```python
alert.send_keys("test")
alert.accept()
```

---

## 28. How would you design a Selenium framework?

**Answer:**

I would separate responsibilities.

Example:

```text
automation/
│
├── tests/
├── pages/
├── utils/
├── config/
├── test_data/
├── drivers/
├── reports/
├── screenshots/
├── conftest.py
└── requirements.txt
```

I would use:

* Page Object Model
* Pytest fixtures
* Configuration management
* Explicit waits
* Logging
* Screenshots on failure
* Test data separation
* API/database utilities
* Parallel execution
* CI/CD integration
* Reporting

The goal is maintainability, not just creating scripts that execute.

---

# SECTION 4 — PLAYWRIGHT

## 29. Why would you choose Playwright over Selenium?

**Answer:**

Playwright provides several modern capabilities:

* Auto-waiting
* Browser contexts
* Multiple browser support
* Network interception
* Built-in tracing
* Screenshots/video
* Strong locator APIs
* Parallel execution
* Multi-tab support
* API testing support

Selenium has a mature ecosystem and broad adoption.

I would choose based on project requirements rather than saying one is universally better.

---

## 30. What is Playwright auto-waiting?

**Answer:**

Playwright automatically waits for actionability conditions before actions.

For example:

```python
page.get_by_role("button", name="Login").click()
```

Playwright can wait for the element to become:

* Visible
* Stable
* Enabled
* Receivable for events

This reduces the need for explicit sleeps.

---

## 31. Locator vs ElementHandle in Playwright?

**Answer:**

A `Locator` represents a way to find an element and performs actions with automatic waiting.

Example:

```python
page.get_by_role("button", name="Login")
```

An `ElementHandle` represents a particular DOM element.

For normal automation, I prefer **Locator** because it is more resilient and integrates with Playwright's waiting model.

---

## 32. What is BrowserContext in Playwright?

**Answer:**

A BrowserContext is an isolated browser session.

Example:

```python
context1 = browser.new_context()
context2 = browser.new_context()
```

They can have separate:

* Cookies
* Local storage
* Sessions
* Authentication

This is extremely useful for testing multiple users in parallel.

---

## 33. How would you test two users simultaneously using Playwright?

**Answer:**

Create separate contexts.

```python
user1 = browser.new_context()
user2 = browser.new_context()

page1 = user1.new_page()
page2 = user2.new_page()
```

Each context has independent session data.

This allows scenarios such as:

* User A sends message
* User B receives message

without sharing cookies.

---

## 34. How do you handle authentication in Playwright?

**Answer:**

One efficient approach is to authenticate once and reuse the storage state.

Example concept:

```python
context = browser.new_context(
    storage_state="auth.json"
)
```

This avoids logging in before every test.

For large suites, this can significantly reduce execution time.

---

## 35. How do you intercept network requests in Playwright?

**Answer:**

Using routing:

```python
page.route(
    "**/api/users",
    lambda route: route.fulfill(
        status=200,
        body='{"users":[]}'
    )
)
```

This is useful for:

* Mocking APIs
* Simulating errors
* Testing frontend behavior
* Testing unavailable backend services

---

## 36. How do you debug a failed Playwright test?

**Answer:**

I use:

* Trace Viewer
* Screenshots
* Video
* Console logs
* Network logs
* Test reports
* Headed execution
* Debug mode

The trace is particularly useful because it can show:

* Actions
* DOM snapshots
* Network
* Timing
* Screenshots

---

# SECTION 5 — SELENIUM VS PLAYWRIGHT

## 37. Selenium vs Playwright — what would you choose in a new project?

**Answer:**

I would evaluate:

| Requirement                | Selenium                          | Playwright |
| -------------------------- | --------------------------------- | ---------- |
| Mature ecosystem           | Excellent                         | Very good  |
| Auto-waiting               | More manual                       | Strong     |
| Network mocking            | Available through ecosystem/tools | Built-in   |
| Browser contexts           | Different approach                | Excellent  |
| Multi-browser              | Excellent                         | Excellent  |
| Debug tracing              | Ecosystem-dependent               | Built-in   |
| Existing company framework | Strong choice                     | Depends    |

If starting a modern web automation project from scratch, I would strongly consider Playwright.

If the organization already has a large Selenium ecosystem, migrating purely for technology preference may not provide enough ROI.

---

# SECTION 6 — PYTHON / CODING

## 38. Write Python code to find the second-largest number.

**Answer:**

```python
numbers = [10, 5, 20, 8, 20, 15]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print(unique_numbers[-2])
```

For an interview, I'd also discuss the duplicate case.

A more optimal approach without sorting:

```python
largest = float("-inf")
second = float("-inf")

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print(second)
```

Time complexity:

**O(n)**

---

## 39. Find duplicate elements in a list.

**Answer:**

```python
numbers = [1, 2, 3, 2, 4, 5, 1]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)
```

Time complexity: **O(n)**

Space complexity: **O(n)**

---

## 40. Reverse a string without using `[::-1]`.

**Answer:**

```python
text = "selenium"

result = ""

for char in text:
    result = char + result

print(result)
```

Alternative:

```python
result = ""

for i in range(len(text) - 1, -1, -1):
    result += text[i]
```

---

## 41. Find the first non-repeating character.

**Answer:**

```python
text = "swiss"

count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

for char in text:
    if count[char] == 1:
        print(char)
        break
```

Output:

```text
w
```

---

## 42. Check whether two strings are anagrams.

**Answer:**

```python
def is_anagram(a, b):
    return sorted(a) == sorted(b)

print(is_anagram("listen", "silent"))
```

For better complexity using frequency counting:

```python
from collections import Counter

def is_anagram(a, b):
    return Counter(a) == Counter(b)
```

---

## 43. Find the missing number from 1 to n.

**Answer:**

```python
numbers = [1, 2, 3, 5, 6]

n = 6

expected = n * (n + 1) // 2
actual = sum(numbers)

print(expected - actual)
```

Output:

```text
4
```

Time complexity: **O(n)**

---

## 44. Count the frequency of each word.

**Answer:**

```python
from collections import Counter

text = "api test api selenium test"

words = text.split()

print(Counter(words))
```

Output conceptually:

```text
api: 2
test: 2
selenium: 1
```

This is useful in log processing and test-data analysis.

---

## 45. Write a Python function to retry an operation.

**Answer:**

```python
import time

def retry(func, attempts=3, delay=2):
    for attempt in range(attempts):
        try:
            return func()
        except Exception:
            if attempt == attempts - 1:
                raise
            time.sleep(delay)
```

In production automation, I would avoid blindly retrying every exception. I would retry only known transient failures.

---

# SECTION 7 — PYTEST

## 46. Why do you use pytest?

**Answer:**

Pytest provides:

* Simple syntax
* Fixtures
* Parameterization
* Markers
* Plugins
* Parallel execution
* Assertions
* Hooks
* Good integration with CI/CD

Example:

```python
def test_login():
    assert login("user", "pass") is True
```

---

## 47. Explain pytest fixtures.

**Answer:**

Fixtures provide reusable setup and teardown.

Example:

```python
import pytest

@pytest.fixture
def browser():
    driver = create_driver()
    yield driver
    driver.quit()
```

Test:

```python
def test_login(browser):
    browser.get("https://example.com")
```

This avoids duplicating setup code.

---

## 48. Explain fixture scopes.

**Answer:**

Common scopes:

* function
* class
* module
* package
* session

Example:

```python
@pytest.fixture(scope="session")
def database():
    ...
```

A session-scoped fixture is created once for the test session.

I select scope based on resource lifetime and test isolation requirements.

---

## 49. What is pytest parameterization?

**Answer:**

It allows the same test logic to run with multiple datasets.

```python
@pytest.mark.parametrize(
    "username,password",
    [
        ("user1", "pass1"),
        ("user2", "pass2"),
        ("user3", "pass3")
    ]
)
def test_login(username, password):
    assert login(username, password)
```

This improves coverage while avoiding duplicated test methods.

---

## 50. How do you execute tests in parallel?

**Answer:**

With pytest-xdist:

```bash
pytest -n 3
```

But parallel execution requires test isolation.

Problems can occur when tests share:

* Database records
* Files
* Users
* Ports
* Browser sessions

So simply adding `-n` isn't enough; the framework must be designed for parallel execution.

---

# SECTION 8 — API TESTING

## 51. How do you test an API?

**Answer:**

I validate:

### Request

* URL
* Method
* Headers
* Authentication
* Query parameters
* Path parameters
* Request body

### Response

* Status code
* Response schema
* Headers
* Body
* Business rules
* Response time

### Negative cases

* Invalid data
* Missing fields
* Unauthorized request
* Invalid token
* Wrong HTTP method

---

## 52. Explain GET, POST, PUT, PATCH and DELETE.

**Answer:**

**GET**
Retrieve data.

**POST**
Create a resource.

**PUT**
Usually replaces/updates a resource completely.

**PATCH**
Partially updates a resource.

**DELETE**
Deletes a resource.

Example:

```text
GET    /users/10
POST   /users
PUT    /users/10
PATCH  /users/10
DELETE /users/10
```

---

## 53. What status codes do you commonly validate?

**Answer:**

Important ones:

* `200` — successful request
* `201` — resource created
* `204` — success with no content
* `400` — bad request
* `401` — authentication required/failed
* `403` — forbidden
* `404` — resource not found
* `409` — conflict
* `422` — validation error
* `429` — rate limited
* `500` — server error
* `502/503/504` — gateway/service availability issues

I don't validate only the status code. I also validate the response body and business behavior.

---

## 54. How would you automate API testing using Python?

**Answer:**

Using `requests`:

```python
import requests

response = requests.get(
    "https://example.com/api/users"
)

assert response.status_code == 200

data = response.json()

assert "users" in data
```

For a framework, I'd add:

* Fixtures
* Configuration
* Authentication handling
* Schema validation
* Logging
* Test data
* Reporting
* Environment management

---

## 55. How do you validate an API response schema?

**Answer:**

I can use JSON Schema validation.

I verify:

* Required fields
* Data types
* Nested structures
* Allowed values
* Optional fields

This catches contract-breaking changes even when the HTTP status code remains `200`.

---

# SECTION 9 — DATABASE / SQL

## 56. How do you validate database data from an automated test?

**Answer:**

Example flow:

```text
UI/API action
      ↓
Application processing
      ↓
Database
      ↓
SQL validation
```

For example, after creating a user through API:

```sql
SELECT * FROM users WHERE email='test@example.com';
```

Then validate:

* Record exists
* Correct ID
* Correct status
* Correct timestamps
* Correct relationships

I avoid depending on database validation when the test is specifically intended to validate only the public API contract.

---

## 57. Write SQL to find duplicate emails.

**Answer:**

```sql
SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

This is a common QA interview SQL question.

---

## 58. How would you test data consistency between API and database?

**Answer:**

Example:

1. Send POST API request.
2. Validate API response.
3. Extract generated ID.
4. Query DB using the ID.
5. Compare important fields.
6. Validate transformations.
7. Validate related records.
8. Verify rollback behavior if applicable.

I would be careful about eventual consistency. If the architecture is asynchronous, I wouldn't immediately fail because the DB hasn't updated within a few milliseconds.

---

# SECTION 10 — AUTOMATION FRAMEWORK DESIGN

## 59. Explain Page Object Model.

**Answer:**

POM separates page-specific UI operations from test logic.

Example:

```text
pages/
    login_page.py
    dashboard_page.py

tests/
    test_login.py
```

Login page:

```python
class LoginPage:

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
```

Test:

```python
def test_valid_login(login_page):
    login_page.login("user", "password")
```

Benefits:

* Reusability
* Maintainability
* Reduced duplication
* Better readability

---

## 60. What would you do if your automation suite has 2,000 tests and execution takes 5 hours?

**Answer:**

I would first measure where time is spent.

Then investigate:

* Parallel execution
* Slow setup
* Repeated login
* Unnecessary UI tests
* Excessive waits
* Database bottlenecks
* Network dependencies
* Test duplication
* Browser startup overhead

I would move suitable validations to API/service level.

I would also implement:

* Test tagging
* Smoke suite
* Regression suite
* Parallel workers
* Sharding
* Authentication reuse

The goal isn't simply "add more machines"; it's to reduce unnecessary work.

---

# SECTION 11 — REAL-WORLD SCENARIOS

## 61. Your Selenium test passes locally but fails in Jenkins. What do you check?

**Answer:**

I would investigate systematically:

1. Browser version
2. Driver/browser compatibility
3. OS differences
4. Environment variables
5. Display/headless configuration
6. Network access
7. Test data
8. File paths
9. Timing issues
10. Parallel execution
11. Permissions
12. Dependency versions
13. Logs/screenshots/videos

I would reproduce using the same CI environment where possible.

I wouldn't immediately increase `sleep()` values.

---

## 62. Your test fails randomly 2 out of 10 times. How do you debug it?

**Answer:**

This is likely a flaky test.

I would:

1. Collect failure logs.
2. Capture screenshots/video/traces.
3. Identify exact failing step.
4. Check synchronization.
5. Check test-data collisions.
6. Check environment instability.
7. Check network/API dependencies.
8. Run repeatedly.
9. Run independently and in parallel.
10. Identify whether the application or test is responsible.

Then fix the root cause rather than hiding it with retries.

---

## 63. A developer says "I cannot reproduce your bug." What do you do?

**Answer:**

I provide reproducible evidence:

* Build/version
* Environment
* Browser
* OS
* Test data
* Exact steps
* Expected result
* Actual result
* Logs
* Screenshot/video
* API request/response if relevant

If it is intermittent, I provide reproduction frequency and timestamps.

I would also try reproducing it together with the developer.

---

## 64. Production has a critical bug. What is your approach?

**Answer:**

First, understand impact.

Then:

1. Reproduce if possible.
2. Identify affected users/workflows.
3. Determine severity.
4. Check whether workaround exists.
5. Help development isolate root cause.
6. Validate the fix.
7. Run targeted regression.
8. Validate production after deployment.
9. Add a permanent regression test.

For critical production defects, communication and risk management are as important as test execution.

---

## 65. You have only two hours to test a new feature. What do you do?

**Answer:**

I use risk-based testing.

Priority:

1. Critical business workflow
2. Happy path
3. High-risk negative scenarios
4. Boundary cases
5. Integration points
6. Permissions/security
7. Regression around impacted areas

I would not try to execute every possible test.

I would communicate clearly what was tested and what remains untested.

---

## 66. The application requirement is ambiguous. What do you do?

**Answer:**

I don't blindly write test cases based on assumptions.

I clarify:

* Expected behavior
* Valid inputs
* Invalid inputs
* Error handling
* Business rules
* Edge cases
* Acceptance criteria

If clarification isn't immediately available, I document my assumptions and identify the risk.

---

## 67. Your automation test fails because an API is unavailable. Should the test be marked failed?

**Answer:**

Not automatically.

I first determine what the test is intended to validate.

If the API is an external dependency and the purpose is frontend behavior, I might mock it.

If the purpose is end-to-end integration, the dependency failure may legitimately make the test fail.

The important thing is to distinguish:

**Product failure vs environment/dependency failure vs automation failure.**

---

# SECTION 12 — SDLC / STLC / AGILE

## 68. What happens in a typical Agile sprint from a QA perspective?

**Answer:**

Typical flow:

```text
Requirement
   ↓
Story refinement
   ↓
Acceptance criteria
   ↓
Test planning
   ↓
Development
   ↓
Unit/API testing
   ↓
QA testing
   ↓
Automation
   ↓
Regression
   ↓
Demo
   ↓
Release
```

As an SDET, I try to contribute early during refinement rather than waiting for development completion.

---

## 69. What is your role as an SDET compared with a manual QA?

**Answer:**

An SDET is expected to combine:

**Testing + Programming + Automation + Engineering**

Responsibilities can include:

* Test strategy
* Automation framework development
* UI automation
* API automation
* Database validation
* CI/CD
* Test infrastructure
* Debugging
* Code reviews
* Framework maintenance
* Flaky-test reduction
* Quality improvements

The important distinction is that an SDET should think about **engineering the testing system**, not only executing tests.

---

## 70. Design an automation strategy for a new web application.

**Answer:**

I would start with the application architecture and testing pyramid.

### Layer 1 — Unit tests

Large number of fast tests.

### Layer 2 — API/service tests

Validate business logic and integrations.

### Layer 3 — UI tests

Smaller number of critical end-to-end workflows.

Example:

```text
              UI / E2E
             /        \
          API          API
         /   \        /   \
       Unit Unit    Unit Unit
```

For the UI layer, if starting a new modern project, I would evaluate Playwright.

Framework components:

```text
tests/
pages/
api/
utils/
fixtures/
config/
test_data/
reports/
logs/
```

CI pipeline:

```text
Code Commit
     ↓
Build
     ↓
Unit Tests
     ↓
API Tests
     ↓
Smoke UI
     ↓
Parallel Regression
     ↓
Report
     ↓
Release
```

I would also define:

* Browser strategy
* Test tagging
* Parallelization
* Environment configuration
* Test-data strategy
* Authentication strategy
* Failure artifacts
* Retry policy
* Flaky-test process
* Reporting
* Ownership

The key principle is:

> **Don't automate everything through the UI. Automate each test at the lowest reliable layer.**






"""


