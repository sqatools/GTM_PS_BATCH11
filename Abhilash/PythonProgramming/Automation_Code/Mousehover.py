#Mouse operations
# 1) Mouse hover --- move_to_element(element)
# 2) right click --- context_click(element)
# 3) double click --- double_click(element)
# 4) Drag and Drop --- drag_and_drop(source,taraget)
# 5) Slider --- drag_and_drop_by_offset(element,X-axis,Y-axis)



from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

import time

driver= webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(3)

