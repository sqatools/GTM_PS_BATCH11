from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class Homework:
    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.goibibo.com")
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator, cond=ec.element_to_be_clickable):
        self.wait.until(cond(locator)).click()

    def select_dropdown(self, locator):
        element = self.get_element(locator=locator)
        return Select(element)

    def flight_booking(self):
        self.click_element(locator=(By.XPATH, "//*[contains(@class,'icClose')]"))
        self.click_element(locator=(By.XPATH,'//span[text()="Flights"]'))
        time.sleep(3)
        self.get_element(locator=(By.XPATH,"//*[text()='From']//following-sibling::p")).send_keys("Delhi")
        self.get_element(locator=(By.XPATH, "//*[text()='To']//following-sibling::p")).send_keys("Mumbai")
        self.click_element(locator=(By.XPATH, "//*[text()='Departure']//following-sibling::p"))
        self.click_element(locator=(By.XPATH, "//*[text()='19']"))



    def bus_booking(self):
        self.click_element(locator=(By.XPATH, "//*[contains(@class,'icClose')]"))
        self.click_element(locator=(By.XPATH, '//span[text()="Bus"]'))
        # self.driver.get("https://www.goibibo.com/bus/")
        self.get_element(locator=(By.XPATH,'//input[@placeholder="Enter Source"]')).send_keys('delhi')
        self.click_element(locator=(By.XPATH,'//span[text()="Delhi"]'))
        # time.sleep(2)
        self.get_element(locator=(By.XPATH, '//input[@placeholder="Enter Destination"]')).send_keys('Dehradun')
        self.click_element(locator=(By.XPATH, '//span[text()="Dehradun, Uttarakhand"]'))
        self.click_element(locator=(By.XPATH, '//input[@placeholder="Pick a date"]'))
        self.click_element(locator=(By.XPATH, '//span[text()="19"]'))
        self.click_element(locator=(By.XPATH, "//button[text()='Search Bus']"))

        #book Bus
        self.click_element(locator=(By.XPATH, "(// span[text() = 'SHOW BUSES'])[1]"))
        self.click_element(locator=(By.XPATH, "(// span[text() = 'SELECT SEAT'])[1]"))
        self.click_element(locator=(By.XPATH, "(//div[contains(@class, 'BusSeat-sc-dkrka')])[23]"))
        self.click_element(locator=(By.XPATH, "//button[text()='CONTINUE']"))
        self .get_element(locator=(By.XPATH,'//input[@placeholder="Enter Email Address"]')).send_keys(("abc@gmail.com"))
        self.get_element(locator=(By.XPATH, '//input[@placeholder="Enter Mobile Number"]')).send_keys(("1234567890"))
        self.get_element(locator=(By.ID, 'Billing Address')).send_keys(("Dehradun"))
        self.get_element(locator=(By.ID, 'Pincode')).send_keys(("248001"))

        self.click_element(locator=(By.XPATH,'(//div[@class="billing-input-container"])[3]'))
        self.click_element(locator=(By.XPATH,'//li[text()="Uttarakhand"]'))
        time.sleep(2)
        #self.get_element(locator=(By.XPATH,"//input[@id='confirm_check']")).click()
        self.click_element(locator=(By.XPATH,"//input[@id='confirm_check']//parent::span"))
        # self.click_element(locator=(By.XPATH,"//input[@id='confirm_check']"))
        # self.click_element(locator=(By.XPATH,"//input[@type='checkbox']"))
        self.click_element(locator=(By.XPATH,'//li[text()="Pay ₹"]'))

# doubt : what is the issue in line number 54 and how we can remove the indexing in above lines.....
obj = Homework()
obj.bus_booking()
#obj.flight_booking()