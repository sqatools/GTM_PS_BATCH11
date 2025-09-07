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
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/ ")

min_slider= driver.find_element(By.XPATH,"//body//div//span[1]")
max_slider = driver.find_element(By.XPATH,"//body//div//span[2]")

print("Location of before sliding.....")
print(min_slider.location) # {'x': 59, 'y': 250}
print(max_slider.location) # {'x': 545, 'y': 250}

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-45,0).perform()

print("Location of after sliding.....")
print(min_slider.location) # {'x': 161, 'y': 250}
print(max_slider.location) # {'x': 502, 'y': 250}

time.sleep(5)