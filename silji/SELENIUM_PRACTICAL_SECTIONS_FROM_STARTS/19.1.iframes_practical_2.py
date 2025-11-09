import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#CLASS
class HANDLE_IFRAME:


    #constructor method
    def __init__(self):
       self.driver=webdriver.Chrome()
       self.driver.maximize_window()
       self.wait=WebDriverWait(self.driver,10)




    def get_element(self,locator, cond=ec.visibility_of_element_located):
        element=self.wait.until(cond(locator))
        return element


    #main function to handle iframe

    def handle_iframe(self):
        self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

        Frame_element=self.get_element(locator=(By.NAME,"globalSqa"))
        print("frame out:",Frame_element)

        #switch to iframe

        self.driver.switch_to.frame(Frame_element)

        menu_element = self.get_element(locator=(By.XPATH, "//div[@id='mobile_menu_toggler']"))
        menu_element.click()
        time.sleep(3)



        About = self.get_element(locator=(By.XPATH, "//div[@id='mobile_menu']//a[contains(text(),'About')]"))
        About.click()
        print("✅ 'About' clicked")


        self.driver.switch_to.default_content()

        #
        #
        # Frames_and_windows = self.get_element(locator=(By.XPATH, "//h1[text()='Frames And Windows']")).text
        # print("✅ Text on main page:", Frames_and_windows)

        Frames_and_windows = self.get_element(locator=(By.XPATH, "//h1[text()='Frames And Windows']")).text
        print("✅ Text on main page:", Frames_and_windows)


        time.sleep(3)
        self.driver.quit()



obj=HANDLE_IFRAME()
obj.handle_iframe()















