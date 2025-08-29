from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element =self.wait.until(cond(locator))
        return element

    def enter_text(self, locator, value):
        self.get_element(locator).send_keys(value)

    def click_element(self, locator, **kwargs):
        self.get_element(locator, **kwargs).click()


