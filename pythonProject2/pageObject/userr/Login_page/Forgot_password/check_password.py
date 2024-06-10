import time
from selenium.webdriver.common.by import By
from cchc_automation.pythonProject2.Base.base_driver import Basedriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
import time
from datetime import datetime


class Forgotpassword:
    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.forgot_password_btn_click_xpath = "//h2[contains(text(),'Forgot Password')]"
        self.email_input_field_xpath = "//body/div[@id='root']/div[2]/div[1]/div[3]/div[1]/input[1]"
        self.send_pin_btn_xpath = "//button[contains(text(),'Send PIN')]"
        self.enter_pin_input_field_xpath = "//body/div[@id='root']/div[2]/div[1]/div[3]/div[1]/input[1]"
        self.verify_btn_xpath = "//button[contains(text(),'Verify PIN')]"

    def forgot_password_btn_click(self):
        self.driver.find_element(By.XPATH, self.forgot_password_btn_click_xpath).click()

    def email_input_field(self, email):
        self.driver.find_element(By.XPATH, self.email_input_field_xpath).send_keys(email)

    def send_pin_btn(self):
        self.driver.find_element(By.XPATH, self.send_pin_btn_xpath).click()

    def enter_pin_input_field(self, pin):
        self.driver.find_element(By.XPATH, self.enter_pin_input_field_xpath).send_keys(pin)

    def verify_btn(self):
        self.driver.find_element(By.XPATH, self.verify_btn_xpath).click()
