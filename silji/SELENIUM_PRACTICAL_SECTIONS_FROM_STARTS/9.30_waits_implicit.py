from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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


    def implicit_wait_example(self):
        self.driver.get("https://www.facebook.com/")
        #initiate implicit wait
        self.driver.implicitly_wait(15)

        t1= time.time()
        try:
            user_name_field=self.driver.find_element(By.NAME,'email')
            user_name_field.send_keys("user1@gmail.com")
        except Exception as e:
            print(e)
        t2=time.time()
        print("total time taken:",t2-t1)


    




obj=SeleniumMethods(browser="chrome")
obj.implicit_wait_example()









