from .selenium_base import SeleniumBase
from .login_page_locators import *


class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.enter_text(locator=username_fields, value=username)

    def enter_password(self, password):
        self.enter_text(locator=password_fields, value=password)

    def click_login_button(self):
        self.click_element(locator=login_button)

    def login_to_rhm(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
