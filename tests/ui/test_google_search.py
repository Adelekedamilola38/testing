import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.google_page import DuckDuckGoPage
from pages.login_page import LoginPage
from utils.logger import get_logger
import time

logger = get_logger()



@pytest.mark.smoke
def test_duckduckgo_search(driver: WebDriver):
    logger.info("Starting DuckDuckGo Search Test")

    page = DuckDuckGoPage(driver)
    page.load()
    page.search("QA Testing with Python")
    time.sleep(5)

    assert "QA Testing" in driver.title

    logger.info("Search successful, title verified.")



@pytest.mark.regression
def test_login_page(driver: WebDriver):
    logger.info("Starting Login Page Test")


    page = LoginPage(driver)
    page.load()
    page.login("tomsmith", "SuperSecretPassword!")
    time.sleep(5)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((LoginPage.success_message))
    )

    msg = page.get_message_text()
    logger.info(f"Message displayed: {msg}")

    assert "You logged into a secure area!" in msg


    logger.info("Login successful, message verified.")
   
