import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()