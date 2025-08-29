from selenium.webdriver.common.by import By

username_field = (By.NAME, "email")
password_field = (By.NAME, "pass")
login_button = (By.XPATH, "//button[text()='Log in']")

create_account = (By.LINK_TEXT, "Create new account")
firstname_field = (By.NAME, "firstname")
lastname_field = (By.NAME, "lastname")
dd_day = (By.NAME, "birthday_day")
dd_month = (By.NAME, "birthday_month")
dd_year = (By.NAME, "birthday_year")
gender_ = (By.XPATH, "//input[@type='radio' and @value='2']")
email_id = (By.NAME, "reg_email__")
new_password = (By.NAME, "reg_passwd__")
signup_button = (By.NAME, "websubmit")
