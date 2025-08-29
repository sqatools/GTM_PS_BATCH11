import time

from ..page_object.login_HRM.login_page_class import loginHRM
import  pytest

@pytest.mark.usefixtures("get_driver")

class TestHRM:
    @pytest.fixture(autouse=True)
    def setup(self,get_driver):
        self.driver=get_driver
        self.lp=loginHRM(self.driver)

    def test_login_hrm_website_and_verify(self):
        self.lp.launch_login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lp.HRM(username="Admin",password="admin123")
        time.sleep(10)
