# ctrl + A
# ctrl + c
# TAB
# ctrl + v

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
driver.get("https://testautomationpractice.blogspot.com/ ")

input1 = driver.find_element(By.ID,"name")
input2 = driver.find_element(By.ID,"email")

input1.send_keys("webdriver")

act = ActionChains(driver)

# ctrl + A
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# ctrl + c
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# TAB key
act.send_keys(Keys.TAB).perform()

# ctrl + v
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)


