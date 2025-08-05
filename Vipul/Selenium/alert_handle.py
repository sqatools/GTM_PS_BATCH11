import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

class Alert_handle:

    def __init__(self):
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.alert = Alert(self.driver)

    def get_element(self, locator, con=ec.visibility_of_element_located):
        element = self.wait.until(con(locator))
        return element

    def click_element(self, locator):
        self.get_element(locator).click()

    def get_text(self, locator):
        return self.get_element(locator).text

    def handle_alert_box(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
        self.click_element(locator=(By.ID, 'btnShowMsg'))
        print("alert msg ::", self.alert.text)

