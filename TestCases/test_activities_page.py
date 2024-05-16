import pytest
import  softest
from  Pages.Activities_page import activities_page_code
from  ddt import ddt,data,unpack
from  Utilities.utilities import utilities

@pytest.mark.usefixtures("setup")
@ddt
class Test_forgot_password_page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.Activities_page_code = activities_page_code(self.driver)

    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Activities_page.xlsx", "Sheet1"))
    @unpack
    def test_create_activity_page_tc(self, email, password):
        self.Activities_page_code.all(email, password)