from ...base.selenium_base import SeleniumBase
from .admin_page_locator import AdminLoc, LeaveLoc, MaintenanceLoc, CommonLoc
import time


class AdminPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    # Admin Module Methods
    def navigate_admin_page(self):
        self.click_element(AdminLoc.admin_page_link)

    def navigate_job_title(self):
        self.click_element(AdminLoc.job_link)
        self.click_element(AdminLoc.job_title_link)

    def click_on_add_button(self):
        self.click_element(AdminLoc.add_button)

    def navigate_user_management(self):
        self.click_element(AdminLoc.user_management_link)
        self.click_element(AdminLoc.users_link)

    def navigate_job_titles(self):
        self.click_element(AdminLoc.job_link)
        self.click_element(AdminLoc.job_titles_link)

    def navigate_pay_grades(self):
        self.click_element(AdminLoc.job_link)
        self.click_element(AdminLoc.pay_grades_link)

    def navigate_employment_status(self):
        self.click_element(AdminLoc.job_link)
        self.click_element(AdminLoc.employment_status_link)

    def navigate_job_categories(self):
        self.click_element(AdminLoc.job_link)
        self.click_element(AdminLoc.job_categories_link)

    def navigate_work_shifts(self):
        self.click_element(AdminLoc.job_link)
        self.click_element(AdminLoc.work_shifts_link)

    def navigate_organization(self):
        self.click_element(AdminLoc.organization_link)

    def navigate_general_information(self):
        self.click_element(AdminLoc.organization_link)
        self.click_element(AdminLoc.general_information_link)

    def navigate_locations(self):
        self.click_element(AdminLoc.organization_link)
        self.click_element(AdminLoc.locations_link)

    def navigate_structure(self):
        self.click_element(AdminLoc.organization_link)
        self.click_element(AdminLoc.structure_link)

    def navigate_qualifications(self):
        self.click_element(AdminLoc.qualifications_link)

    def navigate_skills(self):
        self.click_element(AdminLoc.qualifications_link)
        self.click_element(AdminLoc.skills_link)

    def navigate_education(self):
        self.click_element(AdminLoc.qualifications_link)
        self.click_element(AdminLoc.education_link)

    def navigate_licenses(self):
        self.click_element(AdminLoc.qualifications_link)
        self.click_element(AdminLoc.licenses_link)

    def navigate_languages(self):
        self.click_element(AdminLoc.qualifications_link)
        self.click_element(AdminLoc.languages_link)

    def navigate_memberships(self):
        self.click_element(AdminLoc.qualifications_link)
        self.click_element(AdminLoc.memberships_link)

    def navigate_nationalities(self):
        self.click_element(AdminLoc.nationalities_link)

    def navigate_corporate_branding(self):
        self.click_element(AdminLoc.corporate_branding_link)

    def navigate_configuration(self):
        self.click_element(AdminLoc.configuration_link)

    def navigate_email_configuration(self):
        self.click_element(AdminLoc.configuration_link)
        self.click_element(AdminLoc.email_configuration_link)

    def navigate_email_subscriptions(self):
        self.click_element(AdminLoc.configuration_link)
        self.click_element(AdminLoc.email_subscriptions_link)

    def navigate_localization(self):
        self.click_element(AdminLoc.configuration_link)
        self.click_element(AdminLoc.localization_link)

    def navigate_modules(self):
        self.click_element(AdminLoc.configuration_link)
        self.click_element(AdminLoc.modules_link)

    def navigate_social_media_auth(self):
        self.click_element(AdminLoc.configuration_link)
        self.click_element(AdminLoc.social_media_authentication_link)

    def navigate_oauth_client(self):
        self.click_element(AdminLoc.configuration_link)
        self.click_element(AdminLoc.register_oauth_client_link)

    # Leave Module Methods
    def navigate_leave_page(self):
        self.click_element(LeaveLoc.leave_page_link)

    def navigate_leave_list(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.leave_list_link)

    def navigate_apply_leave(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.apply_link)

    def navigate_my_leave(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.my_leave_link)

    def navigate_entitlements(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.entitlements_link)

    def navigate_add_entitlements(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.entitlements_link)
        self.click_element(LeaveLoc.add_entitlements_link)

    def navigate_employee_entitlements(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.entitlements_link)
        self.click_element(LeaveLoc.employee_entitlements_link)

    def navigate_my_entitlements(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.entitlements_link)
        self.click_element(LeaveLoc.my_entitlements_link)

    def navigate_leave_reports(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.reports_link)

    def navigate_leave_entitlements_report(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.reports_link)
        self.click_element(LeaveLoc.leave_entitlements_report_link)

    def navigate_my_leave_report(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.reports_link)
        self.click_element(LeaveLoc.my_leave_report_link)

    def navigate_leave_configure(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.configure_link)

    def navigate_leave_types(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.configure_link)
        self.click_element(LeaveLoc.leave_types_link)

    def navigate_leave_period(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.configure_link)
        self.click_element(LeaveLoc.leave_period_link)

    def navigate_work_week(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.configure_link)
        self.click_element(LeaveLoc.work_week_link)

    def navigate_holidays(self):
        self.click_element(LeaveLoc.leave_page_link)
        self.click_element(LeaveLoc.configure_link)
        self.click_element(LeaveLoc.holidays_link)

    # Maintenance Module Methods
    def navigate_maintenance_page(self):
        self.click_element(MaintenanceLoc.maintenance_page_link)

    def navigate_purge_records(self):
        self.click_element(MaintenanceLoc.maintenance_page_link)
        self.click_element(MaintenanceLoc.purge_records_link)

    def navigate_employee_records(self):
        self.click_element(MaintenanceLoc.maintenance_page_link)
        self.click_element(MaintenanceLoc.purge_records_link)
        self.click_element(MaintenanceLoc.employee_records_link)

    def navigate_candidate_records(self):
        self.click_element(MaintenanceLoc.maintenance_page_link)
        self.click_element(MaintenanceLoc.purge_records_link)
        self.click_element(MaintenanceLoc.candidate_records_link)

    def navigate_access_records(self):
        self.click_element(MaintenanceLoc.maintenance_page_link)
        self.click_element(MaintenanceLoc.access_records_link)

    def enter_maintenance_password(self, password):
        self.enter_text(MaintenanceLoc.maintenance_password_field, password)

    def confirm_maintenance_access(self):
        self.click_element(MaintenanceLoc.confirm_button)

    # Common Methods
    def get_page_header(self):
        return self.get_text(CommonLoc.page_header)

    def get_dashboard_header(self):
        return self.get_text(CommonLoc.dashboard_header)

    def click_user_dropdown(self):
        self.click_element(CommonLoc.user_dropdown)

    def logout(self):
        self.click_user_dropdown()
        self.click_element(CommonLoc.logout_link)

    def click_save_button(self):
        self.click_element(CommonLoc.save_button)

    def click_cancel_button(self):
        self.click_element(CommonLoc.cancel_button)

    def click_delete_button(self):
        self.click_element(CommonLoc.delete_button)

    def click_edit_button(self):
        self.click_element(CommonLoc.edit_button)

    def click_search_button(self):
        self.click_element(CommonLoc.search_button)

    def click_reset_button(self):
        self.click_element(CommonLoc.reset_button)

    def wait_for_page_load(self, timeout=10):
        time.sleep(timeout)

    def verify_page_navigation(self, expected_header):
        actual_header = self.get_page_header()
        return expected_header in actual_header
