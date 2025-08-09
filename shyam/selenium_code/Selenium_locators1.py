import time

from  selenium import webdriver
from selenium.webdriver.common.by import By


class Locators:
    def __init__(self,browser):
        if browser.lower()=='chrome':
            self.driver=webdriver.Chrome()
        elif browser.lower()=='edge':
            self.driver=webdriver.Edge()
        elif browser.lower()=='firefox':
            self.driver=webdriver.Firefox()

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def Facebook_Details(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.NAME,"email").send_keys("user1@gmail.com")
        self.driver.find_element(By.ID,"pass").send_keys("user123")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT,"Create new account").click()
        time.sleep(5)
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Already have ").click()
        time.sleep(5)
        all_images=self.driver.find_elements(By.TAG_NAME,"img")
        for images in all_images:
            print(images.get_attribute("alt"))

obj=Locators("EdgE")
obj.Facebook_Details()


