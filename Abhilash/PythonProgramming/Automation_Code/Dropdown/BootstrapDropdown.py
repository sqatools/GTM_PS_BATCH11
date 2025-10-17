import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

Delivery_options = driver.find_element(By.XPATH,"//h2[normalize-space()='Delivery options:']")
driver.execute_script("arguments[0].scrollIntoView();",Delivery_options)


driver.find_element(By.XPATH,"//span[@id='select2-reasondummy-container']").click()
Deliver= driver.find_elements(By.XPATH,"//ul[@id='select2-reasondummy-results']/li")
print(len(Deliver))


for ticket in Deliver:
    if ticket.text.strip() == "Office work place needs it":
        print("Found option:", ticket.text.strip())
        ticket.click()
        break

selected_value = driver.find_element(By.XPATH,"//span[@id='select2-reasondummy-container']").text
print(selected_value)



time.sleep(5)