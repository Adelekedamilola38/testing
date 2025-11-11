import pytest
import os
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def get_headers():
    return {"Content-Type": "application/json"}


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required for Linux CI runners
    options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues in containers
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook: captures a screenshot after each test run.
    - Saves successful screenshots to screenshots/success/
    - Saves failed screenshots to screenshots/failure/
    - Skips non-UI tests with no driver
    """

    outcome = yield
    rep = outcome.get_result()

    # Only on test call phase, not setup/teardown
    if rep.when == "call":
        driver = item.funcargs.get("driver", None)
        if not driver:
            print(f"\nNo WebDriver for '{item.name}' - likely an API test. Skipping screenshot.")
            return

        base_dir = os.path.join(os.getcwd(), "screenshots")
        status = "failure" if rep.failed else "success" if rep.passed else None
        if not status:
            return
            
        folder = os.path.join(base_dir, status)
        os.makedirs(folder, exist_ok=True)
    
        # Create a timestamped screenshot filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{item.name}_{timestamp}.png"
        file_path = os.path.join(folder, file_name)

        # Save screenshot
        try:
            if driver.session_id:
                driver.save_screenshot(file_path)
                print(f"\n[{status.upper()}] screenhot saved: {file_path}")
            else:
                print(f"\n[{status.upper()}] skipped screenshot - driver already closed.")
        except Exception as e:
            print(f"\n[{status.upper()}] could not capture screenshot: {e}")