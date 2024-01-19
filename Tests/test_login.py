from selenium.webdriver.common.by import By
import pytest
from Utilities.BaseClass import BaseClass


class Test_login(BaseClass):

    def test_login_with_correct_creds(self):
        #login operations
        self.driver.find_element(By.NAME,"username").send_keys("sachin")
        self.driver.find_element(By.NAME,"password").send_keys("sachin")
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        self.driver.find_element(By.LINK_TEXT,"Log Out").click()

    def test_login_with_incorrect_creds(self):

        self.driver.find_element(By.NAME,"username").send_keys("abcd")
        self.driver.find_element(By.NAME,"password").send_keys("abcd")
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        assert 'error' in self.driver.find_element(By.CSS_SELECTOR,".error").text

