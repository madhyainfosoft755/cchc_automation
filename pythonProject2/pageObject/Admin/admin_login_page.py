import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
import time
from datetime import datetime
from cchc_automation.pythonProject2.Base.base_driver import Basedriver


class Admin_login:
    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.logout_btn_xpath = "//button[contains(text(),'LOGOUT')]"
        self.apporve_hour_btn_xpath = "//h1[contains(text(),'Approve Hours')]"
        self.manage_Category_btn_xpath = "//h1[contains(text(),'Manage Category')]"
        self.manage_approve_btn_xpath = "//h1[contains(text(),'Manage Approvers')]"
        self.manage_users_btn_xpath = "//h1[contains(text(),'Manage Users')]"
        self.manage_organisation_btn_xpath = "//h1[contains(text(),'Manage Organisation')]"
        self.generate_report_btn_xpath = "//button[contains(text(),'Generate Report')]"
        self.submit_btn_xpath = "//button[contains(text(),'Submit')]"

    def logout_btn(self):
        self.base.return_any("xpath", self.logout_btn_xpath).click()

    def apporve_hour_btn(self):
        self.base.return_any("xpath", self.apporve_hour_btn_xpath).click()

    def manage_Category_btn(self):
        self.base.return_any("xpath", self.manage_Category_btn_xpath).click()

    def manage_approve_btn(self):
        self.base.return_any("xpath", self.manage_approve_btn_xpath).click()

    def manage_users_btn(self):
        self.base.return_any("xpath", self.manage_users_btn_xpath).click()

    def manage_organisation_btn(self):
        self.base.return_any("xpath", self.manage_organisation_btn_xpath).click()

    def generate_report_btn(self):
        self.base.return_any("xpath", self.generate_report_btn_xpath).click()

    def submit_btn(self):
        self.base.return_any("xpath", self.submit_btn_xpath).click()
