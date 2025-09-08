# 1) Static


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# # driver = webdriver.Chrome()
# # driver.maximize_window()
# title= driver.get("https://testautomationpractice.blogspot.com/")

# print(driver.title) # Automation Testing Practice

# 1) count no of rows and columns

# noofrows= len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# noofcolumns= len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))
# print(noofrows) # 7
# print(noofcolumns) # 4
#
# # 2) Read specific row and column data
#
# # specific_row=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]")
# # print(specific_row.text) # Master In Selenium
#
# # specific_col = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[3]/td[3]")
# # print(specific_col.text) # Java
#
# # 3) Read all rows and columns --- issue
# for r in range(2,noofrows+1):
#     for c in range(1,noofcolumns+1):
#         data = driver.find_element(By.XPATH,"//*[@id='HTML1']//tr["+str(r)+"]/td["+str(c)+"]")
#         print(data.text)
#     print()
#
# # 4) read the data based on condition
# for r in range(2,noofrows+1):
#     author=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
#     if author=="Mukesh":
#         book = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
#         print(book,"    ",author)
#
# driver.close()
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://cosmocode.io/automation-practice-webtable/")

















