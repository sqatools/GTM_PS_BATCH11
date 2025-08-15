import time

from selenium  import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class bus:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # self.driver.get("https://www.goibibo.com")
        self.driver.get("https://www.goibibo.com/bus")

    def locators(self):

        # self.driver.find_element(By.XPATH,"//span[@class = 'logSprite icClose']")
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//span[text()='Bus']").click()
        # time.sleep(10)
        # self.driver.find_element(By.ID,"autosuggestBusSRPSrcHome").send_keys("Chennai")
        # time.sleep(30)
        # self.driver.find_element(By.ID,"autosuggestBusSRPDestHome").send_keys("Madurai")
        # time.sleep(30)

        # self.driver.find_element(By.NAME,'autosuggestBusSRPSrcHomeName').send_keys("Koyambedu'")
        # self.driver.find_element(By.XPATH,"//input[contains,(@placeholder = 'Enter Source')]").send_keys("Koyambedu'")
        # self.driver.find_element(By.ID,'autosuggestBusSRPSrcHome').send_keys('Chennai')
        # time.sleep(10)
        # searchbus.click()
        # self.driver.find_element(By.XPATH,"//div[@class = ('SearchWidgetstyles__InputText-sc-1mr4hwz-1 biXizc')]/").send_keys("CHENNIA")
        # time.sleep(10)
        # // *[ @ id = "root"] / section / section / section[1] / section / div[1] / div / label
        # (self.driver.find_element(By.CSS_SELECTOR, "input[placeholder= 'Enter Source']").
        #  send_keys("CHENNAI"))
        # searchbus= self.driver.find_element(By.XPATH,"//button[@data-testid = 'searchBusBtn']")
        # searchbus.click()
        # time.sleep(10)

        # self.driver.close()

        self.driver.find_element(By.ID, "autosuggestBusSRPSrcHome").send_keys("Chennai")
        time.sleep(10)
        ch_list = self. driver.find_element(By.XPATH, "//div[@id='downshift-1-menu']/div[@id='downshift-1-item-0']//span")
        print("from", ch_list)
        ch_list.click( )
        time.sleep(10)
        # driver.find_element(By.ID,"//div[@id='downshift-1-menu']/div[@id='downshift-1-item-0']//span")
        self.driver.find_element(By.ID, "autosuggestBusSRPDestHome").send_keys("Madurai")
        time.sleep(10)
        ch1_list = self.driver.find_element(By.XPATH, "//div[@id='downshift-2-menu']/div[@id='downshift-2-item-0']//span")
        ch1_list.click( )
        time.sleep(10)
        search_bus = self.driver.find_element(By.XPATH, "//div/button[@data-testid = 'searchBusBtn']")
        search_bus.click( )
        time.sleep(30)

obj1= bus()
obj1.locators()

