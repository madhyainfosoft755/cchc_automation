import time
from ddt import ddt
import pytest
from cchc_automation.pythonProject2.pageObject.userr.Add_Activity_page.activity import Activity_page
from cchc_automation.pythonProject2.pageObject.userr.Login_page.loginn import Login
from selenium.webdriver.common.alert import Alert
import configparser
from cchc_automation.pythonProject2.Base.email_random import Random

from selenium.webdriver.support.wait import WebDriverWait

config = configparser.ConfigParser()
config.read("C://Users//Anuj//cchc_automation//pythonProject2//Utilities//.properties")


@pytest.mark.usefixtures("setup")
@ddt
class Test_activity_page:
    def test_without_data(self):
        act = Activity_page(self.driver)
        login = Login(self.driver)
        g_email = config.get("Credentials", "registered_email")
        g_password = config.get("Credentials", "password")
        login.completelogin(g_email, g_password)
        act.submit_button()
        act.without_data_input_click_submit_btn_error_msg()
        time.sleep(5)

    # def test_all_data(self):
    #     act = Activity_page(self.driver)
    #     login = Login(self.driver)
    #     g_email = config.get("Credentials", "registered_email")
    #     g_password = config.get("Credentials", "password")
    #     login.completelogin(g_email, g_password)
    #     time.sleep(5)
    #     act.select_category()
    #     time.sleep(5)
    #     act.date_select()
    #     time.sleep(5)
    #     act.time_selection()
    #     act.to_time_selection()
    #     act.choose_image(config.get("Credentials", "image"))
    #     time.sleep(1)
    #     act.choose_video(config.get("Credentials", "video"))
    #     time.sleep(1)
    #     act.submit_button()
    #     time.sleep(2)

    # def test_only_category_select(self):
    #     act = Activity_page(self.driver)
    #     login = Login(self.driver)
    #     g_email = config.get("Credentials", "registered_email")
    #     g_password = config.get("Credentials", "password")
    #     login.completelogin(g_email, g_password)
    #     act.select_category()
    #     time.sleep(2)
    #     act.submit_button()
    #     time.sleep(2)

    # def test_only_date_select(self):
    #     act = Activity_page(self.driver)
    #     login = Login(self.driver)
    #     g_email = config.get("Credentials", "registered_email")
    #     g_password = config.get("Credentials", "password")
    #     login.completelogin(g_email, g_password)
    #     act.date_select()
    #     time.sleep(2)
    #     act.submit_button()
    #     time.sleep(2)

    # def test_only_time_select(self):
    #     act = Activity_page(self.driver)
    #     login = Login(self.driver)
    #     g_email = config.get("Credentials", "registered_email")
    #     g_password = config.get("Credentials", "password")
    #     login.completelogin(g_email, g_password)
    #     act.time_selection()
    #     act.to_time_selection()
    #     time.sleep(2)
    #     act.submit_button()
    #     time.sleep(2)

    # def test_only_choose_image(self):
    #     act = Activity_page(self.driver)
    #     login = Login(self.driver)
    #     g_email = config.get("Credentials", "registered_email")
    #     g_password = config.get("Credentials", "password")
    #     login.completelogin(g_email, g_password)
    #     act.choose_image(config.get("Credentials", "image"))
    #     time.sleep(2)
    #     act.submit_button()
    #     time.sleep(2)
    #
    # def test_only_choose_video(self):
    #     act = Activity_page(self.driver)
    #     login = Login(self.driver)
    #     g_email = config.get("Credentials", "registered_email")
    #     g_password = config.get("Credentials", "password")
    #     login.completelogin(g_email, g_password)
    #     act.choose_video(config.get("Credentials", "video"))
    #     time.sleep(2)
    #     act.submit_button()
    #     time.sleep(20)
    # #
    def test_endorse_activity(self):
        act = Activity_page(self.driver)
        login = Login(self.driver)
        g_email = config.get("Credentials", "registered_email")
        g_password = config.get("Credentials", "password")
        login.completelogin(g_email, g_password)
        act.endorse_activity_button()
        time.sleep(10)