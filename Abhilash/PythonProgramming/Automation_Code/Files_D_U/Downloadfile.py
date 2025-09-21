import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Location = os.getcwd() # current working directory

#----Chrome----

# def chrome_setup():
#     preferences = {"download.default_directory": "C:\PythonAutomation"} # save the file in desired location
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs",preferences)
#     driver = webdriver.Chrome(options=ops)
#     return driver
# driver = chrome_setup()

# ----Edge---

# def edge_setup():
#     preferences = {"download.default_directory": "C:\PythonAutomation"} # save the file in desired location
#     ops = webdriver.EdgeOptions()
#     ops.add_experimental_option("prefs",preferences)
#     driver = webdriver.Edge(options=ops)
#     return driver
# driver = edge_setup()

# ----Firefox/download directly in default location ----
#  list of mime types ---https://docs.w3cub.com/http/basics_of_http/mime_types/complete_list_of_mime_types.html
# settings ------------ 2,3 line will avoid that popup window
# def firefox_setup():
#
#     ops = webdriver.FirefoxOptions()
#     ops.set_preference("browser.helerApps.neverAsk.savetoDisk","image/jpeg")
#     ops.set_preference("browser.download.manager.showWhenStarting",False)
#     ops.set_preference("browser.download.folderList",2) # Desktop =0 , Downloads folder = 1, Desired location = 2
#     ops.set_preference("browser.download.dir","C:\PythonAutomation")
#
#
# # --------------------------------
#     driver = webdriver.Firefox(options=ops)
#     return driver
# driver = firefox_setup()

#----Chrome---- pdf files

def chrome_setup():
    preferences = {"download.default_directory": "C:\PythonAutomation","plugins.always_open_pdf_externally":True} # save the file in desired location
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=ops)
    return driver
driver = chrome_setup()
# driver.get()
driver.get("https://freetestdata.com/document-files/pdf/")
driver.maximize_window()
driver.find_element(By.XPATH,"(//div[@class='elementor-button-wrapper'])[1]").click()

time.sleep(5)
driver.close()