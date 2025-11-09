from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SeleniumMethod:
    def __init__(self,browser):
        if browser == 'Chrome':
            self.driver=webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    #navigate website to check selected status

    def sqa_tool(self):
        self.driver.get("https://sqatools.in/dummy-booking-website/")
        time.sleep(5)
        check_box_elem=self.driver.find_element(By.XPATH,"//td[text()='Pune']//preceding-sibling::td/input")
        print("is selected status before click:", check_box_elem.is_selected())
        time.sleep(5)
        check_box_elem.click()
        print("is selected status after click:", check_box_elem.is_selected())
        time.sleep(5)

        List_of_checkbox=self.driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        for checkbox in List_of_checkbox:
            print("is selected status before click:", checkbox.is_selected())
            checkbox.click()
            print("is selected status after click:", checkbox.is_selected())
            time.sleep(5)
            print("_"*50)

obj=SeleniumMethod("Chrome")
obj.sqa_tool()
