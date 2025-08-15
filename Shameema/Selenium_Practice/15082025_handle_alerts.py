import time
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class alets_handling:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver,10)
        self.alert = Alert(self.driver)

    def get_ele(self,locator,cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_ele(self,locator,**kwargs):
        self.get_ele(locator=locator,**kwargs).click()

    def send_data(self,locator,value,**kwargs):
        self.get_ele(locator=locator,**kwargs).send_keys(value)

    def get_attrib(self,locator,attrib_value,**kwargs):
        self.get_ele(locator=locator,**kwargs).get_attribute(attrib_value)

    def get_txt(self,locator,**kwargs):
        return self.get_ele(locator=locator,**kwargs).text

    def url_launch(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
        url = self.driver.current_url
        title = self.driver.title
        print(url)
        print(title)


    def handle_alert_box(self):
        header=self.get_txt(locator=(By.XPATH,"//h2[text()='Display Alert Message.']"))
        print("Heading of Alert box :",header)
        self.click_ele(locator=(By.XPATH, "//input[@value='Alert Box']"))
        time.sleep(5)

        print("alert msg :",self.alert.text)
        time.sleep(3)
        self.alert.accept()
        time.sleep(5)

    def handle_confirm_box(self):
         self.click_ele(locator=(By.XPATH,"//button[@onclick = 'myFunction()']"))
         time.sleep(3)
         print("Confirm box msg :",self.alert.text)
         self.alert.accept()
         ui_msg = self.get_txt(locator=(By.XPATH,"//p[@id='demo']"))
         print("message aftrer ok :",ui_msg)
         self.click_ele(locator=(By.XPATH, "//button[@onclick = 'myFunction()']"))
         self.alert.dismiss()
         ui_msg= self.get_txt(locator=(By.XPATH,"//p[@id='demo']"))
         print("message after cancellation  :",ui_msg)

    def handle_prompt_box(self):
        header_text = self.get_txt(locator=(By.XPATH,"//h2[text()='JavaScript Prompt Box']"))
        self.click_ele(locator=(By.XPATH,"//button[@id='promptbtn']"))
        promptbx_msg = self.alert.text
        print(promptbx_msg)
        self.alert.send_keys("SQA Tools")
        self.alert.accept()
        ui_msg = self.get_txt(locator=(By.XPATH,"//p[@id='prompt']"))
        print("Message after ok :", ui_msg)
        assert ui_msg == "Hello SQA Tools! How are you today?"
        self.click_ele(locator=(By.XPATH, "//button[@id='promptbtn']"))
        self.alert.dismiss()
        ui_msg = self.get_txt(locator=(By.XPATH, "//p[@id='prompt']"))
        print("Message after Cancellation :", ui_msg)
        time.sleep(5)
        assert ui_msg == "User cancelled the prompt."

# que:
# 1) how to parameterize the value sent via send keys
# # how to send that parameter into the assert ?
# 2) how to print the assert result
# 3) program errors if assert is not true - how to handle?





obj = alets_handling()
obj.url_launch()
# obj.handle_alert_box()
# obj.handle_confirm_box()
obj.handle_prompt_box()