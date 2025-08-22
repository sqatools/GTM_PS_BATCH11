import time

from .login_page_class import Loginpage
import pytest

@pytest.mark.usefixtures("get_driver")

class TestloginHRM:
    @pytest.fixture(autouse=True)
    def setup(self,get_driver):
        self.driver=get_driver
        self.lp=Loginpage(self.driver)
    def test_login_hrm_website(self):
        self.lp.launch_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lp.hrm(username="Admin",password="admin123")
        time.sleep(10)

