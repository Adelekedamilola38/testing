import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.google_page import DuckDuckGoPage
from utils.logger import get_logger
import time

logger = get_logger()




@pytest.mark.smoke
def test_duckduckgo_search():
    logger.info("Starting DuckDuckGo Search Test")

    options = Options()
    options.add_argument("--headless") # run without UI
    options.add_argument("--no-sandbox") # required for Linux CI runners
    options.add_argument("--disable-dev-shm-usage") # Prevent memory issues in containers

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    page = DuckDuckGoPage(driver)
    page.load()
    page.search("QA Testing with Python")
    time.sleep(5)



    WebDriverWait(driver, 5).until(
        EC.title_contains("QA Testing with Python")
    )

    assert "QA Testing" in driver.title

    driver.save_screenshot("duckduckgo_search.png")

    logger.info("Search successful, title verified.")
    driver.quit()


