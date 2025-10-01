
# Opens Chrome browser.
#
# Navigates to OrangeHRM login page.
#
# Prints URL & title.
#
# Enters login credentials (Admin / admin123).
#
# Clicks Login button.



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumMethods:
        def __init__(self, browser):
            if browser.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser.lower() == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise ValueError("Unsupported browser! Use chrome, firefox, or edge.")


            self.driver.implicitly_wait(10)
            self.driver.maximize_window()


            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#selenium_url_title() → prints current URL & page title

        def selenium_url_title(self):
            print("URL",self.driver.current_url) #give  the url
            print("Title",self.driver.title) #give the info of the title
#get_element_text() → prints heading text on login page
        def get_element_text(self):
            element=self.driver.find_element(By.CSS_SELECTOR,".orangehrm-login-title")
            print("Heading:",element.text)
#check_element_is_enabled_displayed_selected()
        def check_element_is_enabled_displayed_selected(self,user_name,pass_word):
            username_field=self.driver.find_element(By.NAME,"username")
            password_field=self.driver.find_element(By.NAME,"password")

            print("is enabled:",username_field.is_enabled())
            print("is displayed:",username_field.is_displayed())

            # print("is enabled:", password_field.is_enabled())
            # print("is displayed:", password_field.is_displayed())


            if username_field.is_enabled():
                username_field.send_keys(user_name)
                password_field.send_keys(pass_word)


            Login_button=self.driver.find_element(By.XPATH,"//button[contains(.,'Login')]")
            Login_button.click()
            time.sleep(10)


#calling the method
obj=SeleniumMethods(browser='chrome')

obj.selenium_url_title()
obj.check_element_is_enabled_displayed_selected(user_name='Admin',pass_word='admin123')