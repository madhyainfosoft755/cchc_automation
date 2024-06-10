import time
from ddt import ddt
import pytest
from cchc_automation.pythonProject2.pageObject.userr.Add_Activity_page.activity import Activity_page
from cchc_automation.pythonProject2.pageObject.userr.Login_page.loginn import Login
from cchc_automation.pythonProject2.pageObject.userr.Endorsment_page.endors_page import EndorsePage
from selenium.webdriver.common.alert import Alert
import configparser

config = configparser.ConfigParser()
config.read("C://Users//Anuj//cchc_automation//pythonProject2//Utilities//.properties")


@pytest.mark.usefixtures("setup")
@ddt
class Test_Endorse_page:
    def test_check_endorse(self):
        act = Activity_page(self.driver)
        login = Login(self.driver)
        endorse = EndorsePage(self.driver)
        g_email = config.get("Credentials", "registered_email")
        g_password = config.get("Credentials", "password")
        login.completelogin(g_email, g_password)
        endorse.endorse_activity_button()
        time.sleep(5)
        endorse.search_btn_click()
        time.sleep(3)
        endorse.all_categories_view_btn_click()
        time.sleep(40)
