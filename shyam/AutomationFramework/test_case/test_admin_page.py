import time
from ..page_object.hrm_admin_page.admin_page_class import Adminpage
from ..page_object.login_HRM.login_page_class import loginHRM
from ..utilities.util_tools import Utils
import pytest
import os


@pytest.mark.usefixtures("get_driver")
class Test_admin:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.util = Utils()
        self.ad = Adminpage(self.driver)
        self.lp = loginHRM(self.driver)
        self.read_xls_data = os.path.join(os.getcwd(), "page_object/hrm_admin_page/hrm.xlsx")
        self.read_xls_data =self.util.read_excel_file(self.read_xls_data, "Sheet1")

    def test_admin_management(self):
        self.ad.launch_login_page(url=self.read_xls_data['B2'].value)
        self.lp.HRM(username=self.read_xls_data['B3'].value, password=self.read_xls_data['B4'].value)
        self.ad.Manege(en="Automation2  FC", un="User1234", p="Demo1234", cp="Demo1234")
        time.sleep(3)

    # def test_admin_management(self):
    #     self.ad.launch_login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     self.lp.HRM(username="Admin", password="admin123")
    #     self.ad.Manege(en="Automation2  FC", un="User1234", p="Demo1234", cp="Demo1234")
    #     time.sleep(3)

