from .selenium_base import SeleniumBase
from .login_page_locators import *
from selenium.webdriver.support.select import Select


class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_url(self, url):
        self.driver.get(url)

    def enter_username_field(self, username):
        self.enter_text(locator=username_field, value=username)

    def enter_password_field(self, password):
        self.enter_text(locator=password_field, value=password)

    def click_login_button(self):
        self.click_element(locator=login_button)

    def login_to_facebook(self, username, password):
        self.enter_username_field(username)
        self.enter_password_field(password)
        self.click_login_button()


class CreateAccountPage(SeleniumBase):

    def click_create_acc(self):
        self.click_element(locator=create_account)

    def enter_firstname_field(self, firstname):
        self.enter_text(locator=firstname_field, value=firstname)

    def enter_lastname_field(self, lastname):
        self.enter_text(locator=lastname_field, value=lastname)

    def select_dob(self, day, month, year):
        self.select_dropdown_value(locator=dd_day, value=day)
        self.select_dropdown_value(locator=dd_month, value=month)
        self.select_dropdown_value(locator=dd_year, value=year)

    def select_gender(self, gender):
        self.click_element(locator=gender_)

    def enter_email_id(self, email):
        self.enter_text(locator=email_id, value=email)

    def enter_new_password(self, password):
        self.enter_text(locator=new_password, value=password)

    def click_signup_button(self):
        self.click_element(locator=signup_button)

    def create_new_account(self, firstname, lastname, dob_day, dob_month, dob_year, gender, email, password):
        self.enter_firstname_field(firstname)
        self.enter_lastname_field(lastname)
        self.select_dob(dob_day, dob_month, dob_year)
        self.select_gender(gender)
        self.enter_email_id(email)
        self.enter_new_password(password)
        self.click_signup_button()

