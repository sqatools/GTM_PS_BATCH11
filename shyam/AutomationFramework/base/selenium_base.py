from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class seleniumBase:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,20)

    def get_element(self,locator,cond=ec.visibility_of_element_located):
        element=self.wait.until(cond(locator))
        return element
    def Enter_text(self,locator,value):
        self.get_element(locator).send_keys(value)
    def Click_element(self,locator):
        self.get_element(locator).click()
    def get_text(self,locator):
        return self.get_element(locator).text
