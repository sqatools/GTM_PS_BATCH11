from selenium.webdriver.common.by import By


class loginPage:
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    Login_button = (By.XPATH,"//button[@type = 'submit']")
    Forgot_password = (By.CLASS_NAME,"oxd-text oxd-text--p orangehrm-login-forgot-header")

# Home work:
# repeat :  Handle Iframe, Handle Droddown, Handle Alerts
# Automate 5 areas of openhrm website in class format
# https://opensource-demo.orangehrmlive.com/web/index.php
# Admin
# Leave
# PIM
# Time
# Recruitment
