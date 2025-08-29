from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SeleniumBase:
    def __int__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,timeout=20)

    def get_element(self,locator,cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self,locator,**kwargs):
        self.get_element(locator=locator,**kwargs).click()

    def enert_text(self,locator,value,**kwargs):
        self.get_element(locator=locator,**kwargs).send_keys(value)

    def get_text(self,locator,**kwargs):
        return self.get_element(locator=locator).text