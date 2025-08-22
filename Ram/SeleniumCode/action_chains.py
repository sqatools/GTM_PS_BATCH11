import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class ActionChain:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def get_element(self, locator, condition=ec.visibility_of_element_located):
        element = self.wait.until(condition(locator))
        return element

    def element_click(self, locator, **kwargs):
        self.get_element(locator, **kwargs).click()

    def get_text(self, locator):
        return self.get_element(locator).text

    def hover_to_element(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        tester_hub_element = self.get_element(locator=(By.XPATH, "//div[@id='menu']//a[contains(text(), 'Tester’s Hub')]"))
        self.action.move_to_element(tester_hub_element).perform()
        time.sleep(3)
        demo_testing_element = self.get_element(locator=(By.XPATH, "//ul[@class='sub-menu']//span[text()='Demo Testing Site']"))
        self.action.move_to_element(demo_testing_element).perform()
        time.sleep(3)
        alertbox_element = self.get_element(locator=(By.XPATH, "//ul[@class='sub-menu']//span[text()='AlertBox']"))
        self.action.click(alertbox_element).perform()
        time.sleep(5)

    def drag_and_drop_operations(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        iframe_element = self.get_element(locator=(By.XPATH, "//iframe[contains(@src,'practice/droppable/photo')]"))
        self.driver.switch_to.frame(iframe_element)

        # drag and drop operation for single image
        source_img_element = self.get_element(locator=(By.XPATH, "//h5[text()='High Tatras']//parent::li"))
        trash_element = self.get_element((By.ID, "trash"))
        self.action.drag_and_drop(source_img_element, trash_element).perform()
        time.sleep(5)

        # drag and drop operation for multiple images
        for i in range(2, 5):
            source_img_element1 = self.get_element(locator=(By.XPATH, f"//h5[text()='High Tatras {i}']//parent::li"))
            trash_element = self.get_element((By.ID, "trash"))
            self.action.drag_and_drop(source_img_element1, trash_element).perform()
            time.sleep(5)

    def context_click_operations(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        # heading_element = self.get_element(locator=(By.XPATH, "//h1[text()='Drag And Drop']"))
        # self.action.context_click(heading_element).perform()
        # time.sleep(3)

        about_element = self.get_element(locator=(By.XPATH, "//div[@id='menu']//a[text()='About']"))
        self.action.context_click(about_element).perform()
        time.sleep(5)

        # to simulate the mouse and keyboard actions on browser for popup we have to use pyautogui
        # pip install pyautogui
        pyautogui.press("up")
        time.sleep(5)
        pyautogui.press("enter")
        time.sleep(10)
        # about_element.send_keys(Keys.ENTER)


obj = ActionChain()
# obj.hover_to_element()
# obj.drag_and_drop_operations()
obj.context_click_operations()