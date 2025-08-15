import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class bus:

    def __init__(self):
        self.driver = webdriver.Chrome( )
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window( )
        self.driver.implicitly_wait(10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator, **kwargs):
        self.get_element(locator=locator, **kwargs).click( )

    def enter_text(self, locator, value, **kwargs):
        self.get_element(locator=locator, **kwargs).send_keys(value)

    def book_bus(self):
        self.driver.get("https://www.goibibo.com")
        # self.driver.get("https://www.goibibo.com/bus")
        self.click_element(locator=(By.XPATH, "//span[@class = 'logSprite icClose']"), cond=ec.element_to_be_clickable)
        time.sleep(10)
        self.click_element(locator=(By.XPATH, "//span[text()='Bus']"), cond=ec.element_to_be_clickable)
        # self.enter_text(locator=(By.XPATH, "//span[text()='Bus']"),  value="CHENNAI")
        self.enter_text(locator=(By.XPATH,"/html/body/div[1]/section/section/section[1]/section/div[1]/div/input"),value='chennai')
        # time.sleep(10)

        self.driver.close( )


obj = bus( )
obj.book_bus()
