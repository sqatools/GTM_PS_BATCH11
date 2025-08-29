from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()


