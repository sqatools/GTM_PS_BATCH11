import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.NAME, "email").send_keys("vippulkumar85@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("vipul@1264")
time.sleep(5)
driver.find_element(By.NAME, "login").click()
text = driver.find_element(By.XPATH, "//div[@class='_9ay7']").text
print(text)



