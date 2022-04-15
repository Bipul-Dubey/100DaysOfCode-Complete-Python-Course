import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path="D:\software\chromedriver_win32\chromedriver.exe"
service=Service(chrome_driver_path)
driver=webdriver.Chrome(service=service)

web_url="https://www.python.org/"
driver.get(web_url)

event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names=driver.find_elements(By.CSS_SELECTOR,".event-widget ul a")
events={n:{'time':event_times[n].text,'name':event_names[n].text} for n in range(len(event_times))}
print(events)

driver.quit()