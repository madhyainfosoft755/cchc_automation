from selenium import webdriver
import pytest
import configparser

config = configparser.ConfigParser()
config.read("C:\\Users\\Anuj\\cchc_automation\\pythonProject2\\Utilities\\.properties")


@pytest.fixture()
def setup(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get(config.get("Url", "base_url"))
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(10)
    yield
    request.cls.driver.quit()
