from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service()

driver = webdriver.Chrome(service=s)

driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

print(driver.title)

driver.close()
driver.quit()

