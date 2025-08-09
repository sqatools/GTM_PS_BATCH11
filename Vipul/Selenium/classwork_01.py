import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


class Classwork:
    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator):
        self.get_element(locator).click()

    def get_text(self, locator):
        return self.get_element(locator).text

    def select_dropdown_value(self, locator):
        element = self.get_element(locator=locator)
        return Select(element)



    def login(self):
        self.driver.get("https://www.facebook.com/")
        username_element = self.get_element(locator=(By.ID,'email'))
        username_element.send_keys("vipul1264")
        password_element = self.get_element(locator=(By.ID,'pass'))
        password_element.send_keys("vipul1264")
        self.click_element(locator=(By.NAME,'login'))
        error_text = self.get_text(locator=(By.CSS_SELECTOR, '._9ay7'))
        print("error msg : ", error_text)
        time.sleep(3)
        self.driver.back()

    def create_account(self):
        self.driver.get("https://www.facebook.com/")
        self.click_element(locator=(By.LINK_TEXT,'Create new account'))
        first_name_element = self.get_element(locator=(By.XPATH,"//input[@name='firstname']"))
        first_name_element.send_keys("tester")
        last_name_element = self.get_element(locator=(By.XPATH,"//input[@name='lastname']"))
        last_name_element.send_keys("automation")
        time.sleep(2)
        #day_dropdown = self.get_element(locator=(By.ID,'day'))
        # select_obj = Select(day_dropdown)
        # select_obj.select_by_value("19")
        #month_dropdown = self.get_element(locator=(By.ID, 'month'))
        # select_obj = Select(month_dropdown)
        # select_obj.select_by_index(7)
        # year_dropdown = self.get_element(locator=(By.ID, 'year'))
        # select_obj = Select(year_dropdown)
        # select_obj.select_by_visible_text('1995')

        self.select_dropdown_value(locator=(By.ID,'day')).select_by_value("19")
        self.select_dropdown_value(locator=(By.ID, 'month')).select_by_index(7)
        self.select_dropdown_value(locator=(By.ID, 'year')).select_by_visible_text("1995")

        self.click_element(locator=(By.XPATH,"//span[@class='_5k_2 _5dba']//input[@value='2']"))
        email_element = self.get_element(locator=(By.XPATH, "//input[@name='reg_email__']"))
        email_element.send_keys("vipul12645@gmail.com")
        password_element = self.get_element(locator=(By.XPATH,"//input[@name='reg_passwd__']"))
        password_element.send_keys("vipul12645")
        time.sleep(2)
        self.click_element(locator=(By.LINK_TEXT,'Sign Up'))

obj = Classwork()
obj.login()
obj.create_account()