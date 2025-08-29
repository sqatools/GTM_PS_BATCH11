import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumMethods:
    def __init__(self, browser):
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif browser.lower() == "edge":
            self.driver = webdriver.Edge()

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def selenium_get_url_title(self):
        time.sleep(5)
        print("URL :", self.driver.current_url)
        print("Title :", self.driver.title)

    def get_element_text(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-title")
        print("Heading :", element.text)

    def check_element_enabled_displayed(self, uname, pwd):
        user_name = self.driver.find_element(By.NAME, "username")
        user_pwd = self.driver.find_element(By.NAME, "password")
        print("Is Enabled :", user_name.is_enabled())
        print("Is Displayed :", user_name.is_displayed())
        if user_name.is_enabled():
            user_name.send_keys(uname)
            user_pwd.send_keys(pwd)

        login = self.driver.find_element(By.XPATH, "//button[contains(., 'Login')]")
        login.click()
        time.sleep(5)

    def check_element_selected(self):
        self.driver.get("https://sqatools.in/dummy-booking-website/")
        time.sleep(5)
        checkbox_element = self.driver.find_element(By.XPATH, "//td[text()= 'Pune']//preceding-sibling::td/input")
        print("Is Selected status before click :", checkbox_element.is_selected())
        checkbox_element.click()
        print("Is Selected status After click :", checkbox_element.is_selected())

        list_of_checkbox = self.driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
        for checkbox in list_of_checkbox:
            print("Is Selected status before click :", checkbox.is_selected())
            checkbox.click()
            print("Is Selected status After click :", checkbox.is_selected())
            time.sleep(2)
            print("_" * 50)

    def get_element_attribute(self):
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
        time.sleep(3)
        elememt1 = self.driver.find_element(By.XPATH, "//a[contains(text(), 'What is Software Testing')]")
        print("Link :", elememt1.get_attribute("href"))

        temp = 1
        elememt1_list = self.driver.find_elements(By.XPATH, "//ul[@class = 'ullist']//a")
        for element2 in elememt1_list:
            element2.screenshot(f"images/element2_{temp}.png")
            print(element2.get_attribute("href"))
            temp += 1
        self.driver.save_screenshot("manual-testing.png")

    def forward_back_refresh(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.NAME, "email").send_keys("user@gmail.com")
        self.driver.find_element(By.NAME, "pass").send_keys("user1234")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Create new account").click()
        time.sleep(5)
        self.driver.save_screenshot("signup_page.png")

        # Navigate back to login page
        self.driver.back()
        time.sleep(5)
        self.driver.save_screenshot("login_page.png")

        # Navigate forward to create account page
        self.driver.forward()
        time.sleep(5)
        self.driver.save_screenshot("signup_page2.png")

        # Navigate back to login page
        self.driver.back()
        time.sleep(5)
        self.driver.save_screenshot("login_page2.png")

        # Refresh login page
        self.driver.refresh()


obj = SeleniumMethods("chrome")
# obj.selenium_get_url_title()
# obj.check_element_enabled_displayed(uname='Admin', pwd='admin123')
# obj.check_element_selected()
# obj.get_element_attribute()
#obj.forward_back_refresh()
