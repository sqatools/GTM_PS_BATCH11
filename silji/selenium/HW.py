import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os



class SeleniumMethods:

    def __init__(self, browser):

        if browser.lower() == 'chrome':
            # Launch chrome browser and initiate driver variable
            # opt = Options()
            # opt.add_experimental_option("detach", True)
            #self.driver = webdriver.Chrome(options=opt)
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


    def forward_back_refresh(self):
        self.driver.get("https://www.goibibo.com/bus/")
        self.driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
        self.driver.find_element(By.NAME, "pass").send_keys("user12345")

        # Navigate to create account page
        self.driver.find_element(By.LINK_TEXT, "Create new account").click()
        time.sleep(5)
        self.driver.save_screenshot("sign_up_page.png")

        # Navigate to back to login page
        self.driver.back()
        time.sleep(5)
        self.driver.save_screenshot("login_page.png")

        # Navigate forward signup page.
        self.driver.forward()
        time.sleep(5)
        self.driver.save_screenshot("sign_up_page_2.png")

        # Navigate to back to login page
        self.driver.back()
        time.sleep(5)

        # refresh the login page.
        self.driver.refresh()

        # close
        # self.driver.close()

obj = SeleniumMethods(browser='chrome')
obj.forward_back_refresh()