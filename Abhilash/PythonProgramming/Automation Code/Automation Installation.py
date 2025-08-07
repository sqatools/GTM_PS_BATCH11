import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.minimize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.find_element(By.NAME, "email").send_keys("user1@gamil.com")
driver.find_element(By.NAME,"Pass").send_keys("user@123")
time.sleep(5)
driver.find_element(By.NAME, "login").click()
time.sleep(5)
driver.close()