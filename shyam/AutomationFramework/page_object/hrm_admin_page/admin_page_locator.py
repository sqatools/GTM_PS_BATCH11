
from selenium.webdriver.common.by import By

class UserManagement:

    # username_fields = (By.NAME, "username")
    # password_fields = (By.NAME, "password")
    login_button_fields = (By.XPATH, "//button[@type='submit']")
    Admin_page_link=(By.XPATH,"//span[normalize-space()='Admin']")
    User_management_link=(By.XPATH,"//span[normalize-space()='User Management']//parent::li")
    Users_link=(By.XPATH,"//ul[@class='oxd-dropdown-menu']//li")
    add_button=(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']")
    user_role=(By.XPATH,"//label[text()='User Role']//ancestor::div[contains(@class,'oxd-grid-item ')]//div[contains(text(),'Select')]")
    user_role_value=(By.XPATH,"//div[@role='listbox']//*[contains(text(),'ESS')]")
    Emp_name=(By.XPATH,"//input[@placeholder='Type for hints...']")
    Emp_name_value=(By.XPATH,"//div[@role='listbox']//*[contains(text(),'Automation2  FC')]")
    status_role=(By.XPATH,"//label[text()='Status']//ancestor::div[contains(@class,'oxd-grid-item ')]//div[contains(text(),'Select')]")
    status_role_value=(By.XPATH,"//div[@role='listbox']//*[contains(text(),'Enabled')]")
    user_name=(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    pass_value=(By.XPATH,"(//input[@type='password'])[1]")
    con_pass_value=(By.XPATH,"(//input[@type='password'])[2]")
    save=(By.XPATH,"//button[@type='submit']")


