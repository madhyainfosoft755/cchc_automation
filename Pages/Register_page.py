import time
from Base.base_driver import Basedriver

class Register_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)

        self.page_url = 'https://ccsc.helpersin.com/'
        self.register_user = '/html/body/div/div[2]/form/div[3]/div[5]/button'
        self.name = '/html/body/div[1]/div[2]/div/div[3]/form/div[1]/div/input'
        self.email = '/html/body/div[1]/div[2]/div/div[3]/form/div[2]/div/input'
        self.phone = '/html/body/div[1]/div[2]/div/div[3]/form/div[3]/div/input'
        self.address = '/html/body/div[1]/div[2]/div/div[3]/form/div[4]/div/input'
        self.adhar_no = '/html/body/div[1]/div[2]/div/div[3]/form/div[5]/div/input'
        self.password = '/html/body/div[1]/div[2]/div/div[3]/form/div[6]/div/input'
        self.Cpassword = '/html/body/div[1]/div[2]/div/div[3]/form/div[7]/div/input'
        self.profile_pic = '/html/body/div[1]/div[2]/div/div[3]/form/div[8]/div/input'
        self.planting_tree = '/html/body/div[1]/div[2]/div/div[3]/form/div[9]/div[1]/input'
        self.teaching_kids = '/html/body/div[1]/div[2]/div/div[3]/form/div[9]/div[2]/input'
        self.feeding_poor = '/html/body/div[1]/div[2]/div/div[3]/form/div[9]/div[3]/input'
        self.local_cleaning = '/html/body/div[1]/div[2]/div/div[3]/form/div[9]/div[4]/input'
        self.blood_donation = '/html/body/div[1]/div[2]/div/div[3]/form/div[9]/div[5]/input'
        self.running_marathon  = '/html/body/div[1]/div[2]/div/div[3]/form/div[9]/div[6]/input'
        self.create_acc_btn = '/html/body/div[1]/div[2]/div/div[3]/form/button'
        self.login_here_link = '/html/body/div[1]/div[2]/div/div[3]/form/h3/span'

    def tc28(self, name, email, phone, address, adhaar_no, password, Cpassword):
        self.driver.get(self.page_url)
        time.sleep(2)
        self.base.return_any("xpath", self.register_user).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)
        self.base.return_any("xpath", self.name).send_keys(name)
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)
        self.base.return_any("xpath", self.email).send_keys(email)
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)
        self.base.return_any("xpath", self.phone).send_keys(phone)
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)
        self.base.return_any("xpath", self.address).send_keys(address)
        time.sleep(2)
        self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.Cpassword).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc29(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path):
        self.driver.refresh()
        time.sleep(2)
        self.tc28(name, email, phone, address, adhaar_no, password, Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc30(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path):
        self.base.return_any("xpath", self.register_user).click()
        time.sleep(2)
        self.base.return_any("xpath", self.name).send_keys(name)
        time.sleep(2)
        self.base.return_any("xpath", self.email).send_keys(email)
        time.sleep(2)
        self.base.return_any("xpath", self.phone).send_keys(phone)
        time.sleep(2)
        self.base.return_any("xpath", self.address).send_keys(address)
        time.sleep(2)
        self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.Cpassword).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc31(self, name, New_email, phone, address, adhaar_no, password, Cpassword, file_path):
        self.driver.refresh()
        time.sleep(5)
        self.base.return_any("xpath", self.name).send_keys(name)
        time.sleep(2)
        self.base.return_any("xpath", self.email).send_keys(New_email)
        time.sleep(2)
        self.base.return_any("xpath", self.phone).send_keys(phone)
        time.sleep(2)
        self.base.return_any("xpath", self.address).send_keys(address)
        time.sleep(2)
        self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.Cpassword).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc32(self, name, inv_email, New_phone, address, adhaar_no, password, Cpassword, file_path):
        self.driver.refresh()
        time.sleep(5)
        self.base.return_any("xpath", self.name).send_keys(name)
        time.sleep(2)
        self.base.return_any("xpath", self.email).send_keys(inv_email)
        time.sleep(2)
        self.base.return_any("xpath", self.phone).send_keys(New_phone)
        time.sleep(2)
        self.base.return_any("xpath", self.address).send_keys(address)
        time.sleep(2)
        self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.Cpassword).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc33(self, name, New_email1, New_phone1, address, adhaar_no, pass1, pass2, file_path):
        self.driver.refresh()
        time.sleep(5)
        self.base.return_any("xpath", self.name).send_keys(name)
        time.sleep(2)
        self.base.return_any("xpath", self.email).send_keys(New_email1)
        time.sleep(2)
        self.base.return_any("xpath", self.phone).send_keys(New_phone1)
        time.sleep(2)
        self.base.return_any("xpath", self.address).send_keys(address)
        time.sleep(2)
        self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(pass1)
        time.sleep(2)
        self.base.return_any("xpath", self.Cpassword).send_keys(pass2)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc34(self, name, New_email2, New_phone2, address, adhaar_no, Weak_pass, Weak_Cpass, file_path):
        self.driver.refresh()
        time.sleep(5)
        self.base.return_any("xpath", self.name).send_keys(name)
        time.sleep(2)
        self.base.return_any("xpath", self.email).send_keys(New_email2)
        time.sleep(2)
        self.base.return_any("xpath", self.phone).send_keys(New_phone2)
        time.sleep(2)
        self.base.return_any("xpath", self.address).send_keys(address)
        time.sleep(2)
        self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(Weak_pass)
        time.sleep(2)
        self.base.return_any("xpath", self.Cpassword).send_keys(Weak_Cpass)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)


    def tc35(self):
        self.base.return_any("xpath", self.login_here_link).click()
        time.sleep(5)

    def all(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path, New_email, inv_email, New_phone, New_email1, New_phone1, pass1, pass2, New_email2, New_phone2, Weak_pass, Weak_Cpass, New_email3, New_phone3, short_pass, short_Cpass):
        self.tc28(name, email, phone, address, adhaar_no, password, Cpassword)
        self.tc29(name, email, phone, address, adhaar_no, password, Cpassword, file_path)
        self.tc30(name, email, phone, address, adhaar_no, password, Cpassword, file_path)
        self.tc31(name, New_email, phone, address, adhaar_no, password, Cpassword, file_path)
        self.tc32(name, inv_email, New_phone, address, adhaar_no, password, Cpassword, file_path)
        self.tc33(name, New_email1, New_phone1, address, adhaar_no, pass1, pass2, file_path)
        self.tc34(name, New_email2, New_phone2, address, adhaar_no, Weak_pass, Weak_Cpass, file_path)
        self.tc35()


