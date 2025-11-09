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

    def handle_alert_box(self):
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")

        self.get_element(locator=(By.XPATH, "//button[text()='Alert']")).click()
        print("alert msg:", self.alert.text)
        time.sleep(5)

        #accept
        self.alert.accept()
        time.sleep(2)

    def handle_click_box(self):
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")

        self.get_element(locator=(By.XPATH, "//button[text()='Alert']")).click()
        print("alert msg:", self.alert.text)
        time.sleep(5)

        # accept
        self.alert.accept()
        time.sleep(2)
    def handle_click_me(self):
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")
        self.get_element(locator=(By.XPATH, "//h1[text()='Alerts']/following::button[text()='Click Me'][1]")).click()
        time.sleep(6)
        print("click me :", self.alert.text)

        time.sleep(10)

        self.alert.accept()

    def confirm_box(self):
        self.driver.get("https://artoftesting.com/samplesiteforselenium")
        self.get_element(locator=(By.XPATH,"//button[text()='Generate Confirm Box']")).click()
        print("confirm box", self.alert.text)
        self.alert.accept()
        ui_msg=self.get_element(locator=(By.ID,"demo")).text
        assert ui_msg=="You pressed OK!"

        self.get_element(locator=(By.XPATH,"//button[text()='Generate Confirm Box']")).click()
        self.alert.dismiss()
        ui_msg=self.get_element(locator=(By.ID,"demo")).text
        assert ui_msg=="You pressed Cancel!"



        time.sleep(3)





obj=HandleAlerts()
obj.handle_alert_box()
obj.handle_click_me()
obj.confirm_box()




