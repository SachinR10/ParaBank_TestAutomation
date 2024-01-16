from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#service and chrome options
s = Service()
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("incognito")
chromeOptions.add_argument("start-maximized")

#get website
driver = webdriver.Chrome(service=s,options=chromeOptions)
driver.implicitly_wait(5)
driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

#login operations
print(driver.title)
driver.find_element(By.NAME,"username").send_keys("SachinR")
driver.find_element(By.NAME,"password").send_keys("Sachinr@10")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(4)
driver.close()
driver.quit()

