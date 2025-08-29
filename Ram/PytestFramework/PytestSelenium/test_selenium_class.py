import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("get_driver")
class TestFacebookLogin:

    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver

    def test_facebook_login(self):
        self.driver.find_element(By.NAME, "email").send_keys("ram@gmail.com")
        self.driver.find_element(By.NAME, "pass").send_keys("ram12345")
        time.sleep(2)
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(3)
        self.driver.back()
        time.sleep(2)

    def test_create_new_account(self):
        self.driver.find_element(By.LINK_TEXT, "Create new account").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("Ram")
        self.driver.find_element(By.NAME, "lastname").send_keys("V")
        dd_day = self.driver.find_element(By.NAME, "birthday_day")
        dd_select = Select(dd_day)
        dd_select.select_by_visible_text("20")
        dd_day = self.driver.find_element(By.NAME, "birthday_day")
        dd_select = Select(dd_day)
        dd_select.select_by_visible_text("20")
        dd_month = self.driver.find_element(By.NAME, "birthday_month")
        dd_select1 = Select(dd_month)
        dd_select1.select_by_visible_text("Dec")
        dd_year = self.driver.find_element(By.NAME, "birthday_year")
        dd_select2 = Select(dd_year)
        dd_select2.select_by_visible_text("1990")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='radio' and @value='2']").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "reg_email__").send_keys("ram@gmail.com")
        self.driver.find_element(By.NAME, "reg_passwd__").send_keys("ram12345")
        self.driver.find_element(By.NAME, "websubmit").click()
        time.sleep(5)
