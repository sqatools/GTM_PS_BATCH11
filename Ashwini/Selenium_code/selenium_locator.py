"""
command to install selenium on local system
-> pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# set timeout for each time.
driver.implicitly_wait(10)
# Launch URL on browser
driver.get("https://www.facebook.com")
# find element with NAME locator
driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
# find element with NAME locator
driver.find_element(By.NAME, "pass").send_keys("user@12345")
time.sleep(5)  # static wait
driver.find_element(By.NAME, "login").click()
time.sleep(5)  # static wait
driver.close()
#################################