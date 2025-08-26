from ...base.selenium_base import seleniumBase
from .admin_page_locator import UserManagement


class Adminpage(seleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def launch_login_page(self, url):
        self.driver.get(url)

    # def Enter_Username(self, username):
    #     self.Enter_text(UserManagement.username_fields, username)
    #
    # def Enter_password(self, password):
    #     self.Enter_text(UserManagement.password_fields, password)

    # def click_login_button(self):
    #     self.Click_element(UserManagement.login_button_fields)

    def navigate_adminpage_link(self):
        self.Click_element(UserManagement.User_management_link)

    def navigate_userlink(self):
        self.Click_element(UserManagement.Users_link)

    def navigate_addbutton(self):
        self.Click_element(UserManagement.add_button)

    def userrole(self):
        self.Click_element(UserManagement.user_role)
        self.Click_element(UserManagement.user_role_value)

    def Ee_name(self, en):
        self.Enter_text(UserManagement.Emp_name, en)

    def Ce_name(self):
        self.Click_element(UserManagement.Emp_name_value)

    def status(self):
        self.Click_element(UserManagement.status_role)
        self.Click_element(UserManagement.status_role_value)

    def user_name(self, un):
        self.Enter_text(UserManagement.user_name, un)

    def pass_word(self, p, cp):
        self.Enter_text(UserManagement.pass_value, p)
        self.Enter_text(UserManagement.con_pass_value, cp)

    def save(self):
        self.Click_element(UserManagement.save)

    def Manegemnet(self, en, un, p, cp):
        # self.Enter_Username(username)
        # self.Enter_password(password)
        # self.click_login_button()
        self.navigate_adminpage_link()
        self.navigate_userlink()
        self.navigate_addbutton()
        self.userrole()
        self.Ee_name(en)
        self.Ce_name()
        self.status()
        self.user_name(un)
        self.pass_word(p, cp)
        self.save()

        # self.Click_element(UserManagement.Admin_page_link)
        # self.Click_element(UserManagement.User_management_link)
        # self.Click_element(UserManagement.User_management_link)
        # self.Click_element(UserManagement.add_button)
        # self.Click_element(UserManagement.user_role)
        # self.Click_element(UserManagement.user_role_value)
        # self.Enter_text(UserManagement.Emp_name,en)
        # self.Click_element(UserManagement.Emp_name_value)
        # self.Click_element(UserManagement.status_role)
        # self.Click_element(UserManagement.status_role_value)
        # self.Enter_text(UserManagement.user_name,un)
        # self.Enter_text(UserManagement.pass_value,p)
        # self.Enter_text(UserManagement.con_pass_value,cp)
        # self.Click_element(UserManagement.save)
