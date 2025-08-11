import time

from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.select import Select


class handle_iframe:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,10)
        # self.select = Select(self.driver)

    def get_element(self, locator , cond = ec.visibility_of_all_elements_located):
        element = self.wait.until(cond(locator))
        return element

    def select_option_value(self,locator):
        element = self.get_element(locator= locator)
        self.select = Select(import time

f