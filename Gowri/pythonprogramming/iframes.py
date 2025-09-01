from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://vinothqaacademy.com/iframe/")
driver.switch_to.frame("employeetable")
driver.find_element(By.ID, "nameInput").send_keys("Discipline")
# driver.switch_to.default_content()
# driver.switch_to.frame("popuppage")
# alert_box = driver.find_element(By.NAME, "alertbox")
# # driver.execute_script("arguments[0].scrollIntoView();",alert_box)
# time.sleep(5)
# alert_box.click()
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(5)
driver.switch_to.default_content()
driver.switch_to.frame(2)
gender = driver.find_element(By.CLASS_NAME, "vfb-desc")
driver.execute_script("arguments[0].scrollIntoView();",gender)
driver.find_element(By.ID,"vfb-5").send_keys("Courage")
time.sleep(5)