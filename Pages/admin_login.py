import time
from Base.base_driver import Basedriver
from  Pages.Login import Login_page_code
from  Pages.create_activity_page import Create_activity_page_code


class admin_login_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.login_page_code = Login_page_code(self.driver)


        self.profile_pic = '/html/body/div/div[2]/div/div/div[1]/div/img'
        self.username = '/html/body/div/div[2]/div/div/div[1]/div/div/div/p'
        self.logout = '/html/body/div/div[2]/div/div/div[1]/button'
        self.approve_hours = '/html/body/div/div[2]/div/div/div[3]/div[1]/div[1]'
        self.manage_category = '/html/body/div/div[2]/div/div/div[3]/div[1]/div[2]'
        self.manage_approvers = '/html/body/div/div[2]/div/div/div[3]/div[1]/div[3]'
        self.manage_users = '/html/body/div/div[2]/div/div/div[3]/div[1]/div[4]'
        self.manage_org = '/html/body/div/div[2]/div/div/div[3]/div[1]/div[5]'
        self.generate_report = '/html/body/div/div[2]/div/div/div[3]/div[2]/button[1]'
        self.login_btn = "/html/body/div/div[2]/form/div[3]/button"
        self.approve_hours_txt = '/html/body/div/div[2]/div/div[1]/p'
        self.back_btn_approve_page = '/html/body/div/div[2]/div/div[1]/div/img'
        self.manage_cat_txt = '/html/body/div/div[2]/div/div[1]/div/p'
        self.manage_approver_txt = '/html/body/div/div[2]/div/div[1]/p'
        self.manage_users_txt = '/html/body/div/div[2]/div/div[1]/p'
        self.manage_org_txt = '/html/body/div/div[2]/div/div[1]/div/p'
        self.generate_report_txt = '/html/body/div/div[2]/div/div[1]/p'
        self.back_btn_manage_cat = '/html/body/div/div[2]/div/div[1]/div/div/img'
        self.back_btn_manage_approver = '/html/body/div/div[2]/div/div[1]/div/img'
        self.back_btn_manage_users = '/html/body/div/div[2]/div/div[1]/div/img'
        self.back_btn_manage_org = '/html/body/div/div[2]/div/div[1]/div/div/img'
    def tc74(self, Cemail, Cpassword):
        self.login_page_code.tc5(Cemail, Cpassword)
        time.sleep(2)
        profile_pic = self.base.return_any("xpath", self.profile_pic)
        if profile_pic.is_displayed():
            print("Profile picture of user is present")
            assert True
        else:
            print("Profile picture is not present")
            assert False

    def tc75(self):
        username = self.base.return_any("xpath", self.username)
        if username.is_displayed():
            print("Username is present on the page")
            assert True
        else:
            print("Username is not present")
            assert False


    def tc76(self):
        self.base.return_any("xpath", self.logout).click()
        time.sleep(2)
        login_btn = self.base.return_any("xpath", self.login_btn)
        if login_btn.is_displayed():
            assert True
            print("Logout button is working fine")
        else:
            print("Logout button is not working")
            assert False

    def tc77(self, Cemail, Cpassword):
        self.login_page_code.tc5(Cemail, Cpassword)
        time.sleep(2)
        self.base.return_any("xpath", self.approve_hours).click()
        time.sleep(5)
        approve_hours_txt = self.base.return_any("xpath", self.approve_hours_txt)
        if approve_hours_txt.is_displayed():
            print("Approve hours button is working fine")
            assert True
        else:
            print("Approve hours button is not working")
            assert False
        time.sleep(5)

    def tc97(self):
        self.base.return_any("xpath", self.back_btn_approve_page).click()
        time.sleep(2)
        approve_hours_btn = self.base.return_any("xpath", self.approve_hours)
        if approve_hours_btn.is_displayed():
            print("Back button is working fine")
            assert True
        else:
            print("Back button is not working")
            assert False
        time.sleep(5)

    def tc78(self):
        self.base.return_any("xpath", self.manage_category).click()
        time.sleep(2)
        manage_cat_txt = self.base.return_any("xpath", self.manage_cat_txt)
        if manage_cat_txt.is_displayed():
            print("Manage categories button is working fine")
            assert True
        else:
            print("Manage category button is not working")
            assert False

    def tc96(self):
        self.base.return_any("xpath", self.back_btn_manage_cat).click()
        time.sleep(2)
        manage_cat_btn = self.base.return_any("xpath", self.manage_category)
        if manage_cat_btn.is_displayed():
            print("Back button is working fine")
            assert True
        else:
            print("Back button is not working")
            assert False
        time.sleep(5)

    def tc79(self):
        self.base.return_any("xpath", self.manage_approvers).click()
        time.sleep(2)
        manage_approver_txt = self.base.return_any("xpath", self.manage_approver_txt)
        if manage_approver_txt.is_displayed():
            print("Manage approvers button is working fine")
            assert True
        else:
            print("Manage approvers button is not working")

    def tc98(self):
        self.base.return_any("xpath", self.back_btn_manage_approver).click()
        time.sleep(5)
        manage_approver_btn = self.base.return_any("xpath", self.manage_approvers)
        if manage_approver_btn.is_displayed():
            print("Back button is working fine")
            assert True
        else:
            print("Back button is not working")
            assert False

    def tc80(self):
        self.base.return_any("xpath", self.manage_users).click()
        time.sleep(2)
        manage_user_txt = self.base.return_any("xpath", self.manage_users_txt)
        if manage_user_txt.is_displayed():
            print("Manage user button is working fine")
            assert True
        else:
            print("Manage user button is not working")
            assert False

    def tc99(self):
        self.base.return_any("xpath", self.back_btn_manage_users).click()
        time.sleep(2)
        manage_user_btn = self.base.return_any("xpath", self.manage_users)
        if manage_user_btn.is_displayed():
            print("Back button is working fine")
            assert True
        else:
            print("Back button is not working")
            assert False

    def tc81(self):
        self.base.return_any("xpath", self.manage_org).click()
        time.sleep(2)
        manage_org_txt = self.base.return_any("xpath", self.manage_org_txt)
        if manage_org_txt.is_displayed():
            print("Manage organizatioin button is working fine")
            assert True
        else:
            print("Manage organization button is not working")
            assert False
        time.sleep(5)

    def tc100(self):
        self.base.return_any("xpath", self.back_btn_manage_org).click()
        time.sleep(2)
        manage_org_btn = self.base.return_any("xpath", self.manage_org)
        if manage_org_btn.is_displayed():
            print("Back button is working fine")
            assert True
        else:
            print("Back button is not working")
            assert False

    def tc82(self):
        self.base.return_any("xpath", self.generate_report).click()
        time.sleep(2)
        Generate_report_txt = self.base.return_any("xpath", self.generate_report_txt)
        if Generate_report_txt.is_displayed():
            print("Generate report button is working fine")
            assert True
        else:
            print("Generate report button is not working")
            assert False

    def all(self, Cemail, Cpassword):
        self.tc74(Cemail, Cpassword)
        self.tc75()
        self.tc76()
        self.tc77(Cemail, Cpassword)
        self.tc97()
        self.tc78()
        self.tc96()
        self.tc79()
        self.tc98()
        self.tc80()
        self.tc99()
        self.tc81()
        self.tc100()
        self.tc82()
