import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import  expected_conditions as ec

class HandleActionChai:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver,10)
        self.action = ActionChains(self.driver)

    def get_ele(self,locator,cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self,locator,**kwargs):
        self.get_ele(locator=locator,**kwargs).click()

    def get_text(self,locator,**kwargs):
        text = self.get_ele(locator=locator,**kwargs).text
        return text

    def enter_data(self,locator,value,**kwargs):
        self.get_ele(locator=locator,**kwargs).send_keys(value)

    def perform_hover_to_element_operation(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        tester_hub_elem = self.get_ele(locator=(By.XPATH,"//div[@id='menu']//a[contains(text(),'Tester’s Hub')]"))
        self.action.move_to_element(tester_hub_elem).perform()
        time.sleep(5)
        # demo_testing =self.get_ele(locator=(By.XPATH,"//ul[@class='sub-menu']//a[contains(text(),'Demo Testing Site')]"))
        demo_testing=self.get_ele(locator=(By.XPATH,"//div[@id='menu']//a[normalize-space()='Demo Testing Site']"))
        self.action.move_to_element(demo_testing).perform()
        time.sleep(5)
        # alert_elem=self.get_ele(locator=(By.XPATH,"//ul[@class='sub-menu']//a[contains(text(),'AlertBox')]"))
        alert_elem=self.get_ele(locator=(By.XPATH,"//div[@id='menu']//a[normalize-space()='AlertBox']"))
        self.action.click(alert_elem).perform()
        time.sleep(10)

# que - what is the difference between move to ele and click?
    def perform_drag_drop_operations(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        iframe_ele = self.get_ele(locator=(By.XPATH,"//iframe[contains(@src,'droppable/photo')]"))
        self.driver.switch_to.frame(iframe_ele)
        # source_ele = self.get_ele(locator=(By.XPATH,"//ul[@id='gallery']"))
        image1_ele=self.get_ele(locator=(By.XPATH,"//h5[text()='High Tatras']//parent::li"))
        targ_ele=self.get_ele(locator=(By.XPATH,"//div[@id='trash']"))
        self.action.drag_and_drop(image1_ele,targ_ele).perform()
        time.sleep(7)

        for i in range(2,5):
            image1_ele =self.get_ele(locator=(By.XPATH,f"//h5[text()='High Tatras {i}']//parent::li"))
            targ_ele = self.get_ele(locator=(By.XPATH, "//div[@id='trash']"))
            self.action.drag_and_drop(image1_ele, targ_ele).perform( )
            time.sleep(7)

    def perfrom_context_click_opertions(self):
        import pyautogui
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        # heading_ele = self.get_ele(locator=(By.XPATH,"//h1[text()='Drag And Drop']"))
        # # self.action.double_click(heading_ele).context_click(heading_ele).perform()
        # self.action.context_click(heading_ele).perform()
        # time.sleep(7)
        about_ele = self.get_ele(locator=(By.XPATH,"//div[@id='menu']//a[text()='About']"))
        self.action.context_click(about_ele).perform()
        time.sleep(5)
        #about_ele.send_keys(keys.UP+keys.ENTER)
        pyautogui.press("up")
        time.sleep(5)
        pyautogui.press("Enter")
        time.sleep(5)
        about_ele.send_keys(Keys.ENTER)
        time.sleep(10)


obj = HandleActionChai()
# obj.perform_hover_to_element_operation()
# obj.perform_drag_drop_operations()
obj.perfrom_context_click_opertions()