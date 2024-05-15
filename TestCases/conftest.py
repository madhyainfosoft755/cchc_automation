import pytest
from selenium import webdriver
from selenium.webdriver import Chrome, Edge, firefox

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome, firefox, edge")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    server_url = "https://ccsc.helpersin.com/"
    if browser == "chrome":
        options = webdriver.ChromeOptions()  # Create ChromeOptions instance
        # Add any additional options if needed
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Invalid browser specified: {browser}")

    driver.get(server_url)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
