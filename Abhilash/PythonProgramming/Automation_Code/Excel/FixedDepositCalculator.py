import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Abhilash.PythonProgramming.Automation_Code.Excel import Utilityfile

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")

file = (r"E:\Practice files\Testcaes.xlsx")
rows= Utilityfile.getRowCount(file, "sales")

# Capture data from the Excel Sheet
for r in range(2,rows+1):
    Princ= Utilityfile.readData(file, "sales", r, 1)
    RateofInt= Utilityfile.readData(file, "sales", r, 2)
    per1= Utilityfile.readData(file, "sales", r, 3)
    per2 = Utilityfile.readData(file, "sales", r, 4)
    fre = Utilityfile.readData(file, "sales", r, 5)
    Exp_mval= Utilityfile.readData(file, "sales", r, 6)

# Passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys("Princ")
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys("RateofInt")
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys("per1")

    prddrp=Select (driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    prddrp.select_by_visible_text(per2)
    frqdrp = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frqdrp.select_by_visible_text(fre)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    Act_mval=driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong")
    Act_mval.text

    if float(Exp_mval) == float(Act_mval):
        print("Test Passed")
        Utilityfile.writeData(file, "sales", r, 8, "Pass")
        Utilityfile.fillGreenColor(file, "sales", r, 8)
    else:
        print("Test Failed")
        Utilityfile.writeData(file, "sales", r, 8, "Fail")
        Utilityfile.fillRedColor(file, "sales", r, 8)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(5)





