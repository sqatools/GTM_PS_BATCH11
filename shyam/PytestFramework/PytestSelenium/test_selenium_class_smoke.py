import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestFacebook:
    @pytest.fixture(autouse=True,scope="function")
    def setup(self,get_driver):
          self.driver = get_driver

    def test_login(self):
        self.driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
        self.driver.find_element(By.NAME, "pass").send_keys("abc123")
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(5)
        self.driver.back()

    def test_create(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Sign up for Facebook']").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("abc")
        self.driver.find_element(By.NAME, "lastname").send_keys("abc123")
        self.driver.find_element(By.XPATH, "//select[@id='day']").click()
        self.driver.find_element(By.XPATH, "//option[normalize-space()='10']").click()
        self.driver.find_element(By.XPATH, "//select[@id='month']").click()
        self.driver.find_element(By.XPATH, "//option[normalize-space()='Jul']").click()
        self.driver.find_element(By.XPATH, "//select[@id='year']").click()
        self.driver.find_element(By.XPATH, "//option[normalize-space()='2020']").click()
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Female']").click()
        self.driver.find_element(By.NAME, "reg_email__").send_keys("8698570520")
        self.driver.find_element(By.ID, "password_step_input").send_keys("ABC@abc")
        self.driver.find_element(By.NAME, "websubmit").click()

