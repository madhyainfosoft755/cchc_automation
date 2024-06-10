import time
from pythonProject2.Base.base_driver import Basedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from selenium.webdriver.remote.webelement import WebElement


class EndorsePage:
    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.endorse_activity_button_xpath = "//button[contains(text(),'Endorse Activities')]"
        self.search_btn_click_xpath = "//body/div[@id='root']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/*[1]"
        self.all_categories_xpath = "//body/div[@id='root']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"
        self.all_categories_click_xpath = "//body/div[@id='root']/div[2]/div[1]/div[1]/div[2]/div[2]/table[1]"
        self.view_activity_details_btn_xpath = ""

    def endorse_activity_button(self):
        self.base.return_any("xpath", self.endorse_activity_button_xpath).click()

    def search_btn_click(self):
        self.base.return_any("xpath", self.search_btn_click_xpath).click()

    def all_categories(self):
        self.base.return_any("xpath", self.all_categories_xpath).click()

    # count = 0
    def all_categories_click(self):
        wait = WebDriverWait(self.base.driver, 10)
        table = wait.until(EC.presence_of_element_located((By.XPATH, self.all_categories_click_xpath)))
        time.sleep(10)
        print("Table found:", table)
        table_content = []
        rows = table.find_elements(By.TAG_NAME, "tr")
        print(f"Number of rows found: {len(rows)}")
        for row in rows:
            row_content = []

            cells = row.find_elements(By.TAG_NAME, "td")
            print(f"Number of cells in row: {len(cells)}")
            for cell in cells:
                # Extract text from the cell and append to row_content
                checkbox = cell.find_elements(By.TAG_NAME, "input")
                for checkboxes in checkbox:
                    if checkboxes.get_attribute("type") == "checkbox":
                        # Click the checkbox
                        checkboxes.click()
                        print(f"Checkbox in row {rows.index(row)} and cell {cells.index(cell)} clicked.")

                row_content.append(cell.text)
                print(f"Cell text: {cell.text}")

            table_content.append(row_content)
        print("Table content:", table_content)
        for row in table_content:
            print(row)

    def all_categories_view_btn_click(self):
        wait = WebDriverWait(self.base.driver, 10)
        table = wait.until(EC.presence_of_element_located((By.XPATH, self.all_categories_click_xpath)))
        time.sleep(10)
        print("Table found:", table)
        table_content = []
        rows = table.find_elements(By.TAG_NAME, "tr")
        print(f"Number of rows found: {len(rows)}")
        for row in rows:
            row_content = []

            cells = row.find_elements(By.TAG_NAME, "td")
            print(f"Number of cells in row: {len(cells)}")
            for cell in cells:
                # Extract text from the cell and append to row_content
                checkbox = cell.find_elements(By.TAG_NAME, "a")
                for checkboxes in checkbox:
                    if checkboxes.get_attribute("type") == "checkbox":
                        # Click the checkbox
                        checkboxes.click()
                        print(f"Checkbox in row {rows.index(row)} and cell {cells.index(cell)} clicked.")

                row_content.append(cell.text)
                print(f"Cell text: {cell.text}")

            table_content.append(row_content)
        print("Table content:", table_content)
        for row in table_content:
            print(row)
