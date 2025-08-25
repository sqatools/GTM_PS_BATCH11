import time

from ..page_object.login_fb.fb_loginpage_class import loginFB
import  pytest
@pytest.mark.usefixtures("get_driver")
class TestFb:
    @pytest.fixture(autouse=True)
    def setup(self,get_driver):
        self.driver=get_driver
        self.fb=loginFB(self.driver)

    def test_login_fb_website_and_verify(self):
        self.fb.lauch_fb_page("https://www.facebook.com/")
        self.fb.login_to_fb(email="user@123.com",password="user123")
        time.sleep(10)
        self.driver.back()
        time.sleep(10)
        self.fb.Create_new_Ac(fname="abc",lname="xyz",ed="8698570520",npass="Demo@123")
        time.sleep(20)


