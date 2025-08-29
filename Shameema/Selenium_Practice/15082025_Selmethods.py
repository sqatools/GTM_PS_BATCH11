import time
import datetime from datetime
import os

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
class selmethods:

    driver = webdriver.Chrome( )
    driver.implicitly_wait(10)
    driver.maximize_window( )
    wait = WebDriverWait(driver, 10)
    alert = Alert(driver)
    action = ActionChains(driver)


def get_ele(self, locator, cond=ec.visibility_of_element_located):
    element = self.wait.until(cond(locator))
    return element


def get_txt(self, locator, **kwargs):
    return (self.get_ele(locator=locator)).text


def get_attrib(self, locator, attr_name, **kwargs):
    attr_value = (self.get_ele(locator=locator)).get_attribute(attr_name)
    return attr_value


def click_ele(self, locator, **kwargs):
    self.get_ele(locator=locator).click( )


def send_data(self, locator, value, **kwargs):
    self.get_ele(locator=locator).send_keys(value)
