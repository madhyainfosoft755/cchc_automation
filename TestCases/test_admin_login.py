import pytest
import  softest
from  Pages.admin_login import admin_login_page_code
from  ddt import ddt,data,unpack
from  Utilities.utilities import utilities

@pytest.mark.usefixtures("setup")
@ddt
class Test_admin_login_page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.admin_login_page = admin_login_page_code(self.driver)

    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\admin_login.xlsx", "Sheet1"))
    @unpack
    def test_create_activity_page_tc(self, Cemail, Cpassword):
        self.admin_login_page.all(Cemail, Cpassword)
