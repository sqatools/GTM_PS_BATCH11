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

    def facebook(self):
        self.driver.get("https://www.facebook.com/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("siljiprakash@gmail.com")
        time.sleep(5)
        self.driver.find_element(By.NAME, "pass").send_keys("abc")
        time.sleep(5)

        #navigative to create new account page
        self.driver.find_element(By.LINK_TEXT, "Create new account").click()
        time.sleep(5)
        self.driver.save_screenshot("sign_up_page.png")

        #navigate to back to login page
        self.driver.back()
        time.sleep(5)
        self.driver.save_screenshot("login_page.png")

        #navigate forward signup page
        self.driver.forward()
        time.sleep(5)
        self.driver.save_screenshot("sign_up_page_2.png")

        #navigate to back to login page
        self.driver.back()
        time.sleep(5)

        #refresh login page
        self.driver.refresh()







obj=SeleniumMethod(browser='Chrome')
obj.facebook()
