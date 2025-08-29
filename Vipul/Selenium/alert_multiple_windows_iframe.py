import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class AlertIframe:

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.alert = Alert(self.driver)


    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator, cond=ec.element_to_be_clickable):
        self.wait.until(cond(locator)).click()

    def get_text(self, locator, cond=ec.visibility_of_element_located):
        text = self.wait.until(cond(locator))
        return text


    def alert_box(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
        self.click_element(locator=(By.XPATH, "//*[@id='btnShowMsg']"))
        print("alert msg", self.alert.text)
        self.alert.accept()
        time.sleep(3)

    def alert_confirm_box(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
        self.click_element(locator=(By.XPATH, "//*[text()='Confirm Box']"))
        print("alert msg", self.alert.text)
        self.alert.dismiss()
        time.sleep(3)
        self.click_element(locator=(By.XPATH, "//*[text()='Confirm Box']"))
        print("alert msg", self.alert.text)
        self.alert.accept()
        time.sleep(3)

    def alert_prompt_box(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
        self.click_element(locator=(By.XPATH, "//*[@id='promptbtn']"))
        self.alert.send_keys("Vipul")
        self.alert.accept()
        time.sleep(3)
        msg = self.get_text(locator=(By.XPATH,"//*[@id='prompt']")).text
        print(msg)

    def iframe_methods(self):
        self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
        frame_element = self.get_element(locator=(By.NAME, "globalSqa"))
        self.driver.switch_to.frame(frame_element)
        self.click_element(locator=(By.XPATH, "(//*[@id='mobile_menu_toggler'])[1]"))
        self.click_element(locator=(By.XPATH, "(//*[@id='mobile_menu']//a[text()='Contact Us'])[1]"))
        # Switch back to default main page
        self.driver.switch_to.default_content()

    def multiple_windows(self):
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

        # click on the Software Testing Principles link
        self.click_element(locator=(By.LINK_TEXT, 'Software Testing Principles'))

        # get list of windows tabs
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[1])

        heading_list = self.get_element(locator=(By.XPATH, "//*[@class='post-body entry-content']//h3"), cond=ec.presence_of_all_elements_located)
        for heading in heading_list:
            print(heading.text)

        # switch to back the previous tab
        self.driver.switch_to.window(windows_list[0])







obj = AlertIframe()
# obj.alert_box()
# obj.alert_confirm_box()
# obj.alert_prompt_box()
# obj.iframe_methods()
obj.multiple_windows()



