import time
from ddt import ddt
import pytest
import configparser
from cchc_automation.pythonProject2.pageObject.userr.Login_page.Forgot_password.check_password import Forgotpassword
from cchc_automation.pythonProject2.Base.google_forgot_password_vrification import get_forgot_password_email_body, \
    extract_pin_code_from_email_body

config = configparser.ConfigParser()
config.read("C://Users//Anuj//cchc_automation//pythonProject2//Utilities//.properties")


@pytest.mark.usefixtures("setup")
@ddt
class Test_forgot_password:

    def test_checker_password(self):
        pasw = Forgotpassword(self.driver)
        # Trigger the email
        pasw.forgot_password_btn_click()
        pasw.email_input_field(config.get("Credentials", "google_email"))
        pasw.send_pin_btn()
        time.sleep(30)

        # Check the email
        email_body = get_forgot_password_email_body(config.get("Credentials", "google_email"),
                                                    config.get("Credentials", "google_password"))
        if email_body:
            pin_code = extract_pin_code_from_email_body(email_body)
            pasw.enter_pin_input_field(pin_code)
            print(pin_code)
            pasw.verify_btn()
        else:
            print("No 'Reset Password PIN' email found.")
            assert False, "Failed to receive the 'Reset Password PIN' email"

    time.sleep(10)
