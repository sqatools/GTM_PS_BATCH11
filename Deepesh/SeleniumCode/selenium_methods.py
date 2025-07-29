import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import os



class SeleniumMethods:

    def __init__(self, browser):
        if browser.lower() == 'chrome':
            # Launch chrome browser and initiate driver variable
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            # Launch Firefox browser and initiate driver variable
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            # Launch Edge browser and initiate driver variable
            self.driver = webdriver.Edge()

        # wait for element
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def selenium_url_title(self):
        time.sleep(5)
        print("URL :", self.driver.current_url)
        print("Title :", self.driver.title)

    def get_element_text(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-title")

        print("Heading :", element.text)

    def check_element_is_enabled_displayed(self, user_name, pass_value):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.selenium_url_title()
        self.get_element_text()
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")

        print("is enabled :", username_field.is_enabled())
        print("is displayed :", username_field.is_displayed())
        if username_field.is_enabled():
            username_field.send_keys(user_name)
            password_field.send_keys(pass_value)

        login_button = self.driver.find_element(By.XPATH, "//button[contains(., 'Login')]")
        login_button.click()
        time.sleep(10)

    def check_element_is_selected(self):
        # navigate website to check selected status
        self.driver.get("https://sqatools.in/dummy-booking-website/")
        time.sleep(5)
        check_box_elem = self.driver.find_element(By.XPATH, "//td[text()='Pune']//preceding-sibling::td/input")
        print("is selected status before click  :", check_box_elem.is_selected())
        check_box_elem.click()
        print("is selected status after click  :", check_box_elem.is_selected())

        list_of_checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        for checkbox in list_of_checkboxes:
            print("is selected status before click  :", checkbox.is_selected())
            checkbox.click()
            print("is selected status after click  :", checkbox.is_selected())
            time.sleep(3)
            print("_"*50)

    def get_element_attribute_value(self):
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
        time.sleep(5)
        elem = self.driver.find_element(By.XPATH, "  //a[contains(text(), 'What is Software Testing')]")
        print("link :", elem.get_attribute("href"))

        #temp =1
        elements_list = self.driver.find_elements(By.XPATH, "//ul[@class='ullist']//a")
        for element in elements_list:
            file_name = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
            folder_name = datetime.now().strftime("%d_%m_%y")
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            element.screenshot(f"{folder_name}/element_{file_name}.png")
            print(element.get_attribute("href"))
            #temp += 1

        self.driver.save_screenshot("manual_testing.png")



obj = SeleniumMethods(browser='chrome')
obj.get_element_attribute_value()
# obj.check_element_is_selected()
# obj.check_element_is_enabled_displayed(user_name='Admin', pass_value='admin123')
# obj.selenium_url_title()
