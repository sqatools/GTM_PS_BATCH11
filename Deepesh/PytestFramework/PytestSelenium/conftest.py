import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
