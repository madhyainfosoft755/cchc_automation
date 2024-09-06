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
    def test_register_tc(self, name, email, phone, address, password, Cpassword):
        self.Register_page_code.all(name, email, phone, address, password, Cpassword)
