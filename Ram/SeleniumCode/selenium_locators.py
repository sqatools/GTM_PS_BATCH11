import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumMethods:
    """
        Type of locators

        1. ID = "id"  # done
        2. XPATH = "xpath"
        3. LINK_TEXT = "link text" # done
        4. PARTIAL_LINK_TEXT = "partial link text" # done
        5. NAME = "name" # done
        6. TAG_NAME = "tag name"
        7. CLASS_NAME = "class name"
        8. CSS_SELECTOR = "css selector"
        """

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


