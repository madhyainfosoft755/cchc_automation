import time
from Base.base_driver import Basedriver

class Create_activity_page_code:

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
        self.base.return_any("xpath", self.password).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc29(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path):
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
        self.base.return_any("xpath", self.password).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc30(self, name, Reg_email, phone, address, adhaar_no, password, Cpassword, file_path):
        self.base.return_any("xpath", self.register_user).click()
        time.sleep(2)
        self.base.return_any("xpath", self.name).send_keys(name)
        time.sleep(2)
        self.base.return_any("xpath", self.email).send_keys(Reg_email)
        time.sleep(2)
        self.base.return_any("xpath", self.phone).send_keys(phone)
        time.sleep(2)
        self.base.return_any("xpath", self.address).send_keys(address)
        time.sleep(2)
        self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc31(self, name, email, reg_phone, address, adhaar_no, password, Cpassword, file_path):
        self.base.return_any("xpath", self.register_user).click()
        time.sleep(2)
        self.base.return_any("xpath", self.name).send_keys(name)
        time.sleep(2)
        self.base.return_any("xpath", self.email).send_keys(email)
        time.sleep(2)
        self.base.return_any("xpath", self.phone).send_keys(reg_phone)
        time.sleep(2)
        self.base.return_any("xpath", self.address).send_keys(address)
        time.sleep(2)
        self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc32(self, name, inv_email, phone, address, adhaar_no, password, Cpassword, file_path):
        self.base.return_any("xpath", self.register_user).click()
        time.sleep(2)
        self.base.return_any("xpath", self.name).send_keys(name)
        time.sleep(2)
        self.base.return_any("xpath", self.email).send_keys(inv_email)
        time.sleep(2)
        self.base.return_any("xpath", self.phone).send_keys(phone)
        time.sleep(2)
        self.base.return_any("xpath", self.address).send_keys(address)
        time.sleep(2)
        self.base.return_any("xpath", self.adhar_no).send_keys(adhaar_no)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(password)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc33(self, name, email, phone, address, adhaar_no, pass1, pass2, file_path):
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
        self.base.return_any("xpath", self.password).send_keys(pass1)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(pass2)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc35(self, name, email, phone, address, adhaar_no, short_pass, short_Cpass, file_path):
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
        self.base.return_any("xpath", self.password).send_keys(short_pass)
        time.sleep(2)
        self.base.return_any("xpath", self.password).send_keys(short_Cpass)
        time.sleep(2)
        self.base.return_any("xpath", self.profile_pic).send_keys(file_path)
        time.sleep(2)
        self.base.return_any("xpath", self.local_cleaning).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_acc_btn).click()
        time.sleep(2)

    def tc36(self):
        self.base.return_any("xpath", self.login_here_link).click()
        time.sleep(5)

    def all(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path, Reg_email, reg_phone, inv_email, pass1, pass2, short_pass, short_Cpass):
        self.tc28(name, email, phone, address, adhaar_no, password, Cpassword)
        self.tc29(name, email, phone, address, adhaar_no, password, Cpassword, file_path)
        self.tc30(name, Reg_email, phone, address, adhaar_no, password, Cpassword, file_path)
        self.tc31(name, email, reg_phone, address, adhaar_no, password, Cpassword, file_path)
        self.tc32(name, inv_email, phone, address, adhaar_no, password, Cpassword)
        self.tc33(name, email, phone, address, adhaar_no, pass1, pass2, file_path)
        self.tc35(name, email, phone, address, adhaar_no, short_pass, short_Cpass, file_path)
        self.tc36()
