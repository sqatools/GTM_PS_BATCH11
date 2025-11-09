import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HandleBrowserTabs:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # Increased to 20 seconds for safety
        self.wait = WebDriverWait(self.driver, 20)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        """Reusable method to wait and return element"""
        return self.wait.until(cond(locator))

    def login_to_hrm_website(self):
        """Optional: Example for HRM login"""
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.get_element(locator=(By.NAME, "username")).send_keys("Admin")
        self.get_element(locator=(By.NAME, "password")).send_keys("admin123")
        self.get_element(locator=(By.XPATH, "//button[contains(., 'Login')]"), cond=ec.element_to_be_clickable).click()

    def handle_browser_tabs(self):
        """Handles multiple browser tabs"""
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

        # Click on link to open new tab
        self.get_element(locator=(By.LINK_TEXT, "Software Testing Principles")).click()

        # Wait until a new window is opened (more reliable than sleep)
        self.wait.until(ec.new_window_is_opened(self.driver.window_handles))

        # Get the list of all open window handles
        windows_list = self.driver.window_handles


        # Switch to the new tab (last one)
        self.driver.switch_to.window(windows_list[-1])
        print("Switched to new tab:", self.driver.title)
        time.sleep(2)

        # Wait for and get all h3 headings in the new tab
        headings_list = self.wait.until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='post-body entry-content']//h3"))
        )

        print("\nHeadings on 'Software Testing Principles' page:\n")
        for heading in headings_list:
            print("-", heading.text)

        # Close only the new tab
        self.driver.close()

        # Switch back to the original tab
        self.driver.switch_to.window(windows_list[0])
        print("\nSwitched back to main tab:", self.driver.title)

        time.sleep(2)

        # Click on "Robot Framework" link (opens in the same tab)
        # self.get_element(locator=(By.LINK_TEXT, "Robot Framework")).click()
        # print("\nOpened 'Robot Framework' link successfully.")
        # time.sleep(5)

        # Do NOT quit the browser if you want to keep it open
        # self.driver.


# ---------- Run Script ----------
if __name__ == "__main__":
    obj = HandleBrowserTabs()
    # obj.login_to_hrm_website()
    obj.handle_browser_tabs()
