import time
from ddt import ddt
import pytest
from cchc_automation.pythonProject2.pageObject.userr.Add_Activity_page.activity import Activity_page
from cchc_automation.pythonProject2.pageObject.userr.Login_page.loginn import Login
from cchc_automation.pythonProject2.pageObject.userr.Endorsment_page.endors_page import EndorsePage
from selenium.webdriver.common.alert import Alert
from cchc_automation.pythonProject2.pageObject.Admin.admin_login_page import Admin_login
import configparser

config = configparser.ConfigParser()
config.read("C://Users//Anuj//cchc_automation//pythonProject2//Utilities//.properties")

@pytest.mark.usefixtures("setup")
@ddt
class Test_Admin_login_page:
    def test_approve_btn(self):
        act = Activity_page(self.driver)
        login = Login(self.driver)
        admin = Admin_login(self.driver)
        login.email_login_input(config.get("Credentials","admin_login"))
        time.sleep(2)
        login.password_login_input(config.get("Credentials","admin_password"))
        time.sleep(2)
        login.login_button()
        time.sleep(10)
        admin.apporve_hour_btn()
        time.sleep(10)

    def test_manage_Category_btn(self):
        act = Activity_page(self.driver)
        login = Login(self.driver)
        admin = Admin_login(self.driver)
        login.email_login_input(config.get("Credentials", "admin_login"))
        time.sleep(2)
        login.password_login_input(config.get("Credentials", "admin_password"))
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        admin.manage_approve_btn()

    def test_manage_approve_btn(self):
        act = Activity_page(self.driver)
        login = Login(self.driver)
        admin = Admin_login(self.driver)
        login.email_login_input(config.get("Credentials", "admin_login"))
        time.sleep(2)
        login.password_login_input(config.get("Credentials", "admin_password"))
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        admin.manage_users_btn()

    def test_manage_organisation_btn(self):
        act = Activity_page(self.driver)
        login = Login(self.driver)
        admin = Admin_login(self.driver)
        login.email_login_input(config.get("Credentials", "admin_login"))
        time.sleep(2)
        login.password_login_input(config.get("Credentials", "admin_password"))
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        admin.manage_Category_btn()

    def test_generate_report_btn(self):
        act = Activity_page(self.driver)
        login = Login(self.driver)
        admin = Admin_login(self.driver)
        login.email_login_input(config.get("Credentials", "admin_login"))
        time.sleep(2)
        login.password_login_input(config.get("Credentials", "admin_password"))
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        admin.generate_report_btn()

    def test_submit_btn(self):
        act = Activity_page(self.driver)
        login = Login(self.driver)
        admin = Admin_login(self.driver)
        login.email_login_input(config.get("Credentials", "admin_login"))
        time.sleep(2)
        login.password_login_input(config.get("Credentials", "admin_password"))
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        admin.submit_btn()