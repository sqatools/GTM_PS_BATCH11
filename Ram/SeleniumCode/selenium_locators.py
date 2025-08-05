import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumMethods:
    def __init__(self, browser):
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif browser.lower() == "edge":
            self.driver = webdriver.Edge()

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def facebook_login(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.NAME, "email").send_keys("user@gmail.com")
        self.driver.find_element(By.NAME, "pass").send_keys("user1234")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Create new account").click()
        time.sleep(5)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Already have an").click()

        self.driver.close()


obj = SeleniumMethods("Chrome")
obj.facebook_login()


