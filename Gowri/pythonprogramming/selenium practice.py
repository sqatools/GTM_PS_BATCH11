#
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

# # driver = webdriver.Chrome()
# # driver.maximize_window()
# # driver.get("https://demo.automationtesting.in/Register.html")
# # Title = driver.title
# # print(Title)
# # ele = driver.find_element(By.ID, "Skills")
# # drp = Select(ele)
# # drp.select_by_visible_text("Software")
# # time.sleep(5)
# #
# # #Count the no of options
# # print(len(drp.options))
# ## ## Capture all options
# ## all_Options = drp.options
# ## for option in all_Options:
# #     print(option.text)
# #
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Register.html")
# Title = driver.title
# print(Title)
# Hobbies = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[6]/label")
# drp = Select(Hobbies)
# print(len(drp.options))
#
# all_options = drp.options
# if drp in all_options:
#     print(all_options.text)
#
#
# # driver.find_elements(By.CSS_SELECTOR,[".col-md-4 col-xs-4 col-sm-4"]).click()
# # time.sleep(5)
#
# # col-md-4 col-xs-4 col-sm-4
#


### link ####
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.demoblaze.com/")
# print(driver.title)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Nokia").click()
# print(driver.title)
# time.sleep(5)


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# print("Homepage Title:", driver.title)
# driver.find_element(By.LINK_TEXT, "Dummy Content for Testing.").click()
# time.sleep(5)
# print("Product Page Title:", driver.title)
# driver.quit()

# #### Alerts ###
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# print("Homepage Title:", driver.title)
# driver.find_element(By.CSS_SELECTOR, "[onclick='displayAlert()']").click()
# time.sleep(5)
# driver.switch_to.alert.accept()
# driver.find_element(By.CSS_SELECTOR, "[onclick='displayConfirm()']").click()
# time.sleep(5)
# driver.switch_to.alert.accept()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, "[onclick='displayConfirm()']").click()
# time.sleep(5)
# driver.switch_to.alert.dismiss()
# time.sleep(5)
# driver.close()

#
### iframes ######

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# print(driver.title)
# driver.switch_to.frame("iframe-name")
# print(driver.title)
# time.sleep(5)
# driver.switch_to.default_content()
# print(driver.title)
# time.sleep(5)

### Handle windows ###

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Windows.html")
# print(driver.title)
# driver.find_element(By.LINK_TEXT, "click").click()
# time.sleep(5)
# print(driver.current_window_handle)
# handles = driver.window_handles
# print(handles)
# for handle in handles:
#     driver.switch_to.window(handle)
#     print(driver.title)


# ele = driver.find_element(By.ID, "Skills")
# # drp = Select(ele)
# # drp.select_by_visible_text("Software")

#### practice on drop down and frames ####

# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Windows.html")
# ele = driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[4]/a")
# ele.click()
# time.sleep(5)
# option = driver.find_element(By.XPATH,"//*[@id='header']/nav/div/div[2]/ul/li[4]/ul/li[3]/a")
# option.click()
# time.sleep(5)
# driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()
# time.sleep(5)
#
# # driver.switch_to.frame("Iframe with in an Iframe")
# # print(driver.title)
# # time.sleep(5)
# driver.switch_to.default_content()
# print(driver.title)
# time.sleep(5)

### dropdown Example ###
#
# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# ele = driver.find_element(By.ID, "dropdown-class-example")
# drp = Select(ele)
# drp.select_by_visible_text("Option2")
# time.sleep(5)
# driver.close()


##### Scrolling a webpage ###
# driver = webdriver.Chrome()
# driver.get("https://flagpedia.net/index")
# driver.maximize_window()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,5000)", "")
# # time.sleep(5)
# # flag = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/ul[2]/li[77]/a/img")
#  driver.execute_script("arguments[0].scrollIntoView();",flag)
# # alt_text = flag.get_attribute("alt")
# # print(alt_text)
# # time.sleep(5)
#
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(5)


# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Register.html")
# driver.execute_script("window.scrollBy(0,document.body.scrollheight)")
# time.sleep(3)

### Practice


