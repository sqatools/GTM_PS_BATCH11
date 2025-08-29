
from ...base.selenium_base import seleniumBase
from .fb_loginpage_locator import *

class loginFB(seleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def lauch_fb_page(self,url):
        self.driver.get(url)

    def login_to_fb(self,email,password):
        self.Enter_text(username_field,email)
        self.Enter_text(password_field,password)
        self.Click_element(fb_login_button_field)
    def Create_new_Ac(self,fname,lname,ed,npass):
        self.Click_element(create_new_account_field)
        self.Enter_text(Firstname_field,fname)
        self.Enter_text(Lastname_field,lname)
        self.Click_element(Date_field)
        self.Click_element(Day_field)
        self.Click_element(Month_field)
        self.Click_element(M_field)
        self.Click_element(Year_field)
        self.Click_element(Y_field)
        self.Click_element(Gender_field)
        self.Enter_text(Email_address_field,ed)
        self.Enter_text(New_password_field,npass)
        self.Click_element(Signup_field)

