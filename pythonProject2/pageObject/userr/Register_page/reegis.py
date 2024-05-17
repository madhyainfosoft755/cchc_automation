import time

from selenium.webdriver.common.by import By
from cchc_automation.pythonProject2.Base.base_driver import Basedriver

from selenium.webdriver.common.alert import Alert
import configparser


config = configparser.ConfigParser()
config.read("C://Users//Anuj//cchc_automation//pythonProject2//Utilities//.properties")

class Register:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.register_button_xpath = "//button[contains(text(),'Register As New User')]"
        self.name_input_xpath = "//input[@placeholder='Name']"
        self.email_input_xpath = "//input[@placeholder='Email']"
        self.phone_input_xpath = "//input[@placeholder='Phone']"
        self.address_input_xpath = "//input[@placeholder='Address']"
        self.aadhar_number_input_xpath = "//input[@placeholder='Aadhar Number']"
        self.password_input_xpath = "//input[contains(@name,'password')]"
        self.confirm_password_input_xpath = "//input[@placeholder='Confirm Password']"
        self.choose_profile_picture_xpath = "//input[@placeholder='select a file']"
        self.select_category_checkbox_xpath = "//input[@type='checkbox']"
        self.wrong_email_error_message_xpath = "//div[contains(text(),'Invalid email format')]"
        self.Create_button_xpath = "//button[contains(text(),'Create Account')]"

        self.eye_icon1_xpath = "//div[@class ='eye-icon-container']"
        self.eye_icon2_xpath = "//div[@class ='eye-icon-container']"
        self.password_required_field_error_message_field_xpath = "//div[@class = 'Toastify__toast-body']"
        self.password_error_message_xpath = "//div[contains(text(),'Passwords do not match')]"
        self.invalid_mobile_number_error_xpath = "//div[@class = 'Toastify__toast-body']"
        self.email_already_exits_error_message_xpath = "//div[@class = 'Toastify__toast-body']"
        self.check_confirm_password_error_message = "//div[@class = 'Toastify__toast-body']"
        self.login_here_button_xpath = "//span[contains(text(),'Login Here')]"
        # self.invalid_mobile_number_error_xpath

    def register_button(self):
        self.base.return_any("xpath", self.register_button_xpath).click()

    def name_input(self, username):
        # self.base.return_any("xpath",self.name_input_xpath).clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.name_input_xpath).send_keys(username)

    def email_input(self, email):
        #         self.base.return_any("xpath", self.email_input_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)

    def wrong_email_error_message(self, wemail):
        self.base.return_any("xpath", self.wrong_email_error_message_xpath).send_keys(wemail)

    def phone_input(self, phone):
        #         self.base.return_any("xpath", self.phone_input_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.phone_input_xpath).send_keys(phone)

    def address_input(self, address):
        #         self.base.return_any("xpath", self.address_input_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.address_input_xpath).send_keys(address)
        time.sleep(2)

    def aadhar_number_input(self, aadhar):
        #         self.base.return_any("xpath", self.aadhar_number_input_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.aadhar_number_input_xpath).send_keys(aadhar)

    def password_input(self, password):
        #         self.base.return_any("xpath", self.password_input_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.password_input_xpath).send_keys(password)

    def confirm_password_input(self, confirm_password):
        #         self.base.return_any("xpath",  self.confirm_password_input_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.confirm_password_input_xpath).send_keys(confirm_password)
        time.sleep(2)

    def choose_profile_picture(self, file_path):
        self.driver.find_element(By.XPATH, self.choose_profile_picture_xpath).send_keys(file_path)

    def select_category_checkbox(self):
        # self.driver.find_element(By.XPATH, self.select_category_checkbox_xpath)
        checkboxes = self.driver.find_elements(By.XPATH, self.select_category_checkbox_xpath)
        checkboxes_count = 0
        # print(checkboxes_count)
        for checkbox in checkboxes:
            if checkboxes_count < 2:
                checkboxes_count += 1
                continue
            checkbox.click()

    def eye_icon1(self):
        self.driver.find_element(By.XPATH, self.eye_icon1_xpath).click()

    def eye_icon2(self):
        self.driver.find_element(By.XPATH, self.eye_icon2_xpath).click()

    def Create_button(self):
        self.driver.find_element(By.XPATH, self.Create_button_xpath).click()

    def password_required_field_error_message_field(self):
        error = self.driver.find_element(By.XPATH, self.password_required_field_error_message_field_xpath)
        if error.is_displayed():
            return True
        else:
            return False

    def password_error_message(self):
        error = self.driver.find_element(By.XPATH, self.password_error_message_xpath)
        if error.is_displayed():
            return True
        else:
            return False

    def email_already_exits_error_message(self):
        error = self.driver.find_element(By.XPATH, self.email_already_exits_error_message_xpath)
        if error.is_displayed():
            return True
        else:
            return False

    def invalid_mobile_number_error(self):
        error = self.driver.find_element(By.XPATH, self.invalid_mobile_number_error_xpath)
        if error.is_displayed():
            return True
        else:
            return False

    def validate_form(self):
        self.Create_button()

        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except:
            return None

    def check_confirm_password(self, password, confirm_password):

        password_input = self.driver.find_element(By.XPATH, self.password_input_xpath)
        confirm_password_input = self.driver.find_element(By.XPATH, self.confirm_password_input_xpath)

        password_value = password_input.send_keys(password)
        confirm_password_value = confirm_password_input.send_keys(confirm_password)
        try:
            password_error_message = self.driver.find_element(By.XPATH, self.check_confirm_password_error_message)

            if password_value == password and confirm_password_value == confirm_password:
                print("Password and Confirm Password match.")
            else:
                raise ValueError("Password and Confirm Password do not match.")
        except:
            print("Error message : ", password_error_message.text)

    def login_here_button(self):
        self.driver.find_element(By.XPATH,self.login_here_button_xpath).click()

