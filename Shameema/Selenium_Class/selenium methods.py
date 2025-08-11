
import time
from selenium import webdriver


class SeleniumMethods:

    def __init__(self ,browser):
        if browser.lower() =='chrome':
             self.driver =webdriver.Chrome()
        elif browser.lower() == 'firefox':
             self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
             self.driver = webdriver.Edge()

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(10)
        url1 = self.driver.current_url
        Title = self.driver.title
        print("URL:", url1)
        print("Title:",Title)


SeleniumMethods("Chrome")









