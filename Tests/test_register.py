from selenium import webdriver
from Utilities.BaseClass import BaseClass
from PageObjects.registerPage import RegisterPage
from PageObjects.LoginPage import LoginPage

class TestRegister(BaseClass):
    UserName = "qwerty"
    Password = "qwerty@10"

    def test_register(self):
        #in login page click register link
        login_page = LoginPage(self.driver)
        login_page.get_register_link().click()

        #in regiter page enter all data
        register_page = RegisterPage(self.driver)
        register_page.get_first_name().send_keys("qwerty")
        register_page.get_last_name().send_keys("qwerty")
        register_page.get_address().send_keys("street 1234")
        register_page.get_city().send_keys("qwer city")
        register_page.get_state().send_keys("Karnataka")
        register_page.get_phone().send_keys("6900000000")
        register_page.get_ssn().send_keys("1234567")
        register_page.get_zip_code().send_keys("577436")

        register_page.get_user_name().send_keys(TestRegister.UserName)
        register_page.get_password().send_keys(TestRegister.Password)
        register_page.get_password_cnf().send_keys(TestRegister.Password)

        register_page.get_register_btn().click()


