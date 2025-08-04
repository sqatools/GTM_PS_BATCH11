import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class HRM:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.wait=WebDriverWait(self.driver,10)
        self.alert=Alert(self.driver)
    def get_element(self,locator,cond=ec.visibility_of_element_located):
        return  self.wait.until(cond(locator))

    def get_click(self,locator):
        self.get_element(locator).click()
    def send_keys(self,locator,keys):
        self.get_element(locator).send_keys(keys)
    def Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.send_keys((By.NAME,"username"),"Admin")
        self.send_keys((By.NAME,"password"),"admin123")
        time.sleep(3)
        self.get_click((By.XPATH,"//button[text()=' Login ']"))
        time.sleep(2)

    def Admin(self):
            self.get_element(locator=(By.XPATH, "//*[text()='Admin']")).click()
            self.get_click((By.XPATH, "//*[text()='Admin']"))
            time.sleep(3)
            self.send_keys((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]"),"demotest")
            time.sleep(3)
            self.get_click((By.XPATH, "//button[@type='submit']"))

    def PIM(self):
            self.get_element(locator=(By.XPATH, "(//span[text()='PIM'])")).click()
            time.sleep(3)
            self.get_click((By.XPATH, "//button[normalize-space ()='Add'] "))
            time.sleep(3)
            self.send_keys((By.XPATH, "//input[@name='firstName']"),"shyam")
            self.send_keys((By.XPATH, "//input[@name='middleName']"), "Gajanan")
            self.send_keys((By.XPATH, "//input[@name='lastName']"), "Bodade")
            time.sleep(5)
            self.send_keys((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]"), "123")
            self.get_click((By.XPATH, "//button[normalize-space()='Save']"))
            time.sleep(2)

    def leave(self):
            self.get_click((By.XPATH, "//span[text()='Leave']"))
            time.sleep(5)
            self.get_click((By.XPATH, "//input[@placeholder='yyyy-dd-mm'])[1]"))
            time.sleep(2)
            self.get_click((By.XPATH, "//div[@class='oxd-calendar-date'][normalize-space()='2']"))
            self.get_click((By.XPATH, "//input[@placeholder='yyyy-dd-mm'])[2]"))
            self.get_click((By.XPATH, "//div[@class='oxd-calendar-date'][normalize-space()='5']"))
            time.sleep(3)
            self.get_click((By.XPATH, "//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]"))
            self.get_click((By.XPATH, "//div[normalize-space()='Taken']"))
            time.sleep(2)
            self.get_click((By.XPATH, "//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[2]"))
            time.sleep(3)
            self.get_click((By.XPATH, "//span[text()='CAN - Bereavement']"))
            self.get_click((By.XPATH, "//button[normalize-space()='Search']"))

    def Time(self):
            self.get_click((By.XPATH, "//span[text()='Time']"))
            time.sleep(2)
            self.send_keys((By.XPATH, "//input[@placeholder='Type for hints...']"), "shyam Gajanan Bodade")
            time.sleep(2)
            self.get_click((By.XPATH, "//span[text()='shyam Gajanan Bodade'])[1]"))
            self.get_click((By.XPATH, "//button[@type='submit']"))
            time.sleep(3)
            self.get_click((By.XPATH, "//button[normalize-space()='Create Timesheet']"))
            time.sleep(2)

obj = HRM()
obj.Login()
obj.Admin()
obj.PIM()
obj.leave()
obj.Time()

