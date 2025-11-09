import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

class HandleAlerts:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.wait=WebDriverWait(self.driver,10)
        self.alert=Alert(self.driver)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def handle_prompt_box(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.get_element(locator=(By.XPATH,"//button[text()='Click for JS Prompt']")).click()
        time.sleep(3)
        self.alert.send_keys("TOOL")
        time.sleep(5)
        self.alert.accept()
        ui_msg = self.get_element(locator=(By.ID,"result")).text
        print(ui_msg)
        assert ui_msg == "You entered: TOOL"
        time.sleep(5)

obj=HandleAlerts()
obj.handle_prompt_box()