from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#these 2 things we hav to import


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



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

    def explicit_wait_example(self):
        self.driver.get("https://www.facebook.com/")
        self.wait=WebDriverWait(self.driver,10)

        t1=time.time()
        try:
            user_name_field=self.wait.until(ec.visibility_of_element_located((By.NAME,"email")))
            user_name_field.send_keys("user1@gmail.com")
        except Exception as e:
            print(e)

        t2=time.time()
        print("total time:",t2-t1)






obj = SeleniumMethods(browser="chrome")
obj.explicit_wait_example()









