import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Selenium_Method:
    def __init__(self,browser):
        if browser.lower()=='chrome':
            self.driver=webdriver.Chrome()
        elif browser.lower()=='edge':
            self.driver=webdriver.Edge()
        elif browser.lower()=='firefox':
            self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # self.driver.get("https://www.facebook.com/")
    def url_title(self):
        time.sleep(5)
        print("url :", self.driver.current_url)
        print("title :", self.driver.title)
    def element_text(self):
        # self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        element=self.driver.find_element(By.CSS_SELECTOR,".orangehrm-login-title")
        print("text :",element.text)
    def check_element_enable_display(self,use_name,pass_word):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        self.url_title()
        self.element_text()
        username=self.driver.find_element(By.NAME,"username")
        password= self.driver.find_element(By.NAME,"password")
        print("is enable :", username.is_enabled())
        print("is display :", username.is_displayed())
        if username.is_enabled():
            username.send_keys(use_name)
            password.send_keys(pass_word)

            login_button = self.driver.find_element(By.XPATH, "//button[contains(., 'Login')]")
            login_button.click()
            time.sleep(20)
    def element_selected(self):
        self.driver.get("https://sqatools.in/dummy-booking-website/")
        ele=self.driver.find_element(By.XPATH,"//td[text()='Pune']//preceding-sibling::td/input")
        time.sleep(5)
        print("before :",ele.is_selected())
        time.sleep(5)
        ele.click()
        time.sleep(5)
        print("after :", ele.is_selected())
        time.sleep(5)
        list_checkbox =self.driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        for checkbox in list_checkbox:
            print("Before :", checkbox.is_selected())
            checkbox.click()
            print("After :", checkbox.is_selected())
            time.sleep(5)




obj=Selenium_Method('chrome')
# obj.url_title()
# obj.element_text()
#obj.check_element_enable_display(use_name='Admin',pass_word='admin123')
obj.element_selected()