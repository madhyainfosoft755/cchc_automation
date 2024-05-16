import time
from Base.base_driver import Basedriver
from  Pages.Login import Login_page_code
from  Pages.create_activity_page import Create_activity_page_code


class activities_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.login_page_code = Login_page_code(self.driver)
        self.create_activity_page = Create_activity_page_code(self.driver)

        self.create_activity_btn = '/html/body/div/div[2]/div/div/div[1]/button'
        self.endorse_activity_btn = '/html/body/div/div[2]/div/div/div[2]/div[2]/button[1]'
        self.logout_btn = '/html/body/div/div[2]/div/div/div[2]/div[2]/button[2]'
        self.website_url = 'https://ccsc.helpersin.com'

    def tc48(self, email, password):
        self.login_page_code.tc5(email, password)
        self.create_activity_page.tc38()
        self.base.return_any("xpath", self.create_activity_btn).click()
        time.sleep(5)
        self.driver.get(self.website_url)
        time.sleep(8)

    def tc49(self, email, password):
        self.login_page_code.tc5(email, password)
        self.create_activity_page.tc38()
        self.base.return_any("xpath", self.endorse_activity_btn).click()
        time.sleep(5)
        self.driver.get(self.website_url)
        time.sleep(8)

    def tc50(self, email, password):
        self.login_page_code.tc5(email, password)
        self.create_activity_page.tc38()
        self.base.return_any("xpath", self.logout_btn).click()
        time.sleep(5)

    def all(self, email, password):
        self.tc48(email, password)
        self.tc49(email, password)
        self.tc50(email, password)
        