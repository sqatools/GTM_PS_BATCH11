from selenium_base import SeleniumBase
from login_page_locator import *
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def open_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.enter_text(locator=username_field, value=username)

    def enter_password(self, password):
        self.enter_text(locator=password_field, value=password)

    def click_button(self):
        self.click_element(locator=submit_button, cond=ec.element_to_be_clickable)

    def fb_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_button()




