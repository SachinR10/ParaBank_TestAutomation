from selenium.webdriver.common.by import By
import pytest
from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from Tests.test_register import TestRegister


class Test_login(BaseClass):
    
    @pytest.mark.LoginScenarios
    def test_login_with_correct_creds(self):
        #login operations
        loginPage = LoginPage(self.driver)
        loginPage.get_user_name_field().send_keys(TestRegister.UserName)
        loginPage.get_password_field().send_keys(TestRegister.Password)
        loginPage.get_login_button().click()
        self.driver.find_element(By.LINK_TEXT,"Log Out").click()
    
    @pytest.mark.LoginScenarios
    def test_login_with_incorrect_creds(self):

        loginPage = LoginPage(self.driver)
        loginPage.get_user_name_field().send_keys("abcd")
        loginPage.get_password_field().send_keys("abcd10")
        loginPage.get_login_button().click()
        assert 'error' in self.driver.find_element(By.CSS_SELECTOR,".error").text

