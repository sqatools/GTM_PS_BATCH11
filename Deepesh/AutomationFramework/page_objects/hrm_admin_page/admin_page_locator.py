from selenium.webdriver.common.by import By

class AdminLoc:
    # Admin Module
    admin_page_link = (By.XPATH, "//span[text()='Admin']//parent::a")
    job_link = (By.XPATH, "//span[contains(text(), 'Job')]//parent::li")
    job_title_link = (By.XPATH, "//a[contains(text(), 'Job Titles')]//parent::li")
    add_button = (By.XPATH, "//button[normalize-space()='Add']")
    
    # User Management
    user_management_link = (By.XPATH, "//span[contains(text(), 'User Management')]//parent::li")
    users_link = (By.XPATH, "//a[contains(text(), 'Users')]//parent::li")
    
    # Job Management
    job_titles_link = (By.XPATH, "//a[contains(text(), 'Job Titles')]//parent::li")
    pay_grades_link = (By.XPATH, "//a[contains(text(), 'Pay Grades')]//parent::li")
    employment_status_link = (By.XPATH, "//a[contains(text(), 'Employment Status')]//parent::li")
    job_categories_link = (By.XPATH, "//a[contains(text(), 'Job Categories')]//parent::li")
    work_shifts_link = (By.XPATH, "//a[contains(text(), 'Work Shifts')]//parent::li")
    
    # Organization
    organization_link = (By.XPATH, "//span[contains(text(), 'Organization')]//parent::li")
    general_information_link = (By.XPATH, "//a[contains(text(), 'General Information')]//parent::li")
    locations_link = (By.XPATH, "//a[contains(text(), 'Locations')]//parent::li")
    structure_link = (By.XPATH, "//a[contains(text(), 'Structure')]//parent::li")
    
    # Qualifications
    qualifications_link = (By.XPATH, "//span[contains(text(), 'Qualifications')]//parent::li")
    skills_link = (By.XPATH, "//a[contains(text(), 'Skills')]//parent::li")
    education_link = (By.XPATH, "//a[contains(text(), 'Education')]//parent::li")
    licenses_link = (By.XPATH, "//a[contains(text(), 'Licenses')]//parent::li")
    languages_link = (By.XPATH, "//a[contains(text(), 'Languages')]//parent::li")
    memberships_link = (By.XPATH, "//a[contains(text(), 'Memberships')]//parent::li")
    
    # Nationalities
    nationalities_link = (By.XPATH, "//a[contains(text(), 'Nationalities')]//parent::li")
    
    # Corporate Branding
    corporate_branding_link = (By.XPATH, "//a[contains(text(), 'Corporate Branding')]//parent::li")
    
    # Configuration
    configuration_link = (By.XPATH, "//span[contains(text(), 'Configuration')]//parent::li")
    email_configuration_link = (By.XPATH, "//a[contains(text(), 'Email Configuration')]//parent::li")
    email_subscriptions_link = (By.XPATH, "//a[contains(text(), 'Email Subscriptions')]//parent::li")
    localization_link = (By.XPATH, "//a[contains(text(), 'Localization')]//parent::li")
    modules_link = (By.XPATH, "//a[contains(text(), 'Modules')]//parent::li")
    social_media_authentication_link = (By.XPATH, "//a[contains(text(), 'Social Media Authentication')]//parent::li")
    register_oauth_client_link = (By.XPATH, "//a[contains(text(), 'Register OAuth Client')]//parent::li")

class LeaveLoc:
    # Leave Module
    leave_page_link = (By.XPATH, "//span[text()='Leave']//parent::a")
    
    # Leave List
    leave_list_link = (By.XPATH, "//a[contains(text(), 'Leave List')]//parent::li")
    leave_list_search_button = (By.XPATH, "//button[normalize-space()='Search']")
    leave_list_reset_button = (By.XPATH, "//button[normalize-space()='Reset']")
    
    # Apply Leave
    apply_link = (By.XPATH, "//a[contains(text(), 'Apply')]//parent::li")
    leave_type_dropdown = (By.XPATH, "//label[contains(text(), 'Leave Type')]//following::div[1]//div[@class='oxd-select-text']")
    from_date_field = (By.XPATH, "//label[contains(text(), 'From Date')]//following::input[1]")
    to_date_field = (By.XPATH, "//label[contains(text(), 'To Date')]//following::input[1]")
    comment_field = (By.XPATH, "//textarea[@placeholder='Type comment here']")
    apply_button = (By.XPATH, "//button[normalize-space()='Apply']")
    
    # My Leave
    my_leave_link = (By.XPATH, "//a[contains(text(), 'My Leave')]//parent::li")
    
    # Leave Entitlements
    entitlements_link = (By.XPATH, "//span[contains(text(), 'Entitlements')]//parent::li")
    add_entitlements_link = (By.XPATH, "//a[contains(text(), 'Add Entitlements')]//parent::li")
    employee_entitlements_link = (By.XPATH, "//a[contains(text(), 'Employee Entitlements')]//parent::li")
    my_entitlements_link = (By.XPATH, "//a[contains(text(), 'My Entitlements')]//parent::li")
    
    # Leave Reports
    reports_link = (By.XPATH, "//span[contains(text(), 'Reports')]//parent::li")
    leave_entitlements_report_link = (By.XPATH, "//a[contains(text(), 'Leave Entitlements and Usage Report')]//parent::li")
    my_leave_report_link = (By.XPATH, "//a[contains(text(), 'My Leave Report')]//parent::li")
    
    # Leave Configure
    configure_link = (By.XPATH, "//span[contains(text(), 'Configure')]//parent::li")
    leave_types_link = (By.XPATH, "//a[contains(text(), 'Leave Types')]//parent::li")
    leave_period_link = (By.XPATH, "//a[contains(text(), 'Leave Period')]//parent::li")
    work_week_link = (By.XPATH, "//a[contains(text(), 'Work Week')]//parent::li")
    holidays_link = (By.XPATH, "//a[contains(text(), 'Holidays')]//parent::li")

class MaintenanceLoc:
    # Maintenance Module
    maintenance_page_link = (By.XPATH, "//span[text()='Maintenance']//parent::a")
    
    # Purge Records
    purge_records_link = (By.XPATH, "//a[contains(text(), 'Purge Records')]//parent::li")
    employee_records_link = (By.XPATH, "//a[contains(text(), 'Employee Records')]//parent::li")
    candidate_records_link = (By.XPATH, "//a[contains(text(), 'Candidate Records')]//parent::li")
    
    # Access Records
    access_records_link = (By.XPATH, "//a[contains(text(), 'Access Records')]//parent::li")
    
    # Maintenance Password
    maintenance_password_field = (By.XPATH, "//input[@name='password']")
    confirm_button = (By.XPATH, "//button[normalize-space()='Confirm']")

class CommonLoc:
    # Common elements
    dashboard_header = (By.XPATH, "//h6[contains(text(), 'Dashboard')]")
    user_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    logout_link = (By.XPATH, "//a[contains(text(), 'Logout')]")
    page_header = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")
    cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    delete_button = (By.XPATH, "//button[normalize-space()='Delete']")
    edit_button = (By.XPATH, "//button[normalize-space()='Edit']")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    reset_button = (By.XPATH, "//button[normalize-space()='Reset']")


