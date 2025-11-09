import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HandleBrowserTabs:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def login_to_hrm_website(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.get_element(locator=(By.NAME, "username")).send_keys("Admin")
        self.get_element(locator=(By.NAME, "password")).send_keys("admin123")
        self.get_element(locator=(By.XPATH, "//button[contains(., 'Login')]"),
                         cond=ec.element_to_be_clickable).click()
        # time.sleep(10)

    def handle_browser_tabs(self):
        # Open main page
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

        # Click link to open new tab
        self.get_element(locator=(By.LINK_TEXT, "Software Testing Principles"),
                         cond=ec.element_to_be_clickable).click()

        # Get list of tabs and switch to new one
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[1])

        # Wait until second page fully loads (confirming some content present)
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[contains(@class, 'post-body')]//h3")))
        print("✅ Second page loaded successfully.")

        # Get list of headings in the new page
        headings_list = self.wait.until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'post-body')]//h3"))
        )
        for heading in headings_list:
            print(heading.text)

        # Now click on "Robot Framework" after page is ready
        robot_link = self.get_element(locator=(By.LINK_TEXT, "Robot Framework"),
                                      cond=ec.element_to_be_clickable)
        robot_link.click()
        print("✅ Clicked on 'Robot Framework' successfully!")

        time.sleep(3)  # optional to observe result


# Run
obj = HandleBrowserTabs()
obj.handle_browser_tabs()
