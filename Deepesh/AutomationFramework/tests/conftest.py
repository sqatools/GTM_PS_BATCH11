from selenium import webdriver
import pytest
import os
from datetime import datetime
from ..base.webdriver_factory import WebdriverFactory


@pytest.fixture(scope="class")
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome", help="browser to execute automation")
    parser.addoption("--headlessValue", action="store", default=False, help="headless mode browser execution")


@pytest.fixture(scope="class")
def get_driver_headless(request, pytestconfig):
    browser = pytestconfig.getoption("browserName")
    headless = pytestconfig.getoption("headlessValue")
    wf = WebdriverFactory(browser=browser, headless=headless)
    driver = wf.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_configure(config):
    logs_path = os.path.join(os.getcwd(), "logs")
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)
    folder_name = datetime.now().strftime("%d_%m_%Y")
    folder_path = os.path.join(logs_path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    unique_name = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    log_file_name = f"{unique_name}_trace.log"
    log_file_path = os.path.join(folder_path, log_file_name)
    config.option.log_file = log_file_path
