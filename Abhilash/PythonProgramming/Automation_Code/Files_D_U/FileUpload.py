import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
file_path = (r"C:\PythonAutomation\AutomationRepo\First_git_file.txt")
driver.find_element(By.XPATH,"//input[@id='singleFileInput']").send_keys(file_path)

time.sleep(5)