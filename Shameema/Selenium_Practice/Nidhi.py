
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.google.com")

searchele = driver.find_element(By.NAME,'q')
searchele.send_keys("Selenium automation")

time.sleep(10)
driver.close()

