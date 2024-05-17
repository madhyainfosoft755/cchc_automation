import  time
from  Base.base_driver import Basedriver

class forgot_password_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        
        self.page_url = 'https://ccsc.helpersin.com/forget'
        self.send_pin_btn = '/html/body/div/div[2]/div/div[3]/button[1]'
        self.enter_email = '/html/body/div/div[2]/div/div[3]/div/input'
        self.go_to_login_page = '/html/body/div/div[2]/div/div[3]/button[2]'
        self.verify_pin = '/html/body/div/div[2]/div/div[3]/button[1]'
        self.enter_pin = '/html/body/div/div[2]/div/div[3]/div/input'
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


    def tc22(self):
        self.base.return_any("xpath", self.go_to_login_page).click()
        time.sleep(3)

    def tc18(self):
        self.driver.get(self.page_url)
        time.sleep(2)
        self.base.return_any("xpath", self.go_to_login_page).click()
        time.sleep(8)

    def all(self, Wemail, Cemail, Wpin):
        self.tc14()
        self.tc15(Wemail)
        self.tc16(Cemail)
        self.tc18()
        self.tc14()
        self.tc15(Wemail)
        self.tc16(Cemail)
        self.tc19()
        self.tc20(Wpin)
        self.tc22()

