from selenium import webdriver
from LoginPage import LoginPage
import time

driver = webdriver.Chrome()
driver.get("http://10.10.141.79:8080/icompaign/login.html")
time.sleep(1)
loginpage = LoginPage(driver)
loginpage.login_icompaign("12345678987", "1")
time.sleep(1)
driver.close()
