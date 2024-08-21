import pytest
import  softest
from Pages.Login import Login_page_code
from  ddt import ddt,data,unpack
from  Utilities.utilities import utilities

@pytest.mark.usefixtures("setup")
@ddt
class Test_login_page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login_page_code = Login_page_code(self.driver)

    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\login_pageTC.xlsx", "Sheet1"))
    @unpack
    def test_login_page_tc(self, email, password, Wemail, Cemail, Wpassword, Cpassword):
        self.login_page_code.all(email, password, Wemail, Cemail, Wpassword, Cpassword)
