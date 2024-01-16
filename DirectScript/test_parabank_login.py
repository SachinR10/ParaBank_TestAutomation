from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service()

chromeOptions = webdriver.ChromeOptions()

chromeOptions.add_argument("incognito")
chromeOptions.add_argument("start-maximized")

driver = webdriver.Chrome(service=s,options=chromeOptions)
driver.implicitly_wait(5)


driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

print(driver.title)

driver.close()
driver.quit()

