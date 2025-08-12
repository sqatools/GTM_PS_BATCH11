from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class ActionMethods():

    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        # self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        self.wait = WebDriverWait(self.driver,10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator, cond=ec.element_to_be_clickable):
        self.wait.until(cond(locator)).click()

    # def action_method(self):
    #     self.action = ActionChains(self.driver)

    def drag_drop(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        frame_element = self.get_element(locator=(By.XPATH, "(//*[@class='demo-frame'])[1]"))
        self.driver.switch_to.frame(frame_element)
        action = ActionChains(self.driver)
        drag_element = self.get_element(locator=(By.XPATH,"//*[@alt='The peaks of High Tatras']"))
        drop_element = self.get_element(locator=(By.XPATH,"//*[@id='trash']"))
        action.drag_and_drop(drag_element, drop_element).perform()

    def multiple_drag_drop(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        frame_element = self.get_element(locator=(By.XPATH, "(//*[@class='demo-frame'])[1]"))
        self.driver.switch_to.frame(frame_element)
        action = ActionChains(self.driver)
        drag_elements = self.driver.find_elements(By.XPATH, "//*[@id='gallery']//img")# self.get_element(locator=(By.XPATH, "//*[@id='gallery']//img"))
        drop_element = self.get_element(locator=(By.XPATH, "//*[@id='trash']"))

        for element in drag_elements:
            action.drag_and_drop(element, drop_element).perform()
            time.sleep(2)

#

obj = ActionMethods()
obj.drag_drop()


