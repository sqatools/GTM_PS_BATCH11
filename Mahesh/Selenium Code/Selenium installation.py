import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.find_element(By.NAME,"email").send_keys("8795485658")
driver.find_element(By.NAME,"pass").send_keys("Mahesh123")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='login']").click()
time.sleep(10)