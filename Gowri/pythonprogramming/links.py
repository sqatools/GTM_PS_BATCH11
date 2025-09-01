from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#
d = webdriver.Chrome()
d.maximize_window()
d.get("https://demo.nopcommerce.com/#main")
# d.find_element(By.LINK_TEXT, "Digital downloads").click()
# d.find_element(By.PARTIAL_LINK_TEXT, "Gift").click()
# time.sleep(5)
