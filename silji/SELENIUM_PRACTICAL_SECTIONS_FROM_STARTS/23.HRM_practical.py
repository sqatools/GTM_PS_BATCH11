import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
class HandleAlerts:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.wait=WebDriverWait(self.driver,10)
        self.alert=Alert(self.driver)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def select_option_value(self,dropdownlocator):
        dropdown_element=self.get_element(locator=dropdownlocator)
        select_obj=Select(dropdown_element)
        return select_obj

    def orange_hrm(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.get_element(locator=(By.NAME,"username")).send_keys("Admin")
        self.get_element(locator=(By.NAME,"password")).send_keys("admin123")
        self.get_element(locator=(By.XPATH,"//button[@type='submit']")).click()
        time.sleep(5)

    def Admin(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='Dashboard']")))
        time.sleep(2)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='Admin']"))).click()
        time.sleep(5)

    def UserManagement(self):
        user_mgmt = self.get_element(locator=(By.XPATH, "//span[normalize-space(text())='User Management']"))
        user_mgmt.click()
        time.sleep(2)

        # Click on "Users"
        users_option = self.get_element(locator=(By.XPATH, "//a[text()='Users']"))
        users_option.click()
        time.sleep(5)











obj=HandleAlerts()
obj.orange_hrm()
obj.Admin()
obj.UserManagement()
# obj.click_user_management_users()
