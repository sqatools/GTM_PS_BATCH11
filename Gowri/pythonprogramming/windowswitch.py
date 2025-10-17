from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://testpages.eviltester.com/styled/windows-test.html")
driver.find_element(By.PARTIAL_LINK_TEXT, "Basic").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Attributes").click()
all_links = driver.find_elements(By.XPATH, "/html/body/div/div[3]/ul/li")
print(len(all_links))
window_handles = driver.window_handles
print(window_handles)

for win in window_handles:
    driver.switch_to.window(win)
    if driver.title =="Test Page For Element Attributes" and driver.title == "Test Page For Basic Ajax Example":
        driver.close()



# for link in all_links:
#     print(link.text)

time.sleep(5)

