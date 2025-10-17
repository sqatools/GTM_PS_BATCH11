
from .Selenium_page import SeleniumBase
from .Login_page_locator import *

class LoginPage(SeleniumBase):
    def __int__(self,driver):
        super().__int__(driver)


    def launch_login_page(self,url):
        self.driver.get(url)

    def enter_username(self,username):
        self.enert_text(username_field,username)


    def enter_password(self,password):
        self.enert_text(password_field,password)


    def click_login_button(self):
        self.click_element(Login_button)


    def login_to_hrm(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
