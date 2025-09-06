# URl --- https://www.dummyticket.com/dummy-ticket-for-visa-application/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# Scroll down by  pixels
driver.execute_script("window.scrollBy(0, 500);")

#dd/mm/yyyy

# driver.find_element(By.XPATH,"//input[@id='dob']").send_keys("10/09/2025")



driver.find_element(By.XPATH,"//input[@id='dob']").click() # open
Month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
Month.select_by_visible_text("May") # Month

Year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
Year.select_by_visible_text("1997") # Year

Dates= driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a") # date

for date in Dates:
    if date.text == "8":
        date.click()
        break








time.sleep(5)
