import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumLocators:
    def __init__(self, browser):
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Unsupported browser! Use chrome, firefox, or edge.")

        # These should be outside of the if-elif block so they run for all browsers
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def facebook_website(self):
        self.driver.get("https://www.facebook.com/")
        time.sleep(3)  # Just to keep it open for a few seconds


        # self.driver.find_element(By.ID, "email").send_keys("silji@gmail.com")

        self.driver.find_element(By.XPATH, "//input[starts-with(@placeholder, 'Email')]").send_keys("silji@gmail.com")


        # // input[starts-with(@ placeholder, "Email")]
        time.sleep(3)
        self.driver.find_element(By.NAME,"pass").send_keys("pass")
        time.sleep(3)
        # self.driver.find_element(By.XPATH, "//button[text() = 'Log in']").click()
        # self.driver.find_element(By.NAME, "Login"]).click()
        # self.driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # // button[text() = 'Log in']
        # time.sleep(10)

        # self.driver.find_element(By.NAME, "login").click()




        # self.driver.find_element(By.LINK_TEXT,"Create a new account").click()
        # self.driver.find_element(By.LINK_TEXT, "Create  new account").click()
        # self.driver.find_element(By.LINK_TEXT, "Create new account").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Create new')]").click()

        time.sleep(3)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Already have").click()
        time.sleep(4)
        # get element with tagname locator
        all_images = self.driver.find_elements(By.TAG_NAME, "img")

        # iterate through the element and perform operation.
        for image in all_images:
            print(image.get_attribute("alt"))
        time.sleep(3)


        self.driver.close()

# Run the test
obj = SeleniumLocators("chrome")
obj.facebook_website()