import time

from pythonProject2.Base.base_driver import Basedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from selenium.webdriver.remote.webelement import WebElement


class Activity_page:
    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.base_url = "https://ccsc.helpersin.com/create"
        self.select_category_xpath = "// label[ @class ='flex flex-wrap text-sm rounded-lg items-center justify-center border-2 overflow-hidden border-double border-white mt-1 w-5/12 px-5 py-2  sm:px-5 sm:py-3  cursor-pointer  ']"

        #
        self.date_picker_xpath = "//input[@id='datepicker']"
        self.from_time_picker_xpath = "//input[@id='fromTime']"
        self.to_time_picker_xpath = "//input[@id='toTime']"
        self.choose_image_xpath = "//input[@id='photo']"
        self.choose_video_xpath = "//input[@id='video']"
        self.submit_button_xpath = "//button[contains(text(),'SUBMIT')]"
        self.endorse_activity_button_xpath = "//button[contains(text(),'Endorse Activities')]"
        self.my_activity_btn_xpath = "//button[contains(text(),'My Activity')]"

        self.from_time_input_id = "fromTime"
        self.to_time_input_id = "toTime"
        self.without_data_input_click_submit_btn_error_msg_xpath = "//div[contains(text(),'Missing required fields: selectedCategories, date,')]"

    def select_category(self):
        category = self.driver.find_elements(By.XPATH, self.select_category_xpath)
        category_count = 0
        for categoryies in category:
            # print(categoryies)
            if category_count < 4:
                category_count += 1
                continue
            categoryies.click()

    def date_select(self):
        # Get tomorrow's date
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_formatted = tomorrow.strftime('%m/%d/%Y')
        print(tomorrow_formatted)
        datepicker_input = self.driver.find_element(By.XPATH, self.date_picker_xpath)
        datepicker_input.clear()
        time.sleep(2)
        datepicker_input.send_keys(tomorrow_formatted)
        time.sleep(5)

    def time_selection(self):
        current_time = datetime.now().time()

        # Print the current time
        print("Current Time:", current_time)

        # Format the current time as HH:MM:SS
        formatted_time = datetime.now().strftime("%H:%M:%p")
        from_time = self.base.return_any("id", self.from_time_input_id)
        from_time.clear()
        from_time.send_keys(formatted_time)

        # from_time.send_keys("02:35")
        time.sleep(5)

    def to_time_selection(self):
        # Calculate the current time and add 1 hour
        current_time = datetime.now()
        one_hour_later = current_time + timedelta(hours=1)
        formatted_time = one_hour_later.strftime("%H:%M %p")  # Formats time as HH:MM AM/PM
        to_time = self.base.return_any("id", self.to_time_input_id)
        to_time.clear()
        to_time.send_keys(formatted_time)
        time.sleep(1)

    def choose_image(self, image):
        img = self.driver.find_element(By.XPATH, self.choose_image_xpath)
        img.send_keys(image)

    def choose_video(self, video):
        videeo = self.driver.find_element(By.XPATH, self.choose_video_xpath)
        videeo.send_keys(video)

    def submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def my_activity_btn(self):
        self.driver.find_element(By.XPATH, self.my_activity_btn_xpath).click()

    def endorse_activity_button(self):
        self.driver.find_element(By.XPATH, self.endorse_activity_button_xpath).click()

    def without_data_input_click_submit_btn_error_msg(self):
        msg = self.base.return_any("xpath", self.without_data_input_click_submit_btn_error_msg_xpath)

        # Ensure msg is a WebElement
        if isinstance(msg, WebElement):
            print(msg.text)
            if msg.is_displayed():
                print(msg.text)
                return False
        return True
