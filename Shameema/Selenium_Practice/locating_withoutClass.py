import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def browserlaunch():
    driver = webdriver.Chrome()
def open_browser():
        nonlocal driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.facebook.com")
        driver.implicitly_wait(25)
        driver.close()
#
#  # driver.get("https://www.flipkart.com")
#  # driver.implicitly_wait(25)
#  # driver.close()

def locate_element():
          nonlocal driver
          driver.find_element(By.NAME,"email").send_keys("user1@gmail.com")
          driver.implicitly_wait(25)
          driver.close()

browserlaunch()
open_browser()
locate_element()



# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com")
# driver.maximize_window()
# driver.implicitly_wait(25)
#
# driver.find_element(By.NAME,'email').send_keys("user123")
# driver.find_element(By.NAME, "pass").send_keys("user@12345")
# time.sleep(5)  # static wait
# driver.find_element(By.NAME, "login").click()
# time.sleep(5)  # static wait
# driver.close()
