import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains


class HYR():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.alert = Alert(self.driver)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def select_option_value(self, dropdownlocator):
        dropdown_element = self.get_element(locator=dropdownlocator)
        select_obj = Select(dropdown_element)
        return select_obj

    def text_box(self):
        self.driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")


