from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path="D:\software\chromedriver_win32\chromedriver.exe"
service=Service(chrome_driver_path)
driver=webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname=driver.find_element(By.NAME,"fName")
fname.send_keys("bipul")

lname=driver.find_element(By.NAME,"lName")
lname.send_keys("dubey")

email=driver.find_element(By.NAME,"email")
email.send_keys("smtpcheck9@gmail.com")

btn=driver.find_element(By.TAG_NAME,"button")
btn.click()

