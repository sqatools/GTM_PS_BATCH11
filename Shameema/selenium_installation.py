"""
Command to install selenium in local system
-> pip install selenium
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print(driver.current_url)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com")
driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
# driver.find_element(By.NAME,"password").send_keys("user@12345")
# time.sleep(5) #static wait
# driver.find_element(By.NAME, "login").click()
# time.sleep(5)
# driver.close()

driver.find_element(By.NAME, "pass").send_keys("user@12345")
time.sleep(5)  # static wait
driver.find_element(By.NAME, "login").click()
time.sleep(5)  # static wait
driver.close()