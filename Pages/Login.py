# Pages/Login.py

import time
import datetime
from selenium.webdriver import ActionChains
from geopy.geocoders import Nominatim
from constants.constants import LoginPageLocators, URLs, Messages
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_driver import BaseDriver
from Utilities.utilities import Utilities
import logging

# Configure logging
logging.basicConfig(
    filename='logs/automation.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
logger = logging.getLogger()

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.base = BaseDriver(driver)
        self.actions = ActionChains(self.driver)
        self.page_url = URLs.BASE_URL

    def tc2(self):
        try:
            self.driver.get(self.page_url)
            logger.info("Navigated to login page")
            email_element = self.base.return_any("xpath", LoginPageLocators.EMAIL_INPUT)
            email_element.clear()
            logger.info("Cleared email input field")
            password_element = self.base.return_any("xpath", LoginPageLocators.PASSWORD_INPUT)
            password_element.clear()
            logger.info("Cleared password input field")
            login_button = self.base.return_any("xpath", LoginPageLocators.LOGIN_BTN)
            login_button.click()
            logger.info("Clicked login button without credentials")

            email_validation_message = email_element.get_attribute("validationMessage")
            assert Messages.REQ_FIELD in email_validation_message, "Required field message not displayed for email."
            logger.info("Validation message for email field verified")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc2: {ae}")
            self.base.capture_screenshot("tc2_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc2: {e}")
            self.base.capture_screenshot("tc2_exception")
            assert False

    def tc3(self, email):
        try:
            email_field = self.base.return_any("xpath", LoginPageLocators.EMAIL_INPUT)
            email_field.send_keys(email)
            logger.info(f"Entered email: {email}")
            login_button = self.base.return_any("xpath", LoginPageLocators.LOGIN_BTN)
            login_button.click()
            logger.info("Clicked login button with only email")

            password_element = self.base.return_any("xpath", LoginPageLocators.PASSWORD_INPUT)
            password_validation_message = password_element.get_attribute("validationMessage")
            assert Messages.REQ_FIELD in password_validation_message, "Required field message not displayed for password."
            logger.info("Validation message for password field verified")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc3: {ae}")
            self.base.capture_screenshot("tc3_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc3: {e}")
            self.base.capture_screenshot("tc3_exception")
            assert False

    def tc4(self, password):
        try:
            email_field = self.base.return_any("xpath", LoginPageLocators.EMAIL_INPUT)
            email_field.clear()
            logger.info("Cleared email input field in tc4")
            password_field = self.base.return_any("xpath", LoginPageLocators.PASSWORD_INPUT)
            password_field.send_keys(password)
            logger.info(f"Entered password: {password}")
            login_button = self.base.return_any("xpath", LoginPageLocators.LOGIN_BTN)
            login_button.click()
            logger.info("Clicked login button with only password")

            email_validation_message = email_field.get_attribute("validationMessage")
            assert Messages.REQ_FIELD in email_validation_message, "Required field message not displayed for email."
            logger.info("Validation message for email field verified in tc4")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc4: {ae}")
            self.base.capture_screenshot("tc4_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc4: {e}")
            self.base.capture_screenshot("tc4_exception")
            assert False

    def tc5(self, Wemail, password):
        try:
            email_field = self.base.return_any("xpath", LoginPageLocators.EMAIL_INPUT)
            email_field.clear()
            logger.info("Cleared email input field in tc5")
            email_field.send_keys(Wemail)
            logger.info(f"Entered email: {Wemail}")
            password_field = self.base.return_any("xpath", LoginPageLocators.PASSWORD_INPUT)
            password_field.clear()
            logger.info("Cleared password input field in tc5")
            password_field.send_keys(password)
            logger.info(f"Entered password: {password}")
            login_button = self.base.return_any("xpath", LoginPageLocators.LOGIN_BTN)
            login_button.click()
            logger.info("Clicked login button with invalid credentials")

            presence_check = self.base.is_element_present("xpath", LoginPageLocators.LOGIN_ERROR)
            assert presence_check, "Login error message not displayed."
            logger.info("Login error message verified in tc5")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc5: {ae}")
            self.base.capture_screenshot("tc5_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc5: {e}")
            self.base.capture_screenshot("tc5_exception")
            assert False

    def tc6(self, Cemail, Wpassword):
        try:
            email_field = self.base.return_any("xpath", LoginPageLocators.EMAIL_INPUT)
            email_field.clear()
            logger.info("Cleared email input field in tc6")
            email_field.send_keys(Cemail)
            logger.info(f"Entered email: {Cemail}")
            password_field = self.base.return_any("xpath", LoginPageLocators.PASSWORD_INPUT)
            password_field.clear()
            logger.info("Cleared password input field in tc6")
            password_field.send_keys(Wpassword)
            logger.info(f"Entered wrong password: {Wpassword}")
            login_button = self.base.return_any("xpath", LoginPageLocators.LOGIN_BTN)
            login_button.click()
            logger.info("Clicked login button with correct email and wrong password")

            presence_check = self.base.is_element_present("xpath", LoginPageLocators.INVALID_PASS_ERR)
            assert presence_check, "Invalid password error message not displayed."
            logger.info("Invalid password error message verified in tc6")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc6: {ae}")
            self.base.capture_screenshot("tc6_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc6: {e}")
            self.base.capture_screenshot("tc6_exception")
            assert False

    def tc7(self, Cemail, Cpass):
        try:
            email_field = self.base.return_any("xpath", LoginPageLocators.EMAIL_INPUT)
            email_field.clear()
            logger.info("Cleared email input field in tc7")
            email_field.send_keys(Cemail)
            logger.info(f"Entered correct email: {Cemail}")
            password_field = self.base.return_any("xpath", LoginPageLocators.PASSWORD_INPUT)
            password_field.clear()
            logger.info("Cleared password input field in tc7")
            password_field.send_keys(Cpass)
            logger.info(f"Entered correct password: {Cpass}")
            login_button = self.base.return_any("xpath", LoginPageLocators.LOGIN_BTN)
            login_button.click()
            logger.info("Clicked login button with correct credentials")

            current_url = self.driver.current_url
            assert current_url == URLs.EXPECTED_URL_AFTER_LOGIN, f"Expected URL after login: {URLs.EXPECTED_URL_AFTER_LOGIN}, but got {current_url}"
            logger.info("Successfully logged in and navigated to expected URL")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc7: {ae}")
            self.base.capture_screenshot("tc7_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc7: {e}")
            self.base.capture_screenshot("tc7_exception")
            assert False

    def tc8(self):
        try:
            self.driver.get(self.page_url)
            logger.info("Navigated to login page for tc8")
            presence_check1 = self.base.is_element_present("xpath", LoginPageLocators.WELCOME_TEXT1)
            presence_check2 = self.base.is_element_present("xpath", LoginPageLocators.WELCOME_TEXT2)
            assert presence_check1 and presence_check2, "Welcome texts not displayed correctly."
            logger.info("Welcome texts verified in tc8")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc8: {ae}")
            self.base.capture_screenshot("tc8_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc8: {e}")
            self.base.capture_screenshot("tc8_exception")
            assert False

    def tc9(self):
        try:
            presence_check = self.base.is_element_present("xpath", LoginPageLocators.HINDI_TEXT)
            assert presence_check, "Hindi text not displayed."
            logger.info("Hindi text verified in tc9")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc9: {ae}")
            self.base.capture_screenshot("tc9_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc9: {e}")
            self.base.capture_screenshot("tc9_exception")
            assert False

    def tc10(self):
        try:
            forgot_pass = self.base.return_any("xpath", LoginPageLocators.FORGOT_PASSWORD)
            forgot_pass.click()
            logger.info("Clicked on Forgot Password link")
            WebDriverWait(self.driver, 10).until(EC.url_to_be(URLs.FORGOT_PASSWORD_URL))
            current_url = self.driver.current_url
            assert current_url == URLs.FORGOT_PASSWORD_URL, f"Expected Forgot Password URL: {URLs.FORGOT_PASSWORD_URL}, but got {current_url}"
            logger.info("Navigated to Forgot Password page successfully in tc10")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc10: {ae}")
            self.base.capture_screenshot("tc10_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc10: {e}")
            self.base.capture_screenshot("tc10_exception")
            assert False

    def tc11(self):
        try:
            original_window = self.driver.current_window_handle
            windows_before_click = self.driver.window_handles
            google_login_btn = self.base.return_any("xpath", LoginPageLocators.GOOGLE_LOGIN_BTN)
            google_login_btn.click()
            logger.info("Clicked Google login button")

            WebDriverWait(self.driver, 10).until(EC.new_window_is_opened(windows_before_click))
            new_window = [window for window in self.driver.window_handles if window != original_window][0]
            self.driver.switch_to.window(new_window)
            logger.info("Switched to Google login window")
            WebDriverWait(self.driver, 10).until(EC.url_contains("https://accounts.google.com"))
            logger.info("Navigated to Google login page in tc11")
        except AssertionError as ae:
            logger.error(f"Assertion failed in tc11: {ae}")
            self.base.capture_screenshot("tc11_failure")
            assert False
        except Exception as e:
            logger.error(f"Exception in tc11: {e}")
            self.base.capture_screenshot("tc11_exception")
            assert False

