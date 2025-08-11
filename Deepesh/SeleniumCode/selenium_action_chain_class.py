import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class HandleActionChain:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)


    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator):
        self.get_element(locator).click()

    def get_text(self, locator):
        return self.get_element(locator).text


    def perform_hover_to_element_operation(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        tester_hub_elem = self.get_element(locator=(By.XPATH, "//div[@id='menu']//a[contains(text(), 'Tester')]"))
        self.action.move_to_element(tester_hub_elem).perform()
        time.sleep(5)

        demo_testing = self.get_element(locator=(By.XPATH, "//div[@id='menu']//a[normalize-space()='Demo Testing Site']"))
        self.action.move_to_element(demo_testing).perform()
        time.sleep(5)

        alert_elem = self.get_element(locator=(By.XPATH, "//div[@id='menu']//a[normalize-space()='AlertBox']"))
        self.action.click(alert_elem).perform()
        time.sleep(5)

    def perform_drag_drop_operations(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        iframe_element = self.get_element(locator=(By.XPATH, "//iframe[contains(@src,'droppable/photo')]"))
        self.driver.switch_to.frame(iframe_element)

        image1_elem = self.get_element(locator=(By.XPATH, "//h5[text()='High Tatras']//parent::li"))
        trash_element = self.get_element(locator=(By.ID, "trash"))
        self.action.drag_and_drop(image1_elem, trash_element).perform()
        time.sleep(5)

        for i in range(2, 5):
            image_elem = self.get_element(locator=(By.XPATH, f"//h5[text()='High Tatras {i}']//parent::li"))
            trash_element = self.get_element(locator=(By.ID, "trash"))
            self.action.drag_and_drop(image_elem, trash_element).perform()
            time.sleep(3)


    def perform_context_click_operation(self):
        """
        module to simulate the mouse action on browser we have to use pyautogui module
        -> pip install pyautogui


        :return:
        """
        import pyautogui
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        time.sleep(10)
        # heading_elem = self.get_element(locator=(By.XPATH, "//h1[text()='Drag And Drop']"))
        # #self.action.double_click(heading_elem).context_click(heading_elem).perform()
        # self.action.context_click(heading_elem).perform()
        # time.sleep(5)

        about_elem = self.get_element(locator=(By.XPATH, "//div[@id='menu']//a[text()='About']"))
        self.action.context_click(about_elem).perform()
        time.sleep(5)
        #about_elem.send_keys(Keys.UP + Keys.ENTER)
        pyautogui.press("up")
        time.sleep(5)
        pyautogui.press("enter")
        time.sleep(10)
        about_elem.send_keys(Keys.ENTER)






obj = HandleActionChain()
obj.perform_context_click_operation()
#obj.perform_drag_drop_operations()
#obj.perform_hover_to_element_operation()