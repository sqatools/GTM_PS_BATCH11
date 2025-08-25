import time

from...base.selenium_base import seleniumBase
from .login_page_locator import *

class loginHRM(seleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def launch_login_page(self,url):
        self.driver.get(url)
    def Enter_Username(self,username):
        self.Enter_text(username_fields,username)
    def Enter_password(self,password):
        self.Enter_text(password_fields,password)
    def click_login_button(self):
        self.Click_element(locator=login_button_fields)

    def HRM(self,username,password):
        self.Enter_Username(username)
        self.Enter_password(password)
        self.click_login_button()
