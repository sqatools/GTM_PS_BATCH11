from ...page_object.hrm_page.login_page import LoginPage
import pytest

@pytest.mark.usefixtures("get_driver")
class TestLogin_hrm:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.lp = LoginPage(self.driver)


    def test_verify_login_hrm(self):
        self.lp.launch_login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lp.login_hrm(username="Admin", password="admin123")