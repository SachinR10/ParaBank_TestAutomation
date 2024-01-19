from selenium.webdriver.common.by import By

class RegisterPage:
    first_name  = (By.ID,"customer.firstName")
    last_name = (By.ID,"customer.lastName")
    address = (By.ID,"customer.address.street")
    city = (By.ID,"customer.address.city")
    state = (By.ID,"customer.address.state")
    zip_code = (By.ID,"customer.address.zipCode")
    phone = (By.ID,"customer.phoneNumber")
    ssn = (By.ID,"customer.ssn")

    user_name = (By.ID,"customer.username")
    password = (By.ID,"customer.password")
    password_cnf = (By.ID,"repeatedPassword")

    register_btn = (By.CSS_SELECTOR,"div[id='rightPanel'] input[class='button']")

    def __init__(self,driver):
        self.driver = driver

    def get_first_name(self):
        return self.driver.find_element(*RegisterPage.first_name)
    
    def get_last_name(self):
        return self.driver.find_element(*RegisterPage.last_name)

    def get_address(self):
        return self.driver.find_element(*RegisterPage.address)

    def get_city(self):
        return self.driver.find_element(*RegisterPage.city)
    
    def get_state(self):
        return self.driver.find_element(*RegisterPage.state)
    
    def get_zip_code(self):
        return self.driver.find_element(*RegisterPage.zip_code)
    
    def get_phone(self):
        return self.driver.find_element(*RegisterPage.phone)
    
    def get_ssn(self):
        return self.driver.find_element(*RegisterPage.ssn)

    def get_user_name(self):
        return self.driver.find_element(*RegisterPage.user_name)

    def get_password(self):
        return self.driver.find_element(*RegisterPage.password)

    def get_password_cnf(self):
        return self.driver.find_element(*RegisterPage.password_cnf)

    def get_register_btn(self):
        return self.driver.find_element(*RegisterPage.register_btn)



