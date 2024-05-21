import pytest
import  softest
from  Pages.Login import Login_page_code
from  Pages.forgot_password_page import forgot_password_page_code
from  Pages.create_activity_page import Create_activity_page_code
from  Pages.Register_page import Register_page_code
from  Pages.Activities_page import activities_page_code
from  ddt import ddt,data,unpack
from  Utilities.utilities import utilities

@pytest.mark.usefixtures("setup")
@ddt
class Test_all_page_automation(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login_page_code = Login_page_code(self.driver)
        self.forgot_pass_page_code = forgot_password_page_code(self.driver)
        self.create_act_page = Create_activity_page_code(self.driver)
        self.activity_page = activities_page_code(self.driver)
        self.register_page = Register_page_code(self.driver)

    @pytest.mark.run(order=1)
    def test_tc1(self):
        self.login_page_code.tc1()

    @pytest.mark.run(order=2)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\login_page\\tc2.xlsx", "Sheet1"))
    @unpack
    def test_tc2(self, email):
        self.login_page_code.tc2(email)

    @pytest.mark.run(order=3)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\login_page\\tc3.xlsx", "Sheet1"))
    @unpack
    def test_tc3(self, password):
        self.login_page_code.tc3(password)

    @pytest.mark.run(order=4)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\login_page\\tc4.xlsx", "Sheet1"))
    @unpack
    def test_tc4(self, email,password):
        self.login_page_code.tc4(email, password)

    @pytest.mark.run(order=5)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\login_page\\tc5.xlsx", "Sheet1"))
    @unpack
    def test_tc5(self, Cemail, Cpassword):
        self.login_page_code.tc5(Cemail, Cpassword)

    @pytest.mark.run(order=6)
    def test_tc6(self):
        self.login_page_code.tc6()

    @pytest.mark.run(order=7)
    def test_tc7(self):
        self.login_page_code.tc7()

    @pytest.mark.run(order=8)
    def test_tc9(self):
        self.login_page_code.tc9()

    @pytest.mark.run(order=9)
    def test_tc10(self):
        self.login_page_code.tc10()

    @pytest.mark.run(order=10)
    def test_tc11(self):
        self.login_page_code.tc11()

    @pytest.mark.run(order=11)
    def test_tc8(self):
        self.login_page_code.tc8()

    @pytest.mark.run(order=12)
    def test_tc14(self):
        self.forgot_pass_page_code.tc14()

    @pytest.mark.run(order=13)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass_page\\tc15.xlsx", "Sheet1"))
    @unpack
    def test_tc15(self, Wemail):
        self.forgot_pass_page_code.tc15(Wemail)

    @pytest.mark.run(order=14)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass_page\\tc16.xlsx", "Sheet1"))
    @unpack
    def test_tc16(self, Cemail):
        self.forgot_pass_page_code.tc16(Cemail)


    @pytest.mark.run(order=15)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass_page\\tc15_16.xlsx", "Sheet1"))
    @unpack
    def test_tc19(self):
        self.forgot_pass_page_code.tc19()

    @pytest.mark.run(order=16)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass_page\\tc20.xlsx", "Sheet1"))
    @unpack
    def test_tc20(self, Wpin):
        self.forgot_pass_page_code.tc20(Wpin)

    @pytest.mark.run(order=17)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass_page\\tc20.xlsx", "Sheet1"))
    @unpack
    def test_tc21(self):
        self.forgot_pass_page_code.tc21()

    @pytest.mark.run(order=18)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass_page\\tc20.xlsx", "Sheet1"))
    @unpack
    def test_tc23(self):
        self.forgot_pass_page_code.tc23()

    @pytest.mark.run(order=19)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass_page\\tc20.xlsx", "Sheet1"))
    @unpack
    def test_tc24(self, pass1, pass2):
        self.forgot_pass_page_code.tc24(pass1, pass2)

    @pytest.mark.run(order=20)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass_page\\tc20.xlsx", "Sheet1"))
    @unpack
    def test_tc25(self, password):
        self.forgot_pass_page_code.tc25(password)

    @pytest.mark.run(order=21)
    def test_tc18(self):
        self.forgot_pass_page_code.tc18()

    @pytest.mark.run(order=22)
    def test_tc22(self, Cemail):
        self.forgot_pass_page_code.tc22(Cemail)

    @pytest.mark.run(order=23)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass_page\\tc20.xlsx", "Sheet1"))
    @unpack
    def test_tc27(self, Cemail):
        self.forgot_pass_page_code.tc27(Cemail)

    @pytest.mark.run(order=24)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Create Activity page\\tc36.xlsx", "Sheet1"))
    @unpack
    def test_tc36(self, Cemail, Cpassword):
        self.create_act_page.tc36(Cemail, Cpassword)

    @pytest.mark.run(order=25)
    def test_tc38(self):
        self.create_act_page.tc38()

    @pytest.mark.run(order=26)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Create Activity page\\tc39.xlsx", "Sheet1"))
    @unpack
    def test_tc39(self, Cemail, Cpassword):
        self.create_act_page.tc39(Cemail, Cpassword)

    @pytest.mark.run(order=27)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Create Activity page\\tc37.xlsx", "Sheet1"))
    @unpack
    def test_tc37(self, Cemail, Cpassword, date, time_from, time_to, file_path_photo, file_path_video):
        self.create_act_page.tc37(Cemail, Cpassword, date, time_from, time_to, file_path_photo, file_path_video)

    @pytest.mark.run(order=28)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Activity page\\tc48.xlsx", "Sheet1"))
    @unpack
    def test_tc48(self, email, password):
        self.activity_page.tc48(email, password)

    @pytest.mark.run(order=29)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Activity page\\tc48.xlsx", "Sheet1"))
    @unpack
    def test_tc49(self, email, password):
        self.activity_page.tc49(email, password)

    @pytest.mark.run(order=30)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Activity page\\tc48.xlsx", "Sheet1"))
    @unpack
    def test_tc50(self, email, password):
        self.activity_page.tc50(email, password)

    @pytest.mark.run(order=31)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Register page\\tc28.xlsx", "Sheet1"))
    @unpack
    def test_tc28(self, name, email, phone, address, adhaar_no, password, Cpassword):
        self.register_page.tc28(name, email, phone, address, adhaar_no, password, Cpassword)

    @pytest.mark.run(order=32)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Register page\\tc29.xlsx", "Sheet1"))
    @unpack
    def test_tc29(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path):
        self.register_page.tc29(name, email, phone, address, adhaar_no, password, Cpassword, file_path)

    @pytest.mark.run(order=33)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Register page\\tc29.xlsx", "Sheet1"))
    @unpack
    def test_tc30(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path):
        self.register_page.tc30(name, email, phone, address, adhaar_no, password, Cpassword, file_path)

    @pytest.mark.run(order=34)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Register page\\tc31.xlsx", "Sheet1"))
    @unpack
    def test_tc31(self, name, New_email, phone, address, adhaar_no, password, Cpassword, file_path):
        self.register_page.tc31(name, New_email, phone, address, adhaar_no, password, Cpassword, file_path)

    @pytest.mark.run(order=35)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Register page\\tc32.xlsx", "Sheet1"))
    @unpack
    def test_tc32(self, name, inv_email, New_phone, address, adhaar_no, password, Cpassword, file_path):
        self.register_page.tc32(name, inv_email, New_phone, address, adhaar_no, password, Cpassword, file_path)

    @pytest.mark.run(order=36)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Register page\\tc33.xlsx", "Sheet1"))
    @unpack
    def test_tc33(self, name, New_email1, New_phone1, address, adhaar_no, pass1, pass2, file_path):
        self.register_page.tc33(name, New_email1, New_phone1, address, adhaar_no, pass1, pass2, file_path)

    @pytest.mark.run(order=37)
    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Register page\\tc34.xlsx", "Sheet1"))
    @unpack
    def test_tc34(self, name, New_email2, New_phone2, address, adhaar_no, Weak_pass, Weak_Cpass, file_path):
        self.register_page.tc34(name, New_email2, New_phone2, address, adhaar_no, Weak_pass, Weak_Cpass, file_path)

    @pytest.mark.run(order=38)
    def test_tc35(self):
        self.register_page.tc35()

