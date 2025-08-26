import time
from ..page_object.hrm_admin_page.admin_page_class import Adminpage
import  pytest

@pytest.mark.usefixtures("get_driver")
class Test_admin:
    @pytest.fixture(autouse=True)
    def setup(self,get_driver):
        self.driver=get_driver
        self.ad=Adminpage(self.driver)

    def test_admin_usermanagement(self):
        self.ad.launch_login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(10)
        self.ad.Manegemnet(username="Admin", password="admin123",en="Test",un="User1234",p="Demo1234",cp="Demo1234")
        time.sleep(10)

