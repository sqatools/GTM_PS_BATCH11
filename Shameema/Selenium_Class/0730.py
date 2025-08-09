import time

from selenium import webdriver
from selenium.webdriver.common.by import  By
# from selenium.webdriver.support.wait import  wait

class Selmethod:

    def __init__(self,browser):
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif browser.lower() == "edge":
            self.driver = webdriver.Edge()

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def forwa_back(self):
        self.driver.get("https://www.facebook.com")
        self.driver.find_element(By.ID , 'email').send_keys("user12")
        self.driver.find_element(By.ID, "pass").send_keys("1234")
        self.driver.find_element(By.XPATH, '//*[text()="Create new account"]').click()

        self.driver.save_screenshot("sign up page.png")
        self.driver.back()
        self.driver.save_screenshot("login page.png")
        self.driver.forward()
        self.driver.save_screenshot("sign up page.png")
        self.driver.back()
        time.sleep(10)
        self.driver.refresh()
        time.sleep(10)

    def implicit_wait(self):
        self.driver.get("https://www.facebook.com")
        # self.driver.find_element(By.ID , 'email').send_keys("user12")

        t1 = time.time()
        try:
              user_name_field =  self.driver.find_element(By.ID , 'email')
              user_name_field.send_keys("user12")
        except Exception as  e:
              print(e)
        t2 = time.time()

        print("time taken:" , t2-t1)
# obj = Selmethod("Chrome")
# # obj.forwa_back()
# obj.implicit_wait()
class SeleniumWaits:
 """
      # 1. implicit wait: --> Implicit wait by default applies on all the web elements
     #                    -->taskl can complete anytime till maximum time - not required to wait until the maxtime
     #   2. Explicit wait --> Explicit wait - it will apply specifically on a particular web element
                            --. Expliciit wait provide different wait condition to look for specific element

     # 3.fluent wait --> Fluent wait is the poll frequency of wait time to find any element in the DOM(entire HTML structure is known as DOM)
                                structure
                          .._ this we will define along with explicit wait as parameter value
     # 4. static wait --> This is hard code wait time, in automation execution ( this is not recommended in live project)
                            e.g time.sleep()

 """
 def __init__(self, browser):
         if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
         elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
         elif browser.lower() =='edge':
            self.driver = webdriver.Edge()

         self.driver.maximize_window()
         self.driver.get("https://www.facebook.com")
         time.sleep(10)

SeleniumWaits("Chrome")



