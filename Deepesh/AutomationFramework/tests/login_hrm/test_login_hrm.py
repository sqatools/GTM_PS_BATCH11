import time
import os
import pytest
from ...page_objects.login_hrm.login_page_class import LoginPage
from ...utilities.util_tools import Utils

@pytest.mark.usefixtures("get_driver")
class TestLoginHRM:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.lp = LoginPage(self.driver)
        self.util = Utils()
        self.json_file_path = os.path.join(os.getcwd(), "page_objects/login_hrm/login_data.json")
        self.login_data = self.util.read_json_file(self.json_file_path)

    # def test_login_hrm_website_and_verify(self):
    #     self.lp.launch_login_page(url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     self.lp.login_to_rhm(username="Admin", password="admin123")
    #     time.sleep(10)
    @pytest.mark.sanity
    def test_login_hrm_website_and_verify(self):
        self.lp.launch_login_page(url=self.login_data['url'])
        self.lp.login_to_rhm(username=self.login_data['username'], password=self.login_data['password'])
        time.sleep(10)

