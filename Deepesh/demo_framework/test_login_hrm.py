import time

import pytest
from .login_page_class import LoginPage


@pytest.mark.usefixtures("get_driver")
class TestLoginHRM:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.lp = LoginPage(self.driver)


    def test_login_hrm_website_and_verify(self):
        self.lp.launch_login_page(url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lp.login_to_rhm(username="Admin", password="admin123")
        time.sleep(10)
