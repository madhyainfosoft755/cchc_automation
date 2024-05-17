import time
from selenium.webdriver.common.by import By


class Basedriver:

    def __init__(self, driver):
        self.driver = driver

    def locator(self, locator_name, locator_value):
        locators = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR
        }
        if locator_name not in locators:
            raise ValueError(f"invalid locator name {locator_name}")

        return self.driver.find_element(locators[locator_name], locator_value)

    def return_any(self, locator_name, locator_var):
        return self.locator(locator_name, locator_var)
