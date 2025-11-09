import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HandleIframes:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def Handle_iframe_element(self):
        self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
        frame_element = self.get_element(locator=(By.NAME, "globalSqa"))
        # switch to iframe
        self.driver.switch_to.frame(frame_element)

        # navigate to menu button in the iframe
        menu_element = self.get_element(locator=(By.XPATH, "//div[@id='mobile_menu_toggler']"))
        menu_element.click()
        time.sleep(3)

        # get heading inside the iframe
        frame_heading = self.get_element(locator=(By.XPATH, "//div[@class='page_heading']")).text
        print("frame heading :", frame_heading)

        # Navigate to menu button and click on it.
        # self.get_element(locator=(By.XPATH, "//div[@id='mobile_menu']//a[text()='Contact Us']")).click()
        self.get_element(locator=(By.XPATH, "//a[normalize-space()='Contact Us']")).click()

        time.sleep(3)

        # Switch back to default main page
        self.driver.switch_to.default_content()

        # get heading of main page
        main_heading = self.get_element(locator=(By.XPATH, "//div[@class='page_heading']")).text
        print("main page heading :", main_heading)


obj = HandleIframes()
obj.Handle_iframe_element()
