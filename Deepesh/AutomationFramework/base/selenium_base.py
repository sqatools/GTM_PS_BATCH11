import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.util_tools import Utils


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=20)
        self.log = logging.getLogger(__name__)
        self.util = Utils()

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        try:
            self.log.info(f"getting element with locator {locator}")
            element = self.wait.until(cond(locator))
            return element
        except Exception as e:
            self.log.info(f"element not found with locator: {locator}")
            self.log.info(e)
            image_file_path = self.util.generate_screenshot_path()
            self.log.info(f"screenshot: {image_file_path}")
            self.driver.save_screenshot(image_file_path)

            raise

    def click_element(self, locator, **kwargs):
        try:
            self.log.info(f"click on element with locator: {locator}")
            self.get_element(locator=locator, **kwargs).click()
        except Exception as e:
            self.log.info(f"unable to click element locator: {locator}")
            self.log.info(e)
            image_file_path = self.util.generate_screenshot_path()
            self.driver.save_screenshot(image_file_path)
            self.log.info(f"screenshot: {image_file_path}")
            raise

    def enter_text(self, locator, value, **kwargs):
        try:
            self.log.info(f"enter value: {value} on element with locator: {locator}")
            self.get_element(locator=locator, **kwargs).send_keys(value)
        except Exception as e:
            self.log.info(f"unable to click element locator: {locator}")
            self.log.info(e)
            image_file_path = self.util.generate_screenshot_path()
            self.driver.save_screenshot(image_file_path)
            self.log.info(f"screenshot: {image_file_path}")
            raise

    def get_text(self, locator, **kwargs):
        try:
            self.log.info(f"get from element with locator: {locator}")
            return self.get_element(locator=locator).text
        except Exception as e:
            self.log.info(f"unable to click element locator: {locator}")
            self.log.info(e)
            image_file_path = self.util.generate_screenshot_path()
            self.driver.save_screenshot(image_file_path)
            self.log.info(f"screenshot: {image_file_path}")
            raise

