from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_option
from selenium.webdriver.firefox.options import Options as firefox_option
from selenium.webdriver.edge.options import Options as edge_option


class WebdriverFactory:
    def __init__(self, browser, headless=False):
        self.browser = browser
        self.headless = headless

    def get_driver_instance(self):
        driver = None
        if self.browser.lower() == 'chrome':
            opt = chrome_option()
            if self.headless:
                opt.add_argument("--headless")
            driver = webdriver.Chrome(options=opt)

        elif self.browser.lower() == 'firefox':
            opt = firefox_option()
            if self.headless:
                opt.add_argument("--headless")
            driver = webdriver.Firefox(options=opt)

        elif self.browser.lower() == 'edge':
            opt = edge_option()
            if self.headless:
                opt.add_argument("--headless")
            driver = webdriver.Edge(options=opt)

        driver.maximize_window()
        return driver


