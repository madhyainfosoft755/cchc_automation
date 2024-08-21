import  time
from  Base.base_driver import Basedriver
import  datetime
from selenium.webdriver import ActionChains
from geopy.geocoders import Nominatim

class Login_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.actions = ActionChains(self.driver)

        self.page_url = 'https://cch247.com/apps'
        self.login_btn = "/html/body/div/div[2]/form/div[3]/button"
        self.email_input_field = "//input[@placeholder='Email']"
        self.password_input_field = "//input[@placeholder='Password']"
        self.forgot_password = "//h2[normalize-space()='Forgot Password']"
        self.google_login_btn = "//img[contains(@class,'h-full w-full cursor-pointer')]"
        self.facebook_login_btn = '/html/body/div/div[2]/form/div[3]/div[3]/div[3]/div/img'
        self.linkedin_login_btn = '//*[@id="root"]/div[2]/form/div[3]/div[3]/div[2]/div/img'
        self.twitter_login = '//*[@id="root"]/div[2]/form/div[3]/div[3]/div[4]/div/img'
        self.instagram_login = '//*[@id="root"]/div[2]/form/div[3]/div[3]/div[5]/div/div/img'
        self.New_volunteer_registration = '//*[@id="root"]/div[2]/form/div[3]/div[5]/button'
        self.date_field_login_page = "/html/body/div/div[2]/form/div[3]/div[6]/button[2]/div[2]"
        self.location_field = '/html/body/div/div[2]/form/div[3]/div[6]/button[1]'
        self.login_error_xpath = '//*[@id="root"]/div[2]/form/div[3]/div[3]/span[1]'
        self.invalid_pass_err = "//span[contains(@class,'block sm:inline py-2 text-xs')]"
        self.req_field_message = "Please fill out this field."
        self.expected_url_after_login = "https://cch247.com/apps/create"
        self.welcome_txt1 = "//p[normalize-space()='Welcome to CCH247 (Community Care 247)']"
        self.welcome_txt2 = '//*[@id="root"]/div[2]/form/div[3]/p[2]'
        self.hindi_txt = '//*[@id="root"]/div[2]/form/div[3]/p[3]'
        self.forgot_pass_page_url = "https://cch247.com/apps/forget"
        self.eye_btn_pass_field = '.svg-inline--fa.fa-eye.text-gray-700.cursor-pointer'

    def tc2(self):
        self.driver.get(self.page_url)
        time.sleep(2)
        email_element = self.base.return_any("xpath", self.email_input_field)
        email_element.clear()
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        # print(f"Email validation message: {email_validation_message}")
        email_validation_message = email_element.get_attribute("validationMessage")
        assert self.req_field_message in email_validation_message
        time.sleep(8)

    def tc3(self, email):
        self.base.return_any("xpath", self.email_input_field).send_keys(email)
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        time.sleep(2)
        password_element = self.base.return_any("xpath", self.password_input_field)
        password_validation_message = password_element.get_attribute("validationMessage")
        assert self.req_field_message in password_validation_message
        time.sleep(5)

    def tc4(self, password):
        email_element = self.base.return_any("xpath", self.email_input_field)
        email_element.clear()
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        time.sleep(2)
        email_validation_message = email_element.get_attribute("validationMessage")
        assert self.req_field_message in email_validation_message
        time.sleep(2)

    def tc5(self, Wemail, password):
        self.base.return_any("xpath", self.email_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.email_input_field).send_keys(Wemail)
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        time.sleep(2)
        presense_check = self.base.is_element_present("xpath", self.login_error_xpath)
        if presense_check:
            assert True
        else:
            assert False
        time.sleep(8)

    def tc6(self, Cemail, Wpassword):
        self.base.return_any("xpath", self.email_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.email_input_field).send_keys(Cemail)
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).send_keys(Wpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        presence_check = self.base.is_element_present("xpath", self.invalid_pass_err)
        if presence_check:
            assert True
        else:
            assert False
        time.sleep(5)

    def tc7(self, Cemail, Cpass):
        self.base.return_any("xpath", self.email_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.email_input_field).send_keys(Cemail)
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).clear()
        time.sleep(2)
        self.base.return_any("xpath", self.password_input_field).send_keys(Cpass)
        time.sleep(2)
        self.base.return_any("xpath", self.login_btn).click()
        time.sleep(8)
        current_url = self.driver.current_url
        if current_url == self.expected_url_after_login:
            assert True
        else:
            assert False
        time.sleep(5)

    def tc8(self):
        self.driver.get(self.page_url)
        time.sleep(2)
        presence_check1 = self.base.is_element_present("xpath", self.welcome_txt1)
        presence_check2 = self.base.is_element_present("xpath", self.welcome_txt2)
        if presence_check1 and presence_check2:
            assert True
        else:
            assert False

    def tc9(self):
        presence_check = self.base.is_element_present("xpath", self.hindi_txt)
        if presence_check:
            assert True
        else:
            assert False

    def tc10(self):
        self.base.return_any("xpath", self.forgot_password).click()
        time.sleep(5)
        current_url = self.driver.current_url
        if current_url == self.forgot_pass_page_url:
            assert True
        else:
            assert False

    def tc11(self):
        self.driver.get(self.page_url)
        time.sleep(2)
        original_window = self.driver.current_window_handle
        window_before_click = self.driver.window_handles
        self.base.return_any("xpath", self.google_login_btn).click()
        time.sleep(2)
        window_after_click = self.driver.window_handles
        new_window = None
        for window in window_after_click:
            if window not in window_before_click:
                new_window = window
                break

        if new_window:
            self.driver.switch_to.window(new_window)
        else:
            print("No new window opened")
            return False

        try:
            page_source = self.driver.page_source
            if "Sign in with Google" in page_source:
                assert True
            else:
                assert False
        finally:
            self.driver.close()
            self.driver.switch_to.window(original_window)

    def tc12(self):
        self.driver.refresh()
        time.sleep(2)
        facebook_icon = self.base.return_any("xpath", self.facebook_login_btn)
        linkedin_icon = self.base.return_any("xpath", self.linkedin_login_btn)
        instagram_icon = self.base.return_any("xpath", self.instagram_login)
        twitter_icon = self.base.return_any("xpath", self.twitter_login)
        google_icon = self.base.return_any("xpath", self.google_login_btn)

        # print(facebook_icon.get_attribute('class'))
        icons = [facebook_icon, linkedin_icon, instagram_icon, twitter_icon]

        for icon in icons:
            class_attribute = icon.get_attribute('class')
            is_disable = 'filter grayscale' in class_attribute
            # print(is_disable)
            if is_disable:
                assert True
        class_attribute = google_icon.get_attribute('class')
        is_enalbe = 'cursor-pointer' in class_attribute
        if is_enalbe:
            assert True

    def tc13(self):
        self.base.return_any("xpath", self.New_volunteer_registration).click()
        time.sleep(2)
        page_source = self.driver.page_source
        if "Create an account to access all features" in page_source:
            assert True
            time.sleep(3)

    def get_current_location(self):
        geolocator = Nominatim(user_agent="geoapiExercises")
        latitude = "23.855990"
        longitude = "78.783640"
        location = geolocator.reverse(f"{latitude}, {longitude}")
        address = location.raw['address']
        city = address.get('city', '')
        state = address.get('state', '')
        return city, state

    def tc14(self):
        current_city, current_state = self.get_current_location()
        location_field = self.base.return_any("xpath", self.location_field)
        location_text = location_field.text

        if current_city in location_text and current_state in location_text:
            assert True
        else:
            print(f"Location field text: {location_text}")
            print(f"Expected City: {current_city}, State: {current_state}")
            assert False

    def tc15(self):
        date_field_txt = self.base.return_any("xpath", self.date_field_login_page).text
        todays_date = datetime.datetime.now().strftime('%d %b %Y')
        if date_field_txt == todays_date:
            print("Date field is displaying today's date")
            assert True
        else:
            print(f'Expected date {todays_date} but found {date_field_txt}')
            assert False

    def tc16(self):
        self.driver.refresh()
        #  ActionChains to perform mouse hover
        email_field = self.base.return_any("xpath", self.email_input_field)
        password_filed = self.base.return_any("xpath", self.password_input_field)

        #  List of fields to check
        fields = [email_field, password_filed]

        # Expected cursors
        # expected_cursors = ["text", "pointer", "not-allowed"]

        for field in fields:
            self.actions.move_to_element(field).perform()
            time.sleep(2)
            cursor_style = field.value_of_css_property('cursor')
            if cursor_style == "text":
                assert True
            else:
                assert False

    def tc17(self):
        eye_btn = self.base.return_any("css", self.eye_btn_pass_field)
        filed = eye_btn
        cursor_style = filed.value_of_css_property('cursor')
        print(cursor_style)
        if cursor_style == "pointer":
            assert True
        else:
            assert False

    def tc18(self):
        login_btn = self.base.return_any("xpath", self.login_btn)
        field = login_btn
        cursor_style = field.value_of_css_property("cursor")
        if cursor_style == "pointer":
            assert True
        else:
            assert False

    def tc19(self):
        forgot_pass = self.base.return_any("xpath", self.forgot_password)
        field = forgot_pass
        cursor_style = field.value_of_css_property("cursor")
        if cursor_style == "pointer":
            assert True
        else:
            assert False

    def tc20(self):
        google_icon = self.base.return_any("xpath", self.google_login_btn)
        field = google_icon
        cursor_style = field.value_of_css_property("cursor")
        if cursor_style == "pointer":
            assert True
        else:
            assert False

    def tc21(self):
        facebook_icon = self.base.return_any("xpath", self.facebook_login_btn)
        linkedin_icon = self.base.return_any("xpath", self.linkedin_login_btn)
        instagram_icon = self.base.return_any("xpath", self.instagram_login)
        twitter_icon = self.base.return_any("xpath", self.twitter_login)

        fields = [facebook_icon, linkedin_icon, instagram_icon, twitter_icon]

        for field in fields:
            self.actions.move_to_element(field).perform()
            time.sleep(2)
            cursor_style = field.value_of_css_property('cursor')
            if cursor_style == "not-allowed":
                assert True
            else:
                assert False

    def tc22(self):
        register_user = self.base.return_any("xpath", self.New_volunteer_registration)
        field = register_user
        cursor_style = field.value_of_css_property("cursor")
        if cursor_style == "pointer":
            assert True
        else:
            assert False

    def tc23(self):
        date_field = self.base.return_any("xpath", self.date_field_login_page)
        location_field = self.base.return_any("xpath", self.location_field)

        fields = [date_field, location_field]

        for field in fields:
            self.actions.move_to_element(field).perform()
            time.sleep(2)
            cursor_style = field.value_of_css_property('cursor')
            if cursor_style == "default":
                assert True
            else:
                assert False

    def tc24(self, Cemail, Cpassword):
        email_field = self.base.return_any("xpath", self.email_input_field)
        password_field = self.base.return_any("xpath", self.password_input_field)
        eye_btn = self.base.return_any("css", self.eye_btn_pass_field)
        attribute_val = password_field.get_attribute('type')

        email_field.send_keys(Cemail)
        time.sleep(2)
        password_field.send_keys(Cpassword)
        time.sleep(4)

        assert  attribute_val == "password", "Password field should be initially hidden"
        eye_btn.click()
        time.sleep(5)
        assert attribute_val == "text", "Password field should be visible after clicking the eye button"
        time.sleep(2)
        eye_btn.click()
        time.sleep(5)
        assert attribute_val == "password", "Password field should be hidden after clicking the eye button again"

    def all(self, email, password, Wemail, Cemail, Wpassword, Cpassword):
        self.tc2()
        self.tc3(email)
        self.tc4(password)
        self.tc5(Wemail, password)
        self.tc6(Cemail, Wpassword)
        self.tc7(Cemail, Cpassword)
        self.tc8()
        self.tc9()
        self.tc10()
        self.tc11()
        self.tc12()
        # self.tc14()
        self.tc15()
        self.tc16()
        self.tc17()
        self.tc18()
        self.tc19()
        self.tc20()
        self.tc21()
        self.tc22()
        self.tc23()
        self.tc24()



