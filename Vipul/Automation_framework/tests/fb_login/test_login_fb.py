
from ...page_object.fb_page.login_page import LoginPage
import pytest

@pytest.mark.usefixtures("get_driver")

class Test_FB_Login:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.lp = LoginPage(self.driver)

    def test_fb_login_verify(self):
        self.lp.open_url("https://www.facebook.com/")
        self.lp.fb_login(username='vippulkumar85@gmail.com', password='Vipul@1264')
