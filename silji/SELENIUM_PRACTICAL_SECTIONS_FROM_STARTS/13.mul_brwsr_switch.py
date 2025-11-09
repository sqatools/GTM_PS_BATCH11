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
        """Reusable wait to return a single element"""
        return self.wait.until(cond(locator))

    def handle_browser_tabs(self):
        # Open main page
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

        # Click on link (opens in new tab)
        self.get_element(locator=(By.LINK_TEXT, "Software Testing Principles")).click()
        time.sleep(2)

        # Get list of all open tabs
        windows_list = self.driver.window_handles

        # Switch to the new tab
        self.driver.switch_to.window(windows_list[1])
        print("Switched to new tab:", self.driver.title)

        # Wait and get all headings
        headings_list = self.wait.until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'post-body')]//h3"))
        )

        print("\nHeadings found on 'Software Testing Principles' page:\n")
        for heading in headings_list:
            print("-", heading.text)

        # Close new tab
        self.driver.close()

        # Switch back to original tab
        self.driver.switch_to.window(windows_list[0])
        print("\nSwitched back to main tab:", self.driver.ti tle)

        # Click on Robot Framework link
        self.get_element(locator=(By.LINK_TEXT, "Robot Framework")).click()
        print("\nOpened 'Robot Framework' link successfully.")

        time.sleep(5)
        self.driver.quit()


# ---------- Run ----------
obj = HandleBrowserTabs()
obj.handle_browser_tabs()
