from select import select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
Title = driver.title
print(Title)
driver.find_element(By.ID, "name").send_keys("Consistency")
driver.find_element(By.CSS_SELECTOR,"[placeholder='Enter EMail']").send_keys("cons@gmail.com")
driver.find_element(By.XPATH,"//*[@id='phone']").send_keys("453567667")
driver.find_element(By.CSS_SELECTOR, "#textarea").send_keys("Chennai")
driver.execute_script("window.scrollBy(0,300)","")
# colour = driver.find_element(By.CSS_SELECTOR, "[for='colors']")
# driver.execute_script("arguments[0].scrollIntoView();",colour)
driver.find_element(By.CSS_SELECTOR,"[value='male']").click()
# count of radio buttons and their values
genders = driver.find_elements(By.CSS_SELECTOR, "[name='gender']")
print(len(genders))
for g in genders:
    value = g.get_attribute("value")
    print(value)
checkboxes = driver.find_elements(By.XPATH,"//*[contains(@id,'day')]")
print(len(checkboxes))
# for box in checkboxes:
#     box.click()
#     if box.is_selected():
#         box.click()

# select first 2 checkboxes
# for i in range(2):
#     checkboxes[i].click()

# select last 2 checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#  select any random checkboxes
# for box in checkboxes:
#     cbox = box.get_attribute("id")
#     if cbox == "tuesday" or cbox == "friday":
#         box.click()

## dropdown
country = driver.find_element(By.ID, "country")
dropdown = Select(country)
dropdown.select_by_visible_text("India")
time.sleep(3)
Alloptions = dropdown.options
print(len(Alloptions))
for opt in Alloptions:
    print(opt.text)










