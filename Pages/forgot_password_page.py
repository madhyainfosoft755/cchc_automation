import time
from Base.base_driver import Basedriver
from Pages.get_forgot_pass_pin_form_gmail import Get_pin_form_gmail
import re


class forgot_password_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.get_pin = Get_pin_form_gmail()

        self.page_url = 'https://ccsc.helpersin.com/forget'
        self.send_pin_btn = '/html/body/div/div[2]/div/div[3]/button[1]'
        self.enter_email = '/html/body/div/div[2]/div/div[3]/div/input'
        self.go_to_login_page = '/html/body/div/div[2]/div/div[3]/button[2]'
        self.goto_login_update_pass_page = '/html/body/div/div[2]/div/div[3]/button'
        self.verify_pin = '/html/body/div/div[2]/div/div[3]/button[1]'
        self.enter_pin = '/html/body/div/div[2]/div/div[3]/div/input'
        self.update_pass = '/html/body/div/div[2]/div/div[3]/div/button'
        self.enter_new_pass = '/html/body/div/div[2]/div/div[3]/div/div[1]/input'
        self.confirm_mew_pass = '/html/body/div/div[2]/div/div[3]/div/div[2]/input'

    def tc14(self):
        self.driver.get(self.page_url)
        time.sleep(5)
        self.base.return_any("xpath", self.send_pin_btn).click()
        time.sleep(3)

    def tc15(self, Wemail):
        self.base.return_any("xpath", self.enter_email).send_keys(Wemail)
        time.sleep(2)
        self.base.return_any("xpath", self.send_pin_btn).click()
        time.sleep(8)

    def tc16(self, Cemail):
        self.base.return_any("xpath", self.enter_email).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.enter_email).send_keys(Cemail)
        time.sleep(2)
        self.base.return_any("xpath", self.send_pin_btn).click()
        time.sleep(8)

    def tc19(self):
        self.base.return_any("xpath", self.verify_pin).click()
        time.sleep(3)

    def tc20(self, Wpin):
        self.base.return_any("xpath", self.enter_pin).send_keys(Wpin)
        time.sleep(3)
        self.base.return_any("xpath", self.verify_pin).click()
        time.sleep(5)

    def tc21(self):
        email_body = self.get_pin.get_forgot_password_email_body()
        if email_body:
            print("Email body:\n", email_body)
            pin = self.extract_pin_from_email(email_body)
            if pin:
                self.base.return_any("xpath", self.enter_pin).clear()
                time.sleep(3)
                self.base.return_any("xpath", self.enter_pin).send_keys(pin)
                time.sleep(3)
                self.base.return_any("xpath", self.verify_pin).click()
                time.sleep(5)
            else:
                print("Failed to extract PIN from the email.")
        else:
            print("No 'Forgot Password' email found.")

    def extract_pin_from_email(self, email_body):
        match = re.search(r'\b\d{6}\b', email_body)
        if match:
            return match.group(0)
        else:
            print("PIN not found in the email body")
            return None

    def tc23(self):
        self.base.return_any("xpath", self.update_pass).click()
        time.sleep(3)

    def tc24(self, pass1, pass2):
        self.base.return_any("xpath", self.enter_new_pass).send_keys(pass1)
        time.sleep(3)
        self.base.return_any("xpath", self.confirm_mew_pass).send_keys(pass2)
        time.sleep(3)
        self.base.return_any("xpath", self.update_pass).click()
        time.sleep(5)

    def tc25(self, password):
        self.base.return_any("xpath", self.enter_new_pass).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.enter_new_pass).send_keys(password)
        time.sleep(3)
        self.base.return_any("xpath", self.confirm_mew_pass).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.confirm_mew_pass).send_keys(password)
        time.sleep(3)
        self.base.return_any("xpath", self.update_pass).click()
        time.sleep(5)

    def tc22(self, Cemail):
        self.driver.get(self.page_url)
        time.sleep(3)
        self.tc16(Cemail)
        self.base.return_any("xpath", self.go_to_login_page).click()
        time.sleep(3)

    def tc18(self):
        self.driver.get(self.page_url)
        time.sleep(2)
        self.base.return_any("xpath", self.go_to_login_page).click()
        time.sleep(8)

    def tc27(self, Cemail):
        self.driver.get(self.page_url)
        time.sleep(2)
        self.tc16(Cemail)
        self.tc21()
        self.base.return_any("xpath", self.goto_login_update_pass_page).click()
        time.sleep(5)

    def all(self, Wemail, Cemail, Wpin, pass1, pass2, password):
        self.tc14()
        self.tc15(Wemail)
        self.tc16(Cemail)
        self.tc19()
        self.tc20(Wpin)
        self.tc21()
        self.tc23()
        self.tc24(pass1, pass2)
        self.tc25(password)
        self.tc18()
        self.tc22(Cemail)
        self.tc27(Cemail)
