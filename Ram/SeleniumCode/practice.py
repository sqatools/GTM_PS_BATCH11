import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FacebookLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, condition=ec.visibility_of_element_located):
        element = self.wait.until(condition(locator))
        return element

    def element_click(self, locator):
        self.get_element(locator).click()

    def facebook_login(self):
        self.driver.get("https://www.facebook.com/")
        self.get_element(locator=(By.NAME, "email")).send_keys("user@gmail.com")
        self.get_element(locator=(By.NAME, "pass")).send_keys("User@123")
        time.sleep(3)
        self.element_click(locator=(By.LINK_TEXT, "Create new account"))
        time.sleep(3)


obj = FacebookLogin()
obj.facebook_login()
