from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# Title = driver.title
# print(Title)
# ### 1. finding total no of rows and columns ####
#
# noofrows = len(driver.find_elements(By.XPATH,"//*[@id='HTML1']//tbody/tr"))
# noofcolumns = len(driver.find_elements(By.XPATH,"//*[@id='HTML1']//tbody/tr/th"))
# print(noofrows)
# print(noofcolumns)
#
# #### 2. finding the specific value from the table ####
# #
# # data = driver.find_element(By.XPATH,"//*[@id='HTML1']//tr[5]/td[4]").text
# # print(data)
#
# ### 3. Find all the data from the table ####
#
# # for r in range(2,noofrows+1):
# #     for c in range(1,noofcolumns+1):
# #         data = driver.find_element(By.XPATH,"//*[@id='HTML1']//tr["+str(r)+"]/td["+str(c)+"]").text
# #         print(data,end='    ')
# #     print()
#
# #### find the books written by author mukesh ###
# for r in range(2,noofrows+1):
#     Authorname = driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]//tr["+str(r)+"]/td[2]").text
#     if Authorname == "Mukesh":
#         Bookname = driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]//tr["+str(r)+"]/td[1]").text
#         print(Bookname,'  ',Authorname)



##### practice ####

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://cosmocode.io/automation-practice-webtable/")
#
# # Count no of rows and columns
#
# noofrows = len(driver.find_elements(By.XPATH, "//*[@id='countries']/tbody/tr"))
# print(noofrows)
# noofcolumns = len(driver.find_elements(By.XPATH, "//*[@id='countries']/tbody/tr[1]/td"))
# print(noofcolumns)

# Read specific row and column data

# data = driver.find_element(By.XPATH,"//*[@id='countries']/tbody/tr[14]/td[2]")
# print(data.text)

# Read all the rows and columns data

# for r in range(2,noofrows+1):
#     for c in range(2,noofcolumns+1):
#         country = driver.find_element(By.XPATH, "//*[@id='countries']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(country,end='  ')
#     print()

# for r in range(2,noofrows+1):
#     lang = driver.find_element(By.XPATH,"//*[@id='countries']/tbody/tr["+str(r)+"]/td[5]").text
#     if lang == "English":
#         country = driver.find_element(By.XPATH, "//*[@id='countries']/tbody/tr["+str(r)+"]/td[2]").text
#
#         print(country,end='  ')
# english_count = 0
#
# # Loop through each row (skip header if present)
# rows = driver.find_elements(By.XPATH, "//*[@id='countries']/tbody/tr")
# for row in rows[1:]:  # Skip header row
#     cols = row.find_elements(By.TAG_NAME, "td")
#     if len(cols) >= 5:  # Ensure the row has enough columns
#         language = cols[4].text.strip()
#         if language == "English":
#             english_count += 1
# count  = 0
# for r in range(2,noofrows+1):
#
#     lang = driver.find_element(By.XPATH,"//*[@id='countries']/tbody/tr["+str(r)+"]/td[5]").text
#     if lang == "English":
#         count = count+1
# print("Total no of countries having English as primary language:",count)

# english = driver.find_elements(By.XPATH,"//*[@id='countries']/tbody/tr["+str(r)+"]/td['Eng']")
# print(english)

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
 ### total no of rows and columns ###

rows = len(driver.find_elements(By.XPATH, "//*[@id='rows']/tr"))
print(rows)
columns = len(driver.find_elements(By.XPATH,"//*[@id='taskTable']/thead/tr/th"))
print(columns)

## Read specific row and column data ###
data = driver.find_element(By.XPATH, "//*[@id='rows']/tr[4]/td[5]")
print(data.text)

### Read all the rows and columns data

# for r in range(1,rows+1):
#     for c in range(1,columns+1):
#         data  = driver.find_element(By.XPATH,"//*[@id='rows']/tr["+str(r)+"]/td["+str(c)+"]")
#         print(data.text,end='  ')
#     print()