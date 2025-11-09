from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SeleniumLocators:
    def __init__(self,browser):
        if browser == 'Chrome':
            self.driver=webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def redbus(self):
        self.driver.get("https://www.redbus.com/")
        time.sleep(5)

obj=SeleniumLocators("Chrome")
obj.redbus()