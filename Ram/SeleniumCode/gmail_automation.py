"""
command to install selenium
-> pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")  # Only if needed
options.add_argument("--disable-dev-shm-usage")  # Helps in Docker
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.gmail.com/")
driver.find_element(By.NAME, "identifier").send_keys("ramakrishna6833@gmail.com")
time.sleep(3)
driver.find_element(By.ID, "identifierNext").click()
driver.find_element(By.NAME, "Passwd").send_keys("abcd123")
time.sleep(3)
driver.find_element(By.ID, "passwordNext").click()
time.sleep(15)
driver.find_element(By.ID, ":lq").click()

time.sleep(30)
driver.close()

