import pytest
import os
from ...page_objects.fb_page.fb_page_class import FBPage
from ...utilities.util_tools import Utils
import time


@pytest.mark.usefixtures("get_driver")
class TestFGPage:

    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.fb = FBPage(self.driver)
        self.util = Utils()
        self.exl_filepath = os.path.join(os.getcwd(), "page_objects/fb_page/fb_data.xlsx")
        self.exl_data = self.util.read_excel_data(self.exl_filepath, sheet_name="Sheet1")

    # def test_facebook_loginpage(self):
    #     self.fb.launch_fb_login("https://www.facebook.com")
    #     self.fb.login_to_fb(email="user1@gmail.com", password="user@1234")
    #     time.sleep(5)

    @pytest.mark.smoke
    def test_facebook_loginpage(self, request):
        self.fb.log.info(f"Test name: {request.node.name}")
        self.fb.launch_fb_login(url=self.exl_data['B2'].value)
        self.fb.login_to_fb(email=self.exl_data['B3'].value, password=self.exl_data['B4'].value)
        time.sleep(5)
