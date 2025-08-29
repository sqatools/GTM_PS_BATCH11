import time
from datetime import datetime
import os

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
# from selmethods import *
class  mutibrowwindows:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,10)
        self.alert = Alert(self.driver)
        self.action_chain = ActionChains(self.driver)

    def get_ele(self,locator,cond = ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_el(self,locator,**kwargs):
        self.get_ele(locator=locator).click()

    def send_data(self,locator,value,**kwargs):
        self.get_ele(locator=locator).send_keys(value)

    def get_txt(self,locator,**kwargs):
        return(self.get_ele(locator=locator)).text

    def get_attrib(self,locator,attr_name,**kwargs):
        attr_value= self.get_ele(locator=locator).get_attribute(attr_name)
        print (attr_value)

    def url_launch(self):
         self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
         url = self.driver.current_url
         title = self.driver.title
         print(url)
         print(title)

    def multiple_browser_handle(self):
        self.click_el(locator=(By.XPATH,"//a[contains(text(),'What is Software Testing')]"))
        time.sleep(3)


obj = mutibrowwindows()
obj.url_launch()
obj.multiple_browser_handle()