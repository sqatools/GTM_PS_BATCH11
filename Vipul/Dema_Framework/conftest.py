from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='class')
def get_driver():
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver