
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SeleniumMethod:
    def __init__(self,browser):
        if browser == 'Chrome':
            self.driver=webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def sel_url_title(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        print("URL", self.driver.current_url)
        print("Title", self.driver.title)



    def get_element_text(self):
        element=self.driver.find_element(By.CSS_SELECTOR,".orangehrm-login-title")
        print("Heading", element.text)


#1.Go to login page

    def check_element_is_enabled_displayed_selected(self,user_name,pass_name):
        username_field=self.driver.find_element(By.NAME,"username")
        password_field=self.driver.find_element(By.NAME,"password")

        print("is enabled:", username_field.is_enabled())
        print("is displayed:", username_field.is_displayed())
        if username_field.is_enabled():
            username_field.send_keys(user_name)
            password_field.send_keys(pass_name)

        login_button =self.driver.find_element(By.XPATH,"//button[contains(.,'Login')]")
        login_button.click()
        time.sleep(10)





    def close_browser(self):
        self.driver.close()

obj=SeleniumMethod("Chrome")
obj.sel_url_title()
obj.get_element_text()
obj.check_element_is_enabled_displayed_selected(user_name='Admin',pass_name='admin123')
obj.close_browser()