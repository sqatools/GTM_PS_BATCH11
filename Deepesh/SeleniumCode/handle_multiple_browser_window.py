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

    def login_to_hrm_website(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.get_element(locator=(By.NAME, "username")).send_keys("Admin")
        self.get_element(locator=(By.NAME, "password")).send_keys("admin123")
        self.get_element(locator=(By.XPATH, "//button[contains(., 'Login')]"), cond=ec.element_to_be_clickable).click()
        #time.sleep(10)

    def handle_browser_tabs(self):
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

        # click on link by text
        self.get_element(locator=(By.LINK_TEXT, "Software Testing Principles")).click()

        # get list of window tabs
        windows_list = self.driver.window_handles

        # switch to new tab
        self.driver.switch_to.window(windows_list[1])

        # get list of headings in the new page
        headings_list = self.get_element(locator=(By.XPATH, "//div[contains(@class, 'post-body')]//h3"),cond=ec.presence_of_all_elements_located)
        for heading in headings_list:
            print(heading.text)

        # close new tab
        self.driver.close()

        # switch back to original tab
        self.driver.switch_to.window(windows_list[0])

        time.sleep(5)
        # navigate to back to   robotframework page.
        self.get_element(locator=(By.LINK_TEXT, "Robot Framework")).click()

        time.sleep(5)







obj = HandleBrowserTabs()
#obj.login_to_hrm_website()
obj.handle_browser_tabs()