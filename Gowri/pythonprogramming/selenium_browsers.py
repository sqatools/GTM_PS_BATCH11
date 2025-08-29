from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

### Basic commands ###

# driver = webdriver.Chrome()
# driver.get("https://www.automationexercise.com/")
# Title = driver.title
# print(Title)
# time.sleep(10)
# driver.close()
# print("Program executed successfully")

# driver = webdriver.Edge()
# driver.get("https://www.automationexercise.com/")
# Title = driver.title
# time.sleep(5)
# print(Title)
# URL = driver.current_url
# print(URL)
# print(driver.page_source)
# driver.close()


# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Windows.html")
# print(driver.title)
# driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
# time.sleep(10)
# driver.close()
#
# # <button class="btn btn-primary" onclick="newwindow()">click</button>


# driver = webdriver.Edge()
# driver.get("https://demo.automationtesting.in/Windows.html")
# time.sleep(10)
# driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
#
# driver.close()


#
###### Navigation commands ######


# test = webdriver.Chrome()
# test.get("https://demo.automationtesting.in/Register.html")
# Title = test.title
# print(Title)
# test.get("https://www.facebook.com/")
# print(test.title)
# test.back()
# print(Title)
# test.forward()
# print(test.title)

#### Webdriver conditional commands ###

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Register.html")
# Title = driver.title
# print(Title)
# User_ele = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[1]/div[1]/input").is_displayed()
# print(User_ele)
# Gender_ele = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input").is_enabled()
# print(Gender_ele)
#
# checkbox = driver.find_element(By.ID, "checkbox1").is_selected()
#
# print(checkbox)