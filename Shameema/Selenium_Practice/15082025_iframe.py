import time
import os
from datetime import datetime

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class ifram:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,10)
        self.alert = Alert(self.driver)
        self.action = ActionChains(self.driver)

    def get_ele(self,locator,cond = ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def get_txt(self,locator,**kwargs):
        return(self.get_ele(locator=locator)).text

    def get_attrib(self,locator,attr_name,**kwargs):
        attr_value = (self.get_ele(locator=locator)).get_attribute(attr_name)
        return attr_value

    def click_ele(self,locator,**kwargs):
        self.get_ele(locator=locator).click()
    def send_data(self,locator,value,**kwargs):
        self.get_ele(locator=locator).send_keys(value)

    def url_launch(self):
        self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iframe")
        url = self.driver.current_url
        url_title = self.driver.title
        print(url)
        print(url_title)



    def working_in_framework(self):
        self.click_ele (locator=(By.ID,'iFrame'))
        iFram_1=self.get_ele(locator=(By.XPATH,"//iFrame[contains(@name,'Sqa')]"))
        time.sleep(5)
        self.driver.switch_to.frame(iFram_1)
        iFrame_header = self.get_txt()


obj = ifram()
obj.url_launch()
obj.working_in_framework()
