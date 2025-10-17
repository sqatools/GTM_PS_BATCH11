import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_fixture")
class Test_fb:

    @pytest.fixture(autouse=True, scope="function")
    def setup(self, setup_fixture):
        self.driver = setup_fixture

    def test_login(self):
        self.driver.find_element(By.ID, 'email').send_keys("vippulkumar85@gmail.com")
        self.driver.find_element(By.ID,'pass').send_keys("vipul@1264")
        self.driver.find_element(By.XPATH,"//*[@name='login']").click()

    # def test_signup(self):
    #     self.driver.find_element(By.XPATH, "//*[text()='Create new account']").click()
    #     time.sleep(3)
    #     self.driver.find_element((By.XPATH, "//*[@name='firstname']")).send_keys("senior")
    #     time.sleep(3)
    #     self.driver.find_element((By.XPATH, "//*[@name='lastname']")).send_keys("tester")
    #     time.sleep(3)
    #     self.driver.find_element((By.ID, "day")).click()
    #     time.sleep(3)
    #     self.driver.find_element((By.XPATH, "//*[@value='19']")).click()
    #     time.sleep(3)
    #     self.driver.find_element((By.ID, "month")).click()
    #     time.sleep(3)
    #     self.driver.find_element((By.XPATH, "//*[@value='8']")).click()
    #     time.sleep(3)
    #     self.driver.find_element((By.ID, "year")).click()
    #     time.sleep(3)
    #     self.driver.find_element((By.XPATH, "//*[@value='1990']")).click()
    #     time.sleep(3)
    #     self.driver.find_element((By.ID, "sex")).click()
    #     time.sleep(3)
    #     self.driver.find_element((By.NAME, "reg_email__")).send_keys("seniortester@gmail.com")
    #     time.sleep(3)
    #     self.driver.find_element((By.NAME, "reg_passwd__")).send_keys("senior@tester")
