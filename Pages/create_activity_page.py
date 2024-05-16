import time
from Base.base_driver import Basedriver
from  Pages.Login import Login_page_code


class Create_activity_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.login_page_code = Login_page_code(self.driver)

        self.page_url = 'https://ccsc.helpersin.com'
        self.submit_btn = '/html/body/div/form/div[2]/div/div[2]/button'
        self.my_activity_btn = '/html/body/div/form/div[2]/div/div[1]/button'
        self.endorse_activity_btn = '/html/body/div/form/div[2]/div/div[2]/div[1]/button'
        self.gardening = '/html/body/div/form/div[2]/div/div[2]/div[2]/label[1]/span'
        self.cleaning = '/html/body/div/form/div[2]/div/div[2]/div[2]/label[2]/span'
        self.teaching_poor = '/html/body/div/form/div[2]/div/div[2]/div[2]/label[3]/span'
        self.planting_tree = '/html/body/div/form/div[2]/div/div[2]/div[2]/label[4]/span'
        self.marathon = '/html/body/div/form/div[2]/div/div[2]/div[2]/label[5]/span'
        self.social_activity = '/html/body/div/form/div[2]/div/div[2]/div[2]/label[6]/span'
        self.date_field = '/html/body/div/form/div[2]/div/div[2]/div[3]/div[2]/input'
        self.time_from = '/html/body/div/form/div[2]/div/div[2]/div[4]/div[1]/input'
        self.time_to = '/html/body/div/form/div[2]/div/div[2]/div[4]/div[2]/input'
        self.photos = '/html/body/div/form/div[2]/div/div[2]/div[5]/div[1]/div/div/p/input'
        self.videos = '/html/body/div/form/div[2]/div/div[2]/div[5]/div[2]/div/div/p/input'



    def tc36(self, Cemail, Cpassword):
        self.driver.get(self.page_url)
        time.sleep(5)
        self.login_page_code.tc5(Cemail, Cpassword)
        self.base.return_any("xpath", self.submit_btn).click()
        time.sleep(3)

    def tc37(self, Cemail, Cpassword, date, time_from, time_to, file_path_photo, file_path_video):
        date_str = date.strftime("%Y-%m-%d")
        time_from_str = time_from.strftime("%H:%M")
        time_to_str = time_to.strftime("%H:%M")

        self.driver.get(self.page_url)
        time.sleep(5)
        self.login_page_code.tc5(Cemail, Cpassword)
        self.base.return_any("xpath", self.planting_tree).click()
        time.sleep(2)
        self.base.return_any("xpath", self.date_field).send_keys(date_str)
        time.sleep(2)
        self.base.return_any("xpath", self.time_from).send_keys(time_from_str)
        time.sleep(2)
        self.base.return_any("xpath", self.time_to).send_keys(time_to_str)
        time.sleep(2)
        self.base.return_any("xpath", self.photos).send_keys(file_path_photo)
        time.sleep(2)
        self.base.return_any("xpath", self.videos).send_keys(file_path_video)
        time.sleep(2)
        self.base.return_any("xpath", self.submit_btn).click()
        time.sleep(5)

    def tc38(self):
        self.base.return_any("xpath", self.my_activity_btn).click()
        time.sleep(3)

    def tc39(self, Cemail, Cpassword):
        self.driver.get(self.page_url)
        time.sleep(5)
        self.login_page_code.tc5(Cemail, Cpassword)
        self.base.return_any("xpath", self.endorse_activity_btn).click()
        time.sleep(6)

    def all(self, Cemail, Cpassword, date, time_from, time_to, file_path_photo, file_path_video):
        self.tc36(Cemail, Cpassword)
        self.tc38()
        self.tc39(Cemail, Cpassword)
        self.tc37(Cemail, Cpassword, date, time_from, time_to, file_path_photo, file_path_video)



