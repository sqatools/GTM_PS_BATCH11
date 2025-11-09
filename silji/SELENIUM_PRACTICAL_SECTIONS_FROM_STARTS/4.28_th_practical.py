
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SeleniumLocators:
    def __init__(self,browser):
        if browser == 'Chrome':
            self.driver=webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def facebook_website(self):
        self.driver.get("https://www.facebook.com/")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("siljiprakash@gmail.com") #//*[@name='sl']
        time.sleep(5)
        self.driver.find_element(By.NAME, "pass").send_keys("abc")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT,"Create new account").click()
        time.sleep(5)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Already").click()
        time.sleep(5)

        self.driver.close()

obj=SeleniumLocators("Chrome")
obj.facebook_website()