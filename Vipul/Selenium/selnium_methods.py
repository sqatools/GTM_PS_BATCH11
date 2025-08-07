
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# options = Options()
# options.add_experimental_option('detach',"True")

# driver = webdriver.Chrome(options=options)

class SeleniumMethods:
    def __init__(self, browser):
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()


        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get_title(self):
        self.driver.get("https://sqatools.in/")
        print(self.driver.title)

    # def check_element_is_selected

obj = SeleniumMethods(browser='chrome')
obj.get_title()

