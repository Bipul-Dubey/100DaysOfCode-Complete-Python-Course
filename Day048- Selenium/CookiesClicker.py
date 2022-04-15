import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path="D:\software\chromedriver_win32\chromedriver.exe"
service=Service(chrome_driver_path)
driver=webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

clicker=driver.find_element(By.ID,"bigCookie")
for i in range(100):
    time.sleep(0.1)
    clicker.click()
