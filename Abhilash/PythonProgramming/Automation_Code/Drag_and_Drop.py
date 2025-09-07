#Mouse operations
# 1) Mouse hover --- move_to_element(element)
# 2) right click --- context_click(element)
# 3) double click --- double_click(element)
# 4) Drag and Drop --- drag_and_drop(source,taraget)
# 5) Slider --- drag_and_drop_by_offset(element,X-axis,Y-axis)




from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testautomationcentral.com/demo/drag_and_drop.html")


act= ActionChains(driver)
source= driver.find_element(By.ID,"draggable")
target= driver.find_element(By.ID,"droppable")
act.drag_and_drop(source,target).perform()


time.sleep(5)


