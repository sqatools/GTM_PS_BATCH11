import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
skills= driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[8]/label")
driver.execute_script("arguments[0].scrollIntoView();",skills)

skills = driver.find_element(By.ID,"Skills")
drp = Select(skills)
# drp.select_by_visible_text("Android")
# drp.select_by_index(7)
# drp.select_by_value("C++")
# print(len(drp.options)) ----- count
all_options = drp.options
for option in all_options:
    print(option.text)  #list of all text


time.sleep(5)