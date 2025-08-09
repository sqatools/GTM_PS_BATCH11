import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumLocators:

    def __init__ (self,browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def facebook_website(self):
        self.driver.get("https://www.facebook.com")
        self.driver.find_element(By.NAME,"email").send_keys("user1@gmail.com")
        self.driver.find_element(By.NAME,"pass").send_keys("user@12345")
        self.driver.find_element()

        time.sleep(5)

        self.driver.find_element(By.LINK_TEXT,"Create new account").click()

        time.sleep(5)

        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Already have").click()

        time.sleep (5)

        all_images = self.driver.find_elements(By.TAG_NAME,"img")
        for imgs in all_images:


        self.driver.close()


rum = SeleniumLocators("chrome")
rum.facebook_website()

