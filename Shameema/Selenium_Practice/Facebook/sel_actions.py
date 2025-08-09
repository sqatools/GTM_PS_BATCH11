import time

from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from  selenium.webdriver.support.select import Select


class generic_selactions:

    def __init__(self):
        self.wait = None

    def get_element(self,locator,cond = ec.visibility_of_all_elements_located):
        web_element = self.wait.until(cond(locator))
        return web_element

    def click_element(self, click_locator, **kwargs):
        self.get_element(locator = click_locator, **kwargs).click()

    def send_value(self,locator,**kwargs):
        self.get_element(locator = locator,**kwargs).sendkeys()

    def drop_down(self,locator,**kwargs):
        dropdown = self.get_element(locator = locator,**kwargs).select