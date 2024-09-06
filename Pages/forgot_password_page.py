import time
from Base.base_driver import Basedriver
import re
from PIL import Image, ImageChops

class forgot_password_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)

        self.page_url = 'https://cch247.com/apps'
        self.forgot_pass_link = "/html/body/div/div[2]/form/div[3]/h2"
        self.send_pin_btn = '/html/body/div/div[2]/div/div[3]/button[1]'
        self.enter_email = '/html/body/div/div[2]/div/div[3]/div/input'
        self.go_to_login_page = '/html/body/div/div[2]/div/div[3]/button[2]'
        self.goto_login_update_pass_page = '/html/body/div/div[2]/div/div[3]/button'
        self.verify_pin = '/html/body/div/div[2]/div/div[3]/button[1]'
        self.enter_pin = '/html/body/div/div[2]/div/div[3]/div/input'
        self.update_pass = '/html/body/div/div[2]/div/div[3]/div/button'
        self.enter_new_pass = '/html/body/div/div[2]/div/div[3]/div/div[1]/input'
        self.confirm_mew_pass = '/html/body/div/div[2]/div/div[3]/div/div[2]/input'

    def tc47(self):
        self.driver.get(self.page_url)
        time.sleep(2)
        self.base.return_any("xpath", self.forgot_pass_link).click()
        time.sleep(5)
        self.driver.save_screenshot("C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\scrennshots\\before_click.png")
        self.base.return_any("xpath", self.send_pin_btn).click()
        self.driver.save_screenshot("C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\scrennshots\\after_click.png")
        before_click = Image.open("C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\scrennshots\\before_click.png")
        after_click = Image.open("C:\\Users\\mohni\\PycharmProjects\\cchc_automation\\scrennshots\\after_click.png")
        diff = ImageChops.difference(before_click, after_click)

        if diff.getbbox():
            print("Error message appeared")
            assert True
        else:
            print("Error message not appear")
            assert False

    def all(self):
        self.tc47()








