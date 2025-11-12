import pytest

# Try to import Selenium (only needed for Selenium UI tests)
try:
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
except ModuleNotFoundError:
    Options = None
    webdriver = None
    print("⚠️ Selenium not installed — skipping Selenium setup.")


# ---------- API Fixtures ----------
@pytest.fixture(scope="session")
def base_url():
    """Base URL for API testing"""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def get_headers():
    """Default headers for API requests"""
    return {"Content-Type": "application/json"}


# ---------- Selenium Driver Fixture ----------
@pytest.fixture
def driver():
    """Launch Chrome WebDriver (only if Selenium is installed)"""
    if webdriver is None or Options is None:
        pytest.skip("Selenium not available in this environment.")
    options = Options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required for Linux CI runners
    options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues in containers
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
