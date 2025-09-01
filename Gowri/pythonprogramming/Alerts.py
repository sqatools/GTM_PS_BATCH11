from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
driver.maximize_window()
### Alert box ###
# driver.find_element(By.ID, 'alertexamples').click()
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
# time.sleep(3)

### confirm box ###
# driver.find_element(By.ID, "confirmexample").click()
# alert = driver.switch_to.alert
# print(alert.text)
# time.sleep(5)
# # alert.accept()
# alert.dismiss()
# time.sleep(5)


### prompt box ####
# prompt = driver.find_element(By.ID, "promptexample")
# driver.execute_script("arguments[0].scrollIntoView();",prompt)
# prompt.click()
# alert = driver.switch_to.alert
# print(alert.text)
# alert.send_keys("Consistency")
# time.sleep(5)
# # alert.accept()
# alert.dismiss()
# time.sleep(5)

#### Authentication popup ###

# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# time.sleep(5)
