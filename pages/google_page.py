from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DuckDuckGoPage(BasePage):
    search_box = (By.NAME, "q")
    

    def load(self):
        self.open("https://duckduckgo.com/")

    def search(self, query):
        self.type(self.search_box, query + "\n", clear_first=False)
