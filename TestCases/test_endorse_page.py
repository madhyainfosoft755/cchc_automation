import pytest
import  softest
from Pages.endorse_page import Endorse_page_code
from  ddt import ddt,data,unpack
from  Utilities.utilities import utilities

@pytest.mark.usefixtures("setup")
@ddt
class Test_endorse_page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.endorser_page = Endorse_page_code(self.driver)

    @data(*utilities.read_data_from_excel(
        "C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\TestData\\Endorse_pag.xlsx", "Sheet1"))
    @unpack
    def test_endorse_page(self, email, password):
        self.endorser_page.all(email, password)

