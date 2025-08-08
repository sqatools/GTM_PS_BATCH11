import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class W3Schools:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, condition=ec.visibility_of_element_located):
        element = self.wait.until(condition(locator))
        return element

    def element_click(self, locator, **kwargs):
        self.get_element(locator, **kwargs).click()

    def w3school_links(self):
        self.driver.get("https://www.w3schools.com/")
        time.sleep(2)
        self.element_click(locator=(By.XPATH, "//a[text()='BOOTSTRAP']"))
        self.element_click(locator=(By.XPATH, "//a[text()='Learn Bootstrap 3 »']"))
        time.sleep(3)


obj = W3Schools()
obj.w3school_links()