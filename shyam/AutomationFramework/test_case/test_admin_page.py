import time
from ..page_object.hrm_admin_page.admin_page_class import Adminpage
from ..page_object.login_HRM.login_page_class import loginHRM
import  pytest

@pytest.mark.usefixtures("get_driver")
class Test_admin:
    @pytest.fixture(autouse=True)
    def setup(self,get_driver):
        self.driver=get_driver
        self.ad=Adminpage(self.driver)
        self.lp = loginHRM(self.driver)

    def test_admin_usermanagement(self):
        self.ad.launch_login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lp.HRM(username="Admin", password="admin123")
        self.ad.Manegemnet(en="Test",un="User1234",p="Demo1234",cp="Demo1234")
        time.sleep(10)

