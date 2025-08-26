from selenium.webdriver.common.by import By

class AdminLoc:
    admin_page_link = (By.XPATH, "//span[text()='Admin']//parent::a")
    job_link = (By.XPATH, "//span[contains(text(), 'Job')]//parent::li")
    job_title_link = (By.XPATH, "//a[contains(text(), 'Job Titles')]//parent::li")
    add_button = (By.XPATH, "//button[normalize-space()='Add']")


