from ...base.selenium_base import SeleniumBase
from ...page_object.hrm_page.login_page_locator import *


class LoginPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def launch_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.enter_text(locator=username_field, value=username)

    def enter_password(self, password):
        self.enter_text(locator=password_field, value=password)

    def click_login_button(self):
        self.click_element(locator=button_field)

    def login_hrm(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

'''
why we dont use self.driver = driver below line number 7

'''