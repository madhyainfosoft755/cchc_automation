import time
from Base.base_driver import Basedriver
from Pages.Login import Login_page_code
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class manage_category_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.login = Login_page_code()

        self.plus_icon = '/html/body/div/div[2]/div/div[1]/div/button/svg'
        self.category_input_field = '/html/body/div/div[2]/div/div[1]/div[2]/div/input'
        self.check_btn = '/html/body/div/div[2]/div/div[1]/div[2]/div/svg/path'
        self.back_btn = '/html/body/div/div[2]/div/div[1]/div/div/img'
        self.manage_cat_btn = "/html/body/div/div[2]/div/div/div[3]/div[1]/div[2]"
        self.error_msg_req_field = '/html/body/div/div[2]/div/div[1]/div[2]/small'
        self.btn1 = '/html/body/div/div[2]/div/div[2]/div[1]/button'
        self.btn2 = '/html/body/div/div[2]/div/div[2]/div[2]/button'
        self.btn3 = '/html/body/div/div[2]/div/div[2]/div[3]/button'
        self.btn4 = '/html/body/div/div[2]/div/div[2]/div[4]/button'
        self.btn5 = '/html/body/div/div[2]/div/div[2]/div[5]/button'
    def tc90(self, Cemail, Cpassword):
        self.login.tc5(Cemail, Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.manage_cat_btn).click()
        time.sleep(2)
        self.base.return_any("xpath", self.plus_icon).click()
        time.sleep(2)
        input_field = self.base.return_any("xpath", self.category_input_field)
        if input_field.is_displayed():
            print("Plus icon is working fine")
            assert True
        else:
            print("Plus icon is not working")
            assert False

    def tc91(self):
        self.base.return_any("xpath", self.check_btn).click()
        time.sleep(2)
        error_msg = self.base.return_any("xpath", self.error_msg_req_field)
        if error_msg.is_displayed():
            print("Check button is displaying error message of necessary field when user not giving category name")
            assert True
        else:
            print("Error message of necessary field is not present")
            assert False

    def tc92(self, cat_name):
        self.base.return_any("xpath", self.category_input_field).send_keys(cat_name)
        time.sleep(2)
        self.base.return_any("xpath", self.check_btn).click()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        body = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        if cat_name in body.text:
            print("Category added sucessfully")
            assert True
        else:
            print("Category is not added")
            assert False











