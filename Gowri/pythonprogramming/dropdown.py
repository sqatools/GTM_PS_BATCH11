from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
print(driver.title)
#skills = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[8]/label")
#driver.execute_script("arguments[0].scrollIntoView();",skills)
#driver.execute_script("window.ScrollBy(0,1000)","")
#driver.execute_script("window.scrollBy(0,5000)", "")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(10)

# lang = driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[7]/label")
# drp = Select(lang)
# # drp.select_by_visible_text('Bulgarian')
# drp.select_by_index('15')

# skills = driver.find_element(By.ID, "Skills")
# drp = Select(skills)
# # drp.select_by_visible_text('Corel Word Perfect')
# # drp.select_by_index('15')
# drp.select_by_value('Diagnostics')
#
# print(len(drp.options))
# sk = drp.options
# for i in sk:
#     print(i.text)
# time.sleep(5)
### getting all the dropdown values ###

# count = driver.find_element(By.ID, "countries")
# drp = Select(count)
# # drp.select_by_value('Japan')
# drp.select_by_index('5')
# #print(len(drp.options))

year = driver.find_element(By.ID, "yearbox")
drp = Select(year)
drp.select_by_visible_text('1922')
print(len(drp.options))

yr = drp.options

for i in yr:
    print(i.text)

time.sleep(5)