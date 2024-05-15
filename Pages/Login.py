import  time
from  Base.base_driver import Basedriver

class Login_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)

        self.page_url = 'https://ccsc.helpersin.com/'
        self.login_btn = '/html/body/div/div[2]/form/div[3]/button'
        self.email_input_field = '/html/body/div/div[2]/form/div[3]/div[1]/input'
        self.password_input_field = '/html/body/div/div[2]/form/div[3]/div[2]/input'
        self.forgot_password = '/html/body/div/div[2]/form/div[3]/h2'
        self.google_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[2]/div/img'
        self.facebook_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[1]/div/img'
        self.twitter_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[3]/div/img'
        self.instagram_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[4]/div/div/img'
        self.register_user = '/html/body/div/div[2]/form/div[3]/div[5]/button'


    def tc1(self):
        self.driver.get(self.page_url)
        time.sleep(2)
        self.base.return_any("xpath", self.email_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        time.sleep(8)

    def tc2(self, email):
        self.base.return_any("xpath", self.email_input_field).send_keys(email)
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        time.sleep(8)

    def tc3(self, password):
        self.base.return_any("xpath", self.email_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        time.sleep(8)

    def tc4(self, email, password):
        self.base.return_any("xpath", self.email_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.email_input_field).send_keys(email)
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        time.sleep(8)

    def tc5(self, Cemail, Cpassword):
        self.base.return_any("xpath", self.email_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.email_input_field).send_keys(Cemail)
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        time.sleep(8)

    def tc6(self):
        self.driver.get(self.page_url)
        time.sleep(5)
        self.base.return_any("xpath", self.forgot_password).click()
        time.sleep(5)
        self.driver.get(self.page_url)
        time.sleep(4)

    def tc8(self):
        self.driver.get(self.page_url)
        time.sleep(3)
        self.base.return_any("xpath", self.google_login_btn).click()
        time.sleep(5)

    def tc7(self):
        self.base.return_any("xpath", self.facebook_login_btn).click()
        time.sleep(2)

    def tc9(self):
        self.base.return_any("xpath", self.twitter_login_btn).click()
        time.sleep(2)

    def tc10(self):
        self.base.return_any("xpath", self.instagram_login_btn).click()
        time.sleep(2)

    def tc11(self):
        self.base.return_any("xpath", self.register_user).click()
        time.sleep(3)

    def all(self, email, password, Cemail, Cpassword):
        self.tc1()
        self.tc2(email)
        self.tc3(password)
        self.tc4(email, password)
        self.tc5(Cemail, Cpassword)
        self.tc6()
        self.tc7()
        self.tc9()
        self.tc10()
        self.tc11()
        self.tc8()
