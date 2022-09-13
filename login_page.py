import time
import pytest
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):

        user_name_field = self.driver.find_element(By.ID, "email")
        user_name_field.send_keys(username)


        password_field = self.driver.find_element(By.ID, "pass")
        password_field.send_keys(password)


        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()
        time.sleep(1)