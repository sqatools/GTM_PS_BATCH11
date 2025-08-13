import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class selmethods:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window( )
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def url_launch(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def get_title_geturl(self):
        # self.driver.get("https://www.facebook.com")
        print("URL : ",self.driver.current_url)
        print("Title : ",self.driver.title)

    def get_elem(self,locator,cond = ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    # def get_list(self,locator,cond= ec.visibility_of_element_located):
    #     ellist = self.g
    #     return ellist
    def get_text(self,locator,**kwargs):
        text = self.get_elem(locator=locator,**kwargs).text
        print(text)

    def get_attr(self,locator,**kwargs):
        link=self.get_elem(locator=locator,**kwargs).get_attribute("href")
        print("Link :",link)
    def enabl_display_selected(self,locator,**kwargs):
        enable = self.get_elem(locator=locator).is_enabled()
        display = self.get_elem(locator=locator).is_displayed()
        selected = self.get_elem(locator=locator).is_selected()
        return enable , display, selected

    def click_ele(self,locator,**kwargs):
        self.get_elem(locator=locator,**kwargs).click()
    def send_data(self,locator,value,**kwargs):
        self.get_elem(locator=locator,**kwargs).send_keys(value)

    def oranhrm_gettext(self):
        # text=self.get_elem(locator=(By.XPATH,"//h5[text()='Login']")).text
        # print(text)
        self.get_text(locator=(By.XPATH, "//h5[text()='Login']"))
    def check_element_is_enabled_displayed_selected(self,user_name,pass_value):
        user_name_enabled = self.get_elem(locator=(By.NAME,"username")).is_enabled()
        print("user name field is enabled :",user_name_enabled)
        pass_word_enabled = self.get_elem(locator=(By.NAME,"password")).is_enabled()
        print("pass word field is enabled :",pass_word_enabled)

        if (user_name_enabled == True):
            self.send_data(locator=(By.NAME,"username"),value='user_name')
            time.sleep(3)
        if (pass_word_enabled == True):
            self.send_data(locator=(By.NAME, "password"), value='pass_value')
            time.sleep(3)

        self.click_ele(locator=(By.XPATH,"//button[@type='submit']"))
        time.sleep(5)

    def check_element_is_enabled_displayed(self):
            user_name_enabled = self.get_elem(locator=(By.NAME, "username")).is_enabled( )
            print("user name field is enabled :", user_name_enabled)
            pass_word_enabled = self.get_elem(locator=(By.NAME, "password")).is_enabled( )
            print("pass word field is enabled :", pass_word_enabled)

            if (user_name_enabled == True):
                self.send_data(locator=(By.NAME, "username"), value='Admin')
                time.sleep(3)
            if (pass_word_enabled == True):
                self.send_data(locator=(By.NAME, "password"), value='admin123')
                time.sleep(3)

            self.click_ele(locator=(By.XPATH, "//button[@type='submit']"))
            time.sleep(5)
    def isselected_ele(self):
        self.driver.get("https://sqatools.in/dummy-booking-website/")
        b4click = self.get_elem(locator=(By.XPATH, "//td[text()='Pune']//preceding-sibling::td/input")).is_selected()
        self.click_ele(locator=(By.XPATH,"//td[text()='Pune']//preceding-sibling::td/input"))
        after_click = self.get_elem(locator=(By.XPATH, "//td[text()='Pune']//preceding-sibling::td/input")).is_selected()
        time.sleep(20)
        print("element selection status b4 click : ", b4click)
        print("element selection status after_click : ",after_click)
        print("_"*50)
        list_of_checkbox = self.driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        for i in list_of_checkbox:
            print("is selected before click:", i.is_selected())
            i.click()
            print("is selected after click: ",i.is_selected())
            time.sleep(3)
            print("_" * 50)
    def get_ele_attribute(self):
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
        self.get_attr(locator=(By.XPATH,"//a[contains(text(),'What is Software Testing')]"))
        temp = 1
        list_of_link = self.driver.find_elements(By.XPATH,"//ul[@class='ullist']//a")
        for link in list_of_link:
            link.screenshot(f'')
            print(link.get_attribute("href"))










# que? - how to create method for is enabled, is diplayes, is selected?
# que? - how to create common method for find elements



obj = selmethods()
# obj.url_launch( )
# obj.get_title_geturl()
# obj.oranhrm_gettext()
# obj.check_element_is_enabled_displayed_selected()
# obj.isselected_ele()
obj.get_ele_attribute()