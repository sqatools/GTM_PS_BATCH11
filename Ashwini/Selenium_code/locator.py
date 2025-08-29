import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class SeleniumLocator:
    """
       Type of locators

       1. ID = "id"  # done
       2. XPATH = "xpath"
       3. LINK_TEXT = "link text" # done
       4. PARTIAL_LINK_TEXT = "partial link text" # done
       5. NAME = "name" # done
       6. TAG_NAME = "tag name"
       7. CLASS_NAME = "class name"
       8. CSS_SELECTOR = "css selector"
       """

    def __init__(self, browser):
        if browser.lower() == 'chrome':
            # Launch chrome browser and initiate driver variable
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            # Launch Firefox browser and initiate driver variable
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            # Launch Edge browser and initiate driver variable
            self.driver = webdriver.Edge()

        # wait for element
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def facebook_website(self):
        self.driver.get("https://www.facebook.com/")

        # get element with ID locator
        self.driver.find_element(By.ID, "email").send_keys("user1@gmail.com")

        # get element with Name locator
        self.driver.find_element(By.NAME, "pass").send_keys("user@1234")

        time.sleep(5)

        self.driver.find_element(By.XPATH, "//a[@role='button']/div/div").click()
        time.sleep(10)

        # get element with link_text locator
        self.driver.find_element(By.LINK_TEXT, "Create new account").click()

        time.sleep(5)
        # get element with partial_link_text locator
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Already have").click()

        time.sleep(5)
        # get element with tagname locator
        all_images = self.driver.find_elements(By.TAG_NAME, "img")

        # iterate through the element and perform operation.
        for image in all_images:
            print(image.get_attribute("alt"))
            # image.click()

        time.sleep(5)
        self.driver.close()

    def greeting(self):
        print("Hello good morning")


obj = SeleniumLocator("EDGE")
obj.facebook_website()
obj.greeting()