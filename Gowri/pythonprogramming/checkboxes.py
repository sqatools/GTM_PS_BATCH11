from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

### select all checkboxes ####
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# Days = driver.find_element(By.XPATH, "//*[@for='days']")
# driver.execute_script("arguments[0].scrollIntoView();",Days)
# checkboxes = driver.find_elements(By.XPATH, "//*[contains(@id,'day')]")
# print(len(checkboxes))
## select all cehckboxes ###
# for box in checkboxes:
#     box.click()
# time.sleep(5)

# for i in range(len(checkboxes)):
#     checkboxes[i].click()
# time.sleep(5)

### to select last 2 options

# for i in range(len(checkboxes)-3,len(checkboxes)):
#     checkboxes[i].click()

## selecting particular values ###

# for box in checkboxes:
#     Values = box.get_attribute('value')
#     if Values == 'monday' and Values == 'saturday':
#         box.click()
# time.sleep(5)

time.sleep(5)





















driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
Hob = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[6]/label")
driver.execute_script("arguments[0].scrollIntoView();",Hob)
time.sleep(5)
Hobby = driver.find_elements(By.XPATH, "//*[@type='checkbox']")
print(len(Hobby))
# for i in range(len(Hobby)):
#     Hobby[i].click()
# for H in Hobby:
#     H.click()

# for H in Hobby:
#     Values = H.get_attribute('value')
#     if Values == 'Cricket' or Values == 'Hockey':
#         H.click()
# time.sleep(5)

