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
driver.find_element(By.NAME,"username").send_keys("sachin")
driver.find_element(By.NAME,"password").send_keys("sachin@10")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.LINK_TEXT,"Log Out").click()

time.sleep(4)

driver.find_element(By.NAME,"username").send_keys("abcd")
driver.find_element(By.NAME,"password").send_keys("abcd")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
assert 'error' in driver.find_element(By.CSS_SELECTOR,".error").text


driver.close()
driver.quit()

