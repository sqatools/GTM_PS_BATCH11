import pytest
import time
from .login_page import *


@pytest.mark.usefixtures("get_driver")
class TestLoginFacebook:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.login = LoginPage(self.driver)
        self.create = CreateAccountPage(self.driver)

    def test_facebook_login(self):
        self.login.launch_url(url="https://www.facebook.com/")
        time.sleep(2)
        self.login.login_to_facebook(username="ram@gmail.com", password="ram12345")
        time.sleep(3)
        self.driver.back()
        time.sleep(2)

    def test_create_new_account(self):
        self.create.click_create_acc()
        time.sleep(2)
        self.create.create_new_account(firstname="Ram", lastname="V", dob_day="20", dob_month="Dec", dob_year="1990",
                                       gender="Male", email="ram@gmail.com", password="ram12345")
        time.sleep(5)





