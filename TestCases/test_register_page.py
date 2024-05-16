import pytest
import  softest
from Pages.Register_page import Register_page_code
from  ddt import ddt,data,unpack
from  Utilities.utilities import utilities

@pytest.mark.usefixtures("setup")
@ddt
class Test_register_page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.Register_page_code = Register_page_code(self.driver)

    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Register_page.xlsx", "Sheet1"))
    @unpack
    def test_register_tc(self, name, email, phone, address, adhaar_no, password, Cpassword, file_path, New_email, inv_email, New_phone, New_email1, New_phone1, pass1, pass2, New_email2, New_phone2, Weak_pass, Weak_Cpass, New_email3, New_phone3, short_pass, short_Cpass):
        self.Register_page_code.all(name, email, phone, address, adhaar_no, password, Cpassword, file_path, New_email, inv_email, New_phone, New_email1, New_phone1, pass1, pass2, New_email2, New_phone2, Weak_pass, Weak_Cpass, New_email3, New_phone3, short_pass, short_Cpass)


