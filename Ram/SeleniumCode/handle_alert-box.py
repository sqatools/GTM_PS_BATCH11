import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert


class HandleAlerts:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.alert = Alert(self.driver)

    def get_element(self, locator, condition=ec.visibility_of_element_located):
        element = self.wait.until(condition(locator))
        return element

    def element_click(self, locator, **kwargs):
        self.get_element(locator, **kwargs).click()

    def select_dropdown_value(self, locator):
        element = self.get_element(locator=locator)
        return Select(element)

    def click_alert_box(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")

        self.get_element(locator=(By.ID, "btnShowMsg")).click()
        print("Message :", self.alert.text)
        time.sleep(3)
        # accepting alert
        self.alert.accept()
        time.sleep(3)

    def click_confirm_box(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")

        self.get_element(locator=(By.ID, "button")).click()
        print("alert msg  :", self.alert.text)
        time.sleep(4)
        # accept alert
        self.alert.accept()
        ui_msg = self.get_element(locator=(By.ID, "demo")).text
        assert ui_msg == "You pressed OK!"

        self.get_element(locator=(By.ID, "button")).click()
        self.alert.dismiss()
        time.sleep(3)
        ui_msg = self.get_element(locator=(By.ID, "demo")).text
        assert ui_msg == "You pressed Cancel!"
        time.sleep(2)


obj = HandleAlerts()
obj.click_confirm_box()
