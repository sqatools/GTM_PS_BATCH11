import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec


class Fblogin:

    def __init__(self):
        self.driver = webdriver.Chrome( )
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window( )

    def get_ele(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    # def get_text(self,locator,textwrap,**kwargs):
    #     self.get_ele(locator=locator,**kwargs).text
    #
    def click_ele(self, locator, **kwargs):
        self.get_ele(locator=locator, **kwargs).click( )

    def enter_data(self, locator, value, **kwargs):
        self.get_ele(locator=locator, **kwargs).send_keys(value)

    # def sel_dropele(self, drop_down_locator):
    #     drop_down_element = self.get_ele(locator=drop_down_locator)
    #     select_obj = Select(drop_down_element)
    #     return select_obj

    def url_launch(self):
        self.driver.get("https://www.facebook.com")

    def fbLogin(self):
        self.enter_data(locator=(By.ID, 'email'), value="abc")
        self.enter_data(locator=(By.ID, 'pass'), value='123')
        self.click_ele(locator=(By.XPATH, "//button[@name='login']"), cond=ec.element_to_be_clickable)

        time.sleep(20)

    # que: login button is not clicked
    def create_ac(self):
        self.click_ele(locator=(By.XPATH, " // a[ @data-testid='open-registration-form-button']"))
        self.enter_data(locator=(By.XPATH, "//input[@name='firstname']"), value='Renga')
        self.enter_data(locator=(By.XPATH, "//input[@name='lastname']"), value='Nayagi')
        self.click_ele(locator=(By.XPATH, "//select[@id='day']"))
        self.click_ele(locator=(By.XPATH, "//option[text()='1']"))
        self.click_ele(locator=(By.XPATH, "//select[@id='month']"))
        self.click_ele(locator=(By.XPATH, "//option[text()='Jan']"))
        self.click_ele(locator=(By.XPATH, "//select[@id='year']"))
        self.click_ele(locator=(By.XPATH, "//option[text()='2000']"))
        self.click_ele(locator=(By.XPATH, "//label[text()='Female']"))
        time.sleep(5)
        self.enter_data(locator=(By.XPATH, "//input[@aria-label='Mobile number or email address']"),
                        value='testemail@email.com')

        time.sleep(10)
        self.enter_data(locator=(By.NAME, 'reg_passwd__'), value='Rock*135')
        self.click_ele(locator=(By.NAME, 'websubmit'))
        time.sleep(15)
        # self.sel_dropele(locator=(By.XPATH,"//option[text()='1']"),value='1')/\


# que: email id field not working, able to enter password


obj = Fblogin( )
obj.url_launch( )
# obj.fbLogin( )
obj.create_ac()
