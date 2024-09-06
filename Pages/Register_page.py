import time
from Base.base_driver import Basedriver
from selenium.webdriver.support.ui import Select

class Register_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)

        self.page_url = 'https://cch247.com/apps'
        self.register_user = '/html/body/div/div[2]/form/div[3]/div[5]/button'
        self.name = '/html/body/div/div[2]/div/div[3]/form/div[1]/div/input'
        self.email = '/html/body/div/div[2]/div/div[3]/form/div[2]/div/input'
        self.phone = '/html/body/div/div[2]/div/div[3]/form/div[3]/div/input'
        self.address = '/html/body/div/div[2]/div/div[3]/form/div[4]/div/input'
        self.password = '/html/body/div/div[2]/div/div[3]/form/div[5]/div/input'
        self.Cpassword = '/html/body/div/div[2]/div/div[3]/form/div[6]/div/input'
        self.organizations = "/html/body/div/div[2]/div/div[3]/form/div[7]/select"
        self.profile_pic = '/html/body/div/div[2]/div/div[3]/form/div[8]/label/span[1]'
        self.categories = "/html/body/div/div[2]/div/div[3]/form/div[9]/div/div[1]/div[1]/div[1]/div[2]/input"
        self.create_acc_btn = '/html/body/div/div[2]/div/div[3]/form/button'
        self.login_here_link = '/html/body/div/div[2]/div/div[3]/form/h3/span'
        # self.profile_pic_path = "C:\Users\mohni\Downloads\flower6..jpg"
        self.req_field_message = "Please fill out this field."

    def tc28(self, name, email, phone, address, password, Cpassword):

        # Open the registration page
        self.driver.get(self.page_url)
        time.sleep(2)
        self.base.return_any("xpath", self.register_user).click()
        time.sleep(2)

        def fill_field_and_validate(field_xpath, input_value):
            # Click on create account button and validate the required field message
            self.base.return_any("xpath", self.create_acc_btn).click()
            time.sleep(2)
            field = self.base.return_any("xpath", field_xpath)
            time.sleep(2)
            validation_msg = field.get_attribute("validationMessage")
            time.sleep(2)
            assert self.req_field_message in validation_msg
            time.sleep(2)
            field.send_keys(input_value)
            time.sleep(2)

        #  Call the helper function for each field
        fill_field_and_validate(self.name, name)
        fill_field_and_validate(self.email, email)
        fill_field_and_validate(self.phone, phone)
        fill_field_and_validate(self.address, address)
        fill_field_and_validate(self.password, password)
        fill_field_and_validate(self.Cpassword, Cpassword)

        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

        organization_dropdown = self.base.return_any("xpath", self.organizations)
        organization_dropdown.click()
        time.sleep(5)
        select = Select(organization_dropdown)
        select.select_by_visible_text("Amnesty International")
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)
        # self.base.return_any("xpath", self.profile_pic).send_keys(self.profile_pic_path)
        # time.sleep(2)
        # self.base.return_any("xpath", self.categories).send_keys(category_name)
        # time.sleep(2)




    # def tc29(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path):
    #     self.driver.refresh()
    #     time.sleep(2)
    #     self.tc28(name, email, phone, address, adhaar_no, password, Cpassword)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.create_acc_btn).click()
    #     time.sleep(2)
    #
    # def tc30(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path):
    #     self.base.return_any("xpath", self.register_user).click()
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.name).send_keys(name)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.email).send_keys(email)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.phone).send_keys(phone)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.address).send_keys(address)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.password).send_keys(password)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.Cpassword).send_keys(Cpassword)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.local_cleaning).click()
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.create_acc_btn).click()
    #     time.sleep(2)
    #
    # def tc31(self, name, New_email, phone, address, adhaar_no, password, Cpassword, file_path):
    #     self.driver.refresh()
    #     time.sleep(5)
    #     self.base.return_any("xpath", self.name).send_keys(name)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.email).send_keys(New_email)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.phone).send_keys(phone)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.address).send_keys(address)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.password).send_keys(password)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.Cpassword).send_keys(Cpassword)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.local_cleaning).click()
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.create_acc_btn).click()
    #     time.sleep(2)
    #
    # def tc32(self, name, inv_email, New_phone, address, adhaar_no, password, Cpassword, file_path):
    #     self.driver.refresh()
    #     time.sleep(5)
    #     self.base.return_any("xpath", self.name).send_keys(name)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.email).send_keys(inv_email)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.phone).send_keys(New_phone)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.address).send_keys(address)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.password).send_keys(password)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.Cpassword).send_keys(Cpassword)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.local_cleaning).click()
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.create_acc_btn).click()
    #     time.sleep(2)
    #
    # def tc33(self, name, New_email1, New_phone1, address, adhaar_no, pass1, pass2, file_path):
    #     self.driver.refresh()
    #     time.sleep(5)
    #     self.base.return_any("xpath", self.name).send_keys(name)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.email).send_keys(New_email1)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.phone).send_keys(New_phone1)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.address).send_keys(address)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.password).send_keys(pass1)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.Cpassword).send_keys(pass2)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.local_cleaning).click()
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.create_acc_btn).click()
    #     time.sleep(2)
    #
    # def tc34(self, name, New_email2, New_phone2, address, adhaar_no, Weak_pass, Weak_Cpass, file_path):
    #     self.driver.refresh()
    #     time.sleep(5)
    #     self.base.return_any("xpath", self.name).send_keys(name)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.email).send_keys(New_email2)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.phone).send_keys(New_phone2)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.address).send_keys(address)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.password).send_keys(Weak_pass)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.Cpassword).send_keys(Weak_Cpass)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.local_cleaning).click()
    #     time.sleep(2)
    #     self.base.return_any("xpath", self.create_acc_btn).click()
    #     time.sleep(2)
    #
    #
    # def tc35(self):
    #     self.base.return_any("xpath", self.login_here_link).click()
    #     time.sleep(5)

    def all(self, name, email, phone, address, password, Cpassword):
        self.tc28(name, email, phone, address, password, Cpassword)



