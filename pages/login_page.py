from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    success_message = (By.ID, "flash")

    def load(self):
        self.open("https://the-internet.herokuapp.com/login")

    def login(self, username, password):   
        self.type(self.username_field, username)
        self.type(self.password_field, password)
        self.click(self.login_button)

    def get_message_text(self):
        return self.get_text(self.success_message)
