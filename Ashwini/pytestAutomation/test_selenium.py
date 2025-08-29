import time

import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestFacebookLogin:

       @pytest.fixture(autouse=True,scope="function")
       def setup(self,get_driver):
           self.driver = get_driver

       def test_login_facebook(self):
           self.driver.find_element(By.NAME,"email").send_keys("ashuj@gmail.com")
           self.driver.find_element(By.NAME,"pass").send_keys("ashu123")
           time.sleep(5)
           self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()

           time.sleep(5)

           self.driver.find_element(By.LINK_TEXT,"Create new account").click()
           self.driver.find_element(By.NAME,"firstname").send_keys("ram")
           self.driver.find_element(By.NAME,"lastname").send_keys("pawar")
           self.driver.find_element(By.ID,"day").send_keys(20)
           self.driver.find_element(By.ID,"month").send_keys("Aug")
           self.driver.find_element(By.ID,"year").send_keys(2025)
           time.sleep(5)

