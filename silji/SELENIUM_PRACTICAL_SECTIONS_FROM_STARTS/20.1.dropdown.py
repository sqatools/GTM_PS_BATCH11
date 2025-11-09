import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class HandleDropdownValues:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.wait=WebDriverWait(self.driver,10)


    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def select_option_value(self,dropdownlocator):
        dropdown_element=self.get_element(locator=dropdownlocator)
        select_obj=Select(dropdown_element)
        return select_obj

    def select_dropdown_value_by_text(self):
        self.driver.get("https://practice.expandtesting.com/dropdown")
        pass_dropdown_element=self.get_element(locator=(By.ID,"dropdown"))
        select_obj=Select(pass_dropdown_element)
        select_obj.select_by_value("1")
        time.sleep(5)
        select_obj.select_by_visible_text("Option 2")
        time.sleep(5)

    def select_country(self):
        self.driver.get("https://practice.expandtesting.com/dropdown")
        country_options_element = self.get_element(locator=(By.ID, "country"))
        select_obj=Select(country_options_element)
        select_obj.select_by_index(1)
        time.sleep(5)
        print("yes done:", select_obj.first_selected_option.text)


           # This is the portion i just copied here  from top for understanding  how this works and based on this next steps followed
           #  def date_of_birth(self):

        # def select_option_value(self, dropdownlocator):
        #     dropdown_element = self.get_element(locator=dropdownlocator)
        #     select_obj = Select(dropdown_element)
        #     return select_obj
        #     


    def date_of_birth(self):
         self.driver.get("https://practice.expandtesting.com/dropdown")
         self.select_option_value(dropdownlocator=(By.ID,"elementsPerPageSelect")).select_by_value("20")
         time.sleep(5)











obj=HandleDropdownValues()
obj.select_dropdown_value_by_text()
obj.select_country()
obj.date_of_birth()



