import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path="D:\software\chromedriver_win32\chromedriver.exe"

service=Service(chrome_driver_path)
driver=webdriver.Chrome(service=service)

web_url="https://infyspringboard.onwingspan.com/auth/realms/infyspringboard/protocol/openid-connect/auth?client_id=portal&redirect_uri=https%3A%2F%2Finfyspringboard.onwingspan.com%2Fen%2F&state=b9fd33d6-dd7b-4b1d-8f40-6cbf959182c9&response_mode=fragment&response_type=code&scope=openid&nonce=30c050f3-5d34-4d98-9a6c-44decf5cea27"
driver.get(web_url)

email=""
password=""

driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.ID,"kc-login").click()



time.sleep(10)
driver.quit()
