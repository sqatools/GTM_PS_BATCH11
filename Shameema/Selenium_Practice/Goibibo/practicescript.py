import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select




driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://www.goibibo.com")
driver.get("https://www.goibibo.com/bus")
# driver.find_element(By.XPATH ,"//span[@class = 'logSprite icClose']")
# time.sleep(5)
# driver.find_element(By.XPATH, "//span[text()='Bus']").click ()
# time.sleep(10)
driver.find_element(By.ID ,"autosuggestBusSRPSrcHome").send_keys("Chennai")
time.sleep(10)
ch_list = driver.find_element(By.XPATH,"//div[@id='downshift-1-menu']/div[@id='downshift-1-item-0']//span")
print(ch_list)
ch_list.click()
time.sleep(10)
# driver.find_element(By.ID,"//div[@id='downshift-1-menu']/div[@id='downshift-1-item-0']//span")
driver.find_element(By.ID ,"autosuggestBusSRPDestHome").send_keys("Madurai")
time.sleep(10)
ch1_list = driver.find_element(By.XPATH,"//div[@id='downshift-2-menu']/div[@id='downshift-2-item-0']//span")
ch1_list.click()
time.sleep(10)
search_bus= driver.find_element(By.XPATH,"//div/button[@data-testid = 'searchBusBtn']")
search_bus.click()
time.sleep(30)