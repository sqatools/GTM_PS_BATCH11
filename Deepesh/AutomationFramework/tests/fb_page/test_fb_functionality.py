import pytest
from ...page_objects.fb_page.fb_page_class import FBPage
import time

@pytest.mark.usefixtures("get_driver")
class TestFGPage:

    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.fb = FBPage(self.driver)


    def test_facebook_loginpage(self):
        self.fb.launch_fb_login("https://www.facebook.com")
        self.fb.login_to_fb(email="user1@gmail.com", password="user@1234")
        time.sleep(5)



