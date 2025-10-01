import time

import pytest
from selenium.webdriver.common.by import By



class Facebook:

    @pytest.fixture(autouse=True,scope="function")
    def setup(self,get_driver):
        self.driver=get_driver

    def test_login_fb_login(self):
        self.driver.find_element(By.ID,"email").send_keys("silji")
        self.driver.find_element(By.ID, "pass").send_keys("silji123")
        time.sleep(5)