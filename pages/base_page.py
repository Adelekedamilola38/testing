from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base class to be inherited by all page objects."""

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        """Navigate to a specific URL."""
        self.driver.get(url)

    def find_element(self, locator):
        """Wait for an element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Click an element after waiting for it to be clickable."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text, clear_first=True):
        """Type into an input field."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Return visible text of an element."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text