import time

from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec


class handle_iframe:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,10)

    def get_element(self, locator , cond = ec.visibility_of_all_elements_located):
        element = self.wait.until(cond(locator))
        return element

    def Handle_iframe_element(self):
        self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iframe")
        frame_element = self.get_element(locator = (By.Name, ""))

