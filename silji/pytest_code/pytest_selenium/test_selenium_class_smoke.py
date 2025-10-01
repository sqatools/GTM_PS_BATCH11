import time

import pytest
from selenium.webdriver.common.by import By


class Facebook:

    @pytest.fixture(autouse=True,scope="function")
    def setup(self,get_driver):
        self.driver=get_driver

    def test_login_fb:
        self.driver.find_element(By.ID,"email").sendkeys("silji")
        self.driver.find_element(By.ID, "pass").sendkeys("silji123")
        time.sleep(5)