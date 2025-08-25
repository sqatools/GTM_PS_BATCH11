from ...base.selenium_base import SeleniumBase
from .admin_page_locator import AdminLoc


class AdminPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_admin_page(self):
        self.click_element(AdminLoc.admin_page_link)

    def navigate_job_title(self):
        self.click_element(AdminLoc.job_link)
        self.click_element(AdminLoc.job_title_link)

    def click_on_add_button(self):
        self.click_element(AdminLoc.add_button)
