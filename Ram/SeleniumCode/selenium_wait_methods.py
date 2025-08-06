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
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif browser.lower() == "edge":
            self.driver = webdriver.Edge()

        self.driver.maximize_window()


