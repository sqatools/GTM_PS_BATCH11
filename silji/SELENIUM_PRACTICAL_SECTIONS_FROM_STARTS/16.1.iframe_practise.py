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
        return self.wait.until(cond(locator))

    def handle_iframe_element(self):
        self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

        # Switch into iframe
        frame_element = self.get_element((By.NAME, "globalSqa"))
        self.driver.switch_to.frame(frame_element)

        # Click menu inside iframe
        menu_element = self.get_element((By.XPATH, "//div[@id='mobile_menu_toggler']"))
        menu_element.click()
        time.sleep(2)

        # Get heading inside iframe
        frame_heading = self.get_element((By.XPATH, "//div[@class='page_heading']")).text
        print("Frame heading:", frame_heading)

        # Click "Contact Us" link inside iframe
        contact_link = self.get_element((By.XPATH, "//a[normalize-space()='Contact Us']"))
        contact_link.click()
        time.sleep(3)

        # Switch back to main page
        self.driver.switch_to.default_content()

        # Get main page heading
        main_heading = self.get_element((By.XPATH, "//div[@class='page_heading']")).text
        print("Main page heading:", main_heading)
        time.sleep(5)
        self.driver.quit()


obj = HandleIframes()
obj.handle_iframe_element()