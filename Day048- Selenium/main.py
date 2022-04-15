import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path="D:\software\chromedriver_win32\chromedriver.exe"
service=Service(chrome_driver_path)
driver=webdriver.Chrome(service=service)

web_url="https://www.python.org/"
driver.get(web_url)

# logo=driver.find_element(By.CLASS_NAME,"python-logo")
# print(logo.size)
#
# docs_tag=driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
# print(docs_tag.text)

bug_link=driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

time.sleep(5)
driver.quit()