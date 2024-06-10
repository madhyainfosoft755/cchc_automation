import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
import time
from datetime import datetime
from cchc_automation.pythonProject2.Base.base_driver import Basedriver


class ManageCategory:
    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(self.driver)
        self.manage_Category_btn_xpath = "//h1[contains(text(),'Manage Category')]"
        self.add_category_plus_button_xpath = "//body/div[@id='root']/div[2]/div[1]/div[1]/div[1]/button[1]/*[1]"
        self.add_category_input_xpath = "//body/div[@id='root']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]"
