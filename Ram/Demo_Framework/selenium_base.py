from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=20)

    def get_element(self, locator, condition=ec.visibility_of_element_located):
        element = self.wait.until(condition(locator))
        return element

    def click_element(self, locator, **kwargs):
        self.get_element(locator=locator, **kwargs).click()

    def enter_text(self, locator, value, **kwargs):
        self.get_element(locator=locator, **kwargs).send_keys(value)

    def get_text(self, locator, **kwargs):
        return self.get_element(locator=locator).text

    def select_dropdown_value(self, locator, value, **kwargs):
        Select(self.get_element(locator=locator)).select_by_visible_text(value)
