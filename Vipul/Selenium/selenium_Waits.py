from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait


class SeleniumWaits:
    def __init__(self, browser):
        options = Options()
        options.add_experimental_option('detach', True)
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome(options=options)
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox(options=options)
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge(options=options)

        self.driver.maximize_window()

    def implicitly_waits(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.implicitly_wait(10)

        t1 = time.time()
        username_field = self.driver.find_element(By.ID, 'email')
        username_field.send_keys("vipul126@gmail.com")
        password_field = self.driver.find_element(By.ID, 'pass')
        password_field.send_keys('09876hvjh')
        t2 = time.time()
        print("actual time taken in implicitly execution", t2 - t1)

    def explicit_waits(self):
        self.driver.get("https://www.facebook.com/")
        self.wait = WebDriverWait(self.driver, 10)

        t1 = time.time()
        username_field = self.wait.until(ec.visibility_of_element_located((By.ID, 'email')))
        username_field.send_keys("vipul126@gmail.com")
        password_field = self.wait.until(ec.visibility_of_element_located((By.ID, 'pass')))
        password_field.send_keys('09876hvjh')
        t2 = time.time()
        print("actual time taken in explicitly wait execution", t2 - t1)

obj = SeleniumWaits(browser='chrome')
obj.implicitly_waits()
obj.explicit_waits()
