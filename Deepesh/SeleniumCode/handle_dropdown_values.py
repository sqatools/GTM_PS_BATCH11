import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from common_data import *

if LANG == 'eng-us':
    from dd_locators import *
elif LANG == "chinese":
    from dd_locators_chinese import *


class HandleDropdownValues:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def select_option_value(self, dropdown_locator):
        dropdown_element = self.get_element(locator=dropdown_locator)
        select_obj = Select(dropdown_element)
        return select_obj

    def click_element(self, locator, **kwargs):
        self.get_element(locator=locator, **kwargs).click()

    def enter_text(self, locator, value, **kwargs):
        self.get_element(locator=locator, **kwargs).send_keys(value)



    def select_dropdown_value_by_text(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        pass_dropdown_element = self.get_element(locator=(By.ID, "admorepass"))
        select_obj = Select(pass_dropdown_element)
        select_obj.select_by_visible_text("Add 3 more passenger (200%)")
        time.sleep(5)

        country_dropdown_element = self.get_element(locator=(By.ID, "billing_country"))
        select_obj2 = Select(country_dropdown_element)
        select_obj2.select_by_visible_text("India")
        time.sleep(5)


    def select_dropdown_by_value(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.select_option_value(dropdown_locator=(By.ID, "admorepass")).select_by_value("3")
        time.sleep(5)
        self.select_option_value(dropdown_locator=(By.ID, "billing_country")).select_by_value("AD")
        time.sleep(5)


    def select_dropdown_by_indexing(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.select_option_value(dropdown_locator=(By.ID, "admorepass")).select_by_index(1)
        time.sleep(5)
        self.select_option_value(dropdown_locator=(By.ID, "billing_country")).select_by_index(3)

        # Get list of all options
        all_option = self.select_option_value(dropdown_locator=(By.ID, "billing_country")).options
        for opt in all_option:
            print(opt.text)
        time.sleep(5)


    def select_dynamic_values(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.get_element(LoginLocator.username_field_loc).send_keys("Admin")
        self.get_element(LoginLocator.pass_field_loc).send_keys("admin123")
        self.get_element(LoginLocator.login_btn).click()

        self.get_element(LeaveLocator.leave_page_loc).click()
        self.get_element(LeaveLocator.leave_type_dropdown).click()
        time.sleep(3)
        self.get_element(LeaveLocator.leave_type_value).click()
        time.sleep(10)


    def select_dynamic_values_updated(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.enter_text(LoginLocator.username_field_loc, value="Admin")
        self.enter_text(LoginLocator.pass_field_loc, value="admin123")
        self.click_element(LoginLocator.login_btn, cond=ec.element_to_be_clickable)

        self.click_element(LeaveLocator.leave_page_loc)
        self.click_element(LeaveLocator.leave_type_dropdown)
        time.sleep(3)
        self.click_element(LeaveLocator.leave_type_value, cond=ec.element_to_be_clickable)
        time.sleep(10)



obj = HandleDropdownValues()
obj.select_dropdown_value_by_text()
#obj.select_dropdown_by_value()
#obj.select_dropdown_by_indexing()
#obj.select_dynamic_values()
#obj.select_dynamic_values_updated()


