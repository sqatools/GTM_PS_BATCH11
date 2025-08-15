
import  time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class Admin_page:

     def __init__(self,driver):
         self.wait = None
         self.driver = webdriver.Chrome()
         self.driver.implicitly_wait()
         self.driver.maximize_window()
         self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

     def get_element(self,locator,cond = ec.visibility_of_all_elements_located):
         element = self.wait.until(cond(locator))
         return element


     def send_value(self,sv_locator,**kwargs):
         self.get_element(locator=sv_locator, **kwargs).send_keys()

     def click_value(self,cl_locator,**kwargs):
         self.get_element(locator=cl_locator,**kwargs).click()

     def log_in_locator(self):
          username = (By.NAME,'username')

     #
     # def log_in_locator(self):
     #     username =(By.NAME, 'username')
     #     pwd =(By.NAME, 'password')
     #     Login_btn = (By.XPATH, '//*[@type ="submit"]')



    def Login_action(self,log_in_locator, send_value,click_value):
           self.send_value(sv_locator=self.log_in_locator(self.username, value ="Admin"))
           time.sleep(20)







