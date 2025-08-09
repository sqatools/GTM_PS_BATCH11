
import time
from selenium import webdriver
from selenium.webdriver.common.by import  By

class loc:

     def __init__(self,browser):

          if browser == "chrome":
              self.driver = webdriver.Chrome()
          elif browser == "firefox":
              self.driver = webdriver.Firefox()
          elif browser == "edge":
              self.driver = webdriver.Edge()

          self.driver.implicitly_wait(10)
          self.driver.maximize_window()

     def flipkart_website (self):
         self.driver.get("https://www.flipkart.com")
         # self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/header/div[2]/div[2]/div/div/div/div/a/span").click()
         # self.driver.find_element(By.XPATH, '//*[@title = "Cart"]').click()
         self.driver.find_element(By.XPATH, '//*[@alt = "Minutes"]').click()
         self.driver.find_element(By.NAME, 'q').send_keys("Dress")
         time.sleep(10)

         self.driver.close()
         #   self.driver.get("https://www.facebook.com")
         #   self.driver.find_element(By.TYPE, 'text').send_keys("123")
         #   time.sleep(30)
         #   self.driver(close)
         # self.driver.get("https://qatestlab.com/")
         # self.driver.find_element(By.CLASS_NAME,"icon-normal").click()
         # time.sleep(10)
         # self.driver.close()



# launch = loc("chrome")
# launch.flipkart_website()


# class locibi:
#     def __init__(self,browser):
#          if browser.lower() == 'chrome':
#              self.driver = webdriver.Chrome()
#          elif browser.lower() == 'firefox':
#              self.driver = webdriver.Firefox()
#          elif browser.lower() == "edge":
#              self.driver = webdriver.Edge()
#
#          self.driver.get("https://www.goibibo.com")
#          self.driver.maximize_window()
#          self.driver.implicitly_wait(20)
#          time.sleep(10)
#          self.driver.find_element(By.NAME,"phone").send_keys(8990000000)
#          time.sleep(10)
#          self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/span[3]').click()
#          time.sleep(10)
#          self.driver.find_element(By.XPATH,'//*[text()="Continue"]').click()
#          time.sleep(10)
#
# locibi("Chrome")
#

# class NSE:
#
#     def __init__(self,browser):
#         if browser.lower() == 'chrome':
#            self.driver = webdriver.Chrome()
#         if browser.lower == 'Firefox':
#             self.driver = webdriver.Firefox()
#         if browser.lower == 'edge':
#             self.driver = webdriver.Edge()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         self.driver.get("https://www.nseindia.com")
#         time.sleep(5)
#         # self.driver.find_element(By.XPATH,'//*[tr')
#         self.driver.find_element(By.XPATH,'//input[@autocomplete="off"]').send_keys("Check")
#         self.driver.find_element(By.XPATH,'//span[@class = "full"]').click()
#         time.sleep(5)
#         # self.driver.find_element(By.PARTIAL_LINK_TEXT,'nav-link dd-link').click()
#         self.driver.find_element(By.ID,'link_0').click()
#         time.sleep(5)
#         self.driver.close()
#
# # question 07/26- how to access the elements inside a element
# NSE("Chrome")
#


class fb:
#
    def __init__(self,browser):
        if browser.lower() == 'chrome':
           self.driver = webdriver.Chrome()
        if browser.lower == 'Firefox':
            self.driver = webdriver.Firefox()
        if browser.lower == 'edge':
            self.driver = webdriver.Edge()

            self.driver.maximize_window()
            time.sleep(30)
            self.driver.implicitly_wait(10)
            self.driver.get("https://www.facebook.com")
            time.sleep(5)
            self.driver.find_element(By.NAME,'email').send_keys('user1234')
            self.driver.find_element(By.ID,'pass').send_keys("24334")
            self.driver.find_element(By.XPATH,'//button[text() = "Log in"]').click()
            time.sleep(5)
#         # self.driver.find_element(By.PARTIAL_LINK_TEXT,'nav-link dd-link').click()
#         self.driver.find_element(By.ID,'link_0').click()
#         time.sleep(5)
#         self.driver.close()
#
# # question 07/26- how to access the elements inside a element
fb("Chrome")
#