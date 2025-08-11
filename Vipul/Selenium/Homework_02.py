from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class Homework_02:

    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator, cond=ec.element_to_be_clickable):
        self.wait.until(cond(locator)).click()

    def get_text(self, locator):
        text = self.get_element(locator=locator).text
        return text

    def select_dropdown(self, locator):
        element = self.get_element(locator=locator)
        return Select(element)

    def mouse_click(self, locator, cond=ec.element_to_be_clickable):
        action = ActionChains(self.driver)
        action.click(locator).perform()


    def login(self):
        username_text = self.get_text(locator=(By.XPATH,"//*[text()='Username : Admin']"))
        print(username_text)
        username = username_text[11:16]
        print(username)
        password_text = self.get_text(locator=(By.XPATH, "//*[text()='Password : admin123']"))
        password = password_text[11:19]
        print(password)
        self.get_element(locator=(By.XPATH,"//*[@name='username']")).send_keys(username)
        self.get_element(locator=(By.XPATH, "//*[@name='password']")).send_keys(password)
        self.click_element(locator=(By.XPATH, "//*[@type='submit']"))

    def admin_page(self):
        self.click_element(locator=(By.XPATH, "//*[text()='Admin']"))
        self.click_element(locator=(By.XPATH, "//*[@type='button']"))
        # self.click_element(locator=(By.XPATH, "//*[contains(@class,'select')]"))
        # self.click_element(locator=(By.XPATH, "//*[@class='oxd-select-option']//following-sibling::*[text()='Admin']"))
        # self.get_element(locator=(By.XPATH, '//*[@placeholder="Type for hints..."]')).send_keys("automation_tester")
        self.click_element(locator=(By.XPATH,"//*[@class='orangehrm-header-container']//button"))
        self.click_element(locator=(By.XPATH, "//*[contains(@class,'select')]"))

        self.click_element(locator=(By.XPATH, "//*[@class='oxd-select-option']/span[text()='Admin']"))
        self.get_element(locator=(By.XPATH, '//*[@placeholder="Type for hints..."]')).send_keys("FName Mname")
        self.click_element(locator=(By.XPATH, "//*[contains(@class,'select')]"))

        # self.click_element(locator=(By.XPATH, "//*[contains(@class,'select')]"))
        # self.click_element(locator=(By.XPATH, "//*[@class='oxd-select-option']//following-sibling::*[text()='Admin']"))





obj = Homework_02()
obj.login()
obj.admin_page()






