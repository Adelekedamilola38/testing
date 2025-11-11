from selenium.webdriver.common.by import By

class DuckDuckGoPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")
    

    def load(self):
        self.driver.get("https://duckduckgo.com/")

    def search(self, query):
        self.driver.find_element(*self.search_box).send_keys(query + "\n")