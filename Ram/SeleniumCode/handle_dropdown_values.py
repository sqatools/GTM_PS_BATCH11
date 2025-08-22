import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HandleDropdowns:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, condition=ec.visibility_of_element_located):
        element = self.wait.until(condition(locator))
        return element

    def element_click(self, locator, **kwargs):
        self.get_element(locator, **kwargs).click()

    def select_dropdown_value(self, locator):
        element = self.get_element(locator=locator)
        return Select(element)

    def dropdown_values(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

        self.select_dropdown_value(locator=(By.ID, "admorepass")).select_by_visible_text("Add 1 more passenger (100%)")
        time.sleep(3)
        self.select_dropdown_value(locator=(By.ID, "billing_country")).select_by_visible_text("United Kingdom")
        time.sleep(3)

    def dropdown_values_by_indexing(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.select_dropdown_value(locator=(By.ID, "admorepass")).select_by_index(1)
        time.sleep(3)
        self.select_dropdown_value(locator=(By.ID, "billing_country")).select_by_index(2)
        time.sleep(3)


obj = HandleDropdowns()
# obj.dropdown_values()
obj.dropdown_values_by_indexing()