#
# driver = webdriver.Chrome()
# driver.get("https://demo.nopcommerce.com/login")
# driver.maximize_window()
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")
# time.sleep(5)
# driver.find_element(By.LINK_TEXT, "Search").click()
# time.sleep(5)
# print(driver.title)
# time.sleep(5)



# for H in Hobbies:
#     if not H.is_selected():
#         H.click()
#     if H.is_selected():
#         H.click()


# print(len(Hobbies))
# for H in Hobbies:
#     print("Hobbies:", H.get_attribute('id'))
# driver.find_element(By.ID, "checkbox3").click()


#
# time.sleep(5)



# ####### checkboxes ########
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# Title = driver.title
# #driver.execute_script("window.scrollBy(0,500)","")
# Days = driver.find_element(By.XPATH, "//*[@id='post-body-1307673142697428135']/div[4]/label")
# driver.execute_script("arguments[0].scrollIntoView();", Days)
# time.sleep(5)
# checkboxes = driver.find_elements(By.XPATH,"//input[contains(@id,'day')]")

## select all the check boxes

# for box in checkboxes:
#     box.click()

# for i in range(len(checkboxes)):
#     checkboxes[i].click()
# time.sleep(5)

## select particular checkboxes ###
#
# for box in checkboxes:
#   value = box.get_attribute('id')
#   if value == 'tuesday' or  value == 'thursday':
#        box.click()

## select last 2 options ###

# print(len(checkboxes))
#
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()
# #
# # time.sleep(5)
#
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# title = driver.title
# print(title)
# ### xpath--starts-with
# #dynamic_button = driver.find_element(By.XPATH, "//*[starts-with(@name,'st')]")
#
# ## xpath-- and
# #dynamic_button = driver.find_element(By.XPATH, "//*[@class='stop' and @name='stop']")
#
# ## xpath-- or
# dynamic_button = driver.find_element(By.XPATH,"//*[@name='sta' or @class='st']")
# dynamic_button.click()
# time.sleep(5)
#
# from selenium.webdriver.support.ui import Select
# ####dropdown msdd
# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Register.html")
# driver.maximize_window()
# lang = (driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[7]/label"))
# drp = Select(lang)
# drp.select_by_visible_text("English")
#
#
# time.sleep(5)

#
# ('Filipino')
# time.sleep(5)


#
# #### https://testautomationpractice.blogspot.com/
#
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# Title = driver.title
# print(Title)
# driver.find_element(By.ID, "name").send_keys("Test")
# driver.find_element(By.ID, "email").send_keys("test@123")
# driver.find_element(By.CSS_SELECTOR, "[placeholder='Enter Phone']").send_keys("3425676")
# driver.find_element(By.ID, "textarea").send_keys("Chennai")
# genders = driver.find_element(By.XPATH, "//*[@for='gender']")
# driver.execute_script("arguments[0].scrollIntoView;", genders)
# gen = driver.find_elements(By.XPATH, "//*[@name='gender']")
# print(len(gen))
# for g in gen:
#     print(g.get_attribute("value"))
# driver.find_element(By.ID, "male").click()
# days = driver.find_elements(By.XPATH, "//*[contains(@id,'day')]")
# print(len(days))
# for d in days:
#     print(d.get_attribute("id")) ### displays total no of days in text
#
# ### select all the checkboxes
# # for d in days:
# #     d.click()
#     # d.click()
# #    print(d.is_selected())

### select random checkboxes
# for d in days:
#     day = d.get_attribute('id')
#     if day == 'monday' or day == 'wednesday':
#         d.click()

## select last 2 check boxes

# for d in range(len(days)-2,len(days)):
#     days[d].click()

### select first 3 options
# for i in range(3):
#     days[i].click()
#
# driver.find_element(By.CSS_SELECTOR, "[for='sunday']").click()
#
#
#
#
#
#
#
# time.sleep(5)
# driver.close()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Title = driver.title
print(Title)
rd = driver.find_elements(By.NAME,"radioButton")
print(len(rd))
driver.find_element(By.CSS_SELECTOR, "[value='radio3']").click()

for r in rd:
    radio = r.get_attribute('Value')
    print(r)
time.sleep(5)
