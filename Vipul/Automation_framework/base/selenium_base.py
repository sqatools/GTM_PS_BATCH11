from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def get_text(self, locator, cond=ec.presence_of_element_located):
        text = self.wait.until(cond(locator)).text
        return text

    def click_element(self, locator, **kwargs):
        self.get_element(locator=locator, **kwargs).click()


    def enter_text(self, locator, value, **kwargs):
        self.get_element(locator=locator, **kwargs).send_keys(value)

    '''
        why we use **kwargs here inplace of expected condition
        '''
