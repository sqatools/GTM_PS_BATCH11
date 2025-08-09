from selenium.webdriver.common.by import By


class LoginLocator:
    username_field_loc = (By.NAME, "username")
    pass_field_loc = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[contains(.,'Login')]")
    leave_page_loc = (By.XPATH, "//span[text()='Leave']")


class LeaveLocator:
    leave_page_loc = (By.XPATH, "//span[text()='Leave']")
    leave_type_dropdown = (By.XPATH, "//label[text()='Leave Type']//ancestor::div[contains(@class, 'oxd-grid-item')]//div[contains(text(), 'Select')]")
    leave_type_value = (By.XPATH, "//div[@role='listbox']//*[contains(text(), 'Personal')]")