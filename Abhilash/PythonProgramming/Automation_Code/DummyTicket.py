import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.execute_script("window.scrollBy(0, 400);")

# Radio buttons -- Choose the correct option:
driver.find_element(By.CSS_SELECTOR,"#product_550").click()
# scroll
Passenger = driver.find_element(By.XPATH,"//h3[normalize-space()='Passenger details:']")
driver.execute_script("arguments[0].scrollIntoView();",Passenger)

# Passenger Details
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("Sai Chandhu")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("Mike")

# Additional Info
driver.find_element(By.CSS_SELECTOR,"#order_comments").send_keys("Place near the door")

# Date of birth --- date picker
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

#Sex radio button
Sex = driver.find_elements(By.NAME,'sex')
print("Total:",len(Sex))
driver.find_element(By.XPATH,"//input[@id='sex_2']").click()
for S in Sex:
    Radio = S.get_attribute("id")
    label = driver.find_element(By.XPATH, f"//label[@for='{Radio}']")
    print("Option:", label.text)

# scroll
Trip = driver.find_element(By.XPATH,"//p[@id='traveltype_field']//label[@for='1']")
driver.execute_script("arguments[0].scrollIntoView();",Trip)

# Trip Type
driver.find_element(By.CSS_SELECTOR,"#traveltype_2").click()

# From City To City
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Chennai")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("Banglore")

# Depature Date
driver.find_element(By.XPATH,"//input[@id='departon']").click()

Months = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
Months.select_by_visible_text("Oct") # Month

Year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
Year.select_by_visible_text("2025")

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in dates:
    if date.text == "10":
        date.click()
        break

# Delivery_options
Delivery_options = driver.find_element(By.XPATH,"//h2[normalize-space()='Delivery options:']")
driver.execute_script("arguments[0].scrollIntoView();",Delivery_options) # scroll

driver.find_element(By.XPATH,"//span[@id='select2-reasondummy-container']").click()
Deliver= driver.find_elements(By.XPATH,"//ul[@id='select2-reasondummy-results']/li")
print(len(Deliver))

for ticket in Deliver:
    if ticket.text.strip() == "Office work place needs it":
        # print("Found option:", ticket.text.strip())
        ticket.click()
        break

selected_value = driver.find_element(By.XPATH,"//span[@id='select2-reasondummy-container']").text
print(selected_value)

# Appointment / Submission date
# driver.find_element(By.XPATH,"//input[@id='appoinmentdate']").click()
#
# Months = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
# Months.select_by_visible_text("Nov") # Month
#
# Year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
# Year.select_by_visible_text("2025")
#
# dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
#
# for date in dates:
#     if date.text == "20":
#         date.click()
#         break

# How will you like to receive the dummy ticket (optional)

Soc= driver.find_elements(By.XPATH,"//*[@name='deliverymethod']")
print("Total:",len(Soc))
driver.find_element(By.XPATH,"//input[@id='deliverymethod_3']").click()
for S in Soc:
    Radio = S.get_attribute("id")
    label = driver.find_element(By.XPATH, f"//label[@for='{Radio}']")
    print("Option:", label.text)




time.sleep(5)











# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Register.html")
# driver.find_element(By.XPATH,"//input[@ng-model='FirstName']").send_keys('Abhilash')
# driver.find_element(By.XPATH,"//input[@ng-model='LastName']").send_keys('Borra')
# driver.find_element(By.XPATH,"//*[@ng-model='Adress']").send_keys('Goa')
# driver.find_element(By.XPATH,"//input[@ng-model='EmailAdress']").send_keys('abhi113@gmail.com')
# driver.find_element(By.XPATH,"//input[@value='Male']").click()
# # driver.find_element(By.XPATH, "//input[@value='FeMale']").click()
#
#
# time.sleep(5)
# driver.close()


