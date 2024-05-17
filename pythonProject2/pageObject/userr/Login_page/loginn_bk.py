from selenium.webdriver.common.by import By
from cchc_automation.pythonProject2.Base.base_driver import Basedriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)

        self.page_url = 'https://ccsc.helpersin.com/'
        self.login_btn_xpath = "//button[contains(text(),'Login')]"
        self.email_input_field_xpath = '/html/body/div/div[2]/form/div[3]/div[1]/input'
        self.password_input_field_xpath = '/html/body/div/div[2]/form/div[3]/div[2]/input'
        self.login_successfull_message_xpath = "//div[@class = 'Toastify__toast-body']"
        self.forgot_password = '/html/body/div/div[2]/form/div[3]/h2'
        self.google_login_btn_xpath = '/html/body/div/div[2]/form/div[3]/div[3]/div[2]/div/img'
        self.google_input_email_xpath = "//input[@id='identifierId']"
        self.facebook_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[1]/div/img'
        self.twitter_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[3]/div/img'
        self.instagram_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[4]/div/div/img'
        self.register_user = '/html/body/div/div[2]/form/div[3]/div[5]/button'

    def email_login_input(self, register_email):
        self.driver.find_element(By.XPATH, self.email_input_field_xpath).send_keys(register_email)

    def password_login_input(self, password):
        self.driver.find_element(By.XPATH, self.password_input_field_xpath).send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def login_successfull_message(self):
        succsess = self.driver.find_element(By.XPATH, self.login_successfull_message_xpath)
        if succsess.is_displayed():
            print("login successfully")
        else:
            print("Not view message ")

    def validate_form(self):
        self.login_button()

        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except:
            return None

    def google_login_btn(self,g_email):
        self.driver.find_element(By.XPATH, self.google_login_btn_xpath).click()
        main_window_handle = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened([main_window_handle]))

        # Get all window handles
        window_handles = self.driver.window_handles

        # Switch to the new window
        for handle in window_handles:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)
                break
        select_account = self.driver.find_element(By.XPATH, "//div[contains(text(),'anuj choubey')]")
        if select_account.is_displayed():
            select_account.click()
        else:
            self.driver.find_element(By.XPATH, self.google_input_email_xpath).send_keys(g_email)
        # self.driver.find_element(By.XPATH, self.google_input_email_xpath).send_keys(g_email)

    def google_input_email(self, g_email):
        select_account = self.driver.find_element(By.XPATH, "//div[contains(text(),'anuj choubey')]")
        if select_account.is_displayed():
            select_account.click()
        else:
            self.driver.find_element(By.XPATH, self.google_input_email_xpath).send_keys(g_email)
