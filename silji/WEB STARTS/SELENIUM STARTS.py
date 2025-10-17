#TEST CASE
#1)open web browser (chrome/firefox/edge).
#2)open url
#3)enter username
#4)enter password
#5)click on login
#6) capture title of the home page(act title)
#7) verify title of the page: orangehrm(expected)
#8.close browser

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()  # ✅ Capital 'F'
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.find_element(By.NAME, "username").send_keys("Admin")
# time.sleep(20)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait until username field is visible
time.sleep(20)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username"))
).send_keys("Admin")

time.sleep(20)
# Enter password
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password"))
).send_keys("admin123")
time.sleep(20)

# Click login button
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
).click()

driver.quit()


