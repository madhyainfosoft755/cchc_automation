import pytest
import  softest
from  Pages.create_activity_page import Create_activity_page_code
from  ddt import ddt,data,unpack
from  Utilities.utilities import utilities

@pytest.mark.usefixtures("setup")
@ddt
class Test_forgot_password_page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.Create_activity_code = Create_activity_page_code(self.driver)

    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Create_activity.xlsx", "Sheet1"))
    @unpack
    def test_create_activity_page_tc(self, Cemail, Cpassword, date, file_path_photo, file_path_video):
        self.Create_activity_code.all(Cemail, Cpassword, date, file_path_photo, file_path_video)

