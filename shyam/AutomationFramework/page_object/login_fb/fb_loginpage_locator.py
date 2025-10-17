from selenium.webdriver.common.by import By

username_field=(By.NAME,"email")
password_field=(By.NAME,"pass")
fb_login_button_field=(By.NAME,"login")
create_new_account_field=(By.XPATH,"(//a[normalize-space()='Create new account'])[1]")
Firstname_field=(By.NAME,"firstname")
Lastname_field=(By.NAME,"lastname")
Date_field=(By.NAME,"birthday_day")
Month_field=(By.NAME,"birthday_month")
Year_field=(By.NAME,"birthday_year")
Day_field=(By.XPATH, "//option[normalize-space()='10']")
M_field=(By.XPATH, "//option[normalize-space()='Jul']")
Y_field=(By.XPATH, "//option[normalize-space()='2020']")
Gender_field=(By.XPATH, "//label[normalize-space()='Female']")
Email_address_field=(By.NAME, "reg_email__")
New_password_field=(By.ID, "password_step_input")
Signup_field=(By.NAME, "websubmit")


