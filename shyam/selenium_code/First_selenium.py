import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#driver=webdriver.Edge()
#driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.find_element(By.NAME,"email").send_keys("user1@gmail.com")
driver.find_element(By.NAME,"pass").send_keys("user1234")
time.sleep(5)
driver.find_element(By.NAME,"login").click()
time.sleep(5)
driver.close()








