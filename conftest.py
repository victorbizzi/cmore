import pytest
from selenium import webdriver
from utilities.globalVars import globalVars
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver: webdriver.Remote


@pytest.fixture()
def setup_teardown():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # service=service_obj)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(globalVars.base_url)

    yield
    driver.close()