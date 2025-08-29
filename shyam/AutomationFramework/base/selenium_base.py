import logging
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class seleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.log = logging.getLogger(__name__)

    def get_element(self, locator, cond=ec.element_to_be_clickable):
        self.log.info(f"getting element with locator {locator}")
        element = self.wait.until(cond(locator))
        return element

    def Enter_text(self, locator, value):
        self.log.info(f"enter value: {value} on element with locator: {locator}")
        self.get_element(locator).send_keys(value)

    def Click_element(self, locator):
        self.log.info(f"click on element with locator: {locator}")
        self.get_element(locator).click()

    def get_text(self, locator):
        self.log.info(f"get from element with locator: {locator}")
        return self.get_element(locator).text
