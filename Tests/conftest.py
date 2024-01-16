import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def setup_teardown(request):
        s = Service()
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("incognito")
        chromeOptions.add_argument("start-maximized")

        #get website
        driver = webdriver.Chrome(service=s,options=chromeOptions)
        driver.implicitly_wait(5)
        driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
        request.cls.driver = driver
        yield
        driver.close()
        driver.quit()


