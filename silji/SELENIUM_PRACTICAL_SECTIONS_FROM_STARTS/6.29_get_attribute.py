from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SeleniumMethod:
    def __init__(self,browser):
        if browser.lower() =='chrome':
            self.driver=webdriver.Chrome()
        elif browser.lower() =='firefox':
            self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get_element_attribute_value(self):
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
        time.sleep(5)

        # element = self.driver.find_element(By.XPATH, "//a[contains(text(),'What is Software Testing')]")
        element = self.driver.find_element(By.XPATH, "//a[normalize-space(text())='What is Software Testing']")
        # element = self.driver.find_element(By.XPATH, "//a[contains(text(),'Software Development Life Cycle')]")
        element = self.driver.find_element(By.XPATH, "//a[normalize-space(text())='What is Software Testing']")

        print("link:", element.get_attribute("href"))
        print(self.driver.current_url)
        self.driver.quit()


obj=SeleniumMethod("Chrome")
obj.get_element_attribute_value()

