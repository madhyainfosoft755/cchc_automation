import  time
from  Base.base_driver import Basedriver
from  Pages.get_forgot_pass_pin_form_gmail import Get_pin_form_gmail
import re


class forgot_password_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)

        self.endorse_activity = '/html/body/div[1]/form/div[2]/div/div[2]/div[1]/button'
        self.create_activity = '/html/body/div/div[2]/div/div/div[1]/button'
        self.view_link1  = '/html/body/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/a'
        self.view_link2 = '/html/body/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[5]/a'
        self.check_box1 = ''
        self.check_box2 = ''
