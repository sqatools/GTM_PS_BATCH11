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
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

# right click
act=ActionChains(driver)
right_click=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act.context_click(right_click).perform()

driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-cut']").click() # Alert

time.sleep(5)
