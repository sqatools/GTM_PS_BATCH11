import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumLocators:
    def __init__(self, browser):
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Unsupported browser! Use chrome, firefox, or edge.")

        # These should be outside of the if-elif block so they run for all browsers
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def facebook_website(self):
        self.driver.get("https://www.facebook.com/")
        time.sleep(3)  # Just to keep it open for a few seconds


        self.driver.find_element(By.ID, "email").send_keys("silji@gmail.com")
        time.sleep(3)
        self.driver.find_element(By.NAME,"pass").send_keys("pass")
        time.sleep(3)



        self.driver.close()

# Run the test
obj = SeleniumLocators("chrome")
obj.facebook_website()