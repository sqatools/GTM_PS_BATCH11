from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
class HRM:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.alert = Alert(self.driver)
    def get_element(self,locator,cond=ec.visibility_of_element_located):
        return self.wait.until(cond(locator))
    def click(self, locator):
        self.get_element(locator).click()
    def send_keys(self, locator, keys):
        self.get_element(locator).send_keys(keys)
    def login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.send_keys((By.NAME, "username"), "Admin")
        self.send_keys((By.NAME, "password"), "admin123")
        self.click((By.XPATH, "//button[text()=' Login ']"))
obj=HRM()
obj.login()