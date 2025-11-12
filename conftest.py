import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


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


