import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import login_page


class LoginTest(unittest.TestCase):

    # @pytest.mark.skip
    def test_valid_login(self):
        baseURL = "https://facebook.com/"
        executable_path = "C:\\QA\\unit\\Driver\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        login_page.LoginPage(driver).login_orange("Admin", "admin123")

        driver.close()

    def test_Invalid_login(self):
        baseURL = "https://facebook.com"
        executable_path = "C:\\QA\\unit\\Driver\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        login_page.LoginPage(driver).login_orange("Admin213123", "admin123232")

        driver.close()