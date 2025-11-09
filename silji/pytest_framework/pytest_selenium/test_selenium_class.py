import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestOpenHRM:

    @pytest.fixture(autouse=True, scope="function")   
    def setup(self, get_driver):
        """
        # if we don't define the scope of the fixture
        # then default scope is scope=function
        :param get_driver:
        :return:
        """
        self.driver = get_driver


    def test_login_hrm(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(5)