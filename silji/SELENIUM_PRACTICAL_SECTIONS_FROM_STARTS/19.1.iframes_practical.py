import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Handle_Iframe:
        def __init__(self):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 10)

        def get_element(self, locator, cond=ec.visibility_of_element_located):
            element = self.wait.until(cond(locator))
            return element

        def handle_iframe(self):
            self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

            frame_element=self.get_element(locator=(By.NAME,"globalSqa"))
            #SWITCH TO IFRAME
            self.driver.switch_to.frame(frame_element)

            #NAVIGATE TO MENU BUTTON IN THE IFRAME
            menu_element=self.get_element(locator=(By.XPATH,"//div[@id='mobile_menu_toggler']"))
            menu_element.click()
            time.sleep(3)

            #navigate to menu button and click on it
            contact_us=self.get_element(locator=(By.XPATH,"//div[@id='mobile_menu']//a[text()= 'Contact Us']"))
            contact_us.click()
            time.sleep(5)





obj= Handle_Iframe()
obj.handle_iframe()


