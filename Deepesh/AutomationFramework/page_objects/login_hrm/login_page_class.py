from base.selenium_base import SeleniumBase
from .login_page_locators import *


class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_login_page(self, url):
        self.log.info(f"launching the website url : {url}")
        self.driver.get(url)

    def enter_username(self, username):
        self.log.info(f"entering username: {username}")
        self.enter_text(locator=username_fields, value=username)

    def enter_password(self, password):
        self.log.info(f"entering password: {password}")
        self.enter_text(locator=password_fields, value=password)

    def click_login_button(self):
        self.log.info("click on login button")
        self.click_element(locator=login_button)

    def login_to_rhm(self, username, password):
        self.log.info("login to hrm website")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
