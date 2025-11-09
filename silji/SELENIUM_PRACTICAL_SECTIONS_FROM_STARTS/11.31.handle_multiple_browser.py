import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class HandleBrowserTabs:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def handle_browser_tabs(self):
        # Open Facebook
        self.driver.get("https://www.facebook.com/")

        # Click on "Create new account"
        self.get_element(locator=(By.XPATH, "//a[contains(text(),'Create new account')]")).click()


        time.sleep(3)



        # Enter first name
        self.get_element(locator=(By.XPATH, "//input[@name='firstname']")).send_keys("silji")

        time.sleep(5)
        print("Entered first name successfully!")

        # Close the browser
        self.driver.quit()


obj = HandleBrowserTabs()
obj.handle_browser_tabs()