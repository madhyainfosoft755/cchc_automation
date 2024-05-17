import time
from selenium.webdriver.common.by import By
from cchc_automation.pythonProject2.Base.base_driver import Basedriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
import time
from datetime import datetime


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)

        self.page_url = 'https://ccsc.helpersin.com/'
        self.login_btn_xpath = "//button[contains(text(),'Login')]"
        self.email_input_field_xpath = '/html/body/div/div[2]/form/div[3]/div[1]/input'
        self.password_input_field_xpath = '/html/body/div/div[2]/form/div[3]/div[2]/input'
        self.login_successfull_message_xpath = "//div[@class = 'Toastify__toast-body']"
        self.forgot_password_xpath = '/html/body/div/div[2]/form/div[3]/h2'
        self.google_login_btn_xpath = '/html/body/div/div[2]/form/div[3]/div[3]/div[2]/div/img'
        self.google_input_email_xpath = "//input[@id='identifierId']"
        self.google_next_btn_xpath = "//span[contains(text(),'Next')]"
        self.google_password_input_xpath = "//input[@name='Passwd']"
        self.facebook_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[1]/div/img'
        self.twitter_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[3]/div/img'
        self.instagram_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[4]/div/div/img'
        self.register_user = '/html/body/div/div[2]/form/div[3]/div[5]/button'
        self.forgot_email_input_xpath = "//body/div[@id='root']/div[2]/div[1]/div[3]/div[1]/input[1]"
        self.send_pin_btn_xpath = "//button[contains(text(),'Send PIN')]"
        self.date_element_xpath = "//div[contains(text(),'17 May 2024')]"
        self.location_compare_xpath = "//body/div[@id='root']/div[2]/form[1]/div[3]/div[6]/button[1]/div[2]"

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

    def find_and_click(self, xpath):
        for xpath in xpath:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                element.click()
                print(f"Clicked on element with XPath: {xpath}")
                return True
            except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                print(f"Element not interactable or not found: {xpath}")
                continue
        return False

    def google_login_btn(self, g_email, g_password):
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

        self.driver.find_element(By.XPATH, self.google_input_email_xpath).send_keys(g_email)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.google_next_btn_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.google_password_input_xpath).send_keys(g_password)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.google_next_btn_xpath).click()
        time.sleep(5)

    def forgot_password(self, registered_email):
        self.driver.find_element(By.XPATH, self.forgot_password_xpath).click()
        time.sleep(2)
        email = self.driver.find_element(By.XPATH, self.forgot_email_input_xpath)
        email.send_keys(registered_email)
        self.driver.find_element(By.XPATH, self.send_pin_btn_xpath).click()
        time.sleep(5)

    def date_time_compare(self):
        date_element = self.driver.find_element(By.XPATH, self.date_element_xpath)
        page_date_str = date_element.text.strip()
        try:
            page_date = datetime.strptime(page_date_str, "%d %B %Y")
        except ValueError as e:
            print(f"Error parsing date: {e}")

        current_date = datetime.now()

        if page_date.date() == current_date.date():
            print("Page ki date aaj ki hai.")
        elif page_date.date() > current_date.date():
            print("Page ki date future ki hai.")
        else:
            print("Page ki date past ki hai.")

    def get_current_location(self):
        # Retrieve the user's current location using JavaScript
        user_latitude = self.driver.execute_script(
            "return navigator.geolocation.getCurrentPosition(function(position) {return position.coords.latitude});")
        user_longitude = self.driver.execute_script(
            "return navigator.geolocation.getCurrentPosition(function(position) {return position.coords.longitude});")
        return user_latitude, user_longitude

    def location_compare(self):
        # Retrieve the current location displayed on the webpage
        page_location = self.driver.find_element(By.XPATH, self.location_compare_xpath)
        page_location_str = page_location.text.strip()
        print("Location on the page:", page_location_str)

        # Retrieve the user's current location
        user_latitude, user_longitude = self.get_current_location()
        print("Current location:", user_latitude, user_longitude)
