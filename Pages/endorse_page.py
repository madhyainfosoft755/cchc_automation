import  time
from  Base.base_driver import Basedriver
from  Pages.Login import Login_page_code
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Endorse_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.login = Login_page_code(self.driver)

        self.url = 'https://ccsc.helpersin.com/'
        self.endorse_activity = '/html/body/div[1]/form/div[2]/div/div[2]/div[1]/button'
        self.create_activity = '/html/body/div/div[2]/div/div/div[1]/button'
        self.view_link1  = '/html/body/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/a'
        self.view_link2 = '/html/body/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[5]/a'
        self.check_box1 = '/html/body/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[6]/input'
        self.check_box2 = '/html/body/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[6]/input'
        self.endorse_selected_post = '/html/body/div/div[2]/div/div/button'

    def tc58(self, email, password):
        self.driver.get(self.url)
        time.sleep(2)
        self.login.tc4(email, password)
        self.base.return_any("xpath", self.endorse_activity).click()
        time.sleep(2)
        self.base.return_any("xpath", self.create_activity).click()
        time.sleep(2)

    def tc60_and_61(self):
        self.base.return_any("xpath", self.endorse_activity).click()
        time.sleep(2)
        try:
            checkbox1 = self.base.return_any("xpath", self.check_box1)
            checkbox1.click()
            time.sleep(5)
            wait = WebDriverWait(self.driver, 10)
            button = wait.until(EC.presence_of_element_located((By.XPATH, self.endorse_selected_post)))
            if button.is_displayed():
                print("Button is displayed after clicking the checkbox")
            else:
                print("Button is not displayed")
            time.sleep(5)
            checkbox1.click()
            time.sleep(3)
            wait.until(EC.invisibility_of_element_located((By.XPATH, self.endorse_selected_post)))

            # Validate the absence of the button
            try:
                button = self.driver.find_element(By.XPATH, self.endorse_selected_post)
                if not button.is_displayed():
                    print("Button is not visible after unchecking the checkbox.")
                else:
                    print("Button is still visible after unchecking the checkbox.")
            except:
                # If the element is not found, it means it has been successfully removed from the DOM
                print("Button is not present in the DOM after unchecking the checkbox.")
        except Exception as e:
            print(f"An error occured : {e}")
        time.sleep(5)


    def tc62(self):
        self.base.return_any("xpath", self.view_link1).click()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(5)
        self.base.return_any("xpath", self.view_link2).click()
        time.sleep(3)

    def tc63(self):
        self.driver.refresh()
        time.sleep(5)
        self.base.return_any("xpath", self.check_box2).click()
        time.sleep(2)
        self.base.return_any("xpath", self.endorse_selected_post).click()
        time.sleep(3)

    def all(self, email, password):
        self.tc58(email, password)
        self.tc60_and_61()
        self.tc62()
        self.tc63()










