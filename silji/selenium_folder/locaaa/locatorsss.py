import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumLocators:

    def __init__(self, browser):
        if browser.lower() == 'chrome':
            # Launch chrome browser and initiate driver variable
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            # Launch Firefox browser and initiate driver variable
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            # Launch Edge browser and initiate driver variable
            self.driver = webdriver.Edge()

        # wait for element
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def facebook_website(self):
        self.driver.get("https://www.facebook.com/")

        # get element with ID locator
        self.driver.find_element(By.ID, "email").send_keys("user@gmail.com")

        # get element with Name locator
        self.driver.find_element(By.NAME, "pass").send_keys("user#1000")

        time.sleep(5)

        # get element with link_text locator
        self.driver.find_element(By.LINK_TEXT, "Create new account").click()

        time.sleep(5)
        # get element with partial_link_text locator
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Already have").click()

        time.sleep(5)
        # get element with tagname locator
        all_images = self.driver.find_elements(By.TAG_NAME, "img")

        # iterate through the element and perform operation.
        for image in all_images:
            print(image.get_attribute("alt"))


        time.sleep(5)
        self.driver.close()


obj = SeleniumLocators("chrome")
obj.facebook_website()
