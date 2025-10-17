from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SeleniumLocators:
    def __init__(self, browser):
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Browser not supported. Choose 'chrome', 'firefox', or 'edge'.")

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def nopcommerce(self):
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.find_element(By.ID, "small-searchterms").send_keys("laptop")
        time.sleep(5)

# ✅ Create object and run test
obj = SeleniumLocators("chrome")
obj.nopcommerce()