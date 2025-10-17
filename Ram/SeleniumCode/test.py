import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class OrangeHrmLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, condition=ec.visibility_of_element_located):
        element = self.wait.until(condition(locator))
        return element

    def element_click(self, locator, **kwargs):
        self.get_element(locator, **kwargs).click()

    def select_dropdown_value(self, locator):
        element = self.get_element(locator=locator)
        return Select(element)

    def orangehrm_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.get_element(locator=(By.NAME, "username")).send_keys("Admin")
        self.get_element(locator=(By.NAME, "password")).send_keys("admin123")
        self.element_click(locator=(By.XPATH, "//button[contains(@class, 'oxd-button oxd-button--medium')]"),
                           condition=ec.element_to_be_clickable)
        time.sleep(3)
        self.element_click(locator=(By.XPATH, "//span[text()='Admin']"))
        # //a[contains(@class, 'oxd-main-menu-item active toggle')]//following::span[text()='Admin']
        time.sleep(2)
        self.element_click(locator=(By.XPATH, "//span[normalize-space(text())='User Management']"))
        self.element_click(locator=(By.XPATH, "//a[text()= 'Users']"))
        self.element_click(locator=(By.XPATH, "//i[contains(@class, 'oxd-icon bi-plus "
                                              "oxd-button-icon')]//parent::button[normalize-space(string(.))='Add']"))

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//label[text()='User Role']/following::div[1]").click()
        time.sleep(1)
        self.get_element(locator=(By.XPATH, "//*[normalize-space(text())='Admin']")).click()
        time.sleep(3)
        self.get_element(locator=(By.XPATH, "//input[@placeholder='Type for hints...']")).send_keys("John")
        self.driver.find_element(By.XPATH, "//label[text()='Status']/following::div[1]").click()
        time.sleep(1)
        self.get_element(locator=(By.XPATH, "//*[normalize-space(text())='Enabled']")).click()
        time.sleep(2)
        self.get_element(locator=(By.XPATH, "//label[text()='Username']/following::input[1]")).send_keys("John1234")
        self.get_element(locator=(By.XPATH, "//label[text()='Password']/following::input[1]")).send_keys("John@1234")
        self.get_element(locator=(By.XPATH, "//label[text()='Confirm Password']/following::input[1]")).send_keys("John@1234")
        time.sleep(2)
        self.element_click(locator=(By.XPATH, "//button[contains(., 'Save')]"))
        time.sleep(7)


obj = OrangeHrmLogin()
obj.orangehrm_login()
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")
#
# wait = WebDriverWait(driver, 10)
#
#     # Step 1: Click the dropdown
# dropdown = driver.find_element(By.XPATH,
#                                    "//label[text()='User Role']/ancestor::div[contains(@class,'oxd-input-group')]")
# dropdown.click()
#
# # Step 2: Wait for and click the 'Admin' option
# option = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@role='option' and text()='Admin']")))
# option.click()
#
#
#
