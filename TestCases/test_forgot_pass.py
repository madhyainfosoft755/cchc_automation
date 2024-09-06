import pytest
import  softest
from Pages.forgot_password_page import forgot_password_page_code
from  ddt import ddt,data,unpack
from  Utilities.utilities import utilities

@pytest.mark.usefixtures("setup")
@ddt
class Test_forgot_password_page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.forgot_pass_code = forgot_password_page_code(self.driver)

    # @data(*utilities.read_data_from_excel(
        # "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\forgot_pass.xlsx", "Sheet1"))
    # @unpack
    def test_login_page_tc(self):
        self.forgot_pass_code.all()

