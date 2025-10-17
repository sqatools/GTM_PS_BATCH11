import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)

# mm/dd/yyyy -- using send keys
# driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/20/2022")

Year = "2019"
Month = "July"
Date = "18"
# Scroll down by 500 pixels
# driver.execute_script("window.scrollBy(0, 1000);")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("arguments[0].ScrollIntoView();",)

# Action 1 = click
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

# Action 2 = find Year and Month
while True:
    Mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    Yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if Mon == Month and Yr == Year:
        break;
    else:
        # driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]").click() # Feature
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click() # old 

# Action 3 = find Date

Dates= driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in Dates:
    if date.text == Date:
        date.click()
        break




time.sleep(5)

