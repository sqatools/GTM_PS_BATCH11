from ...base.selenium_base import SeleniumBase
from .fb_page_locator import *

class FBPage(SeleniumBase):
    def __ini__(self, driver):
        super().__init__(driver)


    def launch_fb_login(self, url):
        self.driver.get(url)


    def login_to_fb(self, email, password):
        self.enter_text(fb_username_field, email)
        self.enter_text(fb_password_field, password)
        self.click_element(fb_login_button)