from selenium.webdriver.common.by import By
import pytest

class LoginPage:
    user_name_field = (By.NAME,"username")
    password_field = (By.NAME,"password")
    login_button = (By.XPATH,"//input[@type='submit']")
    register_link = (By.LINK_TEXT,"Register")

    def __init__(self,driver):
        self.driver=driver
    
    def get_user_name_field(self):
        return self.driver.find_element(*LoginPage.user_name_field)
    
    def get_password_field(self):
        return self.driver.find_element(*LoginPage.password_field)
    
    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)
    
    def get_register_link(self):
        return self.driver.find_element(*LoginPage.register_link)



