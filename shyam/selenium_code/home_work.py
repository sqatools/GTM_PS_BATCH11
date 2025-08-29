import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class HRM:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.wait=WebDriverWait(self.driver,10)
        self.alert=Alert(self.driver)
    def get_element(self,locator,cond=ec.visibility_of_element_located):
        element=self.wait.until(cond(locator))
        return element
    def click(self,locator):
        self.get_element(locator).click()

    def login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.get_element(locator=(By.NAME,"username")).send_keys("Admin")
        self.get_element(locator=(By.NAME,"password")).send_keys("admin123")
        self.get_element(locator=(By.XPATH,"//button[text()=' Login ']")).click()
        time.sleep(5)
    def Admin(self):
        self.get_element(locator=(By.XPATH,"//*[text()='Admin']")).click()
        time.sleep(3)

        self.get_element(locator=(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")).send_keys("demotest")
        self.driver
        time.sleep(3)
        self.get_element(locator=(By.XPATH,"//button[@type='submit']")).click()
    def PIM(self):
        self.get_element(locator=(By.XPATH,"(//span[text()='PIM'])")).click()
        time.sleep(3)
        self.get_element(locator=(By.XPATH,"//button[normalize-space ()='Add'] ")).click()
        time.sleep(3)
        self.get_element(locator=(By.XPATH, "//input[@name='firstName']")).send_keys("shyam")
        self.get_element(locator=(By.XPATH, "//input[@name='middleName']")).send_keys("Gajanan")
        self.get_element(locator=(By.XPATH, "//input[@name='lastName']")).send_keys("Bodade")
        time.sleep(5)
        self.get_element(locator=(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")).send_keys("123")
        self.get_element(locator=(By.XPATH, "//button[normalize-space()='Save']")).click()
        time.sleep(2)
    def leave(self):
        self.get_element(locator=(By.XPATH,"//span[text()='Leave']")).click()
        time.sleep(5)
        self.get_element(locator=(By.XPATH,"(//input[@placeholder='yyyy-dd-mm'])[1]")).click()
        time.sleep(2)
        self.get_element(locator=(By.XPATH,"//div[@class='oxd-calendar-date'][normalize-space()='2']")).click()
        self.get_element(locator=(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")).click()
        self.get_element(locator=(By.XPATH, "//div[@class='oxd-calendar-date'][normalize-space()='5']")).click()
        time.sleep(3)
        self.get_element(locator=(By.XPATH,"(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]")).click()
        self.get_element(locator=(By.XPATH,"//div[normalize-space()='Taken']")).click()
        time.sleep(2)
        self.get_element(locator=(By.XPATH,"(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[2]")).click()
        time.sleep(2)
        self.get_element(locator=(By.XPATH,"//span[text()='CAN - Bereavement']")).click()
        self.get_element(locator=(By.XPATH,"//button[normalize-space()='Search']")).click()


    def Time(self):
        self.get_element(locator=(By.XPATH,"//span[text()='Time']")).click()
        time.sleep(2)
        self.get_element(locator=(By.XPATH,"//input[@placeholder='Type for hints...']")).send_keys("shyam Gajanan Bodade")
        time.sleep(2)
        self.get_element(locator=(By.XPATH,"(//span[text()='shyam Gajanan Bodade'])[1]")).click()
        self.get_element(locator=(By.XPATH,"//button[@type='submit']")).click()
        time.sleep(3)
        self.get_element(locator=(By.XPATH,'//button[normalize-space()="Create Timesheet"] ')).click()
        time.sleep(2)




obj=HRM()
obj.login()
obj.Admin()
obj.PIM()
obj.leave()
obj.Time()