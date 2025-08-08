import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options


class Classwork:
    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator):
        self.get_element(locator).click()

    def get_text(self, locator):
        return self.get_element(locator).text
        sleep(3)


    def login(self):
        self.driver.get("https://www.facebook.com/")
        username_element = self.get_element(locator=(By.ID,'email'))
        username_element.send_keys("silji@gmail.com")
        password_element = self.get_element(locator=(By.ID,'pass'))
        password_element.send_keys("silji123")
        self.click_element(locator=(By.NAME,'login'))




obj = Classwork()
obj.login()