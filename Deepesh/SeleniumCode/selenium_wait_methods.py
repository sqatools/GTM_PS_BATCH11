import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumWaits:
    """
    1). implicit wait:  ->  Implicit wait by default applies on all the web elements.
                        ->  Implicit wait is maximum timeout to find any web element on web page.
                        ->  If driver is not able to find element within given period of time, then it will fail with
                            exception.

    2). explicit wait : ->  Explicit wait has to apply on specific web element explicitly.
                        ->  Explicit wait is maximum timeout to find any web element on web page.
                        ->  Explicit wait provide different wait condition to look for specific element.

    3). fluent wait :  Fluent wait is the poll frequency of wait time to find any element in the DOM structure.
                      ->  This we will define along with explicit wait as parameter value

    4). static wait :  This is hard code wait time, in automation execution (this is not recommended in live project)
                       e.g   time.sleep(5)
    """
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
        self.driver.maximize_window()

    def implicit_wait_example(self):
        self.driver.get("https://www.facebook.com/")
        # initiate implicit wait
        self.driver.implicitly_wait(10)

        t1 = time.time()
        try:
            user_name_field = self.driver.find_element(By.NAME, 'email1')
            user_name_field.send_keys("user1@gmail.com")
        except Exception as e:
            print(e)
            raise

        t2 = time.time()
        print("total time taken :", t2-t1)

    def explicit_wait_example(self):
        self.driver.get("https://www.facebook.com/")
        # initiate explicit wait object
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=2)

        t1 = time.time()
        try:
            user_name_field = self.wait.until(ec.visibility_of_element_located((By.NAME, "email")))
            user_name_field.send_keys("user1@gmail.com")
        except Exception as e:
            print(e)
            raise

        t2 = time.time()
        print("total time taken :", t2 - t1)


obj = SeleniumWaits(browser='Chrome')
#obj.implicit_wait_example()
obj.explicit_wait_example()