import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AutomationPractice:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, condition=ec.visibility_of_element_located):
        element = self.wait.until(condition(locator))
        return element

    def element_click(self, locator, **kwargs):
        self.get_element(locator, **kwargs).click()

    def select_dropdown_value(self, locator):
        element = self.get_element(locator=locator)
        return Select(element)

    def facebook_login(self):
        self.driver.get("https://www.facebook.com/")
        self.get_element(locator=(By.NAME, "email")).send_keys("user@gmail.com")
        self.get_element(locator=(By.NAME, "pass")).send_keys("User@123")
        self.element_click(locator=(By.NAME, "login"), condition=ec.element_to_be_clickable)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.element_click(locator=(By.LINK_TEXT, "Create new account"), condition=ec.element_to_be_clickable)
        time.sleep(2)
        self.get_element(locator=(By.NAME, "firstname")).send_keys("ram")
        self.get_element(locator=(By.NAME, "lastname")).send_keys("123")
        time.sleep(2)
        # click_dropdown = self.get_element(locator=(By.NAME, "birthday_day"))
        # select_day = Select(click_dropdown)
        # select_day.select_by_visible_text("10")
        # click_dropdown1 = self.get_element(locator=(By.NAME, "birthday_month"))
        # select_month = Select(click_dropdown1)
        # select_month.select_by_visible_text("Dec")
        # click_dropdown2 = self.get_element(locator=(By.NAME, "birthday_year"))
        # select_year = Select(click_dropdown2)
        # select_year.select_by_visible_text("2020")
        self.select_dropdown_value(locator=(By.NAME, "birthday_day")).select_by_visible_text("10")
        self.select_dropdown_value(locator=(By.NAME, "birthday_month")).select_by_visible_text("Dec")
        self.select_dropdown_value(locator=(By.NAME, "birthday_year")).select_by_visible_text("2020")
        time.sleep(2)
        self.element_click(locator=(By.XPATH, "//input[@type='radio' and @value='-1']"))
        value1 = -1
        if value1 == -1:
            click_dropdown3 = self.get_element(locator=(By.XPATH, "//select[@id='preferred_pronoun']"))
            select_pronoun = Select(click_dropdown3)
            select_pronoun.select_by_index(2)
            self.get_element(locator=(By.NAME, "custom_gender")).send_keys("Male")
        else:
            print("Not Selecting")

        time.sleep(2)
        self.get_element(locator=(By.NAME, "reg_email__")).send_keys("user1@gmail.com")
        self.get_element(locator=(By.NAME, "reg_passwd__")).send_keys("user123")
        time.sleep(2)
        self.element_click(locator=(By.NAME, "websubmit"), condition=ec.element_to_be_clickable)
        time.sleep(3)
        self.driver.back()
        # self.element_click(locator=(By.XPATH, "//a[text()='Forgotten password?']"))
        time.sleep(3)


class BusBooking(AutomationPractice):
    def bus_ticket_booking(self):
        self.driver.get("https://www.goibibo.com/")
        self.element_click(locator=(By.XPATH, "//span[@class='logSprite icClose']"),
                           condition=ec.element_to_be_clickable)
        self.element_click(locator=(By.XPATH, "//span[text()= 'Bus']"))

        self.get_element(locator=(By.XPATH, "//input[@placeholder='Enter Source']")).send_keys("Hyderabad")
        # //label[text()='FROM']//following-sibling::input

        self.element_click(locator=(By.XPATH, "//span[text()='Hyderabad, Telangana']"))
        time.sleep(2)
        self.get_element(locator=(By.XPATH, "//input[@placeholder='Enter Destination']")).send_keys("Vizag")
        time.sleep(2)
        self.element_click(locator=(By.XPATH, "//span[text()='Visakhapatnam (Vizag), Andhra Pradesh']"))
        self.element_click(locator=(By.XPATH, "//input[contains(@placeholder,'Pick a date')]"))
        self.element_click(locator=(By.XPATH, "//span[text()='9']"))
        time.sleep(2)
        self.element_click(locator=(By.XPATH, "//button[contains(@data-testid,'searchBusBtn')]"))
        time.sleep(10)
        self.element_click(locator=(By.XPATH, "//p[text()='APSRTC']//following::span[text()='SHOW BUSES'][1]"))
        time.sleep(2)
        self.element_click(locator=(By.XPATH, "//span[text()='SELECT SEAT'][1]"))
        self.element_click(locator=(By.XPATH, "//div[contains(@class, 'SeatWithTooltipstyles__BusSeat') and div//span["
                                              "@class='seatNum' and text()='25']]"))

        time.sleep(2)
        self.element_click(locator=(By.XPATH, "//button[text()= 'CONTINUE']"))
        time.sleep(2)
        self.get_element(locator=(By.XPATH, "//input[@placeholder='Enter Full Name']")).send_keys("Krithik")
        self.get_element(locator=(By.XPATH, "//input[@placeholder='Age']")).send_keys("21")
        self.element_click(locator=(By.XPATH, "//span[text()='Male']"))
        self.get_element(locator=(By.XPATH, "//input[@placeholder='Enter Email Address']")).send_keys("user@gmail.com")
        self.get_element(locator=(By.XPATH, "//input[@placeholder='Enter Mobile Number']")).send_keys("9876543211")
        time.sleep(2)
        self.element_click(locator=(By.XPATH, "//span[contains(@class, 'sc-bfYoXt jZjBWY')]"))
        self.element_click(locator=(By.XPATH, "//button[contains(@class, 'NewReviewstyle__PayButton')]"))
        time.sleep(8)


# obj = AutomationPractice()
# obj.facebook_login()
obj1 = BusBooking()
obj1.bus_ticket_booking()
