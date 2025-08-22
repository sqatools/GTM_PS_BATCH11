from .selenium_basefile import SeleniumBasefile
from .login_pagelocators import *

class Loginpage(SeleniumBasefile):
    def __init__(self,driver):
        super().__init__(driver)

    def launch_url(self,url):
        self.driver.get(url)
    def enter_username(self,username):
        self.enter_text(username_field,username)
    def enter_password(self,password):
        self.enter_text(password_fields,password)
    def click_button(self):
        self.click_method(locator=login_button)
    def hrm(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_button()
