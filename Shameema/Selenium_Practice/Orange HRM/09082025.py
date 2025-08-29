import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


# from 9082025 locators import *

class sle_menthods:

    def __init__(self):
        self.driver = webdriver.Chrome( )
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window( )
        self.driver.implicitly_wait(10)

    def url_launch(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator, **kwargs):
        self.get_element(locator=locator, **kwargs).click()

    def enter_data(self, locator, value, **kwargs):
        self.get_element(locator=locator, **kwargs).send_keys(value)

    def Login(self):
        self.enter_data(locator=(By.NAME, "username"), value='Admin')
        self.enter_data(locator=(By.NAME, 'password'), value='admin123')
        self.click_element(locator=(By.XPATH, "//button[@type='submit']"))
        time.sleep(10)

    def Admin_addnewuser(self):
        # self.click_element(By.XPATH, "//a[@text()='Admin']")
        self.click_element(locator=(By.XPATH,"//span[contains(.,'Admin')]//parent::a[@class='oxd-main-menu-item']"))
        time.sleep(10)
        self.click_element(locator=(By.XPATH,"//button[@type='submit']"))


        # self.enter_data(locator=(By.XPATH,"//label[contains(.,'Username')]//parent::div//following-sibling::div/input"),value='Rumeha')
        # time.sleep(10)
        # # // label[text( ) = 'User Role'] // parent:: // following - sibling::div / div / div / div[contains(., Admin
        # # ')]
        # self.enter_data(locator=(By.XPATH,"//input[@placeholder='Type for hints...']"),value='Rumeha')
        # time.sleep(10)
        # self.click_element(locator=(By.XPATH,"//label[text()='Status']//parent::div//following-sibling::div/div/div/div[text()='Enabled']"))
        # time.sleep(10)

    # def forgot_password(self):
    #     self.enter_data(locator=(By.NAME,'username'),value='Admin')
    #     # self.click_element(locator=(By.CLASS_NAME,'oxd-text oxd-text--p orangehrm-login-forgot-header'))
    #     # self.enter_data(locator=(By.NAME, 'password'), value='123')
    #     self.click_element(locator=(By.XPATH,"//*[@type = 'submit']"),cond = ec.element_to_be_clickable)
    #     time.sleep(20)
    #     self.click_element(locator=(By.XPATH,"//button[contains(@class,'oxd-button--large')and (@type ='button')]"))


#once user name is entered, password is changing to required field hence forgotten password is not clicked.


obj = sle_menthods( )
obj.url_launch( )
obj.Login( )
obj.Admin()
# obj.forgot_password()
