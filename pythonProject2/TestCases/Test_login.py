import time
from ddt import ddt
import pytest
from cchc_automation.pythonProject2.pageObject.userr.Login_page.loginn import Login
from selenium.webdriver.common.alert import Alert
import configparser
from cchc_automation.pythonProject2.Base.email_random import Random
from cchc_automation.pythonProject2.pageObject.userr.Login_page.Forgot_password.check_password import Forgotpassword
from cchc_automation.pythonProject2.Base.google_forgot_password_vrification import get_forgot_password_email_body, \
    extract_pin_code_from_email_body
from cchc_automation.pythonProject2.pageObject.userr.Add_Activity_page.activity import Activity_page
from selenium.webdriver.support.wait import WebDriverWait

config = configparser.ConfigParser()
config.read("C://Users//Anuj//cchc_automation//pythonProject2//Utilities//.properties")


@pytest.mark.usefixtures("setup")
@ddt
class Test_Ccc_Register_Page:
    # def test_without_email_and_password(self):
    #     login = Login(self.driver)
    #     # time.sleep(4)
    #     login.login_button()
    #     time.sleep(4)
    #     login.validate_form()
    #     time.sleep(3)
    #
    # def test_only_email_without_password(self):
    #     login = Login(self.driver)
    #     login.email_login_input(config.get("Credentials","registered_email"))
    #     time.sleep(4)
    #     login.login_button()
    #     time.sleep(4)
    #     login.validate_form()
    #     time.sleep(3)
    #
    # def test_only_password_without_email(self):
    #     login = Login(self.driver)
    #     time.sleep(3)
    #     login.password_login_input(config.get("Credentials","password"))
    #     time.sleep(4)
    #     login.login_button()
    #     time.sleep(4)
    #     login.validate_form()
    #     time.sleep(3)
    #
    # def test_email_and_password_input(self):
    #     login = Login(self.driver)
    #     login.email_login_input(config.get("Credentials", "registered_email"))
    #     time.sleep(4)
    #     login.password_login_input(config.get("Credentials", "password"))
    #     time.sleep(4)
    #     login.login_button()
    #     login.login_successfull_message()
    #     time.sleep(4)

    # def test_google_login(self):
    #     login = Login(self.driver)
    #     g_email = config.get("Credentials", "g_email")
    #     g_password = config.get("Credentials", "g_password")
    #     login.google_login_btn(g_email, g_password)
    #     time.sleep(20)

    # def test_checker_password(self):
    #     pasw = Forgotpassword(self.driver)
    #     # Trigger the email
    #     pasw.forgot_password_btn_click()
    #     pasw.email_input_field(config.get("Credentials", "google_email"))
    #     pasw.send_pin_btn()
    #     time.sleep(30)
    #
    #     # Check the email
    #     email_body = get_forgot_password_email_body(config.get("Credentials", "google_email"),
    #                                                 config.get("Credentials", "google_password"))
    #     if email_body:
    #         pin_code = extract_pin_code_from_email_body(email_body)
    #         pasw.enter_pin_input_field(pin_code)
    #         print(pin_code)
    #         pasw.verify_btn()
    #     else:
    #         print("No 'Reset Password PIN' email found.")
    #         assert False, "Failed to receive the 'Reset Password PIN' email"
    #
    # time.sleep(10)

    def test_logout_button(self):
        login = Login(self.driver)
        act = Activity_page(self.driver)
        login.email_login_input(config.get("Credentials","registered_email"))
        login.password_login_input(config.get("Credentials","password"))
        time.sleep(4)
        login.login_button()
        time.sleep(1)
        act.my_activity_btn()
        login.logout_button()
        time.sleep(1)


    # def test_date_verify(self):
    #     login = Login(self.driver)
    #     login.date_time_compare()

    # def test_location(self):
    #     login = Login(self.driver)
    #     login.location_compare()

