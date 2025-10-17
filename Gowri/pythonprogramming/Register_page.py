from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
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

#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://vinothqaacademy.com/iframe/")
# Title = driver.title
# print(Title)
#
# driver.execute_script("window.scrollBy(0,500);")
# frame3 = driver.switch_to.frame("registeruser")
# driver.find_element(By.CLASS_NAME, "vfb-desc")
# frame3_title = driver.execute_script("return document.title;")
# driver.execute_script("window.scrollBy(0,1000);")
# driver.find_element(By.NAME,"vfb-5").send_keys("Courage")
# #driver.find_element(By.XPATH, "//*[@value='Female']").click()
# radio = driver.find_elements(By.XPATH, "//*[@name='vfb-31']")
# print(len(radio))
# for r in radio:
#     Gender = r.get_attribute("value")
#     print(Gender)
# Checkboxes = driver.find_elements(By.XPATH, "//*[@name='vfb-20[]']")
# print(len(Checkboxes))
# for box in Checkboxes:
#     boxes = box.get_attribute("value")
#     print(boxes)
# country = driver.find_element(By.XPATH, "//*[@id='item-vfb-13']/div/span[7]/span/span[1]/span/span[2]")
# drp_count = Select(country)
# allopts = drp_count.options
# for opt in allopts:
#     count = opt.get_attribute("value")
#     print(count)
#
#
#
#
# # alloptions = drp.
# time.sleep(3)

from selenium.webdriver.chrome.options import Options

ops = Options()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)
driver.maximize_window()
driver.get("https://whatmylocation.com/")
time.sleep(5)
















