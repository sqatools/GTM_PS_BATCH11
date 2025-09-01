from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Register.html")
# driver.maximize_window()
# Title = driver.title
# print(Title)
# #time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[1]/div[1]/input").send_keys("Success")
# #time.sleep(5)
# driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[1]/div[2]/input").send_keys("Consistency")
# #time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[2]/div/textarea").send_keys("Goal")
# #time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, "input[ng-model='EmailAdress']").send_keys("Heidipeter@gmail.com")
# #time.sleep(5)
# driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("123095675")
# #time.sleep(5)
# driver.find_element(By.XPATH, "//input[@value='FeMale']").click()
# #time.sleep(5)
# Value = driver.find_element(By.XPATH, "//*[@id='checkbox2']")
# Value.click()
# time.sleep(5)
# value_text = Value.get_attribute("value")
# print(value_text)
#driver.find_element(By.XPATH, "//*[@id='msdd']").send_keys("English")
# drp = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[8]/label")
# skills = Select(drp)
# skills.select_by_visible_text("FileMaker Pro")

#
# select_element = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[8]/select")
# skills = Select(select_element)
# skills.select_by_visible_text("FileMaker Pro")
#
#
#
# time.sleep(5)
# driver.close()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Title = driver.title
print(Title)

















# Checkboxes = driver.find_elements(By.CLASS_NAME,"form-control ng-pristine ng-valid ng-touched")
# print(len(Checkboxes))