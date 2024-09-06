# Base/base_driver.py

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Constants.constants import Messages

# Configure logging
logging.basicConfig(
    filename='logs/automation.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
logger = logging.getLogger()

class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def locator(self, locator_name, locator_value, timeout=10):
        locators = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR
        }
        if locator_name not in locators:
            logger.error(f"Invalid locator name: {locator_name}")
            raise ValueError(f"Invalid locator name {locator_name}")

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locators[locator_name], locator_value))
            )
            logger.info(f"Element found: {locator_name}={locator_value}")
            return element
        except Exception as e:
            logger.error(f"Element not found: {locator_name}={locator_value}. Error: {e}")
            raise

    def return_any(self, locator_name, locator_var, timeout=10):
        return self.locator(locator_name, locator_var, timeout)

    def is_element_present(self, locator_type, locator_val, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator_type, locator_val))
            )
            logger.info(f"Element is present: {locator_type}={locator_val}")
            return True
        except:
            logger.warning(f"Element not present: {locator_type}={locator_val}")
            return False

    def capture_screenshot(self, file_name="screenshot.png"):
        try:
            self.driver.save_screenshot(f'screenshots/{file_name}')
            logger.info(f"Screenshot saved as {file_name}")
        except Exception as e:
            logger.error(f"Failed to save screenshot: {e}")
