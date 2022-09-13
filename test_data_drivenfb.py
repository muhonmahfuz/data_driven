import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import login_page
import excel_utiles


class LoginTest(unittest.TestCase):

    def test_login(self):
        baseURL = "https://facebook.com"
        executable_path = "C:\\QA\\unit\\Driver\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        # Excel implementation
        data_file = 'login_data.xlsx'
        sheet_name = 'Sheet1'

        number_of_rows = excel_utiles.get_row_count(data_file, sheet_name)

        for r in range(2, number_of_rows + 1):
            email = excel_utiles.read_data(data_file, sheet_name, r, 1)
            password = excel_utiles.read_data(data_file, sheet_name, r, 2)

            login_page.LoginPage(driver).login_orange(email, password)

        driver.close()