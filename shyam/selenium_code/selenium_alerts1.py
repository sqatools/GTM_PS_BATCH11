import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

class Handle_alert:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.wait=WebDriverWait(self.driver,10)
        self.alert=Alert(self.driver)
    def get_element(self,locator,cond=ec.visibility_of_element_located):
        element=self.wait.until(cond(locator))
        return element
    def get_clickable(self,locator):
        self.get_element(locator).click()
    def get_text(self,locator):
        return self.get_element(locator).text

    def handle_alert_box(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
        self.get_element(locator=(By.ID,"btnShowMsg")).click()
        print("msg:",self.alert.text)
        time.sleep(2)
        self.alert.accept()
    def handle_alert_confirm_box(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
        self.get_element(locator=(By.ID,"button")).click()
        self.alert.accept()
        ui_msg=self.get_element(locator=(By.ID,"demo")).text
        assert ui_msg == "You pressed OK!"
        time.sleep(3)
        self.get_element(locator=(By.ID, "button")).click()
        self.alert.dismiss()
        ui_msg = self.get_element(locator=(By.ID, "demo")).text
        assert ui_msg == "You pressed Cancel!"
        time.sleep(3)
    def handle_alert_prompt_box(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
        self.get_element(locator=(By.ID,"promptbtn")).click()
        self.alert.send_keys("python")
        time.sleep(3)
        self.alert.accept()
        time.sleep(3)
        ui_msg =self.get_element(locator=(By.ID,"prompt")).text
        assert ui_msg =="Hello python! How are you today?"
        time.sleep(3)
        self.get_element(locator=(By.ID, "promptbtn")).click()
        time.sleep(3)
        self.alert.dismiss()
        ui_msg= self.get_element(locator=(By.ID,"prompt")).text
        assert ui_msg=="User cancelled the prompt."




obj=Handle_alert()
#obj.handle_alert_box()
#obj.handle_alert_confirm_box()
obj.handle_alert_prompt_box()


# Home work:
# repeat :  Handle Iframe, Handle Droddown, Handle Alerts
# Automate 5 areas of openhrm website in class format
# https://opensource-demo.orangehrmlive.com/web/index.php
# Admin
# Leave
# PIM
# Time
# Recruitment