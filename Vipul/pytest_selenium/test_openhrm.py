import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("hrm_login")
class Test_Hrm:

    @pytest.fixture(autouse=True, scope="function")
    def setup(self, hrm_login):
        self.driver = hrm_login

    def test_login(self):
        self.driver.find_element(By.XPATH, "//*[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//*[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@type='submit']").click()
