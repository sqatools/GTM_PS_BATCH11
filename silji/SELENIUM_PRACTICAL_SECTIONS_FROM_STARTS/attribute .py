from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SeleniumMethod:
    def __init__(self, browser):
        # Convert browser name to lowercase for consistent comparison
        browser = browser.lower()

        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise Exception("Browser not supported")

        # Initialize driver settings
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get_element_attribute_value(self):
        # Open the page
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
        time.sleep(5)

        # ✅ Updated XPath (the link has a question mark at the end)
        element = self.driver.find_element(By.XPATH, "//a[contains(text(),'What is Software Testing?')]")

        # Print the href attribute
        print("link:", element.get_attribute("href"))

        # Close browser
        self.driver.quit()

# ✅ Create object and call method
obj = SeleniumMethod("Chrome")
obj.get_element_attribute_value()